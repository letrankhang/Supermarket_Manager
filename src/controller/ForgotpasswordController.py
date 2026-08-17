import logging
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from src.gui.forgotpassword import Ui_MainWindow
from src.services.impl.ForgotpasswordServiceImpl import ForgotpasswordServiceImpl

logger = logging.getLogger(__name__)


class ForgotpasswordController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._forgotpassword_service = ForgotpasswordServiceImpl()
        self._setup_events()

    def _setup_events(self):
        # Kết nối sự kiện cho nút "Quay lại đăng nhập"
        self.pushButton_2.clicked.connect(self.handle_back_to_login)
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

        try:
            user = self._forgotpassword_service.forgotpassword(email)
            if user:
                QMessageBox.information(
                    self,
                    "Thành công",
                    f"Mã xác thực đặt lại mật khẩu đã được gửi đến email: {email}"
                )
            else:
                QMessageBox.critical(
                    self,
                    "Thất bại",
                    "Không tìm thấy tài khoản nào được đăng ký với email này."
                )
        except Exception as e:
            logger.error("Lỗi xảy ra khi xử lý gửi liên kết đặt lại mật khẩu: %s", e)
            QMessageBox.critical(
                self,
                "Lỗi hệ thống",
                f"Đã xảy ra lỗi hệ thống: {str(e)}"
            )
