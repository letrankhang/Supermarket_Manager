"""src/controller/PasswordResetWorker.py

Luồng nền gửi mã xác thực.

Gửi SMTP mất vài giây, gọi thẳng trên luồng giao diện sẽ làm cửa sổ đứng hình,
nên tách ra QThread giống cách DashboardController đang làm.
"""

import logging
from typing import Optional

from PyQt6.QtCore import QObject, QThread, pyqtSignal

from src.services.PasswordResetService import PasswordResetError
from src.services.impl.PasswordResetServiceImpl import PasswordResetServiceImpl

logger = logging.getLogger(__name__)

# Thông báo chung khi gặp lỗi ngoài dự tính, chi tiết kỹ thuật chỉ ghi vào log
THONG_BAO_LOI_CHUNG = "Đã xảy ra lỗi hệ thống. Vui lòng thử lại sau."


class SendCodeWorker(QThread):
    """Gọi PasswordResetService.send_code ở luồng nền."""

    thanh_cong = pyqtSignal()
    that_bai = pyqtSignal(str)  # Thông điệp tiếng Việt, hiển thị thẳng cho người dùng

    def __init__(self, email: str, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self._email = email

    def run(self) -> None:
        try:
            PasswordResetServiceImpl().send_code(self._email)
            self.thanh_cong.emit()
        except PasswordResetError as e:
            # Lỗi nghiệp vụ: thông điệp đã viết sẵn cho người dùng
            self.that_bai.emit(str(e))
        except Exception:
            logger.exception("Lỗi ngoài dự tính khi gửi mã xác thực tới %s", self._email)
            self.that_bai.emit(THONG_BAO_LOI_CHUNG)
