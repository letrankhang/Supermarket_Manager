"""src/repositories/CustomerRepository.py

Interface tầng repository cho khách hàng.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.entities.customer import Customer


class CustomerRepository(ABC):
    @abstractmethod
    def find_customers(self, keyword: Optional[str] = None,
                       limit: Optional[int] = None) -> List[Customer]:
        """Lấy danh sách khách hàng, lọc theo tên hoặc số điện thoại.

        Args:
            keyword: Từ khóa tìm kiếm. Để trống thì lấy tất cả.
            limit: Giới hạn số dòng trả về, None là không giới hạn.

        Returns:
            Danh sách entity Customer, sắp xếp theo tên.
        """
        pass
