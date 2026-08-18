import logging
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from src.controller.LoginController import LoginController
from src.gui.verification_code import Ui_MainWindow
from src.services.impl.Verification_codeServiceImpl import VerificationCodeServiceImpl

logger = logging.getLogger(__name__)


class VerificationCodeController(QMainWindow, Ui_MainWindow):
    def __init__(self, email: str):
        super().__init__()
        self._email = email
        self._verification_service = VerificationCodeServiceImpl()
        self.setupUi(self)
        self._setup_events()

    def _setup_events(self) -> None:
        # Kết nối các sự kiện nút bấm
        self.pushButton_accept.clicked.connect(self.handle_verification_code)
        self.pushButton_2.clicked.connect(self.handle_login)

    def handle_verification_code(self) -> None:
        code = self.lineEdit_code.text().strip()
        if not code:
            QMessageBox.warning(self, "Thông báo!", "Vui lòng nhập mã xác thực")
            return
        
        try:
            # Gọi service để xác thực mã
            is_valid = self._verification_service.verify(self._email, code)
            if is_valid:
                logger.info("Xác thực mã thành công cho email: %s", self._email)
                QMessageBox.information(
                    self, 
                    "Thành công", 
                    "Xác thực mã thành công! Bạn có thể tiếp tục tiến trình đặt lại mật khẩu."
                )
                from src.controller.NewpasswordController import NewpasswordController
                self.reset_window = NewpasswordController(self._email)
                self.reset_window.show()
                self.close()
            else:
                logger.warning("Mã xác thực không chính xác cho email: %s", self._email)
                QMessageBox.critical(
                    self, 
                    "Thất bại", 
                    "Mã xác thực không hợp lệ. Vui lòng kiểm tra lại mã đã được gửi qua email."
                )
        except Exception as e:
            logger.error("Lỗi xảy ra trong quá trình xác thực mã: %s", e)
            QMessageBox.critical(self, "Lỗi hệ thống", f"Đã xảy ra lỗi: {str(e)}")

    def handle_login(self) -> None:
        self.login_window = LoginController()
        self.login_window.show()
        self.close()