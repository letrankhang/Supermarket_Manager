from abc import ABC, abstractmethod
from typing import Optional

from src.entities.user import User


class UserRepository(ABC):
    """Truy vấn bảng `users`. Một repository cho một bảng, dùng chung cho mọi nghiệp vụ."""

    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def update_password_hash(self, user_id: int, password_hash: str) -> bool:
        pass
