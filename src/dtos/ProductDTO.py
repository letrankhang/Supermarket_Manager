# File: src/dtos/ProductDTO.py
"""DTO cho nghiệp vụ Sản phẩm. Không phụ thuộc SQLAlchemy."""
from __future__ import annotations

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
        """Chỉ mang tính hiển thị nhanh; ngưỡng thật lấy từ settings ở tầng Service."""
        return self.current_stock <= 0


@dataclass(frozen=True)
class CreateProductDTO:
    """Dữ liệu đầu vào khi tạo mới sản phẩm (chưa có product_id)."""
    barcode: str
    product_name: str
    category_id: Optional[int]
    unit: str
    retail_price: float
    image: Optional[str] = None


@dataclass(frozen=True)
class UpdateProductDTO:
    """Dữ liệu đầu vào khi cập nhật sản phẩm."""
    product_id: int
    barcode: str
    product_name: str
    category_id: Optional[int]
    unit: str
    retail_price: float
    image: Optional[str] = None
