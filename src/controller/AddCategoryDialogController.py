import logging
from typing import List, Optional

from PySide6.QtCore import QObject, QThread, Signal, Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from src.dtos.CategoryDTO import CategoryDTO, CreateCategoryDTO, UpdateCategoryDTO
from src.gui.add_category_dialog_ui import Ui_CategoryManagerDialog
from src.services.CategoryService import CategoryService


logger = logging.getLogger(__name__)

class _AsyncWorker(QObject):
    finished = Signal(object)
    failed = Signal(str)


    def __init__(self, func, *args, **kwargs) -> None:
        super().__init__()
        self._func, self._args, self._kwargs = func, args, kwargs


    def run(self) -> None:
        try:
            result = self._func(*self._args, **self._kwargs)
            self.finished.emit(result)
        except Exception as exc:
            logger.exception("AddCategoryDialogController worker loi")
            self.failed.emit(str(exc))

class AddCategoryDialogController(QDialog, Ui_CategoryManagerDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._service = CategoryService()
        self._active_threads: List[tuple] = []  

        self._categories: List[CategoryDTO] = []
        self._selected_category: Optional[CategoryDTO] = None

        self.tblCategories.setSelectionBehavior(self.tblCategories.SelectionBehavior.SelectRows)
        self.tblCategories.horizontalHeader().setStretchLastSection(True)

        self._setup_events()
        self._load_categories()


    def _setup_events(self) -> None:
        self.btnCancel.clicked.connect(self._reset_form)
        self.btnSave.clicked.connect(self._on_save_clicked)
        self.btnEditCategory.clicked.connect(self._on_edit_clicked)
        self.btnDeleteCategory.clicked.connect(self._on_delete_clicked)
        self.tblCategories.itemSelectionChanged.connect(self._on_selection_changed)


    def _load_categories(self) -> None:
        self._run_async(self._service.get_all_categories, self._on_categories_loaded)


    def _on_categories_loaded(self, categories: List[CategoryDTO]) -> None:
        self._categories = categories
        self._render_table()


    def _render_table(self) -> None:
        self.tblCategories.clearContents()
        self.tblCategories.setRowCount(len(self._categories))
        for row, cat in enumerate(self._categories):
            item_name = QTableWidgetItem(cat.category_name)
            item_name.setData(Qt.ItemDataRole.UserRole, cat.category_id)
            item_desc = QTableWidgetItem(cat.description or "")

            self.tblCategories.setItem(row, 0, item_name)
            self.tblCategories.setItem(row, 1, item_desc)

        self.btnEditCategory.setEnabled(False)
        self.btnDeleteCategory.setEnabled(False)


    def _on_selection_changed(self) -> None:
        has_selection = bool(self.tblCategories.selectedItems())
        self.btnEditCategory.setEnabled(has_selection)
        self.btnDeleteCategory.setEnabled(has_selection)


    def _get_selected_category(self) -> Optional[CategoryDTO]:
        selected_rows = self.tblCategories.selectionModel().selectedRows()
        if not selected_rows:
            return None
        row = selected_rows[0].row()
        item = self.tblCategories.item(row, 0)
        if not item:
            return None
        category_id = item.data(Qt.ItemDataRole.UserRole)
        return next((cat for cat in self._categories if cat.category_id == category_id), None)


    def _on_edit_clicked(self) -> None:
        category = self._get_selected_category()
        if not category:
            return

        self._selected_category = category
        self.txtCategoryName.setText(category.category_name)
        self.txtDescription.setPlainText(category.description or "")
        self.lblFormTitle.setText("Sửa danh mục")
        self.btnSave.setText("Cập nhật danh mục")


    def _on_delete_clicked(self) -> None:
        category = self._get_selected_category()
        if not category:
            return

        reply = QMessageBox.question(
            self, "Xác nhận xóa",
            f"Bạn có chắc muốn xóa danh mục '{category.category_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        self._set_loading(True)
        self._run_async(
            self._service.delete_category,
            self._on_deleted,
            category_id=category.category_id,
        )


    def _on_deleted(self, _result: None) -> None:
        QMessageBox.information(self, "Thành công", "Đã xóa danh mục.")
        self._reset_form()
        self._load_categories()


    def _on_save_clicked(self) -> None:
        name = self.txtCategoryName.text().strip()
        description = self.txtDescription.toPlainText().strip() or None

        if not name:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên danh mục.")
            return

        self._set_loading(True)

        if self._selected_category is None:
            dto = CreateCategoryDTO(category_name=name, description=description)
            self._run_async(self._service.create_category, self._on_saved, dto=dto)
        else:
            dto = UpdateCategoryDTO(
                category_id=self._selected_category.category_id,
                category_name=name,
                description=description,
            )
            self._run_async(self._service.update_category, self._on_saved, dto=dto)


    def _on_saved(self, _category: CategoryDTO) -> None:
        QMessageBox.information(self, "Thành công", "Đã lưu danh mục thành công!")
        self._reset_form()
        self._load_categories()


    def _reset_form(self) -> None:
        self._selected_category = None
        self.txtCategoryName.clear()
        self.txtDescription.clear()
        self.lblFormTitle.setText("Thêm danh mục mới")
        self.btnSave.setText("Lưu danh mục")
        self._set_loading(False)
        self.tblCategories.clearSelection()


    def _set_loading(self, loading: bool) -> None:
        self.btnSave.setEnabled(not loading)
        self.btnDeleteCategory.setEnabled(not loading and bool(self.tblCategories.selectedItems()))
        self.btnEditCategory.setEnabled(not loading and bool(self.tblCategories.selectedItems()))
        self.tblCategories.setEnabled(not loading)


    def _on_failed(self, message: str) -> None:
        self._set_loading(False)
        QMessageBox.warning(self, "Lỗi", message)


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