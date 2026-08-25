# File: src/controller/ProductController.py
"""Controller cho man hinh Quan ly San pham, ke thua UI that tu products.ui
(Ui_SanPhamTab trong src/gui/tabs/products.py). Du lieu di qua ProductService
-> DTO, khong dung Entity/SQLAlchemy truc tiep o day."""
from __future__ import annotations

import logging
from typing import List, Optional

from PySide6.QtCore import QObject, Qt, QThread, Signal as pyqtSignal
from PySide6.QtWidgets import (
    QDialog, QHBoxLayout, QLabel, QMessageBox,
    QPushButton, QTableWidgetItem, QWidget,
)

from config.settings import POSSettings
from src.dtos.CategoryDTO import CategoryDTO
from src.dtos.ProductDTO import ProductDTO
from src.gui.tabs.products import Ui_SanPhamTab
from src.services.CategoryService import CategoryService
from src.services.impl.ProductServiceImpl import ProductServiceImpl
from src.utils.Session import Session

logger = logging.getLogger(__name__)

_PAGE_SIZE = 10
_MAX_VISIBLE_PAGE_BUTTONS = 3  # so nut so trang hien thi truc tiep truoc dau "..."

# Chi so cot trong tableSanPham (7 cot, khong con checkbox va cot thao tac)
_COL_BARCODE, _COL_NAME, _COL_CATEGORY, _COL_UNIT, \
    _COL_PRICE, _COL_STOCK, _COL_STATUS = range(7)

# Style badge trang thai, khop mau voi ban mau
_STATUS_STYLE = {
    "Hết hàng": "background:#fee2e2; color:#dc2626;",
    "Sắp hết": "background:#ffedd5; color:#ea580c;",
    "Còn hàng": "background:#dbeafe; color:#1d4ed8;",
}


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
            logger.exception("ProductController worker loi")
            self.failed.emit(str(exc))


class ProductController(QWidget, Ui_SanPhamTab):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._service = ProductServiceImpl()
        self._category_service = CategoryService()
        self._active_threads: List[tuple] = []  # giu tham chieu Python de tranh GC luong dang chay

        self._all_products: List[ProductDTO] = []
        self._current_page: int = 1
        self._categories_seeded = False
        self._page_number_buttons: List[QPushButton] = []

        self._setup_events()

    # ---------------- Su kien ----------------

    def _setup_events(self) -> None:
        self.btnThem.clicked.connect(self._open_create_dialog)
        self.btnThemdm.clicked.connect(self._open_create_category_dialog)
        self.edtSearch.returnPressed.connect(self._apply_filters)
        self.cbDanhMuc.currentIndexChanged.connect(self._apply_filters)
        self.btnsua.clicked.connect(self._edit_selected_product)
        self.btnXoa.clicked.connect(self._delete_selected_product)
        self.btnPrev.clicked.connect(self._go_prev_page)
        self.btnNext.clicked.connect(self._go_next_page)

    # ---------------- Data loading ----------------

    def load_data(self) -> None:
        self._run_async(self._service.search_products, self._on_products_loaded, keyword="")

    def _apply_filters(self) -> None:
        keyword = self.edtSearch.text().strip()
        category_id = self.cbDanhMuc.currentData()
        self._current_page = 1
        self._run_async(
            self._service.search_products,
            self._on_products_loaded,
            keyword=keyword,
            category_id=category_id,
        )

    def _on_products_loaded(self, products: List[ProductDTO]) -> None:
        self._all_products = products
        if not self._categories_seeded:
            self._load_category_filter()
        self._render_current_page()

    def _load_category_filter(self) -> None:
        self._categories_seeded = True  # tranh goi lai nhieu lan trong khi dang cho ket qua
        self._run_async(self._category_service.get_all_categories, self._render_category_filter)

    def _render_category_filter(self, categories: List[CategoryDTO]) -> None:
        self.cbDanhMuc.blockSignals(True)
        while self.cbDanhMuc.count() > 1:
            self.cbDanhMuc.removeItem(1)
        for category in categories:
            self.cbDanhMuc.addItem(category.category_name, category.category_id)
        self.cbDanhMuc.blockSignals(False)

    def _open_create_category_dialog(self) -> None:
        from src.controller.AddCategoryDialogController import AddCategoryDialogController

        dialog = AddCategoryDialogController(self)
        dialog.exec()
        # Dialog nay quan ly Them/Sua/Xoa ngay tai cho, khong goi self.accept()
        # nen luon load lai danh muc sau khi dong, bat ke dong bang cach nao.
        self._categories_seeded = False
        self._load_category_filter()

    # ---------------- Render bang + phan trang ----------------

    def _render_current_page(self) -> None:
        total = len(self._all_products)
        total_pages = max(1, (total + _PAGE_SIZE - 1) // _PAGE_SIZE)
        self._current_page = min(self._current_page, total_pages)

        start = (self._current_page - 1) * _PAGE_SIZE
        end = min(start + _PAGE_SIZE, total)
        page_items = self._all_products[start:end]

        self.tableSanPham.setRowCount(len(page_items))
        for row, p in enumerate(page_items):
            try:
                self._render_row(row, p)
            except Exception:
                logger.exception(
                    "Loi khi render san pham id=%s barcode=%r ten=%r don_vi=%r gia=%r ton=%r",
                    p.product_id, p.barcode, p.product_name, p.unit,
                    p.retail_price, p.current_stock,
                )

        shown_from = 0 if total == 0 else start + 1
        self.lblPage.setText(f"Hiển thị {shown_from} đến {end} của {total} sản phẩm")
        self.btnPrev.setEnabled(self._current_page > 1)
        self.btnNext.setEnabled(self._current_page < total_pages)
        self._render_page_number_buttons(total_pages)

    def _render_row(self, row: int, p: ProductDTO) -> None:
        # Du lieu text
        text_values = {
            _COL_BARCODE: p.barcode,
            _COL_NAME: p.product_name,
            _COL_CATEGORY: p.category_name or "",
            _COL_UNIT: p.unit,
            _COL_PRICE: f"{p.retail_price:,.0f}",
            _COL_STOCK: str(p.current_stock),
        }
        for col, value in text_values.items():
            item = QTableWidgetItem("" if value is None else str(value))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            if col == _COL_BARCODE:
                # Luu product_id o cot dau tien de lay lai khi Sua/Xoa dong dang chon
                item.setData(Qt.ItemDataRole.UserRole, p.product_id)
            self.tableSanPham.setItem(row, col, item)

        # Badge trang thai
        status_text = self._compute_status(p)
        lbl_status = QLabel(status_text, self.tableSanPham)
        lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        style = _STATUS_STYLE.get(status_text, "")
        lbl_status.setStyleSheet(f"{style} border-radius:10px; padding:3px 10px; font-weight:600;")
        status_container = QWidget(self.tableSanPham)
        status_layout = QHBoxLayout(status_container)
        status_layout.setContentsMargins(4, 4, 4, 4)
        status_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status_layout.addWidget(lbl_status)
        self.tableSanPham.setCellWidget(row, _COL_STATUS, status_container)

    @staticmethod
    def _compute_status(p: ProductDTO) -> str:
        if p.current_stock <= 0:
            return "Hết hàng"
        if p.current_stock <= POSSettings.LOW_STOCK_THRESHOLD:
            return "Sắp hết"
        return "Còn hàng"

    # ---------------- Phan trang co danh so ----------------

    def _render_page_number_buttons(self, total_pages: int) -> None:
        for btn in self._page_number_buttons:
            self.horizontalLayout_pageNumbers.removeWidget(btn)
            btn.deleteLater()
        self._page_number_buttons.clear()

        pages_to_show = self._compute_pages_to_show(total_pages)
        for page in pages_to_show:
            if page is None:
                btn = QPushButton("...", self)
                btn.setEnabled(False)
            else:
                btn = QPushButton(str(page), self)
                btn.setCheckable(True)
                btn.setChecked(page == self._current_page)
                if page == self._current_page:
                    btn.setStyleSheet(
                        "QPushButton { background:#1d4ed8; color:white; border-radius:4px; }"
                    )
                else:
                    btn.setStyleSheet(
                        "QPushButton { background:white; border:1px solid #cbd5e1; border-radius:4px; }"
                    )
                btn.clicked.connect(lambda _, target=page: self._go_to_page(target))
            btn.setMaximumSize(32, 32)
            self.horizontalLayout_pageNumbers.addWidget(btn)
            self._page_number_buttons.append(btn)

    @staticmethod
    def _compute_pages_to_show(total_pages: int) -> List[Optional[int]]:
        if total_pages <= _MAX_VISIBLE_PAGE_BUTTONS + 1:
            return list(range(1, total_pages + 1))
        return list(range(1, _MAX_VISIBLE_PAGE_BUTTONS + 1)) + [None, total_pages]

    def _go_to_page(self, page: int) -> None:
        self._current_page = page
        self._render_current_page()

    def _go_prev_page(self) -> None:
        self._current_page -= 1
        self._render_current_page()

    def _go_next_page(self) -> None:
        self._current_page += 1
        self._render_current_page()

    # ---------------- Create / Update / Delete ----------------

    def _open_create_dialog(self) -> None:
        from src.controller.Addproductdialogcontroller import AddProductDialogController

        dialog = AddProductDialogController(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_data()

    def _get_selected_product_id(self) -> Optional[int]:
        """Lay product_id cua dong dang duoc chon trong bang (danh cho nut Sua/Xoa chung)."""
        row = self.tableSanPham.currentRow()
        if row < 0:
            return None
        item = self.tableSanPham.item(row, _COL_BARCODE)
        if item is None:
            return None
        return item.data(Qt.ItemDataRole.UserRole)

    def _edit_selected_product(self) -> None:
        product_id = self._get_selected_product_id()
        if product_id is None:
            self.show_error("Vui lòng chọn một sản phẩm để sửa.")
            return
        self._open_edit_dialog(product_id)

    def _open_edit_dialog(self, product_id: int) -> None:
        from src.controller.Addproductdialogcontroller import AddProductDialogController

        current = next((p for p in self._all_products if p.product_id == product_id), None)
        if current is None:
            return

        dialog = AddProductDialogController(self, initial=current)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_data()

    def _delete_selected_product(self) -> None:
        product_id = self._get_selected_product_id()
        if product_id is None:
            self.show_error("Vui lòng chọn một sản phẩm để xóa.")
            return
        self._delete_product(product_id)

    def _delete_product(self, product_id: int) -> None:
        if not self._is_manager_or_admin():
            self.show_error("Bạn không có quyền xóa sản phẩm.")
            return
        confirm = QMessageBox.question(self, "Xác nhận", "Xóa sản phẩm này?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        self._run_async(self._service.delete_product, lambda _: self.load_data(), product_id=product_id)

    # ---------------- Ha tang chung ----------------

    def _run_async(self, func, on_success, **kwargs) -> None:
        """Chay 1 tac vu tren thread phu. Giu (thread, worker) trong danh sach
        _active_threads de Python KHONG garbage-collect QThread trong khi no
        con dang chay (lam vay se crash native, khong co traceback Python)."""
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

    @staticmethod
    def _is_manager_or_admin() -> bool:
        return Session.get_role_name() in ("Admin", "Manager")