from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from src.entities.base import Base

class SupplierProduct(Base):
    """
    SupplierProduct association model mapped to the 'supplier_products' table.
    Defines the relationship between Suppliers and Products.
    """
    __tablename__ = 'supplier_products'

    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    added_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<SupplierProduct(supplier_id={self.supplier_id}, product_id={self.product_id})>"
