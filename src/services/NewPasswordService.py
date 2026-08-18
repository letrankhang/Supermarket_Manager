from abc import ABC, abstractmethod
class NewPasswordService(ABC):
    @abstractmethod
    def new_password(self, email: str, password: str) -> bool:
        pass