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

# Mã xác thực gồm 6 chữ số, đúng như nội dung email gửi cho người dùng
SO_CHU_SO_MA = 6
HAN_MA = timedelta(minutes=5)          # Phải khớp câu "có hiệu lực trong vòng 5 phút" trong email
HAN_VE_DAT_LAI = timedelta(minutes=10)  # Thời gian còn lại để đổi mật khẩu sau khi xác thực xong
SO_LAN_NHAP_SAI_TOI_DA = 5
CHO_GIUA_HAI_LAN_GUI = timedelta(seconds=60)

# Yêu cầu tối thiểu của mật khẩu mới
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


def _tao_noi_dung_email(code: str) -> str:
    """Dựng email thông báo mã xác thực. Nội dung là nghiệp vụ nên đặt ở tầng service."""
    return f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333333; margin: 0; padding: 0;">
        <div style="max-width: 600px; margin: 20px auto; padding: 20px; border: 1px solid #dddddd; border-radius: 8px; background-color: #ffffff;">
            <div style="text-align: center; border-bottom: 2px solid #1abc9c; padding-bottom: 10px; margin-bottom: 20px;">
                <h2 style="color: #2c3e50; margin: 0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">HỆ THỐNG QUẢN LÝ SIÊU THỊ</h2>
            </div>
            <p style="font-size: 16px;">Xin chào,</p>
            <p style="font-size: 16px;">Chúng tôi nhận được yêu cầu đặt lại mật khẩu cho tài khoản của bạn. Vui lòng sử dụng mã xác thực gồm 6 chữ số dưới đây để tiếp tục:</p>
            <div style="text-align: center; margin: 30px 0;">
                <span style="font-size: 32px; font-weight: bold; letter-spacing: 6px; color: #ffffff; background-color: #1abc9c; padding: 12px 25px; border-radius: 6px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    {code}
                </span>
            </div>
            <p style="font-size: 14px; color: #e74c3c; font-weight: bold;">Mã xác thực này có hiệu lực trong vòng 5 phút và chỉ sử dụng được một lần. Vui lòng không chia sẻ mã này cho bất kỳ ai.</p>
            <p style="font-size: 14px;">Nếu bạn không gửi yêu cầu này, vui lòng bỏ qua email này hoặc liên hệ với quản trị viên để đảm bảo an toàn tài khoản.</p>
            <hr style="border: 0; border-top: 1px solid #eeeeee; margin: 25px 0;">
            <p style="font-size: 12px; color: #7f8c8d; text-align: center; margin: 0;">Đây là email tự động từ Hệ thống Quản lý Siêu thị. Vui lòng không trả lời email này.</p>
        </div>
    </body>
    </html>
    """


class PasswordResetServiceImpl(PasswordResetService):
    # Kho tạm dùng chung cho mọi màn hình, nằm ở mức class nên các controller thấy cùng dữ liệu
    _phien: Dict[str, _PhienDatLai] = {}
    # Thời điểm gửi gần nhất, ghi cho MỌI email kể cả email không tồn tại,
    # để hành vi chờ giữa 2 lần gửi không tiết lộ email nào có trong hệ thống
    _lan_gui_cuoi: Dict[str, datetime] = {}

    # ------------------------------------------------------------------
    # Bước 1: gửi mã xác thực
    # ------------------------------------------------------------------
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
        if not EmailHelper.send(email, f"Mã xác thực đặt lại mật khẩu của bạn: {code}",
                                _tao_noi_dung_email(code)):
            raise EmailSendError(
                "Không gửi được email chứa mã xác thực. "
                "Vui lòng kiểm tra kết nối mạng hoặc liên hệ quản trị viên."
            )

        # Tuyệt đối không ghi giá trị mã ra log: đọc được log là chiếm được tài khoản
        self._phien[email] = _PhienDatLai(ma=code, het_han=datetime.now() + HAN_MA)
        logger.info("Đã gửi mã xác thực đặt lại mật khẩu tới %s", email)

    # ------------------------------------------------------------------
    # Bước 2: đối chiếu mã xác thực
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Bước 3: đổi mật khẩu
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Hàm dùng chung
    # ------------------------------------------------------------------
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
