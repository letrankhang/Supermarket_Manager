# File: src/services/ProductService.py
"""Interface (hop dong) cho nghiep vu Quan ly San pham.
Dinh nghia cac phuong thuc ma ProductServiceImpl phai trien khai,
tuan thu nguyen tac Dependency Inversion (SOLID) - giong pattern
cua LoginService / LoginServiceImpl va ImportService / ImportServiceImpl."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from src.dtos.ProductDTO import CreateProductDTO, ProductDTO, UpdateProductDTO


class ProductService(ABC):

    @abstractmethod
    def search_products(
        self, keyword: str = "", category_id: Optional[int] = None
    ) -> List[ProductDTO]:
        pass

    @abstractmethod
    def get_all_products(self) -> List[ProductDTO]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Optional[ProductDTO]:
        pass

    @abstractmethod
    def get_low_stock_products(self) -> List[ProductDTO]:
        pass

    @abstractmethod
    def create_product(self, dto: CreateProductDTO) -> ProductDTO:
        pass

    @abstractmethod
    def update_product(self, dto: UpdateProductDTO) -> ProductDTO:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        pass