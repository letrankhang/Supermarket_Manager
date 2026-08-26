from sqlalchemy import Column, Integer, Numeric, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.entities.base import Base

class ImportOrder(Base):
    __tablename__ = 'import_orders'

    import_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    import_date = Column(DateTime, server_default=func.now())
    total_amount = Column(Numeric(15, 2), default=0.0)
    note = Column(Text)

    supplier = relationship("Supplier")
    details = relationship("ImportDetail")
    user = relationship("User")

    def __repr__(self):
        return f"<ImportOrder(import_id={self.import_id}, supplier_id={self.supplier_id}, total={self.total_amount})>"
