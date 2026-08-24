from abc import ABC, abstractmethod

class PasswordResetError(Exception):
    pass

class InvalidEmailError(PasswordResetError):
    pass

class EmailSendError(PasswordResetError):
    pass

class ResendTooSoonError(PasswordResetError):
    pass

class InvalidCodeError(PasswordResetError):
    pass

class CodeExpiredError(PasswordResetError):
    pass

class TooManyAttemptsError(PasswordResetError):
    pass

class InvalidResetTokenError(PasswordResetError):
    pass

class WeakPasswordError(PasswordResetError):
    pass

class PasswordResetService(ABC):

    @abstractmethod
    def send_code(self, email: str) -> None:
        pass

    @abstractmethod
    def verify_code(self, email: str, code: str) -> str:
        pass

    @abstractmethod
    def reset_password(self, email: str, reset_token: str, new_password: str) -> None:
        pass