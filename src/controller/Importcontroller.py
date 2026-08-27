import logging
from datetime import datetime, timedelta
from typing import List

from PySide6.QtCore import QObject, QThread, Signal as pyqtSignal, Qt
from PySide6.QtWidgets import (
    QHeaderView, QMessageBox, QTableWidgetItem, QWidget,
)

from src.dtos.ImportDTO import ImportOrderDTO
from src.gui.tabs.import_ui import Ui_ImportTab
from src.services.impl.ImportServiceImpl import ImportServiceImpl
from src.utils.FormIcon import add_awesome_left_icon, apply_awesome_icons
from src.utils.Theme import badge_cell


logger = logging.getLogger(__name__)

class _AsyncWorker(QObject):
    finished = pyqtSignal(object)
    failed = pyqtSignal(str)

    def __init__(self, func, *args, **kwargs) -> None:
        super().__init__()
        self._func, self._args, self._kwargs = func, args, kwargs


    def run(self) -> None:
        try:
            self.finished.emit(self._func(*self._args, **self._kwargs))
        except Exception as exc:
            logger.exception("ImportController worker loi")
            self.failed.emit(str(exc))

class ImportController(QWidget, Ui_ImportTab):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._service = ImportServiceImpl()
        self._active_threads: List[tuple] = []

        self._all_orders: List[ImportOrderDTO] = []
        self._filtered_orders: List[ImportOrderDTO] = []
        self._current_page = 1
        self._page_size = 10

        self._setup_events()


    def _setup_events(self) -> None:
        add_awesome_left_icon(self.txtSearch, "search")
        apply_awesome_icons(self)

        self.btnCreateOrder.clicked.connect(self._on_create_clicked)
        self.txtSearch.textChanged.connect(self._apply_filter)
        self.cboDate.currentIndexChanged.connect(self._apply_filter)
        self.btnPrev.clicked.connect(self._on_prev_page)
        self.btnNext.clicked.connect(self._on_next_page)

        header = self.tblImportOrders.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        self.tblImportOrders.setColumnWidth(3, 165)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        self.tblImportOrders.setColumnWidth(4, 165)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)


    def _on_create_clicked(self) -> None:
        from src.controller.CreateImportOrderDialogController import (CreateImportDialogController)

        dialog = CreateImportDialogController()

        if dialog.exec():
            self.load_data()


    def _on_prev_page(self) -> None:
        if self._current_page > 1:
            self._current_page -= 1
            self._render_current_page()


    def _on_next_page(self) -> None:
        total_items = len(self._filtered_orders)
        total_pages = max(1, (total_items + self._page_size - 1) // self._page_size)
        if self._current_page < total_pages:
            self._current_page += 1
            self._render_current_page()


    def load_data(self) -> None:
        self._run_async(self._service.get_all_import_orders, self._on_data_loaded)


    def _on_data_loaded(self, orders: List[ImportOrderDTO]) -> None:
        self._all_orders = orders
        self._update_statistics()
        self._apply_filter()


    def _update_statistics(self) -> None:
        now = datetime.now()


        total_spend = sum(
            order.total_amount for order in self._all_orders
            if order.import_date and order.import_date.month == now.month and order.import_date.year == now.year
        )
        self.lblTotalSpend.setText(f"đ {total_spend:,.0f}")

        seven_days_ago = now - timedelta(days=7)
        recent = sum(
            1 for order in self._all_orders
            if order.import_date and order.import_date >= seven_days_ago
        )
        self.lblRecent.setText(str(recent))


    def _apply_filter(self) -> None:
        keyword = self.txtSearch.text().strip().lower()
        now = datetime.now()
        date_index = self.cboDate.currentIndex()
        if date_index == 1:
            since = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif date_index in (2, 3):
            since = now - timedelta(days=7 if date_index == 2 else 30)
        else:
            since = None

        orders = self._all_orders
        if since:
            orders = [
                order for order in orders
                if order.import_date and order.import_date >= since
            ]
        if keyword:
            orders = [
                order for order in orders
                if keyword in str(order.import_id).lower()
                or keyword in (order.supplier_name or "").lower()
            ]

        self._filtered_orders = orders

        self._current_page = 1
        self._render_current_page()


    def _render_current_page(self) -> None:
        total_items = len(self._filtered_orders)
        total_pages = max(1, (total_items + self._page_size - 1) // self._page_size)

        if self._current_page > total_pages:
            self._current_page = total_pages
        if self._current_page < 1:
            self._current_page = 1

        start_idx = (self._current_page - 1) * self._page_size
        end_idx = min(start_idx + self._page_size, total_items)

        page_items = self._filtered_orders[start_idx:end_idx]
        self.tblImportOrders.setRowCount(len(page_items))

        for row, order in enumerate(page_items):
            date_text = order.import_date.strftime("%d/%m/%Y %H:%M") if order.import_date else ""
            creator = order.user_name or f"ID: {order.user_id}"

            item_id = QTableWidgetItem(str(order.import_id))
            item_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_supplier = QTableWidgetItem(order.supplier_name or "")

            item_date = QTableWidgetItem(date_text)
            item_date.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_total = QTableWidgetItem(f"{order.total_amount:,.0f} đ")
            item_total.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

            item_creator = QTableWidgetItem(creator)
            item_creator.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.tblImportOrders.setItem(row, 0, item_id)
            self.tblImportOrders.setItem(row, 1, item_supplier)
            self.tblImportOrders.setItem(row, 2, item_date)
            self.tblImportOrders.setItem(row, 3, item_total)
            self.tblImportOrders.setCellWidget(row, 4, badge_cell("Hoàn thành", "success"))
            self.tblImportOrders.setItem(row, 5, item_creator)

        if total_items == 0:
            self.lblPage.setText("Hiển thị 0 của 0 phiếu nhập")
        else:
            self.lblPage.setText(f"Hiển thị {start_idx + 1} đến {end_idx} của {total_items} phiếu nhập")

        self.btnPrev.setEnabled(self._current_page > 1)
        self.btnNext.setEnabled(self._current_page < total_pages)


    def _run_async(self, func, on_success, **kwargs) -> None:
        thread = QThread(self)
        worker = _AsyncWorker(func, **kwargs)
        worker.moveToThread(thread)
        pair = (thread, worker)
        self._active_threads.append(pair)

        def cleanup() -> None:
            thread.quit()
            thread.wait()
            if pair in self._active_threads:
                self._active_threads.remove(pair)

        thread.started.connect(worker.run)
        worker.finished.connect(on_success)
        worker.failed.connect(self.show_error)
        worker.finished.connect(cleanup)
        worker.failed.connect(cleanup)
        thread.start()


    def show_error(self, message: str) -> None:
        QMessageBox.warning(self, "Lỗi", message)