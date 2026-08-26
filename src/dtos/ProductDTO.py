from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class ProductDTO:
    product_id: Optional[int]
    barcode: str
    product_name: str
    category_id: Optional[int]
    category_name: Optional[str]
    unit: str
    retail_price: float
    current_stock: int
    avg_import_price: float
    image: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @property
    def is_low_stock(self) -> bool:
        return self.current_stock <= 0


@dataclass(frozen=True)
class CreateProductDTO:
    barcode: str
    product_name: str
    category_id: Optional[int]
    unit: str
    retail_price: float
    image: Optional[str] = None


@dataclass(frozen=True)
class UpdateProductDTO:
    product_id: int
    barcode: str
    product_name: str
    category_id: Optional[int]
    unit: str
    retail_price: float
    image: Optional[str] = None
