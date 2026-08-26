import logging
from datetime import date
from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget, QMessageBox
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont

from src.gui.customer_form_dialog_ui import Ui_CustomerFormDialog
from src.dtos.CustomerManagementDTO import CustomerDetailDTO, CustomerFormDTO


logger = logging.getLogger(__name__)

class CustomerFormDialog(QDialog, Ui_CustomerFormDialog):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        customer: Optional[CustomerDetailDTO] = None,
    ) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._customer = customer
        self._result_form: Optional[CustomerFormDTO] = None

        self.txtName.setAttribute(Qt.WidgetAttribute.WA_InputMethodEnabled, True)
        self.txtPhone.setAttribute(Qt.WidgetAttribute.WA_InputMethodEnabled, True)
        self.txtName.setFont(QFont("Segoe UI", 10))
        self.txtPhone.setFont(QFont("Segoe UI", 10))

        self._setup_events()
        self._prefill_data()


    @property
    def result_form(self) -> Optional[CustomerFormDTO]:
        return self._result_form


    def _setup_events(self) -> None:
        self.btnCancel.clicked.connect(self.reject)
        self.btnSave.clicked.connect(self._on_save)
        self.chkNoDob.toggled.connect(self._on_no_dob_toggled)


    def _prefill_data(self) -> None:
        if self._customer is not None:
            self.lblHeaderTitle.setText("Sửa thông tin khách hàng")
            self.lblHeaderSubtitle.setText(
                "Cập nhật thông tin liên hệ của khách hàng. Mục có dấu (*) là bắt buộc."
            )
            self.setWindowTitle("Sửa khách hàng")
            self.btnSave.setText("Lưu thay đổi")

            self.txtName.setText(self._customer.full_name)
            self.txtPhone.setText(self._customer.phone)
            if self._customer.dob:
                self.chkNoDob.setChecked(False)
                self.dateDob.setEnabled(True)
                self.dateDob.setDate(
                    QDate(self._customer.dob.year, self._customer.dob.month, self._customer.dob.day)
                )
            else:
                self.chkNoDob.setChecked(True)
                self.dateDob.setEnabled(False)
        else:
            self.lblHeaderTitle.setText("Thêm khách hàng mới")
            self.setWindowTitle("Thêm khách hàng mới")
            self.btnSave.setText("Thêm mới")
            self.chkNoDob.setChecked(True)
            self.dateDob.setEnabled(False)

        # Chieu cao bam theo noi dung, khong chua khoang trong thua truoc 2 nut
        self.setFixedWidth(460)
        self.adjustSize()
        self.setFixedHeight(self.height())


    def _on_no_dob_toggled(self, checked: bool) -> None:
        self.dateDob.setEnabled(not checked)


    def _on_save(self) -> None:
        name = self.txtName.text().strip()
        phone = self.txtPhone.text().strip()

        if not name:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập họ tên khách hàng.")
            self.txtName.setFocus()
            return

        if not phone:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập số điện thoại.")
            self.txtPhone.setFocus()
            return

        if len(phone) < 9 or not phone.replace("+", "").replace("-", "").isdigit():
            QMessageBox.warning(self, "Lỗi", "Số điện thoại không hợp lệ.")
            self.txtPhone.setFocus()
            return

        dob: Optional[date] = None
        if not self.chkNoDob.isChecked():
            q_date = self.dateDob.date()
            dob = date(q_date.year(), q_date.month(), q_date.day())

        self._result_form = CustomerFormDTO(phone=phone, full_name=name, dob=dob)
        self.accept()
