"""src/repositories/impl/CustomerRepositoryImpl.py

Truy vấn bảng customers bằng SQLAlchemy.

Cách lọc từ khóa làm giống hệt POSRepositoryImpl._apply_keyword_filter để
hai màn hình cư xử như nhau.
"""

import logging
from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Query, Session

from src.entities.customer import Customer
from src.repositories.CustomerRepository import CustomerRepository

logger = logging.getLogger(__name__)


class CustomerRepositoryImpl(CustomerRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_customers(self, keyword: Optional[str] = None,
                       limit: Optional[int] = None) -> List[Customer]:
        try:
            query = self.session.query(Customer)
            query = self._apply_keyword_filter(query, keyword)
            query = query.order_by(Customer.full_name.asc())

            if limit is not None and limit > 0:
                query = query.limit(limit)

            return query.all()
        except Exception as e:
            logger.error("Lỗi khi truy vấn khách hàng (keyword=%s): %s", keyword, e)
            raise e

    def _apply_keyword_filter(self, query: Query, keyword: Optional[str]) -> Query:
        """Lọc theo tên HOẶC số điện thoại. Từ khóa rỗng thì bỏ qua bộ lọc."""
        cleaned_keyword = (keyword or "").strip()
        if not cleaned_keyword:
            return query

        pattern = f"%{cleaned_keyword}%"

        return query.filter(
            or_(
                Customer.full_name.ilike(pattern),
                Customer.phone.ilike(pattern)
            )
        )
