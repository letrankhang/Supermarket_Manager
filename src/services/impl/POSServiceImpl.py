import logging
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional

from config.database import Database
from config.settings import POSSettings
from src.converter.POSConverter import POSConverter
from src.dtos.POSDTO import (
    CartDTO, CartItemDTO, CartSummaryDTO, CategoryDTO,
    CheckoutRequestDTO, CheckoutResultDTO, InvoiceDetailDTO, ProductDTO
)
from src.entities.sales_invoice import SalesInvoice
from src.repositories.impl.POSRepositoryImpl import POSRepositoryImpl
from src.services.POSService import (
    EmptyCartError, OutOfStockError, POSError, POSService, ProductNotFoundError
)

logger = logging.getLogger(__name__)

VND_ROUNDING_UNIT = Decimal("1")

WALK_IN_CUSTOMER_LABEL = "Khách lẻ"
UNKNOWN_CASHIER_LABEL = "Không rõ"

class POSServiceImpl(POSService):
    def __init__(self) -> None:
        self._cart: Dict[int, CartItemDTO] = {}
        self._discount_rate: Decimal = POSSettings.DEFAULT_DISCOUNT_RATE


    def get_categories(self) -> List[CategoryDTO]:
        all_category = CategoryDTO(category_id=None, category_name=POSSettings.ALL_CATEGORY_LABEL)
        try:
            with Database.get_session_ctx() as session:
                repository = POSRepositoryImpl(session)
                categories = repository.find_all_categories()
                category_dtos = POSConverter.to_category_dto_list(categories)
            return [all_category] + category_dtos
        except Exception as e:
            logger.error("Không lấy được danh sách danh mục: %s", e)
            return [all_category]


    def get_products(self, category_id: Optional[int] = None,
                     keyword: Optional[str] = None) -> List[ProductDTO]:
        try:
            with Database.get_session_ctx() as session:
                repository = POSRepositoryImpl(session)
                products = repository.find_products(
                    category_id=category_id,
                    keyword=keyword,
                    limit=POSSettings.PRODUCT_PAGE_SIZE
                )

                return POSConverter.to_product_dto_list(products)
        except Exception as e:
            logger.error(
                "Không lấy được danh sách sản phẩm (category_id=%s, keyword=%s): %s",
                category_id, keyword, e
            )
            return []


    def add_product_to_cart(self, product_id: int, quantity: int = 1) -> CartDTO:
        product = self._load_product_dto(product_id)
        if product is None:
            raise ProductNotFoundError("Không tìm thấy sản phẩm cần thêm vào giỏ.")

        requested_quantity = self._get_quantity_in_cart(product_id) + quantity
        self._validate_stock(product, requested_quantity)

        self._upsert_cart_item(product, requested_quantity)

        logger.info(
            "Thêm sản phẩm id=%s vào giỏ, số lượng mới=%d.",
            product_id, requested_quantity
        )
        return self.get_cart()


    def _load_product_dto(self, product_id: int) -> Optional[ProductDTO]:
        try:
            with Database.get_session_ctx() as session:
                repository = POSRepositoryImpl(session)
                product = repository.find_product_by_id(product_id)
                if product is None:
                    return None
                return POSConverter.to_product_dto(product)
        except Exception as e:
            logger.error("Lỗi khi đọc sản phẩm id=%s: %s", product_id, e)
            raise POSError("Không đọc được thông tin sản phẩm. Vui lòng thử lại.")


    def add_product_by_barcode(self, barcode: str) -> CartDTO:
        try:
            with Database.get_session_ctx() as session:
                repository = POSRepositoryImpl(session)
                product = repository.find_product_by_barcode(barcode.strip())
                product_id = product.product_id if product is not None else None
        except Exception as e:
            logger.error("Lỗi khi tra cứu mã vạch %s: %s", barcode, e)
            raise POSError("Không tra cứu được mã sản phẩm. Vui lòng thử lại.")

        if product_id is None:
            raise ProductNotFoundError(f"Không tìm thấy sản phẩm có mã '{barcode}'.")

        return self.add_product_to_cart(product_id)


    def change_item_quantity(self, product_id: int, delta: int) -> CartDTO:
        item = self._cart.get(product_id)
        if item is None:
            logger.warning("Đổi số lượng cho sản phẩm id=%s không có trong giỏ.", product_id)
            return self.get_cart()

        new_quantity = item.quantity + delta

        if new_quantity <= 0:
            return self.remove_item_from_cart(product_id)

        if new_quantity > item.stock_available:
            logger.info(
                "Chặn tăng số lượng sản phẩm id=%s: yêu cầu %d, tồn kho %d.",
                product_id, new_quantity, item.stock_available
            )
            raise OutOfStockError(
                f"Sản phẩm '{item.product_name}' chỉ còn {item.stock_available} trong kho."
            )

        item.quantity = new_quantity
        return self.get_cart()

    
    def remove_item_from_cart(self, product_id: int) -> CartDTO:
        removed_item = self._cart.pop(product_id, None)
        if removed_item is not None:
            logger.info("Đã xóa sản phẩm id=%s khỏi giỏ hàng.", product_id)
        return self.get_cart()


    def clear_cart(self) -> CartDTO:
        self._cart.clear()
        self._discount_rate = POSSettings.DEFAULT_DISCOUNT_RATE
        logger.info("Đã làm mới giỏ hàng.")
        return self.get_cart()


    def get_cart(self) -> CartDTO:
        items = list(self._cart.values())
        return CartDTO(items=items, summary=self._calculate_summary(items))


    def apply_discount_rate(self, discount_rate: Decimal) -> CartDTO:
        if discount_rate < 0 or discount_rate > POSSettings.MAX_DISCOUNT_RATE:
            max_percent = POSSettings.MAX_DISCOUNT_RATE * Decimal("100")
            raise POSError(f"Mức giảm giá chỉ được nằm trong khoảng 0% đến {max_percent:.0f}%.")

        self._discount_rate = discount_rate
        logger.info("Áp dụng mức giảm giá %s cho hóa đơn đang lập.", discount_rate)
        return self.get_cart()


    def checkout(self, request: CheckoutRequestDTO) -> CheckoutResultDTO:
        items = list(self._cart.values())
        if not items:
            raise EmptyCartError("Giỏ hàng đang trống, chưa thể thanh toán.")

        summary = self._calculate_summary(items)

        try:
            with Database.get_session_ctx() as session:
                repository = POSRepositoryImpl(session)

                self._validate_stock_before_checkout(repository, items)

                invoice = self._build_invoice_entity(request, summary)
                saved_invoice = repository.insert_invoice(invoice)
                invoice_id = saved_invoice.invoice_id

                details = POSConverter.to_sales_detail_list(invoice_id, items)
                repository.insert_invoice_details(details)

                self._decrease_stock_for_items(repository, items)

                invoice_date = saved_invoice.invoice_date

            invoice_code = POSConverter.to_invoice_code(invoice_id)
            logger.info(
                "Đã lưu hóa đơn %s, tổng tiền %s, thu ngân user_id=%s.",
                invoice_code, summary.grand_total, request.user_id
            )

            self.clear_cart()

            return CheckoutResultDTO(
                success=True,
                message=f"Thanh toán thành công hóa đơn {invoice_code}.",
                invoice_id=invoice_id,
                invoice_code=invoice_code,
                final_total=summary.grand_total,
                invoice_date=invoice_date
            )
        except POSError:
            raise
        except Exception as e:
            logger.error("Lỗi khi lưu hóa đơn bán hàng: %s", e)
            raise POSError("Không lưu được hóa đơn. Giao dịch đã được hoàn tác, vui lòng thử lại.")


    def _get_quantity_in_cart(self, product_id: int) -> int:
        item = self._cart.get(product_id)
        return item.quantity if item is not None else 0


    def _validate_stock(self, product: ProductDTO, requested_quantity: int) -> None:
        if product.is_out_of_stock:
            raise OutOfStockError(f"Sản phẩm '{product.product_name}' đã hết hàng.")

        if requested_quantity > product.current_stock:
            raise OutOfStockError(
                f"Sản phẩm '{product.product_name}' chỉ còn {product.current_stock} trong kho."
            )


    def _upsert_cart_item(self, product: ProductDTO, quantity: int) -> None:
        existing_item = self._cart.get(product.product_id)

        if existing_item is None:
            self._cart[product.product_id] = POSConverter.to_cart_item_dto(product, quantity)
            return

        existing_item.quantity = quantity

        existing_item.stock_available = product.current_stock


    def _validate_stock_before_checkout(self, repository: POSRepositoryImpl,
                                        items: List[CartItemDTO]) -> None:
        product_ids = [item.product_id for item in items]
        products = repository.find_products_by_ids(product_ids)

        product_map = {
            product.product_id: POSConverter.to_product_dto(product)
            for product in products
        }

        for item in items:
            product = product_map.get(item.product_id)
            if product is None:
                raise ProductNotFoundError(
                    f"Sản phẩm '{item.product_name}' không còn tồn tại trong hệ thống."
                )
            self._validate_stock(product, item.quantity)

    def _decrease_stock_for_items(self, repository: POSRepositoryImpl,
                                  items: List[CartItemDTO]) -> None:
        for item in items:
            repository.decrease_stock(item.product_id, item.quantity)


    def _build_invoice_entity(self, request: CheckoutRequestDTO,
                              summary: CartSummaryDTO) -> SalesInvoice:
        return SalesInvoice(
            customer_id=request.customer_id,
            user_id=request.user_id,
            sub_total=summary.sub_total,
            discount_amount=summary.discount_amount,
            tax_amount=summary.tax_amount,
            final_total=summary.grand_total,
            payment_method=POSConverter.to_payment_method_value(request.payment_method_label)
        )


    def _calculate_summary(self, items: List[CartItemDTO]) -> CartSummaryDTO:
        sub_total = sum((item.line_total for item in items), Decimal("0"))
        item_count = sum(item.quantity for item in items)

        tax_rate = POSSettings.VAT_RATE
        discount_rate = self._discount_rate

        discount_amount = self._round_money(sub_total * discount_rate)
        taxable_amount = sub_total - discount_amount
        tax_amount = self._round_money(taxable_amount * tax_rate)
        grand_total = self._round_money(taxable_amount + tax_amount)

        return CartSummaryDTO(
            item_count=item_count,
            sub_total=self._round_money(sub_total),
            discount_rate=discount_rate,
            discount_amount=discount_amount,
            tax_rate=tax_rate,
            tax_amount=tax_amount,
            grand_total=grand_total
        )


    def _round_money(self, amount: Decimal) -> Decimal:
        return amount.quantize(VND_ROUNDING_UNIT, rounding=ROUND_HALF_UP)


    def get_invoice_detail(self, invoice_id: int) -> Optional[InvoiceDetailDTO]:
        try:
            with Database.get_session_ctx() as session:
                repository = POSRepositoryImpl(session)

                invoice = repository.find_invoice_by_id(invoice_id)
                if invoice is None:
                    logger.warning("Không tìm thấy hóa đơn %s để in.", invoice_id)
                    return None

                rows = repository.find_invoice_lines(invoice_id)
                lines = [
                    POSConverter.to_invoice_line_dto(detail, product)
                    for detail, product in rows
                ]

                customer_name = repository.find_customer_name(invoice.customer_id)
                cashier_name = repository.find_user_name(invoice.user_id)

                payment_value = invoice.payment_method or ""

                return InvoiceDetailDTO(
                    invoice_id=invoice.invoice_id,
                    invoice_code=POSConverter.to_invoice_code(invoice.invoice_id),
                    invoice_date=invoice.invoice_date,
                    cashier_name=(cashier_name or UNKNOWN_CASHIER_LABEL),
                    customer_name=(customer_name or WALK_IN_CUSTOMER_LABEL),
                    payment_method=payment_value,
                    payment_method_label=POSConverter.to_payment_method_label(payment_value),
                    sub_total=POSConverter.to_decimal(invoice.sub_total),
                    discount_amount=POSConverter.to_decimal(invoice.discount_amount),
                    tax_amount=POSConverter.to_decimal(invoice.tax_amount),
                    final_total=POSConverter.to_decimal(invoice.final_total),
                    points_used=int(invoice.points_used or 0),
                    lines=lines
                )
        except Exception as e:
            logger.error("Không lấy được chi tiết hóa đơn %s: %s", invoice_id, e)
            return None
