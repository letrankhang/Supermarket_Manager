from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Enum, func
from sqlalchemy.orm import relationship
from src.entities.base import Base

class SalesInvoice(Base):
    __tablename__ = 'sales_invoices'

    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    invoice_date = Column(DateTime, server_default=func.now())
    sub_total = Column(Numeric(15, 2), nullable=False)
    points_used = Column(Integer, default=0)
    discount_amount = Column(Numeric(15, 2), default=0.0)
    tax_amount = Column(Numeric(15, 2), default=0.0)
    final_total = Column(Numeric(15, 2), nullable=False)
    payment_method = Column(Enum('Cash', 'Banking', 'E-Wallet', name='payment_method_enum'), server_default='Cash')

    customer = relationship("Customer", foreign_keys=[customer_id])
    user = relationship("User", foreign_keys=[user_id])
    details = relationship("SalesDetail", back_populates="invoice", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<SalesInvoice(invoice_id={self.invoice_id}, customer_id={self.customer_id}, total={self.final_total})>"
