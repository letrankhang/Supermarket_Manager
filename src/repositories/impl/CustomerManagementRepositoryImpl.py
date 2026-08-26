import logging
from datetime import date
from typing import List, Optional, Tuple

from sqlalchemy import or_, func
from sqlalchemy.orm import Session, joinedload

from src.entities.customer import Customer
from src.entities.customer_tier import CustomerTier
from src.repositories.CustomerManagementRepository import CustomerManagementRepository

logger = logging.getLogger(__name__)


class CustomerManagementRepositoryImpl(CustomerManagementRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all_customers(
        self,
        keyword: Optional[str] = None,
        tier_id: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List[Customer]:
        try:
            query = self.session.query(Customer).options(joinedload(Customer.tier))

            if keyword:
                cleaned = keyword.strip()
                if cleaned:
                    pattern = f"%{cleaned}%"
                    query = query.filter(
                        or_(
                            Customer.full_name.ilike(pattern),
                            Customer.phone.ilike(pattern),
                        )
                    )

            if tier_id is not None:
                query = query.filter(Customer.tier_id == tier_id)

            query = query.order_by(Customer.created_at.desc(), Customer.customer_id.desc())

            if limit is not None and limit > 0:
                query = query.limit(limit)

            return query.all()
        except Exception as e:
            logger.error("Lỗi khi truy vấn danh sách khách hàng (keyword=%s, tier_id=%s): %s", keyword, tier_id, e)
            raise e

    def find_customer_by_id(self, customer_id: int) -> Optional[Customer]:
        try:
            return (
                self.session.query(Customer)
                .options(joinedload(Customer.tier))
                .filter(Customer.customer_id == customer_id)
                .first()
            )
        except Exception as e:
            logger.error("Lỗi khi tìm khách hàng theo id=%s: %s", customer_id, e)
            raise e

    def find_customer_by_phone(self, phone: str) -> Optional[Customer]:
        try:
            return (
                self.session.query(Customer)
                .options(joinedload(Customer.tier))
                .filter(Customer.phone == phone.strip())
                .first()
            )
        except Exception as e:
            logger.error("Lỗi khi tìm khách hàng theo phone=%s: %s", phone, e)
            raise e

    def count_customers(self) -> int:
        try:
            val = self.session.query(func.count(Customer.customer_id)).scalar()
            return int(val or 0)
        except Exception as e:
            logger.error("Lỗi khi đếm tổng số khách hàng: %s", e)
            raise e

    def count_customers_by_tier(self) -> List[Tuple[str, int]]:
        try:
            results = (
                self.session.query(CustomerTier.tier_name, func.count(Customer.customer_id))
                .outerjoin(Customer, Customer.tier_id == CustomerTier.tier_id)
                .group_by(CustomerTier.tier_id, CustomerTier.tier_name)
                .all()
            )
            return [(str(row[0]), int(row[1] or 0)) for row in results]
        except Exception as e:
            logger.error("Lỗi khi đếm khách hàng theo từng hạng: %s", e)
            raise e

    def insert_customer(self, customer: Customer) -> Customer:
        try:
            self.session.add(customer)
            self.session.flush()
            return customer
        except Exception as e:
            logger.error("Lỗi khi thêm mới khách hàng (phone=%s): %s", customer.phone, e)
            raise e

    def update_customer(self, customer_id: int, phone: str, full_name: str, dob: Optional[date]) -> None:
        try:
            customer = self.session.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer:
                customer.phone = phone.strip()
                customer.full_name = full_name.strip()
                customer.dob = dob
                self.session.flush()
        except Exception as e:
            logger.error("Lỗi khi cập nhật khách hàng id=%s: %s", customer_id, e)
            raise e

    def delete_customer(self, customer_id: int) -> None:
        try:
            customer = self.session.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer:
                self.session.delete(customer)
                self.session.flush()
        except Exception as e:
            logger.error("Lỗi khi xóa khách hàng id=%s: %s", customer_id, e)
            raise e

    def get_all_tiers(self) -> List[CustomerTier]:
        try:
            return self.session.query(CustomerTier).order_by(CustomerTier.min_spent.asc()).all()
        except Exception as e:
            logger.error("Lỗi khi lấy danh sách hạng thành viên: %s", e)
            raise e
