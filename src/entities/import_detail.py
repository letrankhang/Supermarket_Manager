from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.entities.base import Base

class ImportDetail(Base):
    __tablename__ = 'import_details'

    import_id = Column(Integer, ForeignKey('import_orders.import_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(15, 2), nullable=False)

    product = relationship("Product")

    def __repr__(self):
        return f"<ImportDetail(import_id={self.import_id}, product_id={self.product_id}, qty={self.quantity})>"
