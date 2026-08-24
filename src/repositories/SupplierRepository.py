from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.supplier import Supplier

class SupplierRepository(ABC):
    @abstractmethod
    def find_all(self, keyword: Optional[str] = None) -> List[Supplier]:
        """
        Lấy danh sách nhà cung cấp từ Database.
        Hỗ trợ tìm kiếm theo tên công ty, người liên hệ hoặc SĐT.
        """
        pass