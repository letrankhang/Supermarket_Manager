import logging

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from src.controller.PasswordResetWorker import THONG_BAO_LOI_CHUNG
from src.gui.new_password_ui import Ui_MainWindow
from src.services.PasswordResetService import PasswordResetError
from src.services.impl.PasswordResetServiceImpl import PasswordResetServiceImpl
from src.utils.FormIcon import show_logo, add_left_icon, add_toggle_password_button

logger = logging.getLogger(__name__)


class NewPasswordController(QMainWindow, Ui_MainWindow):
    def __init__(self, email: str, reset_token: str) -> None:
        super().__init__()
        self._email = email
        self._reset_token = reset_token
        self._service = PasswordResetServiceImpl()

        self.setupUi(self)
        self._setup_ui()
        self._setup_events()

    def _setup_ui(self) -> None:

        show_logo(self.lblLogo)

        for o_nhap in (self.lineEdit_newpassword, self.lineEdit_againpassword):
            add_left_icon(o_nhap, "lock.png")
            add_toggle_password_button(o_nhap)

    def _setup_events(self) -> None:
        self.pushButton_accept.clicked.connect(self.handle_newpassword)
        self.lineEdit_againpassword.returnPressed.connect(self.handle_newpassword)
        self.btnBackToLogin.clicked.connect(self._go_to_login)

    def _go_to_login(self) -> None:
        from src.controller.LoginController import LoginController

        self.login_window = LoginController()
        self.login_window.show()
        self.close()

    def handle_newpassword(self) -> None:
        new_password = self.lineEdit_newpassword.text()
        again_password = self.lineEdit_againpassword.text()

        if not new_password or not again_password:
            QMessageBox.information(self, "Cảnh báo", "Vui lòng nhập đủ thông tin")
            return

        if new_password != again_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới và mật khẩu nhập lại phải giống nhau")
            return

        try:
            self._service.reset_password(self._email, self._reset_token, new_password)
        except PasswordResetError as e:
            QMessageBox.warning(self, "Không đổi được mật khẩu", str(e))
            return
        except Exception:
            logger.exception("Lỗi ngoài dự tính khi đặt lại mật khẩu cho %s", self._email)
            QMessageBox.critical(self, "Lỗi hệ thống", THONG_BAO_LOI_CHUNG)
            return

        QMessageBox.information(self, "Thành công", "Đổi mật khẩu mới thành công!")
        from src.controller.LoginController import LoginController
        
        self.login_window = LoginController()
        self.login_window.show()
        self.close()