from abc import ABC, abstractmethod
from typing import List, Optional
from src.dtos.SupplierDTO import SupplierDTO

class SupplierService(ABC):
    @abstractmethod
    def get_suppliers(self, keyword: Optional[str] = None) -> List[SupplierDTO]:
        pass

    @abstractmethod
    def add_supplier(self, data: dict) -> bool:
        pass

    @abstractmethod
    def update_supplier(self, supplier_id: str, data: dict) -> bool:
        pass

    @abstractmethod
    def delete_supplier(self, supplier_id: str) -> bool:
        pass