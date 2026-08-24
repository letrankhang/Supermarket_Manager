from PyQt6 import QtWidgets, QtCore


class UserDialog(QtWidgets.QDialog):
    def __init__(self, mode="add", user_data=None, parent=None):
        super().__init__(parent)
        self.mode = mode  # "add" hoặc "edit"
        self.user_data = user_data
        self.setup_ui()
        if self.mode == "edit" and self.user_data:
            self.load_data_to_form()

    def setup_ui(self):
        self.setFixedSize(400, 550 if self.mode == "edit" else 500)
        self.setStyleSheet("background-color: white; font-size: 14px;")

        if self.mode == "add":
            self.setWindowTitle("Thêm tài khoản")
        else:
            self.setWindowTitle("Sửa tài khoản")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Tạo form
        form_layout = QtWidgets.QFormLayout()
        form_layout.setSpacing(10)

        # Style chung cho LineEdit
        input_style = "border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px;"

        self.txtUsername = QtWidgets.QLineEdit()
        self.txtUsername.setPlaceholderText("Nhập tên đăng nhập...")
        self.txtUsername.setStyleSheet(input_style)

        self.txtFullName = QtWidgets.QLineEdit()
        self.txtFullName.setPlaceholderText("Nhập họ và tên...")
        self.txtFullName.setStyleSheet(input_style)

        self.txtEmail = QtWidgets.QLineEdit()
        self.txtEmail.setPlaceholderText("Nhập email...")
        self.txtEmail.setStyleSheet(input_style)

        self.txtPassword = QtWidgets.QLineEdit()
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtPassword.setStyleSheet(input_style)
        if self.mode == "add":
            self.txtPassword.setPlaceholderText("Nhập mật khẩu...")
        else:
            self.txtPassword.setPlaceholderText("Để trống nếu không đổi mật khẩu...")
            self.txtUsername.setEnabled(False)  # Sửa thì không cho sửa username
            self.txtUsername.setStyleSheet(
                "background-color: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px;")

        self.cboRole = QtWidgets.QComboBox()
        self.cboRole.addItems(["Admin", "Manager", "Cashier"])
        self.cboRole.setStyleSheet(input_style)

        form_layout.addRow(self._create_label("Tên đăng nhập:"), self.txtUsername)
        form_layout.addRow(self._create_label("Họ và tên:"), self.txtFullName)
        form_layout.addRow(self._create_label("Email:"), self.txtEmail)

        pwd_label = "Mật khẩu:" if self.mode == "add" else "Đổi mật khẩu:"
        form_layout.addRow(self._create_label(pwd_label), self.txtPassword)
        form_layout.addRow(self._create_label("Chức vụ:"), self.cboRole)

        # Trạng thái (Chỉ hiện khi Sửa)
        if self.mode == "edit":
            self.chkStatus = QtWidgets.QCheckBox("Hoạt động")
            self.chkStatus.setStyleSheet("QCheckBox { color: #10b981; font-weight: bold; }")
            self.chkStatus.setChecked(True)
            form_layout.addRow(self._create_label("Trạng thái:"), self.chkStatus)

        layout.addLayout(form_layout)
        layout.addStretch()

        # Nút bấm Hủy / Lưu
        btn_layout = QtWidgets.QHBoxLayout()
        self.btnCancel = QtWidgets.QPushButton("HỦY")
        self.btnCancel.setStyleSheet(
            "background-color: #e2e8f0; color: #475569; padding: 10px; border-radius: 6px; font-weight: bold;")
        self.btnCancel.clicked.connect(self.reject)

        self.btnSave = QtWidgets.QPushButton("LƯU" if self.mode == "add" else "CẬP NHẬT")
        self.btnSave.setStyleSheet(
            "background-color: #3b82f6; color: white; padding: 10px; border-radius: 6px; font-weight: bold;")
        self.btnSave.clicked.connect(self.accept)

        btn_layout.addWidget(self.btnCancel)
        btn_layout.addWidget(self.btnSave)
        layout.addLayout(btn_layout)

    def _create_label(self, text):
        lbl = QtWidgets.QLabel(text)
        lbl.setStyleSheet("font-weight: bold; color: #334155;")
        return lbl

    def load_data_to_form(self):
        # Đổ dữ liệu cũ vào form khi sửa
        self.txtUsername.setText(self.user_data.get('username', ''))
        self.txtFullName.setText(self.user_data.get('full_name', ''))
        self.cboRole.setCurrentText(self.user_data.get('role_name', ''))
        if self.mode == "edit":
            is_active = self.user_data.get('status') == 'Active'
            self.chkStatus.setChecked(is_active)
            self.chkStatus.setText("Hoạt động" if is_active else "Đã khóa")
            self.chkStatus.setStyleSheet(
                f"QCheckBox {{ color: {'#10b981' if is_active else '#ef4444'}; font-weight: bold; }}")

    def get_data(self):
        # Trả về dữ liệu để Controller lưu vào Database
        data = {
            "username": self.txtUsername.text(),
            "full_name": self.txtFullName.text(),
            "email": self.txtEmail.text(),
            "password": self.txtPassword.text(),
            "role_name": self.cboRole.currentText()
        }
        if self.mode == "edit":
            data["status"] = "Active" if self.chkStatus.isChecked() else "Inactive"
        return data