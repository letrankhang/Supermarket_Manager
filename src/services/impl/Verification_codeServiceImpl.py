from typing import Dict
from src.services.Verification_codeService import VerificationCodeService


class VerificationCodeServiceImpl(VerificationCodeService):
    # Static dictionary to store verification codes: email -> code
    _verification_codes: Dict[str, str] = {}

    @classmethod
    def store_code(cls, email: str, code: str) -> None:
        """
        Stores the verification code generated for an email in memory.
        """
        cls._verification_codes[email] = code

    def verify(self, email: str, code: str) -> bool:
        """
        Verifies if the entered code matches the stored code for the given email.
        """
        stored_code = self._verification_codes.get(email)
        return stored_code is not None and stored_code == code