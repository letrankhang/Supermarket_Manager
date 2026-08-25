# File: src/controller/AddProductDialogController.py
"""Controller cho hop thoai Them/Sua San pham (add_product_dialog.ui, class AddProductDialog).
Dung chung cho ca Them moi va Sua: truyen initial=ProductDTO de mo che do Sua.
Khong xu ly nghiep vu tai day - goi thang ProductService/CategoryService."""
from __future__ import annotations

import logging
import random
from typing import List, Optional

from PySide6.QtCore import QObject, QThread, Signal as pyqtSignal
from PySide6.QtWidgets import QDialog, QMessageBox

from src.dtos.CategoryDTO import CategoryDTO
from src.dtos.ProductDTO import CreateProductDTO, ProductDTO, UpdateProductDTO
from src.gui.tabs.add_product_dialog import Ui_AddProductDialog
from src.services.CategoryService import CategoryService
from src.services.impl.ProductServiceImpl import ProductServiceImpl

logger = logging.getLogger(__name__)


def _generate_barcode() -> str:
    """Sinh ma vach ngau nhien gom 8 chu so, dung khi mo dialog o che do Them moi."""
    return "".join(str(random.randint(0, 9)) for _ in range(8))


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
            logger.exception("AddProductDialogController worker loi")
            self.failed.emit(str(exc))


class AddProductDialogController(QDialog, Ui_AddProductDialog):

    def __init__(self, parent=None, initial: Optional[ProductDTO] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._product_service = ProductServiceImpl()
        self._category_service = CategoryService()
        self._active_threads: List[tuple] = []
        self._initial = initial
        self.result_product: Optional[ProductDTO] = None

        self._apply_mode_labels(is_edit=initial is not None)
        self.btnSave.clicked.connect(self._on_save_clicked)
        self.btnCancel.clicked.connect(self.reject)

        self._load_categories()
        if initial is not None:
            self._prefill(initial)
        else:
            # Che do Them moi: tu sinh san ma vach 8 chu so cho nguoi dung
            self.txtBarcode.setText(_generate_barcode())

    # ---------------- Nhan chu theo che do Them / Sua ----------------

    def _apply_mode_labels(self, is_edit: bool) -> None:
        """Dat tieu de cua so va phan header trong dialog theo che do dang mo.
        Chi doi chu, khong dong den giao dien (dinh nghia trong add_product_dialog.ui)."""
        if is_edit:
            self.setWindowTitle("Sửa sản phẩm")
            self.lblDialogTitle.setText("Sửa sản phẩm")
            self.lblDialogSubtitle.setText("Cập nhật thông tin sản phẩm, mã vạch giữ nguyên.")
            self.btnSave.setText("Cập nhật sản phẩm")
        else:
            self.setWindowTitle("Thêm sản phẩm mới")
            self.lblDialogTitle.setText("Thêm sản phẩm mới")
            self.lblDialogSubtitle.setText("Điền thông tin sản phẩm, mã vạch được sinh tự động.")
            self.btnSave.setText("Lưu sản phẩm")

    # ---------------- Nap danh muc vao combobox ----------------

    def _load_categories(self) -> None:
        self._run_async(self._category_service.get_all_categories, self._render_categories)

    def _render_categories(self, categories: List[CategoryDTO]) -> None:
        self.cboCategory.clear()
        self.cboCategory.addItem("(Không có danh mục)", None)
        for category in categories:
            self.cboCategory.addItem(category.category_name, category.category_id)

        if self._initial is not None and self._initial.category_id is not None:
            index = self.cboCategory.findData(self._initial.category_id)
            if index >= 0:
                self.cboCategory.setCurrentIndex(index)

    # ---------------- Che do Sua: do du lieu co san len form ----------------

    def _prefill(self, product: ProductDTO) -> None:
        self.txtBarcode.setText(product.barcode)
        self.txtProductName.setText(product.product_name)
        self.txtUnit.setText(product.unit)
        self.spnRetailPrice.setValue(product.retail_price)
        self.txtImage.setText(product.image or "")

    # ---------------- Luu ----------------

    def _on_save_clicked(self) -> None:
        barcode = self.txtBarcode.text().strip()
        product_name = self.txtProductName.text().strip()
        unit = self.txtUnit.text().strip()
        retail_price = self.spnRetailPrice.value()
        image = self.txtImage.text().strip() or None
        category_id = self.cboCategory.currentData()

        if not barcode:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập mã vạch.")
            return
        if not product_name:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên sản phẩm.")
            return
        if not unit:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đơn vị tính.")
            return

        self.btnSave.setEnabled(False)

        if self._initial is None:
            dto = CreateProductDTO(
                barcode=barcode, product_name=product_name, category_id=category_id,
                unit=unit, retail_price=retail_price, image=image,
            )
            self._run_async(self._product_service.create_product, self._on_saved, dto=dto)
        else:
            dto = UpdateProductDTO(
                product_id=self._initial.product_id, barcode=barcode,
                product_name=product_name, category_id=category_id,
                unit=unit, retail_price=retail_price, image=image,
            )
            self._run_async(self._product_service.update_product, self._on_saved, dto=dto)

    def _on_saved(self, product: ProductDTO) -> None:
        self.result_product = product
        self.accept()

    def _on_failed(self, message: str) -> None:
        self.btnSave.setEnabled(True)
        QMessageBox.warning(self, "Lỗi", message)

    # ---------------- Ha tang chung (giong ban da sua loi crash QThread) ----------------

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
        worker.failed.connect(self._on_failed)
        worker.finished.connect(cleanup)
        worker.failed.connect(cleanup)
        thread.start()