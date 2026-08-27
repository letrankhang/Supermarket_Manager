import logging
import re
import secrets
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, Optional

from config.database import Database
from src.repositories.impl.UserRepositoryImpl import UserRepositoryImpl
from src.services.PasswordResetService import (
    CodeExpiredError,
    EmailNotFoundError,
    EmailSendError,
    InvalidCodeError,
    InvalidEmailError,
    InvalidResetTokenError,
    PasswordResetService,
    ResendTooSoonError,
    TooManyAttemptsError,
    WeakPasswordError,
)
from src.utils.EmailHelper import EmailHelper
from src.utils.PasswordHasher import hash_password


logger = logging.getLogger(__name__)

CODE_DIGITS = 6
CODE_LIFETIME = timedelta(minutes=5)           
RESET_TOKEN_LIFETIME = timedelta(minutes=10)  
MAX_FAILED_ATTEMPTS = 5
RESEND_COOLDOWN = timedelta(seconds=60)

MIN_PASSWORD_LENGTH = 8
BCRYPT_BYTE_LIMIT = 72  

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")

@dataclass
class _ResetSession:
    code: Optional[str]                   
    expires_at: datetime
    failed_attempts: int = 0
    reset_token: Optional[str] = field(default=None)

    def is_valid(self) -> bool:
        return datetime.now() < self.expires_at


class PasswordResetServiceImpl(PasswordResetService):
    _sessions: Dict[str, _ResetSession] = {}
    _last_sent_at: Dict[str, datetime] = {}


    def send_code(self, email: str) -> None:
        email = self._normalize_email(email)
        self._purge_expired()

        sent_at = self._last_sent_at.get(email)
        if sent_at:
            remaining = (sent_at + RESEND_COOLDOWN) - datetime.now()
            if remaining.total_seconds() > 0:
                raise ResendTooSoonError(
                    f"Vui lòng đợi {int(remaining.total_seconds()) + 1} giây nữa rồi hãy gửi lại mã."
                )
        with Database.get_session_ctx() as db_session:
            user = UserRepositoryImpl(db_session).find_by_email(email)

        if not user:
            logger.warning("Yêu cầu quên mật khẩu cho email không có trong hệ thống: %s", email)
            raise EmailNotFoundError(
                "Email này chưa được đăng ký cho tài khoản nào. "
                "Vui lòng kiểm tra lại hoặc liên hệ quản trị viên."
            )

        code = f"{secrets.randbelow(10 ** CODE_DIGITS):0{CODE_DIGITS}d}"

        minutes = int(CODE_LIFETIME.total_seconds() // 60)
        if not EmailHelper.send_verification_code(email, code, minutes):
            raise EmailSendError(
                "Không gửi được email chứa mã xác thực. "
                "Vui lòng kiểm tra kết nối mạng hoặc liên hệ quản trị viên."
            )

        self._last_sent_at[email] = datetime.now()
        self._sessions[email] = _ResetSession(code=code, expires_at=datetime.now() + CODE_LIFETIME)
        logger.info("Đã gửi mã xác thực đặt lại mật khẩu tới %s", email)


    def verify_code(self, email: str, code: str) -> str:
        email = self._normalize_email(email)
        self._purge_expired()

        reset_session = self._sessions.get(email)
        if not reset_session or not reset_session.code or not reset_session.is_valid():
            raise CodeExpiredError("Mã xác thực đã hết hạn hoặc chưa được gửi. Vui lòng bấm gửi lại mã.")

        if not secrets.compare_digest(reset_session.code, code.strip()):
            reset_session.failed_attempts += 1
            remaining = MAX_FAILED_ATTEMPTS - reset_session.failed_attempts
            if remaining <= 0:
                del self._sessions[email]
                logger.warning("Hủy mã xác thực của %s do nhập sai quá số lần cho phép.", email)
                raise TooManyAttemptsError(
                    "Bạn đã nhập sai mã quá số lần cho phép. Mã đã bị hủy, vui lòng gửi lại mã mới."
                )
            raise InvalidCodeError(f"Mã xác thực không đúng. Bạn còn {remaining} lần thử.")

        reset_session.code = None
        reset_session.failed_attempts = 0
        reset_session.reset_token = secrets.token_urlsafe(32)
        reset_session.expires_at = datetime.now() + RESET_TOKEN_LIFETIME

        logger.info("Xác thực mã đặt lại mật khẩu thành công cho %s", email)
        return reset_session.reset_token


    def reset_password(self, email: str, reset_token: str, new_password: str) -> None:
        email = self._normalize_email(email)
        self._purge_expired()

        reset_session = self._sessions.get(email)
        if (not reset_session or not reset_session.reset_token or not reset_session.is_valid()
                or not secrets.compare_digest(reset_session.reset_token, reset_token)):
            raise InvalidResetTokenError(
                "Phiên đặt lại mật khẩu không hợp lệ hoặc đã hết hạn. Vui lòng làm lại từ đầu."
            )

        self._validate_password(new_password)

        with Database.get_session_ctx() as db_session:
            repo = UserRepositoryImpl(db_session)
            user = repo.find_by_email(email)
            if not user:
                raise InvalidResetTokenError("Không tìm thấy tài khoản. Vui lòng làm lại từ đầu.")

            repo.update_password_hash(user.user_id, hash_password(new_password))

        del self._sessions[email]
        logger.info("Đặt lại mật khẩu thành công cho %s", email)


    @staticmethod
    def _normalize_email(email: str) -> str:
        email = (email or "").strip().lower()
        if not EMAIL_PATTERN.match(email):
            raise InvalidEmailError("Địa chỉ email không hợp lệ. Vui lòng kiểm tra lại.")
        return email


    @staticmethod
    def _validate_password(password: str) -> None:
        if len(password) < MIN_PASSWORD_LENGTH:
            raise WeakPasswordError(f"Mật khẩu phải có ít nhất {MIN_PASSWORD_LENGTH} ký tự.")

        if len(password.encode("utf-8")) > BCRYPT_BYTE_LIMIT:
            raise WeakPasswordError(f"Mật khẩu không được dài quá {BCRYPT_BYTE_LIMIT} byte.")

        if not any(char.isalpha() for char in password):
            raise WeakPasswordError("Mật khẩu phải có ít nhất một chữ cái.")

        if not any(char.isdigit() for char in password):
            raise WeakPasswordError("Mật khẩu phải có ít nhất một chữ số.")


    @classmethod
    def _purge_expired(cls) -> None:
        now = datetime.now()
        for email in [e for e, p in cls._sessions.items() if now >= p.expires_at]:
            del cls._sessions[email]
        for email in [e for e, t in cls._last_sent_at.items()
                      if now - t > RESEND_COOLDOWN]:
            del cls._last_sent_at[email]
