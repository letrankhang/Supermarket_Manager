# File: src/repositories/ImportRepository.py
"""Interface cho tầng truy xuất dữ liệu Đơn nhập hàng."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from src.entities.import_order import ImportOrder


class ImportRepository(ABC):

    @abstractmethod
    def create(self, session: Session, order: ImportOrder) -> ImportOrder:
        ...

    @abstractmethod
    def get_by_id(self, session: Session, import_id: int) -> Optional[ImportOrder]:
        ...

    @abstractmethod
    def list_by_supplier(self, session: Session, supplier_id: int) -> List[ImportOrder]:
        ...

    @abstractmethod
    def list_all(self, session: Session) -> List[ImportOrder]:
        ...