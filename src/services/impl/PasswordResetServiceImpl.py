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

SO_CHU_SO_MA = 6
HAN_MA = timedelta(minutes=5)           # Truyền xuống EmailHelper để câu chữ trong thư khớp hạn thật
HAN_VE_DAT_LAI = timedelta(minutes=10)  # Thời gian còn lại để đổi mật khẩu sau khi xác thực xong
SO_LAN_NHAP_SAI_TOI_DA = 5
CHO_GIUA_HAI_LAN_GUI = timedelta(seconds=60)

DO_DAI_MAT_KHAU_TOI_THIEU = 8
GIOI_HAN_BYTE_BCRYPT = 72  # bcrypt chỉ xử lý 72 byte đầu, dài hơn sẽ bị cắt âm thầm

MAU_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")

@dataclass
class _PhienDatLai:
    """Trạng thái tạm của một lượt quên mật khẩu, sống trong bộ nhớ tiến trình."""

    ma: Optional[str]                       # None sau khi đã xác thực xong, để mã không dùng lại được
    het_han: datetime
    so_lan_sai: int = 0
    ve_dat_lai: Optional[str] = field(default=None)

    def con_hieu_luc(self) -> bool:
        return datetime.now() < self.het_han


class PasswordResetServiceImpl(PasswordResetService):
    # Kho tạm dùng chung cho mọi màn hình, nằm ở mức class nên các controller thấy cùng dữ liệu
    _phien: Dict[str, _PhienDatLai] = {}
    # Thời điểm gửi gần nhất, ghi cho MỌI email kể cả email không tồn tại,
    # để hành vi chờ giữa 2 lần gửi không tiết lộ email nào có trong hệ thống
    _lan_gui_cuoi: Dict[str, datetime] = {}

    def send_code(self, email: str) -> None:
        email = self._chuan_hoa_email(email)
        self._don_phien_het_han()

        # Chặn spam trước khi tra cứu, để email lạ và email thật phản hồi như nhau
        gui_lan_truoc = self._lan_gui_cuoi.get(email)
        if gui_lan_truoc:
            con_lai = (gui_lan_truoc + CHO_GIUA_HAI_LAN_GUI) - datetime.now()
            if con_lai.total_seconds() > 0:
                raise ResendTooSoonError(
                    f"Vui lòng đợi {int(con_lai.total_seconds()) + 1} giây nữa rồi hãy gửi lại mã."
                )
        self._lan_gui_cuoi[email] = datetime.now()

        with Database.get_session_ctx() as db_session:
            user = UserRepositoryImpl(db_session).find_by_email(email)

        if not user:
            # Kết thúc êm: không báo cho người gọi biết email này không tồn tại
            logger.warning("Yêu cầu quên mật khẩu cho email không có trong hệ thống: %s", email)
            return

        # secrets thay cho random: random đoán được nếu biết vài giá trị trước đó
        code = f"{secrets.randbelow(10 ** SO_CHU_SO_MA):0{SO_CHU_SO_MA}d}"

        # Gửi trước, gửi được rồi mới lưu, tránh để lại mã sống khi email hỏng
        so_phut = int(HAN_MA.total_seconds() // 60)
        if not EmailHelper.send_verification_code(email, code, so_phut):
            raise EmailSendError(
                "Không gửi được email chứa mã xác thực. "
                "Vui lòng kiểm tra kết nối mạng hoặc liên hệ quản trị viên."
            )

        # Tuyệt đối không ghi giá trị mã ra log: đọc được log là chiếm được tài khoản
        self._phien[email] = _PhienDatLai(ma=code, het_han=datetime.now() + HAN_MA)
        logger.info("Đã gửi mã xác thực đặt lại mật khẩu tới %s", email)

    def verify_code(self, email: str, code: str) -> str:
        email = self._chuan_hoa_email(email)
        self._don_phien_het_han()

        phien = self._phien.get(email)
        if not phien or not phien.ma or not phien.con_hieu_luc():
            raise CodeExpiredError("Mã xác thực đã hết hạn hoặc chưa được gửi. Vui lòng bấm gửi lại mã.")

        # compare_digest để thời gian so sánh không phụ thuộc nội dung, tránh dò mã qua độ trễ
        if not secrets.compare_digest(phien.ma, code.strip()):
            phien.so_lan_sai += 1
            con_lai = SO_LAN_NHAP_SAI_TOI_DA - phien.so_lan_sai
            if con_lai <= 0:
                del self._phien[email]
                logger.warning("Hủy mã xác thực của %s do nhập sai quá số lần cho phép.", email)
                raise TooManyAttemptsError(
                    "Bạn đã nhập sai mã quá số lần cho phép. Mã đã bị hủy, vui lòng gửi lại mã mới."
                )
            raise InvalidCodeError(f"Mã xác thực không đúng. Bạn còn {con_lai} lần thử.")

        # Xác thực xong thì mã hết giá trị ngay, đổi sang vé một lần cho bước đặt mật khẩu
        phien.ma = None
        phien.so_lan_sai = 0
        phien.ve_dat_lai = secrets.token_urlsafe(32)
        phien.het_han = datetime.now() + HAN_VE_DAT_LAI

        logger.info("Xác thực mã đặt lại mật khẩu thành công cho %s", email)
        return phien.ve_dat_lai

    def reset_password(self, email: str, reset_token: str, new_password: str) -> None:
        email = self._chuan_hoa_email(email)
        self._don_phien_het_han()

        phien = self._phien.get(email)
        if (not phien or not phien.ve_dat_lai or not phien.con_hieu_luc()
                or not secrets.compare_digest(phien.ve_dat_lai, reset_token)):
            raise InvalidResetTokenError(
                "Phiên đặt lại mật khẩu không hợp lệ hoặc đã hết hạn. Vui lòng làm lại từ đầu."
            )

        self._kiem_tra_mat_khau(new_password)

        with Database.get_session_ctx() as db_session:
            repo = UserRepositoryImpl(db_session)
            user = repo.find_by_email(email)
            if not user:
                raise InvalidResetTokenError("Không tìm thấy tài khoản. Vui lòng làm lại từ đầu.")

            # Băm ở tầng service, repository chỉ nhận chuỗi hash và ghi xuống DB
            repo.update_password_hash(user.user_id, hash_password(new_password))

        # Dùng xong thì hủy phiên, vé không tái sử dụng được
        del self._phien[email]
        logger.info("Đặt lại mật khẩu thành công cho %s", email)

    @staticmethod
    def _chuan_hoa_email(email: str) -> str:
        """Chuẩn hóa một lần tại đây để lúc gửi và lúc xác thực luôn tra cùng một khóa."""
        email = (email or "").strip().lower()
        if not MAU_EMAIL.match(email):
            raise InvalidEmailError("Địa chỉ email không hợp lệ. Vui lòng kiểm tra lại.")
        return email

    @staticmethod
    def _kiem_tra_mat_khau(mat_khau: str) -> None:
        """Kiểm tra độ mạnh mật khẩu mới. Đặt ở service để mọi nơi đổi mật khẩu đều theo cùng luật."""
        if len(mat_khau) < DO_DAI_MAT_KHAU_TOI_THIEU:
            raise WeakPasswordError(f"Mật khẩu phải có ít nhất {DO_DAI_MAT_KHAU_TOI_THIEU} ký tự.")

        if len(mat_khau.encode("utf-8")) > GIOI_HAN_BYTE_BCRYPT:
            raise WeakPasswordError(f"Mật khẩu không được dài quá {GIOI_HAN_BYTE_BCRYPT} byte.")

        if not any(ky_tu.isalpha() for ky_tu in mat_khau):
            raise WeakPasswordError("Mật khẩu phải có ít nhất một chữ cái.")

        if not any(ky_tu.isdigit() for ky_tu in mat_khau):
            raise WeakPasswordError("Mật khẩu phải có ít nhất một chữ số.")

    @classmethod
    def _don_phien_het_han(cls) -> None:
        """Xóa phiên và mốc gửi đã quá hạn, tránh hai kho tạm phình mãi khi chạy lâu."""
        bay_gio = datetime.now()
        for email in [e for e, p in cls._phien.items() if bay_gio >= p.het_han]:
            del cls._phien[email]
        for email in [e for e, t in cls._lan_gui_cuoi.items()
                      if bay_gio - t > CHO_GIUA_HAI_LAN_GUI]:
            del cls._lan_gui_cuoi[email]
