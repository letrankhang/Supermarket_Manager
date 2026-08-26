from PySide6 import QtWidgets
from src.gui.supplier_dialog_ui import Ui_SupplierDialog


class SupplierDialog(QtWidgets.QDialog):
    def __init__(self, mode="add", supplier_data=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_SupplierDialog()
        self.ui.setupUi(self)

        self.mode = mode
        self.supplier_data = supplier_data

        if self.mode == "edit":
            self.ui.lblHeaderTitle.setText("Cập nhật đối tác")
            self.ui.lblHeaderSubtitle.setText(
                "Chỉnh sửa thông tin liên hệ của nhà cung cấp. Mục có dấu (*) là bắt buộc."
            )
            self.ui.btnSave.setText("Cập nhật")
            self.setWindowTitle("Sửa nhà cung cấp")

            self.load_data_to_form()
        else:
            self.setWindowTitle("Thêm nhà cung cấp")

        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnSave.clicked.connect(self.accept)

        # Chieu cao bam theo noi dung, khong chua khoang trong thua
        self.setFixedWidth(480)
        self.adjustSize()
        self.setFixedHeight(self.height())


    def load_data_to_form(self):
        if self.supplier_data:
            self.ui.txtCompanyName.setText(str(self.supplier_data.get('company_name') or ''))
            self.ui.txtContactName.setText(str(self.supplier_data.get('contact_name') or ''))
            self.ui.txtPhone.setText(str(self.supplier_data.get('phone') or ''))
            self.ui.txtEmail.setText(str(self.supplier_data.get('email') or ''))
            self.ui.txtAddress.setText(str(self.supplier_data.get('address') or ''))


    def get_data(self):
        return {
            "company_name": self.ui.txtCompanyName.text().strip(),
            "contact_name": self.ui.txtContactName.text().strip(),
            "phone": self.ui.txtPhone.text().strip(),
            "email": self.ui.txtEmail.text().strip(),
            "address": self.ui.txtAddress.text().strip()
        }