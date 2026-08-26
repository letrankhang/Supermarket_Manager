from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from src.entities.user import User
from src.entities.role import Role


class UserRepository(ABC):
    @abstractmethod
    def find_users_with_roles(self, keyword: Optional[str] = None) -> List[Tuple[User, Role]]:
        pass