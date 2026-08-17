from abc import ABC, abstractmethod
from typing import Optional
from src.entities.user import User

class LoginRepository(ABC):

    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        pass