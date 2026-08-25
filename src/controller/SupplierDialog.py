from PySide6 import QtWidgets
from src.gui.supplier_dialog_ui import Ui_SupplierDialog


class SupplierDialog(QtWidgets.QDialog):
    def __init__(self, mode="add", supplier_data=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_SupplierDialog()
        self.ui.setupUi(self)

        self.mode = mode
        self.supplier_data = supplier_data

        # 1. THIẾT LẬP GIAO DIỆN DỰA THEO MODE (THÊM / SỬA)
        if self.mode == "edit":
            self.ui.lblHeader.setText("CẬP NHẬT NHÀ CUNG CẤP")
            self.ui.btnSave.setText("CẬP NHẬT")
            self.setWindowTitle("Sửa Nhà cung cấp")

            # Khóa ô Tên công ty không cho sửa (Tùy chọn: Nếu bạn muốn giống Username bên nhân sự)
            # self.ui.txtCompanyName.setEnabled(False)
            # self.ui.txtCompanyName.setStyleSheet("background-color: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px;")

            # Đổ dữ liệu cũ vào Form
            self.load_data_to_form()
        else:
            self.setWindowTitle("Thêm Nhà cung cấp")

        # 2. BẮT SỰ KIỆN NÚT BẤM
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnSave.clicked.connect(self.accept)

    def load_data_to_form(self):
        """Hàm này sẽ chạy khi bấm nút Sửa, lấy dữ liệu từ DB đổ lên giao diện"""
        if self.supplier_data:
            # Sử dụng str( ... or '') để chống lỗi văng app nếu dữ liệu dưới SQL Server bị NULL
            self.ui.txtCompanyName.setText(str(self.supplier_data.get('company_name') or ''))
            self.ui.txtContactName.setText(str(self.supplier_data.get('contact_name') or ''))
            self.ui.txtPhone.setText(str(self.supplier_data.get('phone') or ''))
            self.ui.txtEmail.setText(str(self.supplier_data.get('email') or ''))
            self.ui.txtAddress.setText(str(self.supplier_data.get('address') or ''))

    def get_data(self):
        """Hàm này chạy khi bấm nút Lưu/Cập nhật, gom chữ trên màn hình thành Dictionary"""
        return {
            "company_name": self.ui.txtCompanyName.text().strip(),
            "contact_name": self.ui.txtContactName.text().strip(),
            "phone": self.ui.txtPhone.text().strip(),
            "email": self.ui.txtEmail.text().strip(),
            "address": self.ui.txtAddress.text().strip()
        }