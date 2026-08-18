from abc import ABC, abstractmethod

class NewpasswordRepository(ABC):
    @abstractmethod
    def update_password(self, email: str, new_password_plain: str) -> bool:
        pass
