from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.entities.base import Base

class Product(Base):
    """
    Product entity model mapped to the 'products' table.
    """
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    barcode = Column(String(50), nullable=False, unique=True)
    product_name = Column(String(200), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    unit = Column(String(20))
    retail_price = Column(Numeric(15, 2), default=0.0)
    current_stock = Column(Integer, default=0)
    avg_import_price = Column(Numeric(15, 2), default=0.0)
    image = Column(String(500), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    category = relationship("Category", foreign_keys=[category_id])

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, name='{self.product_name}', stock={self.current_stock}, image='{self.image}')>"
