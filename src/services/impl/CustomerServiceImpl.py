"""src/services/impl/CustomerServiceImpl.py

Nghiệp vụ tìm kiếm khách hàng cho màn hình POS.

Việc đổi Entity sang DTO phải làm NGAY TRONG session. Ra khỏi khối
`with` là session đã đóng, đọc thuộc tính của entity sẽ ném
DetachedInstanceError.
"""

import logging
from typing import List, Optional

from config.database import Database
from src.dtos.CustomerDTO import CustomerDTO
from src.entities.customer import Customer
from src.repositories.impl.CustomerRepositoryImpl import CustomerRepositoryImpl
from src.services.CustomerService import CustomerService

logger = logging.getLogger(__name__)

# Giới hạn số khách nạp mỗi lần để dialog không đơ khi bảng lớn
GIOI_HAN_KET_QUA = 50


class CustomerServiceImpl(CustomerService):

    def search_customers(self, keyword: Optional[str] = None) -> List[CustomerDTO]:
        with Database.get_session_ctx() as session:
            repository = CustomerRepositoryImpl(session)
            customers = repository.find_customers(keyword=keyword, limit=GIOI_HAN_KET_QUA)

            # Đổi sang DTO khi session còn mở
            danh_sach = [self._to_dto(customer) for customer in customers]

        logger.info("Tìm khách hàng với từ khóa '%s': %d kết quả.", keyword or "", len(danh_sach))
        return danh_sach

    def _to_dto(self, customer: Customer) -> CustomerDTO:
        """Đổi entity Customer thành CustomerDTO, chỉ giữ 3 trường cần dùng."""
        return CustomerDTO(
            customer_id=customer.customer_id,
            full_name=customer.full_name or "",
            phone=customer.phone or "",
        )
