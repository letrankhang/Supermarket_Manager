from typing import Optional

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from src.controller.PasswordResetWorker import SendCodeWorker
from src.gui.forgot_password_ui import Ui_MainWindow
from src.utils.FormIcon import hien_thi_logo, them_icon_trai

# Luôn hiện cùng một câu dù email có tồn tại hay không, để không lộ tài khoản nào đã đăng ký
THONG_BAO_DA_GUI = (
    "Nếu email này có trong hệ thống, mã xác thực đã được gửi tới hộp thư của bạn. Vui lòng kiểm tra cả mục Spam."
)

class ForgotPasswordController(QMainWindow, Ui_MainWindow):
    """Bước 1: nhập email để nhận mã xác thực."""

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._worker: Optional[SendCodeWorker] = None
        self._setup_ui()
        self._setup_events()

    def _setup_ui(self) -> None:
        """Gắn logo và icon. Màu sắc nằm trong forgot_password.ui."""
        hien_thi_logo(self.lblLogo)
        them_icon_trai(self.lineEdit_email, "mail.png")

    def _setup_events(self) -> None:
        self.pushButton_accept.clicked.connect(self.handle_send_code)
        self.lineEdit_email.returnPressed.connect(self.handle_send_code)

    def handle_send_code(self) -> None:
        email = self.lineEdit_email.text().strip()
        if not email:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập email đã đăng ký.")
            return

        if self._worker and self._worker.isRunning():
            return

        self.pushButton_accept.setEnabled(False)
        self.pushButton_accept.setText("Đang gửi...")

        self._worker = SendCodeWorker(email, self)
        self._worker.thanh_cong.connect(lambda: self._on_sent(email))
        self._worker.that_bai.connect(self._on_error)
        self._worker.finished.connect(self._reset_button)
        self._worker.start()

    def _on_sent(self, email: str) -> None:
        QMessageBox.information(self, "Đã gửi mã", THONG_BAO_DA_GUI)

        # Nhập vòng ở đây để tránh hai controller import lẫn nhau lúc nạp module
        from src.controller.VerificationCodeController import VerificationCodeController

        self.code_window = VerificationCodeController(email)
        self.code_window.show()
        self.close()

    def _on_error(self, message: str) -> None:
        QMessageBox.critical(self, "Không gửi được mã", message)

    def _reset_button(self) -> None:
        self.pushButton_accept.setEnabled(True)
        self.pushButton_accept.setText("Gửi mã xác thực")
