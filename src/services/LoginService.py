from abc import ABC, abstractmethod
from typing import Optional
from src.entities.user import User

class LoginService(ABC):
    @abstractmethod
    def login(self, username: str, password: str) -> Optional[User]:
        pass