from sqlalchemy import Column, Integer, Numeric, ForeignKey
from src.entities.base import Base

class SalesDetail(Base):
    """
    SalesDetail entity model mapped to the 'sales_details' table.
    """
    __tablename__ = 'sales_details'

    invoice_id = Column(Integer, ForeignKey('sales_invoices.invoice_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(15, 2), nullable=False)
    cost_price = Column(Numeric(15, 2), nullable=False)

    def __repr__(self):
        return f"<SalesDetail(invoice_id={self.invoice_id}, product_id={self.product_id}, qty={self.quantity})>"
