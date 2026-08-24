import logging
from typing import List, Optional
from config.database import Database
from src.dtos.SupplierDTO import SupplierDTO
from src.repositories.impl.SupplierRepositoryImpl import SupplierRepositoryImpl
from src.converter.SupplierConverter import SupplierConverter
from src.services.SupplierService import SupplierService

# Cài đặt logger để theo dõi luồng chạy
logger = logging.getLogger(__name__)


class SupplierServiceImpl(SupplierService):
    def get_suppliers(self, keyword: Optional[str] = None) -> List[SupplierDTO]:
        try:
            # Mở luồng kết nối an toàn với CSDL
            with Database.get_session_ctx() as session:
                repo = SupplierRepositoryImpl(session)

                # 1. Kéo dữ liệu gốc (Entity) từ Database lên
                suppliers = repo.find_all(keyword=keyword)

                # 2. Dịch toàn bộ Entity thô thành DTO an toàn
                danh_sach_dto = [SupplierConverter.to_dto(s) for s in suppliers]

                logger.info("Tải thành công %d nhà cung cấp.", len(danh_sach_dto))
                return danh_sach_dto

        except Exception as e:
            logger.error("Lỗi ở tầng Service khi lấy danh sách nhà cung cấp: %s", e)
            return []  # Trả về mảng rỗng nếu có lỗi để giao diện không bị sập

    def add_supplier(self, data: dict) -> bool:
        from src.entities.supplier import Supplier

        try:
            with Database.get_session_ctx() as session:
                # Tạo đối tượng Entity mới từ dữ liệu Form gửi lên
                new_supplier = Supplier(
                    company_name=data.get('company_name'),
                    contact_name=data.get('contact_name'),
                    phone=data.get('phone'),
                    email=data.get('email'),
                    address=data.get('address')
                )

                # Lưu vào Database
                session.add(new_supplier)
                session.commit()
                return True

        except Exception as e:
            logger.error("Lỗi khi thêm Nhà cung cấp: %s", e)
            return False

    def update_supplier(self, supplier_id: str, data: dict) -> bool:
        from src.entities.supplier import Supplier
        try:
            with Database.get_session_ctx() as session:
                supplier = session.query(Supplier).filter(Supplier.supplier_id == int(supplier_id)).first()
                if not supplier:
                    return False

                supplier.company_name = data.get('company_name')
                supplier.contact_name = data.get('contact_name')
                supplier.phone = data.get('phone')
                supplier.email = data.get('email')
                supplier.address = data.get('address')

                session.commit()
                return True
        except Exception as e:
            logger.error("Lỗi khi cập nhật Nhà cung cấp: %s", e)
            return False

    def delete_supplier(self, supplier_id: str) -> bool:
        from src.entities.supplier import Supplier
        try:
            with Database.get_session_ctx() as session:
                supplier = session.query(Supplier).filter(Supplier.supplier_id == int(supplier_id)).first()
                if supplier:
                    session.delete(supplier)
                    session.commit()
                    return True
                return False
        except Exception as e:
            logger.error("Lỗi khi xóa Nhà cung cấp: %s", e)
            return False