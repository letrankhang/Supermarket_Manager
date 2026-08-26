from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from src.entities.base import Base

class CustomerTier(Base):
    """
    CustomerTier entity model mapped to the 'customer_tiers' table.
    """
    __tablename__ = 'customer_tiers'

    tier_id = Column(Integer, primary_key=True, autoincrement=True)
    tier_name = Column(String(50), nullable=False)
    min_spent = Column(Numeric(15, 2), default=0.0)
    discount_percent = Column(Integer, default=0)

    # Relationships
    customers = relationship("Customer", back_populates="tier")

    def __repr__(self):
        return f"<CustomerTier(tier_id={self.tier_id}, tier_name='{self.tier_name}', discount={self.discount_percent}%)>"
