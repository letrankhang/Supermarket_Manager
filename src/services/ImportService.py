# File: src/services/ImportService.py
"""Interface (hop dong) cho nghiep vu Nhap hang.
Dinh nghia cac phuong thuc ma ImportServiceImpl phai trien khai,
tuan thu nguyen tac Dependency Inversion (SOLID) - giong pattern
cua LoginService / LoginServiceImpl."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from src.dtos.ImportDTO import CreateImportOrderDTO, ImportOrderDTO


class ImportService(ABC):

    @abstractmethod
    def create_import_order(self, dto: CreateImportOrderDTO) -> ImportOrderDTO:
        pass

    @abstractmethod
    def get_import_order(self, import_id: int) -> Optional[ImportOrderDTO]:
        pass

    @abstractmethod
    def get_all_import_orders(self) -> List[ImportOrderDTO]:
        pass

    @abstractmethod
    def get_import_orders_by_supplier(self, supplier_id: int) -> List[ImportOrderDTO]:
        pass