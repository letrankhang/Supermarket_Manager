import logging
from typing import List, Optional, Tuple

from sqlalchemy import func

from config.database import Database
from src.converter.CustomerManagementConverter import CustomerManagementConverter
from src.dtos.CustomerManagementDTO import (
    CustomerDetailDTO,
    CustomerFormDTO,
    CustomerManagementDTO,
)
from src.entities.customer import Customer
from src.entities.sales_invoice import SalesInvoice
from src.repositories.impl.CustomerManagementRepositoryImpl import CustomerManagementRepositoryImpl
from src.services.CustomerManagementService import CustomerManagementService


logger = logging.getLogger(__name__)

class CustomerManagementServiceImpl(CustomerManagementService):
    def get_customers(
        self, keyword: Optional[str] = None, tier_id: Optional[int] = None
    ) -> CustomerManagementDTO:
        try:
            with Database.get_session_ctx() as session:
                repo = CustomerManagementRepositoryImpl(session)
                customers = repo.find_all_customers(keyword=keyword, tier_id=tier_id)
                tiers = repo.get_all_tiers()
                total_count = repo.count_customers()
                tier_counts = repo.count_customers_by_tier()

                dto = CustomerManagementConverter.to_customer_management_dto(
                    customers=customers,
                    tiers=tiers,
                    count=total_count,
                    tier_counts=tier_counts,
                )
            logger.info("Lấy dữ liệu khách hàng thành công: %d khách hàng tìm thấy.", len(dto.customers))
            return dto
        except Exception as e:
            logger.error("Lỗi trong CustomerManagementServiceImpl.get_customers: %s", e)
            raise e


    def add_customer(self, form: CustomerFormDTO) -> CustomerDetailDTO:
        try:
            with Database.get_session_ctx() as session:
                repo = CustomerManagementRepositoryImpl(session)

                existing = repo.find_customer_by_phone(form.phone)
                if existing:
                    raise ValueError(f"Số điện thoại '{form.phone}' đã được đăng ký cho khách hàng khác.")

                tiers = repo.get_all_tiers()
                default_tier = tiers[0] if tiers else None

                customer = Customer(
                    phone=form.phone.strip(),
                    full_name=form.full_name.strip(),
                    dob=form.dob,
                    total_points=0,
                    total_spent=0.0,
                    tier_id=default_tier.tier_id if default_tier else None,
                )
                saved_customer = repo.insert_customer(customer)
                dto = CustomerManagementConverter.to_customer_detail_dto(saved_customer, default_tier)

            logger.info("Thêm khách hàng thành công (ID=%s, Phone=%s)", dto.customer_id, dto.phone)
            return dto
        except ValueError:
            raise
        except Exception as e:
            logger.error("Lỗi khi thêm mới khách hàng: %s", e)
            raise e


    def update_customer(self, customer_id: int, form: CustomerFormDTO) -> None:
        try:
            with Database.get_session_ctx() as session:
                repo = CustomerManagementRepositoryImpl(session)

                customer = repo.find_customer_by_id(customer_id)
                if not customer:
                    raise ValueError(f"Không tìm thấy khách hàng với mã ID {customer_id}.")

                phone_check = repo.find_customer_by_phone(form.phone)
                if phone_check and phone_check.customer_id != customer_id:
                    raise ValueError(f"Số điện thoại '{form.phone}' đã được sử dụng bởi khách hàng khác.")

                repo.update_customer(
                    customer_id=customer_id,
                    phone=form.phone,
                    full_name=form.full_name,
                    dob=form.dob,
                )
            logger.info("Cập nhật thông tin khách hàng ID=%s thành công.", customer_id)
        except ValueError:
            raise
        except Exception as e:
            logger.error("Lỗi khi cập nhật khách hàng ID=%s: %s", customer_id, e)
            raise e


    def delete_customer(self, customer_id: int) -> None:
        try:
            with Database.get_session_ctx() as session:
                repo = CustomerManagementRepositoryImpl(session)

                customer = repo.find_customer_by_id(customer_id)
                if not customer:
                    raise ValueError(f"Không tìm thấy khách hàng với mã ID {customer_id}.")

                invoice_count = (
                    session.query(func.count(SalesInvoice.invoice_id))
                    .filter(SalesInvoice.customer_id == customer_id)
                    .scalar()
                )
                if invoice_count and invoice_count > 0:
                    raise ValueError(
                        f"Không thể xóa khách hàng '{customer.full_name or customer.phone}' "
                        f"do đã có {invoice_count} hóa đơn giao dịch trong hệ thống."
                    )

                repo.delete_customer(customer_id)
            logger.info("Xóa khách hàng ID=%s thành công.", customer_id)
        except ValueError:
            raise
        except Exception as e:
            logger.error("Lỗi khi xóa khách hàng ID=%s: %s", customer_id, e)
            raise e


    def get_tiers(self) -> List[Tuple[int, str]]:
        try:
            with Database.get_session_ctx() as session:
                repo = CustomerManagementRepositoryImpl(session)
                tiers = repo.get_all_tiers()
                return [(t.tier_id, t.tier_name) for t in tiers]
        except Exception as e:
            logger.error("Lỗi khi lấy danh sách hạng thành viên: %s", e)
            return []
