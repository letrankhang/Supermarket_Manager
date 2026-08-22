from abc import ABC, abstractmethod
from typing import List, Optional

from src.entities.category import Category
from src.entities.product import Product
from src.entities.sales_detail import SalesDetail
from src.entities.sales_invoice import SalesInvoice


class POSRepository(ABC):
    @abstractmethod
    def find_all_categories(self) -> List[Category]:
        pass

    @abstractmethod
    def find_products(self, category_id: Optional[int] = None,
                      keyword: Optional[str] = None,
                      limit: Optional[int] = None) -> List[Product]:
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
