import logging
from typing import List, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QDialog, QHeaderView, QTableWidgetItem, QWidget)

from src.dtos.CustomerDTO import CustomerDTO
from src.gui.customer_picker_ui import Ui_Dialog
from src.services.impl.CustomerServiceImpl import CustomerServiceImpl

logger = logging.getLogger(__name__)

COL_NAME = 0
COL_PHONE = 1

class CustomerPickerController(QDialog, Ui_Dialog):
    def __init__(self, parent: Optional[QWidget] = None, selected_customer: Optional[CustomerDTO] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.tblCustomers.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tblCustomers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self._service = CustomerServiceImpl()

        self.selected_customer: Optional[CustomerDTO] = None

        self._danh_sach: List[CustomerDTO] = []

        self._setup_table()
        self._setup_events()
        self._load_customers("")

    def _setup_table(self) -> None:
        self.tblCustomers.setColumnCount(2)
        self.tblCustomers.setHorizontalHeaderLabels(["Tên khách hàng", "Số điện thoại"])

        header = self.tblCustomers.horizontalHeader()
        header.setSectionResizeMode(COL_NAME, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(COL_PHONE, QHeaderView.ResizeMode.ResizeToContents)

        self.tblCustomers.verticalHeader().setVisible(False)
        self.tblCustomers.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblCustomers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblCustomers.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    def _setup_events(self) -> None:
        self.txtSearchCustomer.textChanged.connect(self._load_customers)

        self.tblCustomers.itemSelectionChanged.connect(self._cap_nhat_trang_thai_nut)

        self.tblCustomers.itemDoubleClicked.connect(lambda _item: self._on_select())

        self.btnSelect.clicked.connect(self._on_select)
        self.btnClearCustomer.clicked.connect(self._on_clear)
        self.btnCancel.clicked.connect(self.reject)

    def _load_customers(self, keyword: str) -> None:
        try:
            self._danh_sach = self._service.search_customers(keyword)
        except Exception as e:
            logger.exception("Không tải được danh sách khách hàng: %s", e)
            self._danh_sach = []
            self.lblStatus.setText("Không tải được danh sách khách hàng.")
            self.tblCustomers.setRowCount(0)
            self._cap_nhat_trang_thai_nut()
            return

        self._do_len_bang(self._danh_sach)
        self._cap_nhat_dong_trang_thai(keyword)
        self._cap_nhat_trang_thai_nut()

    def _do_len_bang(self, danh_sach: List[CustomerDTO]) -> None:
        self.tblCustomers.setRowCount(0)

        for dong, khach in enumerate(danh_sach):
            self.tblCustomers.insertRow(dong)

            o_ten = QTableWidgetItem(khach.ten_hien_thi)
            o_ten.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.tblCustomers.setItem(dong, COL_NAME, o_ten)

            o_sdt = QTableWidgetItem(khach.phone)
            o_sdt.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tblCustomers.setItem(dong, COL_PHONE, o_sdt)

    def _cap_nhat_dong_trang_thai(self, keyword: str) -> None:
        so_luong = len(self._danh_sach)

        if so_luong == 0:
            self.lblStatus.setText(
                f"Không tìm thấy khách hàng nào khớp '{keyword}'."
                if keyword.strip() else "Chưa có khách hàng nào trong hệ thống."
            )
            return

        self.lblStatus.setText(f"Tìm thấy {so_luong} khách hàng.")

    def _cap_nhat_trang_thai_nut(self) -> None:
        self.btnSelect.setEnabled(self._lay_dong_dang_chon() is not None)

    def _lay_dong_dang_chon(self) -> Optional[int]:
        dong_da_chon = self.tblCustomers.selectionModel().selectedRows()
        if not dong_da_chon:
            return None

        chi_so = dong_da_chon[0].row()

        if chi_so < 0 or chi_so >= len(self._danh_sach):
            return None

        return chi_so

    def _on_select(self) -> None:
        chi_so = self._lay_dong_dang_chon()
        if chi_so is None:
            return

        self.selected_customer = self._danh_sach[chi_so]
        logger.info("POS: đã chọn khách hàng id=%s.", self.selected_customer.customer_id)
        self.accept()

    def _on_clear(self) -> None:
        self.selected_customer = None
        logger.info("POS: bỏ gắn khách hàng, quay lại Khách lẻ.")
        self.accept()
