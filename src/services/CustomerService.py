"""src/services/CustomerService.py

Interface tầng service cho khách hàng.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.dtos.CustomerDTO import CustomerDTO


class CustomerService(ABC):
    @abstractmethod
    def search_customers(self, keyword: Optional[str] = None) -> List[CustomerDTO]:
        """Tìm khách hàng theo tên hoặc số điện thoại.

        Args:
            keyword: Từ khóa tìm kiếm. Để trống thì trả về danh sách mặc định.

        Returns:
            Danh sách CustomerDTO đã tách khỏi session, an toàn để đưa lên GUI.
        """
        pass
