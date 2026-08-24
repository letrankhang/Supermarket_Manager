from dataclasses import dataclass

@dataclass
class SupplierDTO:
    """Đối tượng vận chuyển dữ liệu Nhà cung cấp lên giao diện."""
    supplier_id: str
    company_name: str
    contact_name: str
    phone: str
    email: str
    address: str