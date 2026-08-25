# File: src/dtos/ImportDTO.py
"""DTO cho nghiệp vụ Nhập hàng."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass(frozen=True)
class ImportDetailDTO:
    """Dòng chi tiết đã được lưu (dùng khi đọc dữ liệu ra)."""
    product_id: int
    product_name: Optional[str]
    quantity: int
    unit_price: float

    @property
    def line_total(self) -> float:
        return self.quantity * self.unit_price


@dataclass(frozen=True)
class ImportOrderDTO:
    """Đơn nhập hàng đã lưu (dùng khi đọc dữ liệu ra)."""
    import_id: Optional[int]
    supplier_id: int
    supplier_name: Optional[str]
    user_id: int
    import_date: Optional[datetime]
    total_amount: float
    note: Optional[str]
    details: List[ImportDetailDTO]
    user_name: Optional[str] = None


@dataclass(frozen=True)
class CreateImportLineDTO:
    """Một dòng sản phẩm khi tạo phiếu nhập mới (đầu vào)."""
    product_id: int
    quantity: int
    unit_price: float


@dataclass(frozen=True)
class CreateImportOrderDTO:
    """Toàn bộ dữ liệu đầu vào để tạo một phiếu nhập hàng."""
    supplier_id: int
    user_id: int
    note: Optional[str]
    lines: List[CreateImportLineDTO]
