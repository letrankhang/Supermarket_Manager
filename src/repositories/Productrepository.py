from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from src.entities.product import Product

ProductWithCategoryName = Tuple[Product, Optional[str]]


class ProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, session: Session, product_id: int) -> Optional[ProductWithCategoryName]:
        pass

    @abstractmethod
    def get_by_barcode(self, session: Session, barcode: str) -> Optional[ProductWithCategoryName]:
        pass

    @abstractmethod
    def search(self, session: Session, keyword: str = "", category_id: Optional[int] = None) -> List[ProductWithCategoryName]:
        pass

    @abstractmethod
    def list_all(self, session: Session) -> List[ProductWithCategoryName]:
        pass

    @abstractmethod
    def list_low_stock(self, session: Session, threshold: int) -> List[ProductWithCategoryName]:
        pass

    @abstractmethod
    def create(self, session: Session, product: Product) -> Product:
        pass

    @abstractmethod
    def update(self, session: Session, product: Product) -> Product:
        pass

    @abstractmethod
    def delete(self, session: Session, product_id: int) -> bool:
        pass

    @abstractmethod
    def increase_stock_after_import( self, session: Session, product_id: int, quantity: int, import_unit_price: float) -> None:
        pass