from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.entities.base import Base

class User(Base):
    """
    User entity model mapped to the 'users' table.
    """
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    full_name = Column(String(100))
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    is_active = Column(Boolean, server_default='1', default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    role = relationship("Role", foreign_keys=[role_id])

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}', full_name='{self.full_name}', email='{self.email}')>"
