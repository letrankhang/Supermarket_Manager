from sqlalchemy import Column, Integer, String, Text, DateTime, func
from src.entities.base import Base

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Category(category_id={self.category_id}, category_name='{self.category_name}')>"
