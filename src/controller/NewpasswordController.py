import logging
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from src.gui.newpassword import Ui_MainWindow
from src.services.impl.NewpasswordServiceImpl import NewpasswordServiceImpl

logger = logging.getLogger(__name__)


class NewpasswordController(QMainWindow, Ui_MainWindow):
    def __init__(self, email: str):
        super().__init__()
        self._email = email
        self._newpassword_service = NewpasswordServiceImpl()
        self.setupUi(self)
        self._setup_ui()
        self._setup_events()

    def _setup_ui(self):
        # Thiết lập chế độ ẩn mật khẩu
        self.lineEdit_newpassword.setEchoMode(self.lineEdit_newpassword.EchoMode.Password)
        self.lineEdit_againpassword.setEchoMode(self.lineEdit_againpassword.EchoMode.Password)

    def _setup_events(self):
        # Kết nối sự kiện nút xác nhận và quay lại đăng nhập
        self.pushButton_accept.clicked.connect(self.handle_newpassword)
        self.pushButton_2.clicked.connect(self.handle_back_to_login)

    def handle_back_to_login(self):
        from src.controller.LoginController import LoginController
        self.login_window = LoginController()
        self.login_window.show()
        self.close()

    def handle_newpassword(self):
        new_password = self.lineEdit_newpassword.text().strip()
        again_password = self.lineEdit_againpassword.text().strip()
        if new_password == "" or again_password == "":
            QMessageBox.information(self, "Cảnh báo", "Vui lòng nhập đủ thông tin")
            return
        elif new_password != again_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới và mật khẩu nhập lại phải giống nhau")
            return

        try:
            success = self._newpassword_service.new_password(self._email, new_password)
            if success:
                QMessageBox.information(self, "Thành công", "Đổi mật khẩu mới thành công!")
                self.handle_back_to_login()
            else:
                QMessageBox.critical(self, "Thất bại", "Không thể cập nhật mật khẩu. Email không tồn tại.")
        except Exception as e:
            logger.error("Lỗi khi đặt lại mật khẩu cho email %s: %s", self._email, e)
            QMessageBox.critical(self, "Lỗi hệ thống", f"Đã xảy ra lỗi hệ thống: {str(e)}")
