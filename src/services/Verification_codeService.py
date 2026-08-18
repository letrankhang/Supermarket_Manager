from abc import ABC, abstractmethod

class VerificationCodeService(ABC):
    @abstractmethod
    def verify(self, email: str, code: str) -> bool:
        pass