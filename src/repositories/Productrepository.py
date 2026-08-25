# File: src/repositories/ProductRepository.py
"""Interface (hợp đồng) cho tầng truy xuất dữ liệu Product.
Không dùng SQLAlchemy relationship -> cac ham tra ve them ten danh muc
duoi dang tuple (Product, Optional[str]) thay vi chi tra ve Product."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from src.entities.product import Product

ProductWithCategoryName = Tuple[Product, Optional[str]]


class ProductRepository(ABC):

    @abstractmethod
    def get_by_id(self, session: Session, product_id: int) -> Optional[ProductWithCategoryName]:
        ...

    @abstractmethod
    def get_by_barcode(self, session: Session, barcode: str) -> Optional[ProductWithCategoryName]:
        ...

    @abstractmethod
    def search(
        self,
        session: Session,
        keyword: str = "",
        category_id: Optional[int] = None,
    ) -> List[ProductWithCategoryName]:
        ...

    @abstractmethod
    def list_all(self, session: Session) -> List[ProductWithCategoryName]:
        ...

    @abstractmethod
    def list_low_stock(self, session: Session, threshold: int) -> List[ProductWithCategoryName]:
        ...

    @abstractmethod
    def create(self, session: Session, product: Product) -> Product:
        ...

    @abstractmethod
    def update(self, session: Session, product: Product) -> Product:
        ...

    @abstractmethod
    def delete(self, session: Session, product_id: int) -> bool:
        ...

    @abstractmethod
    def increase_stock_after_import(
        self,
        session: Session,
        product_id: int,
        quantity: int,
        import_unit_price: float,
    ) -> None:
        """Cộng tồn kho và tính lại giá nhập bình quân gia quyền."""
        ...