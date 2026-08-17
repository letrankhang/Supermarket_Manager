import logging
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from src.gui.forgotpassword import Ui_MainWindow

logger = logging.getLogger(__name__)


class ForgotpasswordController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._setup_events()

    def _setup_events(self):
        # Kết nối sự kiện cho nút "Quay lại đăng nhập"
        self.pushButton_2.clicked.connect(self.handle_back_to_login)
        # Kết nối sự kiện cho nút "Gửi liên kết đặt lại"
        self.pushButton_glket.clicked.connect(self.handle_send_link)

    def handle_back_to_login(self):
        from src.controller.LoginController import LoginController
        self.login_window = LoginController()
        self.login_window.show()
        self.close()

    def handle_send_link(self):
        email = self.lineEdit_email.text().strip()
        if not email:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập địa chỉ email.")
            return

        # Hiển thị thông báo gửi liên kết thành công (giả lập)
        logger.info("Gửi liên kết đặt lại mật khẩu đến email: %s", email)
        QMessageBox.information(
            self,
            "Thành công",
            f"Liên kết đặt lại mật khẩu đã được gửi đến email: {email}"
        )
