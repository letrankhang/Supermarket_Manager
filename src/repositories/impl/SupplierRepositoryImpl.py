import logging
from typing import List, Optional
from sqlalchemy import or_
from sqlalchemy.orm import Session
from src.entities.supplier import Supplier
from src.repositories.SupplierRepository import SupplierRepository

# Cài đặt logger để ghi log lỗi nếu có
logger = logging.getLogger(__name__)


class SupplierRepositoryImpl(SupplierRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self, keyword: Optional[str] = None) -> List[Supplier]:
        try:
            query = self.session.query(Supplier)
            cleaned_keyword = (keyword or "").strip()

            if cleaned_keyword:
                pattern = f"%{cleaned_keyword}%"
                query = query.filter(
                    or_(
                        Supplier.company_name.ilike(pattern),
                        Supplier.contact_name.ilike(pattern),
                        Supplier.phone.ilike(pattern)
                    )
                )
            # Sắp xếp danh sách theo tên công ty từ A-Z
            return query.order_by(Supplier.company_name.asc()).all()

        except Exception as e:
            logger.error("Lỗi khi truy vấn danh sách Nhà cung cấp (keyword=%s): %s", keyword, e)
            raise e