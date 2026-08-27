from __future__ import annotations

from typing import Dict, Optional

from PySide6.QtWidgets import QDialog, QLineEdit, QWidget

from src.gui.user_dialog_ui import Ui_UserDialog

ADD_TITLE = "Thêm tài khoản"
EDIT_TITLE = "Sửa tài khoản"

DIALOG_WIDTH = 440

ROLE_NAMES = ["Admin", "Cashier", "Warehouse"]

ADD_PASSWORD_HINT = "Nhập mật khẩu"
EDIT_PASSWORD_HINT = "Để trống nếu không đổi mật khẩu"

ACTIVE_LABEL = "Hoạt động"
LOCKED_LABEL = "Đã khóa"

ACTIVE_STATUS = "Active"
INACTIVE_STATUS = "Inactive"


class UserDialog(QDialog, Ui_UserDialog):
    def __init__(
        self,
        mode: str = "add",
        user_data: Optional[Dict[str, str]] = None,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.mode = mode
        self.user_data = user_data

        self._setup_ui()
        self._setup_events()

        if self.mode == "edit" and self.user_data:
            self.load_data_to_form()


    def _setup_ui(self) -> None:
        is_edit = self.mode == "edit"

        self.setWindowTitle(EDIT_TITLE if is_edit else ADD_TITLE)
        self.lblHeaderTitle.setText(EDIT_TITLE if is_edit else ADD_TITLE)

        self.cboRole.clear()
        self.cboRole.addItems(ROLE_NAMES)

        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.txtPassword.setPlaceholderText(
            EDIT_PASSWORD_HINT if is_edit else ADD_PASSWORD_HINT
        )

        self.lblPassword.setText("Đổi mật khẩu:" if is_edit else "Mật khẩu:")
        self.btnSave.setText("Cập nhật" if is_edit else "Lưu")

        self.txtUsername.setEnabled(not is_edit)

        self.formLayout.setRowVisible(self.chkStatus, is_edit)
        if is_edit:
            self.chkStatus.setChecked(True)
            self._refresh_status_label()

        self.setFixedWidth(DIALOG_WIDTH)
        self.adjustSize()
        self.setFixedHeight(self.height())


    def _setup_events(self) -> None:
        self.btnCancel.clicked.connect(self.reject)
        self.btnSave.clicked.connect(self.accept)
        self.chkStatus.toggled.connect(self._refresh_status_label)


    def _refresh_status_label(self) -> None:
        self.chkStatus.setText(
            ACTIVE_LABEL if self.chkStatus.isChecked() else LOCKED_LABEL
        )


    def load_data_to_form(self) -> None:
        self.txtUsername.setText(self.user_data.get("username", ""))
        self.txtFullName.setText(self.user_data.get("full_name", ""))
        self.txtEmail.setText(self.user_data.get("email") or "")
        self.cboRole.setCurrentText(self.user_data.get("role_name", ""))

        self.chkStatus.setChecked(self.user_data.get("status") == ACTIVE_STATUS)
        self._refresh_status_label()


    def get_data(self) -> Dict[str, str]:
        data = {
            "username": self.txtUsername.text().strip(),
            "full_name": self.txtFullName.text().strip(),
            "email": self.txtEmail.text().strip(),
            "password": self.txtPassword.text().strip(),
            "role_name": self.cboRole.currentText(),
        }
        if self.mode == "edit":
            data["status"] = ACTIVE_STATUS if self.chkStatus.isChecked() else INACTIVE_STATUS
        return data
