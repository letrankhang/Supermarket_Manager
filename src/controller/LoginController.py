import logging
import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
from src.gui.login import Ui_MainWindow
from src.services.impl.LoginServiceImpl import LoginServiceImpl
from src.controller.MainWindowController import MainWindowController

logger = logging.getLogger(__name__)


class LoginController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._fix_logo()
        self._login_service = LoginServiceImpl()
        self._setup_events()

    def _fix_logo(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.abspath(os.path.join(current_dir, "..", "..", "assets", "images", "logo.png"))
        if os.path.exists(logo_path):
            self.label_4.setPixmap(QPixmap(logo_path))
        else:
            logger.error("Logo not found at path: %s", logo_path)


    def _setup_events(self):
        # Kết nối sự kiện nút đăng nhập
        self.pushButton_login.clicked.connect(self.handle_login)
        # Cho phép nhấn Enter ở username/password để đăng nhập
        self.lineEdit_username.returnPressed.connect(self.handle_login)
        self.lineEdit_passwprd.returnPressed.connect(self.handle_login)
        
        # Đặt chế độ hiển thị mật khẩu ẩn (Password mode) cho password field
        self.lineEdit_passwprd.setEchoMode(self.lineEdit_passwprd.EchoMode.Password)

    def handle_login(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_passwprd.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu.")
            return

        try:
            user = self._login_service.login(username, password)
            if user:
                # Đăng nhập thành công, mở MainWindowController
                self.main_window = MainWindowController()
                self.main_window.show()
                self.close()  # Đóng cửa sổ đăng nhập hiện tại
            else:
                QMessageBox.critical(self, "Lỗi đăng nhập", "Tên đăng nhập hoặc mật khẩu không chính xác.")
        except Exception as e:
            logger.error("Lỗi đăng nhập trong controller: %s", e)
            QMessageBox.critical(self, "Lỗi hệ thống", f"Đã xảy ra lỗi hệ thống: {str(e)}")