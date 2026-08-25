# File: src/controller/Importcontroller.py
"""Man hinh + Controller Nhap hang (gop View+Controller giong DashboardController).
Su dung truc tiep Ui_NhapHangTab tu import.ui va hop thoai CreateImportOrderDialogController.
Quy tac SRP va SOLID: logic nghiep vu goi qua ImportService, khong tinh toan tai day."""
from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import List, Optional

from PySide6.QtCore import QObject, QThread, Signal as pyqtSignal, Qt
from PySide6.QtWidgets import (
    QAbstractItemView, QHBoxLayout, QHeaderView, QMessageBox,
    QTableWidget, QTableWidgetItem, QWidget,
)

import importlib
from src.dtos.ImportDTO import ImportOrderDTO
from src.services.impl.ImportServiceImpl import ImportServiceImpl

# Load module 'import' containing keyword to bypass Python SyntaxError
_import_tab_module = importlib.import_module("src.gui.tabs.import")
Ui_NhapHangTab = _import_tab_module.Ui_NhapHangTab

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


class ImportController(QWidget, Ui_NhapHangTab):

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
        self.btnTaoPhieu.clicked.connect(self._on_create_clicked)
        self.cbTrangThai.currentIndexChanged.connect(self._on_filter_changed)
        self.btnPrev.clicked.connect(self._on_prev_page)
        self.btnNext.clicked.connect(self._on_next_page)

        # Thiet lap layout cho table
        header = self.tablePhieuNhap.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Mã
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # NCC
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # Ngày
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # Tổng tiền
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Trạng thái
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)  # Người tạo

    # ---------------- Hanh dong ----------------

    def _on_create_clicked(self) -> None:
        from src.controller.CreateImportOrderDialogController import (CreateImportDialogController)

        dialog = CreateImportDialogController()

        if dialog.exec():
            self.load_data()

    def _on_filter_changed(self) -> None:
        self._apply_filter()

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

    # ---------------- Nap va Loc du lieu ----------------

    def load_data(self) -> None:
        self._run_async(self._service.get_all_import_orders, self._on_data_loaded)

    def _on_data_loaded(self, orders: List[ImportOrderDTO]) -> None:
        self._all_orders = orders
        self._update_statistics()
        self._apply_filter()

    def _update_statistics(self) -> None:
        now = datetime.now()

        # 1. Tong chi thang nay
        tong_chi = sum(
            o.total_amount for o in self._all_orders
            if o.import_date and o.import_date.month == now.month and o.import_date.year == now.year
        )
        self.lblTongChi.setText(f"đ {tong_chi:,.0f}")

        # 2. Luot nhap gan day (7 ngay qua)
        seven_days_ago = now - timedelta(days=7)
        gan_day = sum(
            1 for o in self._all_orders
            if o.import_date and o.import_date >= seven_days_ago
        )
        self.lblGanDay.setText(str(gan_day))

    def _apply_filter(self) -> None:
        filter_text = self.cbTrangThai.currentText()
        if filter_text == "Chờ xử lý":
            self._filtered_orders = []
        else:
            self._filtered_orders = self._all_orders

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
        self.tablePhieuNhap.setRowCount(len(page_items))

        for row, o in enumerate(page_items):
            date_text = o.import_date.strftime("%d/%m/%Y %H:%M") if o.import_date else ""
            creator = o.user_name or f"ID: {o.user_id}"

            # Cot: Ma nhap
            item_id = QTableWidgetItem(str(o.import_id))
            item_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Cot: Nha cung cap
            item_supplier = QTableWidgetItem(o.supplier_name or "")

            # Cot: Ngay nhap
            item_date = QTableWidgetItem(date_text)
            item_date.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Cot: Tong tien
            item_total = QTableWidgetItem(f"{o.total_amount:,.0f} đ")
            item_total.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

            # Cot: Trang thai
            item_status = QTableWidgetItem("Hoàn thành")
            item_status.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Cot: Nguoi tao
            item_creator = QTableWidgetItem(creator)

            self.tablePhieuNhap.setItem(row, 0, item_id)
            self.tablePhieuNhap.setItem(row, 1, item_supplier)
            self.tablePhieuNhap.setItem(row, 2, item_date)
            self.tablePhieuNhap.setItem(row, 3, item_total)
            self.tablePhieuNhap.setItem(row, 4, item_status)
            self.tablePhieuNhap.setItem(row, 5, item_creator)

        if total_items == 0:
            self.lblPage.setText("Hiển thị 0-0 của 0 mục")
        else:
            self.lblPage.setText(f"Hiển thị {start_idx + 1}-{end_idx} của {total_items} mục")

        self.btnPrev.setEnabled(self._current_page > 1)
        self.btnNext.setEnabled(self._current_page < total_pages)

    # ---------------- Ha tang chung ----------------

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