from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from src.entities.user import User
from src.entities.role import Role

class UserRepository(ABC):
    # ... (giữ nguyên các hàm find_by_username, update_password_hash cũ) ...

    @abstractmethod
    def find_users_with_roles(self, keyword: Optional[str] = None) -> List[Tuple[User, Role]]:
        """Lấy danh sách người dùng kèm theo vai trò, lọc theo tên hoặc username."""
        pass