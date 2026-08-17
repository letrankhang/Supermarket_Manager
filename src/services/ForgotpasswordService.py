from abc import ABC, abstractmethod
from typing import Optional
from src.entities.user import User


class ForgotpasswordService(ABC):

    @abstractmethod
    def forgotpassword(self, email: str) -> Optional[User]:
        pass
