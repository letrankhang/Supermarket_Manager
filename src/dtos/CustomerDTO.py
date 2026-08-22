"""src/dtos/CustomerDTO.py

DTO khách hàng dùng cho màn hình POS.

Chỉ mang 3 thông tin tối thiểu để chọn và hiển thị khách trên hóa đơn.
Phần điểm tích lũy / hạng thành viên chưa cần tới nên không đưa vào đây.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CustomerDTO:
    """Một khách hàng hiển thị trong dialog chọn khách."""

    customer_id: int
    full_name: str
    phone: str

    @property
    def ten_hien_thi(self) -> str:
        """Tên để in lên nhãn 'Khách lẻ' của POS.

        Cột full_name trong bảng customers cho phép NULL, nên khách không có
        tên thì lấy tạm số điện thoại làm tên hiển thị.
        """
        return self.full_name or self.phone
