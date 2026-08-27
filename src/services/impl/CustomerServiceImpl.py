import logging
from typing import List, Optional, Tuple

from config.database import Database
from src.dtos.CustomerDTO import CustomerDTO
from src.entities.customer import Customer
from src.entities.customer_tier import CustomerTier
from src.repositories.impl.CustomerRepositoryImpl import CustomerRepositoryImpl
from src.services.CustomerService import CustomerService


logger = logging.getLogger(__name__)

RESULT_LIMIT = 50

class CustomerServiceImpl(CustomerService):
    def search_customers(self, keyword: Optional[str] = None) -> List[CustomerDTO]:
        with Database.get_session_ctx() as session:
            repository = CustomerRepositoryImpl(session)
            customers = repository.find_customers(keyword=keyword, limit=RESULT_LIMIT)

            dtos = [self._to_dto(customer) for customer in customers]

        logger.info("Tìm khách hàng với từ khóa '%s': %d kết quả.", keyword or "", len(dtos))
        return dtos


    def _to_dto(self, customer: Customer) -> CustomerDTO:
        return CustomerDTO(
            customer_id=customer.customer_id,
            full_name=customer.full_name or "",
            phone=customer.phone or "",
        )


    @staticmethod
    def _resolve_tier_id(session, total_spent) -> Optional[int]:
        tier = (
            session.query(CustomerTier)
            .filter(CustomerTier.min_spent <= total_spent)
            .order_by(CustomerTier.min_spent.desc(), CustomerTier.tier_id.asc())
            .first()
        )
        return tier.tier_id if tier else None


    def get_tier_discount_percent(self, customer_id: Optional[int]) -> int:
        if not customer_id:
            return 0
        try:
            with Database.get_session_ctx() as session:
                customer = (
                    session.query(Customer)
                    .filter(Customer.customer_id == customer_id)
                    .first()
                )
                if not customer or not customer.tier_id:
                    return 0

                tier = session.query(CustomerTier).get(customer.tier_id)
                return int(tier.discount_percent or 0) if tier else 0
        except Exception as e:
            logger.error("Khong lay duoc muc giam theo hang cua khach ID=%s: %s", customer_id, e)
            return 0


    def add_purchase_points(self, customer_id: int, total_amount: float, point_rate: float = 10000.0) -> Tuple[int, int]:
        from decimal import Decimal

        amount_dec = Decimal(str(total_amount))
        rate_dec = Decimal(str(point_rate))

        earned_points = int(amount_dec // rate_dec)
        if earned_points < 0:
            earned_points = 0

        with Database.get_session_ctx() as session:
            customer = session.query(Customer).filter(Customer.customer_id == customer_id).first()
            if not customer:
                raise ValueError(f"Không tìm thấy khách hàng ID {customer_id}")

            current_spent = customer.total_spent if customer.total_spent is not None else Decimal("0")
            customer.total_spent = current_spent + amount_dec

            current_points = customer.total_points if customer.total_points is not None else 0
            customer.total_points = current_points + earned_points

            resolved_tier_id = self._resolve_tier_id(session, customer.total_spent)
            if resolved_tier_id is not None:
                customer.tier_id = resolved_tier_id

            session.commit()
            new_total_points = customer.total_points

        logger.info(
            "Khách hàng ID %d thanh toán %s đ: +%d điểm. Tổng điểm mới: %d",
            customer_id, amount_dec, earned_points, new_total_points
        )
        return earned_points, new_total_points