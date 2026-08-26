from typing import Optional

from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.controller.PasswordResetWorker import SendCodeWorker
from src.gui.forgot_password_ui import Ui_MainWindow
from src.utils.FormIcon import add_left_icon, show_logo

MESSAGE_SENT = (
    "Nếu email này có trong hệ thống, mã xác thực đã được gửi tới hộp thư của bạn. \n"
    "Lưu ý: hãy kiểm tra cả mục Spam."
)

class ForgotPasswordController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._worker: Optional[SendCodeWorker] = None
        self.code_window = None  
        self._setup_ui()
        self._setup_events()


    def _setup_ui(self):
        show_logo(self.lblLogo)
        add_left_icon(self.lineEdit_email, "mail.png")


    def _setup_events(self):
        self.pushButton_accept.clicked.connect(self.handle_send_code)
        self.lineEdit_email.returnPressed.connect(self.handle_send_code)
        self.lblBackLogin.clicked.connect(self._go_back_to_login)


    def _go_back_to_login(self) -> None:
        from src.controller.LoginController import LoginController

        self.login_window = LoginController()
        self.login_window.show()
        self.close()


    def handle_send_code(self):
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
        
        self._worker.that_bai.connect(self._reset_button)
        self._worker.start()


    def _on_sent(self, email: str):
        QMessageBox.information(self, "Đã gửi mã", MESSAGE_SENT)

        from src.controller.VerificationCodeController import VerificationCodeController

        self.code_window = VerificationCodeController(email)
        self.code_window.show()
        self.close()


    def _on_error(self, message: str):
        QMessageBox.critical(self, "Không gửi được mã", message)


    def _reset_button(self):
        self.pushButton_accept.setEnabled(True)
        self.pushButton_accept.setText("Gửi mã xác thực")