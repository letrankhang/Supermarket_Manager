import logging
from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Query, Session

from src.entities.category import Category
from src.entities.product import Product
from src.entities.sales_detail import SalesDetail
from src.entities.sales_invoice import SalesInvoice
from src.repositories.POSRepository import POSRepository

logger = logging.getLogger(__name__)


class POSRepositoryImpl(POSRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all_categories(self) -> List[Category]:
        try:
            return self.session.query(Category)\
                .order_by(Category.category_name.asc())\
                .all()
        except Exception as e:
            logger.error("Lỗi khi truy vấn danh sách danh mục: %s", e)
            raise e

    def find_products(self, category_id: Optional[int] = None,
                      keyword: Optional[str] = None,
                      limit: Optional[int] = None) -> List[Product]:
        try:
            query = self.session.query(Product)
            query = self._apply_category_filter(query, category_id)
            query = self._apply_keyword_filter(query, keyword)
            query = query.order_by(Product.product_name.asc())

            if limit is not None and limit > 0:
                query = query.limit(limit)

            return query.all()
        except Exception as e:
            logger.error(
                "Lỗi khi truy vấn sản phẩm (category_id=%s, keyword=%s): %s",
                category_id, keyword, e
            )
            raise e

    def _apply_category_filter(self, query: Query, category_id: Optional[int]) -> Query:
        if category_id is None:
            return query
        return query.filter(Product.category_id == category_id)

    def _apply_keyword_filter(self, query: Query, keyword: Optional[str]) -> Query:
        cleaned_keyword = (keyword or "").strip()
        if not cleaned_keyword:
            return query

        pattern = f"%{cleaned_keyword}%"

        return query.filter(
            or_(
                Product.product_name.ilike(pattern),
                Product.barcode.ilike(pattern)
            )
        )

    def find_product_by_id(self, product_id: int) -> Optional[Product]:
        try:
            return self.session.query(Product)\
                .filter(Product.product_id == product_id)\
                .first()
        except Exception as e:
            logger.error("Lỗi khi truy vấn sản phẩm id=%s: %s", product_id, e)
            raise e

    def find_product_by_barcode(self, barcode: str) -> Optional[Product]:
        try:
            return self.session.query(Product)\
                .filter(Product.barcode == barcode)\
                .first()
        except Exception as e:
            logger.error("Lỗi khi truy vấn sản phẩm theo mã vạch %s: %s", barcode, e)
            raise e

    def find_products_by_ids(self, product_ids: List[int]) -> List[Product]:
        if not product_ids:
            return []
        try:
            return self.session.query(Product)\
                .filter(Product.product_id.in_(product_ids))\
                .all()
        except Exception as e:
            logger.error("Lỗi khi truy vấn sản phẩm theo danh sách ID %s: %s", product_ids, e)
            raise e

    def insert_invoice(self, invoice: SalesInvoice) -> SalesInvoice:
        try:
            self.session.add(invoice)
            self.session.flush()
            return invoice
        except Exception as e:
            logger.error("Lỗi khi ghi hóa đơn bán hàng: %s", e)
            raise e

    def insert_invoice_details(self, details: List[SalesDetail]) -> None:
        if not details:
            return
        try:
            self.session.add_all(details)
            self.session.flush()
        except Exception as e:
            logger.error("Lỗi khi ghi chi tiết hóa đơn: %s", e)
            raise e

    def decrease_stock(self, product_id: int, quantity: int) -> None:
        try:
            self.session.query(Product)\
                .filter(Product.product_id == product_id)\
                .update(
                    {Product.current_stock: Product.current_stock - quantity},
                    synchronize_session=False
                )
        except Exception as e:
            logger.error("Lỗi khi trừ tồn kho sản phẩm id=%s: %s", product_id, e)
            raise e
