from abc import ABC, abstractmethod
from typing import Optional
from src.entities.user import User


class ForgotpasswordRepository(ABC):

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:

        pass
