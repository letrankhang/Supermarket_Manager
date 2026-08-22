import logging
from typing import Optional

from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from src.entities.user import User
from src.gui.login_ui import Ui_MainWindow
from src.services.impl.LoginServiceImpl import LoginServiceImpl
from src.controller.MainWindowController import MainWindowController
from src.utils.FormIcon import hien_thi_logo, them_icon_trai, them_nut_an_hien

logger = logging.getLogger(__name__)

class LoginController(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._settings: QSettings = QSettings("SupermarketManager", "RetailProERP")
        self._login_service = LoginServiceImpl()

        self._hien_thi_logo()
        self._them_icon_trai_textbox()
        self._them_nut_an_hien_mat_khau()
        self._setup_events()
        self._load_remembered_credentials()

    def _hien_thi_logo(self) -> None:
        """Vẽ logo trong khung label_4."""
        hien_thi_logo(self.label_4)

    def _them_icon_trai_textbox(self) -> None:
        """Gắn icon vào mép trái ô tên đăng nhập và ô mật khẩu."""
        them_icon_trai(self.lineEdit_username, "person.png", "user.png")
        them_icon_trai(self.lineEdit_passwprd, "lock.png")

    def _them_nut_an_hien_mat_khau(self) -> None:
        """Gắn nút con mắt vào ô mật khẩu. Kiểu dáng nút nằm trong login.ui."""
        them_nut_an_hien(self.lineEdit_passwprd)

    def _load_remembered_credentials(self) -> None:
        """Tải thông tin đăng nhập đã lưu từ QSettings nếu tùy chọn Ghi nhớ mật khẩu được bật."""
        try:
            remember_me: bool = self._settings.value("remember_me", False, type=bool)
            saved_username: str = self._settings.value("saved_username", "", type=str)
            saved_password: str = self._settings.value("saved_password", "", type=str)

            if remember_me:
                self.checkBox.setChecked(True)
                if saved_username:
                    self.lineEdit_username.setText(saved_username)
                if saved_password:
                    self.lineEdit_passwprd.setText(saved_password)

                # Focus vào ô mật khẩu hoặc nút đăng nhập nếu đã có đủ thông tin
                if saved_username and saved_password:
                    self.pushButton_login.setFocus()
                elif saved_username:
                    self.lineEdit_passwprd.setFocus()
        except Exception as e:
            logger.error("Lỗi khi tải thông tin ghi nhớ đăng nhập: %s", e)

    def _save_remembered_credentials(self, username: str, password: str) -> None:
        """Lưu hoặc xóa thông tin ghi nhớ đăng nhập theo trạng thái của checkBox."""
        try:
            if self.checkBox.isChecked():
                self._settings.setValue("remember_me", True)
                self._settings.setValue("saved_username", username)
                self._settings.setValue("saved_password", password)
                logger.info("Đã ghi nhớ thông tin đăng nhập cho người dùng: %s", username)
            else:
                self._settings.setValue("remember_me", False)
                self._settings.remove("saved_username")
                self._settings.remove("saved_password")
                logger.info("Bỏ ghi nhớ thông tin đăng nhập.")
        except Exception as e:
            logger.error("Lỗi khi lưu thông tin ghi nhớ đăng nhập: %s", e)

    # ------------------------------------------------------------------
    # Sự kiện và nghiệp vụ đăng nhập
    # ------------------------------------------------------------------
    def _setup_events(self) -> None:
        self.pushButton_login.clicked.connect(self.handle_login)
        self.pushButton_forgotpassword.clicked.connect(self.handle_forgot_password)
        # Cho phép nhấn Enter ở username/password để đăng nhập
        self.lineEdit_username.returnPressed.connect(self.handle_login)
        self.lineEdit_passwprd.returnPressed.connect(self.handle_login)

    def handle_login(self) -> None:
        username: str = self.lineEdit_username.text().strip()
        password: str = self.lineEdit_passwprd.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu.")
            return

        try:
            user: Optional[User] = self._login_service.login(username, password)

            if user:
                self._save_remembered_credentials(username, password)

                role = user.role_id
                role_map = {
                    "1": "Quản trị viên",
                    "2": "Quản lý",
                    "3": "Nhân viên",
                }

                role_display = role_map.get(str(role), f"Không xác định ({role})")
                display_name = user.full_name or user.username

                QMessageBox.information(self,
                    "Đăng nhập thành công",
                    f"Chào mừng {display_name} đến với RetailPro ERP!\n"
                    f"Vai trò: {role_display}"
                )

                self.main_window = MainWindowController()
                self.main_window.show()
                self.close()

            else:
                QMessageBox.critical(self, "Lỗi đăng nhập", "Tên đăng nhập hoặc mật khẩu không chính xác.")
        except Exception as e:
            logger.error("Lỗi đăng nhập trong controller: %s", e)
            QMessageBox.critical(self, "Lỗi hệ thống", f"Đã xảy ra lỗi hệ thống: {str(e)}")

    def handle_forgot_password(self) -> None:
        """Mở màn hình nhập email để nhận mã xác thực đặt lại mật khẩu."""
        # Nhập vòng ở đây để tránh hai controller import lẫn nhau lúc nạp module
        from src.controller.ForgotPasswordController import ForgotPasswordController

        self.forgot_window = ForgotPasswordController()
        self.forgot_window.show()
        self.close()
