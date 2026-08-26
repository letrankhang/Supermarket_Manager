from dataclasses import dataclass

@dataclass
class SupplierDTO:
    supplier_id: str
    company_name: str
    contact_name: str
    phone: str
    email: str
    address: str