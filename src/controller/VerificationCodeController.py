import logging
from typing import Optional

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.controller.PasswordResetWorker import THONG_BAO_LOI_CHUNG, SendCodeWorker
from src.gui.verification_code_ui import Ui_MainWindow
from src.services.PasswordResetService import PasswordResetError
from src.services.impl.PasswordResetServiceImpl import (CHO_GIUA_HAI_LAN_GUI,
                                                        PasswordResetServiceImpl)
from src.utils.FormIcon import show_logo, add_left_icon

logger = logging.getLogger(__name__)

# Lấy thẳng từ service để đồng hồ đếm ngược không lệch với thời gian chờ thật
GIAY_CHO_GUI_LAI = int(CHO_GIUA_HAI_LAN_GUI.total_seconds())


class VerificationCodeController(QMainWindow, Ui_MainWindow):
    """Bước 2: nhập mã xác thực đã gửi qua email."""

    def __init__(self, email: str) -> None:
        super().__init__()
        self._email = email
        self._service = PasswordResetServiceImpl()
        self._worker: Optional[SendCodeWorker] = None

        # Một đồng hồ dùng lại cho mọi lượt đếm, tránh mỗi lần gửi lại đẻ thêm một cái
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._dem_nguoc)

        self.setupUi(self)
        self._setup_ui()
        self._setup_events()
        self._bat_dau_dem_nguoc()

    def _setup_ui(self) -> None:
        """Gắn logo và icon. Màu sắc nằm trong verification_code.ui."""
        show_logo(self.lblLogo)
        add_left_icon(self.lineEdit_code, "otp.png")

    def _setup_events(self) -> None:
        self.pushButton_accept.clicked.connect(self.handle_verification_code)
        self.lineEdit_code.returnPressed.connect(self.handle_verification_code)
        self.pushButton_resend.clicked.connect(self.handle_resend)
        self.lblBackLogin.clicked.connect(self._go_back_to_login)

    def _go_back_to_login(self) -> None:
        from src.controller.LoginController import LoginController

        self.login_window = LoginController()
        self.login_window.show()
        self.close()

    def handle_verification_code(self) -> None:
        code = self.lineEdit_code.text().strip()
        if not code:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập mã xác thực.")
            return

        try:
            reset_token = self._service.verify_code(self._email, code)
        except PasswordResetError as e:
            # Lỗi nghiệp vụ đã có thông điệp rõ ràng: sai mã, hết hạn, quá số lần thử
            QMessageBox.warning(self, "Xác thực thất bại", str(e))
            return
        except Exception:
            logger.exception("Lỗi ngoài dự tính khi xác thực mã cho %s", self._email)
            QMessageBox.critical(self, "Lỗi hệ thống", THONG_BAO_LOI_CHUNG)
            return

        QMessageBox.information(self, "Thành công", "Mã xác thực chính xác! Vui lòng tạo mật khẩu mới.")

        from src.controller.NewPasswordController import NewPasswordController

        self.reset_window = NewPasswordController(self._email, reset_token)
        self.reset_window.show()
        self.close()

    def handle_resend(self) -> None:
        if self._worker and self._worker.isRunning():
            return

        self.pushButton_resend.setEnabled(False)
        self._worker = SendCodeWorker(self._email, self)
        self._worker.thanh_cong.connect(self._on_resent)
        self._worker.that_bai.connect(self._on_resend_error)
        self._worker.start()

    def _on_resent(self) -> None:
        QMessageBox.information(self, "Đã gửi lại", "Mã xác thực mới đã được gửi tới email của bạn.")
        self.lineEdit_code.clear()
        self._bat_dau_dem_nguoc()

    def _on_resend_error(self, message: str) -> None:
        QMessageBox.warning(self, "Không gửi lại được", message)
        self.pushButton_resend.setEnabled(True)

    def _bat_dau_dem_nguoc(self) -> None:
        """Khóa nút gửi lại và đếm ngược, cho khớp thời gian chờ mà service áp dụng."""
        self._giay_con_lai = GIAY_CHO_GUI_LAI
        self.pushButton_resend.setEnabled(False)
        self._timer.start(1000)
        self._dem_nguoc()

    def _dem_nguoc(self) -> None:
        if self._giay_con_lai <= 0:
            self._timer.stop()
            self.pushButton_resend.setEnabled(True)
            self.pushButton_resend.setText("Gửi lại mã")
            return

        self.pushButton_resend.setText(f"Gửi lại mã sau {self._giay_con_lai}s")
        self._giay_con_lai -= 1
