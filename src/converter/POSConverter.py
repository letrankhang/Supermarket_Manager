import logging
from decimal import Decimal
from typing import Dict, List, Optional

from src.dtos.POSDTO import CartItemDTO, CategoryDTO, ProductDTO
from src.entities.category import Category
from src.entities.product import Product
from src.entities.sales_detail import SalesDetail

logger = logging.getLogger(__name__)


PAYMENT_METHOD_MAP: Dict[str, str] = {
    "Tiền mặt": "Cash",
    "Chuyển khoản": "Banking",
    "Thẻ": "E-Wallet",
}

DEFAULT_PAYMENT_METHOD: str = "Cash"

class POSConverter:
    @staticmethod
    def to_decimal(value: Optional[object]) -> Decimal:
        if value is None:
            return Decimal("0")
        try:
            return Decimal(str(value))
        except Exception:
            logger.warning("Không thể ép giá trị '%s' về Decimal, dùng 0.", value)
            return Decimal("0")

    @classmethod
    def to_category_dto(cls, category: Category) -> CategoryDTO:
        return CategoryDTO(
            category_id=category.category_id,
            category_name=category.category_name or ""
        )

    @classmethod
    def to_category_dto_list(cls, categories: List[Category]) -> List[CategoryDTO]:
        return [cls.to_category_dto(category) for category in categories]

    @classmethod
    def to_product_dto(cls, product: Product) -> ProductDTO:
        return ProductDTO(
            product_id=product.product_id,
            barcode=product.barcode or "",
            product_name=product.product_name or "",
            unit=product.unit or "",
            retail_price=cls.to_decimal(product.retail_price),
            current_stock=int(product.current_stock or 0),
            image_path=product.image,
            cost_price=cls.to_decimal(product.avg_import_price)
        )

    @classmethod
    def to_product_dto_list(cls, products: List[Product]) -> List[ProductDTO]:
        return [cls.to_product_dto(product) for product in products]

    @classmethod
    def to_cart_item_dto(cls, product: ProductDTO, quantity: int) -> CartItemDTO:
        return CartItemDTO(
            product_id=product.product_id,
            product_name=product.product_name,
            unit_price=product.retail_price,
            quantity=quantity,
            stock_available=product.current_stock,
            cost_price=product.cost_price
        )

    @classmethod
    def to_sales_detail(cls, invoice_id: int, item: CartItemDTO) -> SalesDetail:
        return SalesDetail(
            invoice_id=invoice_id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price,
            cost_price=item.cost_price
        )

    @classmethod
    def to_sales_detail_list(cls, invoice_id: int, items: List[CartItemDTO]) -> List[SalesDetail]:
        return [cls.to_sales_detail(invoice_id, item) for item in items]

    @staticmethod
    def to_payment_method_value(payment_method_label: str) -> str:
        value = PAYMENT_METHOD_MAP.get((payment_method_label or "").strip())
        if value is None:
            logger.warning(
                "Phương thức thanh toán '%s' không hợp lệ, dùng mặc định '%s'.",
                payment_method_label, DEFAULT_PAYMENT_METHOD
            )
            return DEFAULT_PAYMENT_METHOD
        return value

    @staticmethod
    def to_invoice_code(invoice_id: int) -> str:
        return f"#INV-{invoice_id:03d}"
