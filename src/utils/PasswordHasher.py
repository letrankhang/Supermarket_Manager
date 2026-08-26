import hashlib
import logging
import secrets
import string
from typing import Final

import bcrypt


logger = logging.getLogger(__name__)

BCRYPT_PREFIXES: Final[tuple[str, ...]] = ("$2a$", "$2b$", "$2x$", "$2y$")
BCRYPT_ROUNDS: Final[int] = 12       
SHA256_LENGTH: Final[int] = 64
BCRYPT_BYTE_LIMIT: Final[int] = 72    


def is_bcrypt_hash(stored_hash: str) -> bool:
    return stored_hash.startswith(BCRYPT_PREFIXES)


def _is_sha256_hash(stored_hash: str) -> bool:
    return (
        len(stored_hash) == SHA256_LENGTH
        and all(char in string.hexdigits for char in stored_hash)
    )


def hash_password(password: str) -> str:
    password_bytes: bytes = password.encode("utf-8")
    if len(password_bytes) > BCRYPT_BYTE_LIMIT:
        raise ValueError(f"Mật khẩu không được dài quá {BCRYPT_BYTE_LIMIT} byte.")

    hash_text: bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt(rounds=BCRYPT_ROUNDS))
    return hash_text.decode("utf-8")


def verify_password(password: str, stored_hash: str) -> bool:
    if not password or not stored_hash:
        return False

    if is_bcrypt_hash(stored_hash):
        try:
            return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
        except ValueError:
            logger.error("Chuỗi bcrypt trong cơ sở dữ liệu không hợp lệ.")
            return False

    if _is_sha256_hash(stored_hash):
        logger.warning("Tài khoản đang dùng hash SHA-256 cũ, nên đổi mật khẩu để nâng cấp lên bcrypt.")
        candidate_hash: str = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return secrets.compare_digest(candidate_hash, stored_hash.lower())

    logger.warning("Mật khẩu đang lưu dạng văn bản thuần, cần băm lại để bảo đảm an toàn.")
    return secrets.compare_digest(password, stored_hash)
