from abc import ABC, abstractmethod
from typing import List, Optional
from src.dtos.SupplierDTO import SupplierDTO

class SupplierService(ABC):
    @abstractmethod
    def get_suppliers(self, keyword: Optional[str] = None) -> List[SupplierDTO]:
        """
        Xử lý nghiệp vụ: Gọi Repository lấy dữ liệu Entity,
        sau đó dùng Converter để chuyển đổi thành danh sách SupplierDTO.
        """
        pass

    @abstractmethod
    def add_supplier(self, data: dict) -> bool:
        """Thêm một nhà cung cấp mới vào CSDL."""
        pass

    @abstractmethod
    def update_supplier(self, supplier_id: str, data: dict) -> bool:
        """Cập nhật thông tin nhà cung cấp."""
        pass

    @abstractmethod
    def delete_supplier(self, supplier_id: str) -> bool:
        """Xóa vĩnh viễn nhà cung cấp."""
        pass