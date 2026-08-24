from src.dtos.SupplierDTO import SupplierDTO
# Giả sử bạn đã có class Supplier trong src.entities.supplier
from src.entities.supplier import Supplier

class SupplierConverter:
    @staticmethod
    def to_dto(supplier: Supplier) -> SupplierDTO:
        return SupplierDTO(
            supplier_id=str(supplier.supplier_id),
            company_name=supplier.company_name or "Chưa cập nhật",
            contact_name=supplier.contact_name or "N/A",
            phone=supplier.phone or "N/A",
            email=supplier.email or "N/A",
            address=supplier.address or "N/A"
        )