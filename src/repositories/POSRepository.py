from abc import ABC, abstractmethod
from typing import Any, List, Optional, Tuple

from src.entities.category import Category
from src.entities.product import Product
from src.entities.sales_detail import SalesDetail
from src.entities.sales_invoice import SalesInvoice


class POSRepository(ABC):
    @abstractmethod
    def find_all_categories(self) -> List[Category]:
        pass

    @abstractmethod
    def find_products(self, category_id: Optional[int] = None, keyword: Optional[str] = None, limit: Optional[int] = None) -> List[Product]:
        pass

    @abstractmethod
    def find_product_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def find_product_by_barcode(self, barcode: str) -> Optional[Product]:
        pass

    @abstractmethod
    def find_products_by_ids(self, product_ids: List[int]) -> List[Product]:
        pass

    @abstractmethod
    def insert_invoice(self, invoice: SalesInvoice) -> SalesInvoice:
        pass

    @abstractmethod
    def insert_invoice_details(self, details: List[SalesDetail]) -> None:
        pass

    @abstractmethod
    def decrease_stock(self, product_id: int, quantity: int) -> None:
        pass

    @abstractmethod
    def find_invoice_by_id(self, invoice_id: int) -> Optional[SalesInvoice]:
        pass

    @abstractmethod
    def find_invoice_lines(self, invoice_id: int) -> List[Tuple[SalesDetail, Any]]:
        pass

    @abstractmethod
    def find_customer_name(self, customer_id: Optional[int]) -> Optional[str]:
        pass

    @abstractmethod
    def find_user_name(self, user_id: Optional[int]) -> Optional[str]:
        pass
