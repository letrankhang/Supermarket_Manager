from sqlalchemy import Column, Integer, String, Date, Numeric, DateTime, ForeignKey, func
from src.entities.base import Base

class Customer(Base):
    """
    Customer entity model mapped to the 'customers' table.
    """
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(20), nullable=False, unique=True)
    full_name = Column(String(100))
    dob = Column(Date)
    total_points = Column(Integer, default=0)
    total_spent = Column(Numeric(15, 2), default=0.0)
    tier_id = Column(Integer, ForeignKey('customer_tiers.tier_id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Customer(customer_id={self.customer_id}, phone='{self.phone}', name='{self.full_name}')>"
