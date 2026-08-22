"""src/utils/PasswordHasher.py

Tiện ích băm và đối chiếu mật khẩu người dùng.

Toàn bộ nghiệp vụ liên quan tới mật khẩu tập trung tại đây (SRP), tầng service chỉ
gọi `verify_password` / `hash_password` mà không cần biết thuật toán bên dưới.

Chuẩn hiện tại là bcrypt. Hai định dạng cũ (SHA-256 và văn bản thuần) vẫn được
chấp nhận khi đối chiếu để các tài khoản tạo từ trước không bị khóa ngoài, nhưng
mọi mật khẩu mới đều được băm bằng bcrypt.
"""

import hashlib
import logging
import secrets
import string
from typing import Final

import bcrypt

logger = logging.getLogger(__name__)

# Tiền tố nhận diện chuỗi bcrypt theo từng phiên bản thuật toán
TIEN_TO_BCRYPT: Final[tuple[str, ...]] = ("$2a$", "$2b$", "$2x$", "$2y$")
SO_VONG_BCRYPT: Final[int] = 12          # Chi phí băm, càng cao càng chậm và càng an toàn
DO_DAI_SHA256: Final[int] = 64           # Độ dài chuỗi hex của SHA-256
GIOI_HAN_BYTE_BCRYPT: Final[int] = 72    # bcrypt chỉ xử lý tối đa 72 byte đầu tiên


def is_bcrypt_hash(chuoi_luu_tru: str) -> bool:
    """Kiểm tra một chuỗi trong cơ sở dữ liệu có phải hash bcrypt hay không."""
    return chuoi_luu_tru.startswith(TIEN_TO_BCRYPT)


def _la_hash_sha256(chuoi_luu_tru: str) -> bool:
    """Nhận diện hash SHA-256 dạng hex (định dạng cũ của dự án)."""
    return (
        len(chuoi_luu_tru) == DO_DAI_SHA256
        and all(ky_tu in string.hexdigits for ky_tu in chuoi_luu_tru)
    )


def hash_password(mat_khau: str) -> str:
    """Băm mật khẩu dạng văn bản thuần thành chuỗi bcrypt để lưu vào cơ sở dữ liệu.

    Raises:
        ValueError: Khi mật khẩu vượt quá giới hạn 72 byte của bcrypt.
    """
    mat_khau_bytes: bytes = mat_khau.encode("utf-8")
    if len(mat_khau_bytes) > GIOI_HAN_BYTE_BCRYPT:
        raise ValueError(f"Mật khẩu không được dài quá {GIOI_HAN_BYTE_BCRYPT} byte.")

    chuoi_hash: bytes = bcrypt.hashpw(mat_khau_bytes, bcrypt.gensalt(rounds=SO_VONG_BCRYPT))
    return chuoi_hash.decode("utf-8")


def verify_password(mat_khau: str, chuoi_luu_tru: str) -> bool:
    """Đối chiếu mật khẩu người dùng nhập với giá trị đang lưu trong cơ sở dữ liệu.

    Args:
        mat_khau: Mật khẩu dạng văn bản thuần do người dùng nhập.
        chuoi_luu_tru: Giá trị cột `users.password_hash`.

    Returns:
        True nếu mật khẩu khớp, ngược lại False.
    """
    if not mat_khau or not chuoi_luu_tru:
        return False

    # Định dạng chuẩn: bcrypt
    if is_bcrypt_hash(chuoi_luu_tru):
        try:
            return bcrypt.checkpw(mat_khau.encode("utf-8"), chuoi_luu_tru.encode("utf-8"))
        except ValueError:
            # Chuỗi hash bị cắt cụt hoặc sai định dạng -> coi như không khớp
            logger.error("Chuỗi bcrypt trong cơ sở dữ liệu không hợp lệ.")
            return False

    # Định dạng cũ: SHA-256
    if _la_hash_sha256(chuoi_luu_tru):
        logger.warning("Tài khoản đang dùng hash SHA-256 cũ, nên đổi mật khẩu để nâng cấp lên bcrypt.")
        hash_nhap_vao: str = hashlib.sha256(mat_khau.encode("utf-8")).hexdigest()
        return secrets.compare_digest(hash_nhap_vao, chuoi_luu_tru.lower())

    # Định dạng cũ: văn bản thuần
    logger.warning("Mật khẩu đang lưu dạng văn bản thuần, cần băm lại để bảo đảm an toàn.")
    return secrets.compare_digest(mat_khau, chuoi_luu_tru)
