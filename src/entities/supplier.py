from sqlalchemy import Column, Integer, String, Text, DateTime, func
from src.entities.base import Base

class Supplier(Base):
    """
    Supplier entity model mapped to the 'suppliers' table.
    """
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(200), nullable=False)
    contact_name = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Supplier(supplier_id={self.supplier_id}, company_name='{self.company_name}')>"
