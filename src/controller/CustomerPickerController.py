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

        self._customers: List[CustomerDTO] = []

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

        self.tblCustomers.itemSelectionChanged.connect(self._update_button_state)

        self.tblCustomers.itemDoubleClicked.connect(lambda _item: self._on_select())

        self.btnSelect.clicked.connect(self._on_select)
        self.btnClearCustomer.clicked.connect(self._on_clear)
        self.btnCancel.clicked.connect(self.reject)


    def _load_customers(self, keyword: str) -> None:
        try:
            self._customers = self._service.search_customers(keyword)
        except Exception as e:
            logger.exception("Không tải được danh sách khách hàng: %s", e)
            self._customers = []
            self.lblStatus.setText("Không tải được danh sách khách hàng.")
            self.tblCustomers.setRowCount(0)
            self._update_button_state()
            return

        self._fill_table(self._customers)
        self._update_status_line(keyword)
        self._update_button_state()


    def _fill_table(self, dtos: List[CustomerDTO]) -> None:
        self.tblCustomers.setRowCount(0)

        for row, customer in enumerate(dtos):
            self.tblCustomers.insertRow(row)

            name_cell = QTableWidgetItem(customer.display_name)
            name_cell.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.tblCustomers.setItem(row, COL_NAME, name_cell)

            phone_cell = QTableWidgetItem(customer.phone)
            phone_cell.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tblCustomers.setItem(row, COL_PHONE, phone_cell)


    def _update_status_line(self, keyword: str) -> None:
        count = len(self._customers)

        if count == 0:
            self.lblStatus.setText(
                f"Không tìm thấy khách hàng nào khớp '{keyword}'."
                if keyword.strip() else "Chưa có khách hàng nào trong hệ thống."
            )
            return

        self.lblStatus.setText(f"Tìm thấy {count} khách hàng.")


    def _update_button_state(self) -> None:
        self.btnSelect.setEnabled(self._selected_row_index() is not None)


    def _selected_row_index(self) -> Optional[int]:
        selected_rows = self.tblCustomers.selectionModel().selectedRows()
        if not selected_rows:
            return None

        index = selected_rows[0].row()

        if index < 0 or index >= len(self._customers):
            return None

        return index


    def _on_select(self) -> None:
        index = self._selected_row_index()
        if index is None:
            return

        self.selected_customer = self._customers[index]
        logger.info("POS: đã chọn khách hàng id=%s.", self.selected_customer.customer_id)
        self.accept()


    def _on_clear(self) -> None:
        self.selected_customer = None
        logger.info("POS: bỏ gắn khách hàng, quay lại Khách lẻ.")
        self.accept()
