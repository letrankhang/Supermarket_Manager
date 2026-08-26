import logging
from typing import Optional

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.controller.ForgotPasswordController import ForgotPasswordController
from src.entities.user import User
from src.gui.login_ui import Ui_MainWindow
from src.services.impl.LoginServiceImpl import LoginServiceImpl
from src.utils.FormIcon import add_left_icon, add_toggle_password_button, show_logo
from src.utils.Session import Session

logger = logging.getLogger(__name__)


class LoginController(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._settings: QSettings = QSettings("SupermarketManager", "RetailProERP")
        self._login_service = LoginServiceImpl()

        self._show_logo()
        self._add_left_icons()
        self._add_toggle_password_button()
        self._setup_events()
        self._load_remembered_credentials()

    def _show_logo(self) -> None:
        show_logo(self.label_4)

    def _add_left_icons(self) -> None:
        add_left_icon(self.lineEdit_username, "person.png")
        add_left_icon(self.lineEdit_passwprd, "lock.png")

    def _add_toggle_password_button(self) -> None:
        add_toggle_password_button(self.lineEdit_passwprd)

    def _load_remembered_credentials(self) -> None:
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

                if saved_username and saved_password:
                    self.pushButton_login.setFocus()
                elif saved_username:
                    self.lineEdit_passwprd.setFocus()
        except Exception as e:
            logger.error("Error loading remembered credentials: %s", e)

    def _save_remembered_credentials(self, username: str, password: str) -> None:
        try:
            if self.checkBox.isChecked():
                self._settings.setValue("remember_me", True)
                self._settings.setValue("saved_username", username)
                self._settings.setValue("saved_password", password)
                logger.info("Saved credentials for user: %s", username)
            else:
                self._settings.setValue("remember_me", False)
                self._settings.remove("saved_username")
                self._settings.remove("saved_password")
                logger.info("Cleared saved credentials.")
        except Exception as e:
            logger.error("Error saving remembered credentials: %s", e)

    def _setup_events(self) -> None:
        self.pushButton_login.clicked.connect(self.handle_login)
        self.pushButton_forgotpassword.clicked.connect(self.handle_forgot_password)
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

                role_name: str = Session.get_role_name() or "Admin"
                role_map = {
                    "admin": "Quản trị viên",
                    "cashier": "Thu ngân",
                    "warehouse": "Nhân viên kho",
                }

                role_display = role_map.get(role_name.strip().lower(), role_name)
                display_name = user.full_name or user.username

                QMessageBox.information(
                    self,
                    "Đăng nhập thành công",
                    f"Chào mừng {display_name} đến với RetailPro ERP!\n"
                    f"Vai trò: {role_display}"
                )

                from src.controller.MainWindowController import MainWindowController
                self.main_window = MainWindowController()
                self.main_window.show()
                self.close()

            else:
                QMessageBox.critical(self, "Lỗi đăng nhập", "Tên đăng nhập hoặc mật khẩu không chính xác.")
        except Exception as e:
            logger.error("Login error in controller: %s", e)
            QMessageBox.critical(self, "Lỗi hệ thống", f"Đã xảy ra lỗi hệ thống: {str(e)}")

    def handle_forgot_password(self) -> None:
        self.forgot_window = ForgotPasswordController()
        self.forgot_window.show()
        self.close()