from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from src.entities.base import Base

class User(Base):
    """
    User entity model mapped to the 'users' table.
    """
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    # Email dùng cho luồng quên mật khẩu. Khớp cột sẵn có dưới DB: VARCHAR(100), cho phép NULL
    email = Column(String(100))
    full_name = Column(String(100))
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    email = Column(String(100), unique=True, nullable=True)
    is_active = Column(Boolean, server_default='1', default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}', full_name='{self.full_name}', email='{self.email}')>"
