import logging
from typing import Optional

from PySide6.QtCore import QObject, QThread, Signal

from src.services.PasswordResetService import PasswordResetError
from src.services.impl.PasswordResetServiceImpl import PasswordResetServiceImpl

logger = logging.getLogger(__name__)

GENERIC_ERROR_MESSAGE = "Đã xảy ra lỗi hệ thống. Vui lòng thử lại sau."


class SendCodeWorker(QThread):
    thanh_cong = Signal()
    that_bai = Signal(str) 


    def __init__(self, email: str, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self._email = email


    def run(self) -> None:
        try:
            PasswordResetServiceImpl().send_code(self._email)
            self.thanh_cong.emit()
        except PasswordResetError as e:
            self.that_bai.emit(str(e))
        except Exception:
            logger.exception("Lỗi ngoài dự tính khi gửi mã xác thực tới %s", self._email)
            self.that_bai.emit(GENERIC_ERROR_MESSAGE)