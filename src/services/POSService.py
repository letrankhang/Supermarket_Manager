from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Optional

from src.dtos.POSDTO import (
    CartDTO, CategoryDTO, CheckoutRequestDTO, CheckoutResultDTO, ProductDTO
)

class POSError(Exception):
    pass

class OutOfStockError(POSError):
    pass

class ProductNotFoundError(POSError):
    pass

class EmptyCartError(POSError):
    pass

class POSService(ABC):
    @abstractmethod
    def get_categories(self) -> List[CategoryDTO]:
        pass

    @abstractmethod
    def get_products(self, category_id: Optional[int] = None, keyword: Optional[str] = None) -> List[ProductDTO]:
        pass

    @abstractmethod
    def add_product_to_cart(self, product_id: int, quantity: int = 1) -> CartDTO:
        pass

    @abstractmethod
    def add_product_by_barcode(self, barcode: str) -> CartDTO:
        pass

    @abstractmethod
    def change_item_quantity(self, product_id: int, delta: int) -> CartDTO:
        pass

    @abstractmethod
    def remove_item_from_cart(self, product_id: int) -> CartDTO:
        pass

    @abstractmethod
    def clear_cart(self) -> CartDTO:
        pass

    @abstractmethod
    def get_cart(self) -> CartDTO:
        pass

    @abstractmethod
    def apply_discount_rate(self, discount_rate: Decimal) -> CartDTO:
        pass

    @abstractmethod
    def checkout(self, request: CheckoutRequestDTO) -> CheckoutResultDTO:
        pass
