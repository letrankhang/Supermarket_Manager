# src/controller/CreateImportOrderDialogController.py

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
)

from config.database import Database
from src.gui.tabs.create_import_order_dialog_phieu_nhap import (
    Ui_CreateImportOrderDialog,
)
from src.entities.product import Product
from src.entities.supplier import Supplier
from src.services.impl.ImportServiceImpl import ImportServiceImpl
from src.dtos.ImportDTO import (
    CreateImportOrderDTO,
    CreateImportLineDTO,
)

logger = logging.getLogger(__name__)


class CreateImportDialogController(QDialog, Ui_CreateImportOrderDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._service = ImportServiceImpl()

        # Lưu dữ liệu dạng dict, không giữ object SQLAlchemy
        self._products = []

        self._setup_ui()
        self._load_suppliers()
        self._load_products()
        self._setup_events()

    # =========================================================
    # GIAO DIỆN
    # =========================================================

    def _setup_ui(self):
        header = self.tblImportDetails.horizontalHeader()

        header.setSectionResizeMode(
            0, QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            1, QHeaderView.ResizeMode.Stretch
        )
        header.setSectionResizeMode(
            2, QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            3, QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            4, QHeaderView.ResizeMode.ResizeToContents
        )

        self.lblTotalAmount.setText("0 VNĐ")

        # Đảm bảo ComboBox hoạt động
        self.cboSupplier.setEnabled(True)
        self.cboSupplier.setEditable(False)

        self.cbothemsp.setEnabled(True)
        self.cbothemsp.setEditable(False)

    # =========================================================
    # SỰ KIỆN
    # =========================================================

    def _setup_events(self):
        self.btnAddProductRow.clicked.connect(self._add_product_row)
        self.btnSave.clicked.connect(self._save_import_order)
        self.btnCancel.clicked.connect(self.reject)

        self.tblImportDetails.cellChanged.connect(
            self._on_cell_changed
        )

    # =========================================================
    # LOAD NHÀ CUNG CẤP
    # =========================================================

    def _load_suppliers(self):
        try:
            with Database.get_session_ctx() as session:
                suppliers = session.query(Supplier).all()

                data = [
                    (
                        supplier.supplier_id,
                        supplier.company_name,
                    )
                    for supplier in suppliers
                ]

            self.cboSupplier.clear()
            self.cboSupplier.addItem(
                "-- Chọn nhà cung cấp --",
                None,
            )

            for supplier_id, company_name in data:
                self.cboSupplier.addItem(
                    str(company_name),
                    supplier_id,
                )

            self.cboSupplier.setCurrentIndex(0)
            self.cboSupplier.setEnabled(True)

            logger.info(
                "Đã load %d nhà cung cấp vào ComboBox.",
                len(data),
            )

        except Exception as exc:
            logger.exception("Lỗi tải nhà cung cấp")

            QMessageBox.critical(
                self,
                "Lỗi",
                f"Không thể tải nhà cung cấp:\n{exc}",
            )

    # =========================================================
    # LOAD SẢN PHẨM
    # =========================================================

    def _load_products(self):
        try:
            with Database.get_session_ctx() as session:
                products = session.query(Product).all()

                # Chuyển thành dict trước khi session đóng
                self._products = [
                    {
                        "product_id": product.product_id,
                        "barcode": product.barcode,
                        "product_name": product.product_name,
                        "retail_price": float(
                            product.retail_price or 0
                        )
                    }
                    for product in products
                ]

            self.cbothemsp.clear()

            self.cbothemsp.addItem(
                "-- Chọn sản phẩm --",
                None,
            )

            for product in self._products:
                text = (
                    f"{product['barcode']} - "
                    f"{product['product_name']}"
                )

                self.cbothemsp.addItem(
                    text,
                    product["product_id"],
                )

            self.cbothemsp.setCurrentIndex(0)
            self.cbothemsp.setEnabled(True)

            logger.info(
                "Đã load %d sản phẩm vào ComboBox.",
                len(self._products),
            )

        except Exception as exc:
            logger.exception("Lỗi tải sản phẩm")

            QMessageBox.critical(
                self,
                "Lỗi",
                f"Không thể tải sản phẩm:\n{exc}",
            )

    # =========================================================
    # THÊM SẢN PHẨM VÀO BẢNG
    # =========================================================

    def _add_product_row(self):
        product_id = self.cbothemsp.currentData()

        if product_id is None:
            QMessageBox.warning(
                self,
                "Cảnh báo",
                "Vui lòng chọn sản phẩm trước!",
            )
            return

        product = next(
            (
                p
                for p in self._products
                if p["product_id"] == product_id
            ),
            None,
        )

        if product is None:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Không tìm thấy sản phẩm.",
            )
            return

        # Không cho thêm trùng
        for row in range(self.tblImportDetails.rowCount()):
            item = self.tblImportDetails.item(row, 0)

            if item:
                old_product_id = item.data(
                    Qt.ItemDataRole.UserRole
                )

                if old_product_id == product_id:
                    QMessageBox.warning(
                        self,
                        "Cảnh báo",
                        "Sản phẩm này đã có trong phiếu nhập!",
                    )
                    return

        row = self.tblImportDetails.rowCount()
        self.tblImportDetails.insertRow(row)

        # Mã sản phẩm
        code_item = QTableWidgetItem(
            str(product["barcode"])
        )
        code_item.setData(
            Qt.ItemDataRole.UserRole,
            product["product_id"],
        )

        # Tên sản phẩm
        name_item = QTableWidgetItem(
            str(product["product_name"])
        )
        name_item.setFlags(
            name_item.flags()
            & ~Qt.ItemFlag.ItemIsEditable
        )

        # Số lượng
        qty_item = QTableWidgetItem("1")

        # Giá nhập
        price_item = QTableWidgetItem("0")

        # Thành tiền
        total_item = QTableWidgetItem("0 VNĐ")
        total_item.setFlags(
            total_item.flags()
            & ~Qt.ItemFlag.ItemIsEditable
        )

        self.tblImportDetails.setItem(
            row, 0, code_item
        )
        self.tblImportDetails.setItem(
            row, 1, name_item
        )
        self.tblImportDetails.setItem(
            row, 2, qty_item
        )
        self.tblImportDetails.setItem(
            row, 3, price_item
        )
        self.tblImportDetails.setItem(
            row, 4, total_item
        )

        # Đưa ComboBox về lựa chọn đầu tiên
        self.cbothemsp.setCurrentIndex(0)

        self._recalculate_total()

    # =========================================================
    # TÍNH TIỀN
    # =========================================================

    def _on_cell_changed(self, row, col):
        if col not in (2, 3):
            return

        self.tblImportDetails.blockSignals(True)

        try:
            quantity = self._get_number(row, 2)
            price = self._get_number(row, 3)

            total = quantity * price

            item = QTableWidgetItem(
                f"{total:,.0f} VNĐ".replace(",", ".")
            )

            item.setFlags(
                item.flags()
                & ~Qt.ItemFlag.ItemIsEditable
            )

            self.tblImportDetails.setItem(
                row, 4, item
            )

        finally:
            self.tblImportDetails.blockSignals(False)

        self._recalculate_total()

    def _recalculate_total(self):
        total = 0

        for row in range(
            self.tblImportDetails.rowCount()
        ):
            quantity = self._get_number(row, 2)
            price = self._get_number(row, 3)

            total += quantity * price

        self.lblTotalAmount.setText(
            f"{total:,.0f} VNĐ".replace(",", ".")
        )

    def _get_number(self, row, column):
        item = self.tblImportDetails.item(
            row, column
        )

        if not item:
            return 0

        try:
            text = item.text().strip()

            return float(
                text.replace(".", "")
                .replace(",", ".")
            )

        except ValueError:
            return 0

    # =========================================================
    # LƯU PHIẾU NHẬP
    # =========================================================

    def _save_import_order(self):
        if self.tblImportDetails.rowCount() == 0:
            QMessageBox.warning(
                self,
                "Cảnh báo",
                "Vui lòng thêm ít nhất một sản phẩm!",
            )
            return

        supplier_id = self.cboSupplier.currentData()

        if supplier_id is None:
            QMessageBox.warning(
                self,
                "Cảnh báo",
                "Vui lòng chọn nhà cung cấp!",
            )
            return

        try:
            lines = []

            for row in range(
                self.tblImportDetails.rowCount()
            ):
                code_item = self.tblImportDetails.item(
                    row, 0
                )

                if not code_item:
                    continue

                product_id = code_item.data(
                    Qt.ItemDataRole.UserRole
                )

                quantity = self._get_number(row, 2)
                import_price = self._get_number(row, 3)

                if not product_id:
                    continue

                if quantity <= 0:
                    QMessageBox.warning(
                        self,
                        "Cảnh báo",
                        f"Dòng {row + 1}: "
                        "số lượng phải lớn hơn 0!",
                    )
                    return

                if import_price <= 0:
                    QMessageBox.warning(
                        self,
                        "Cảnh báo",
                        f"Dòng {row + 1}: "
                        "giá nhập phải lớn hơn 0!",
                    )
                    return

                lines.append(
                    CreateImportLineDTO(
                        product_id=product_id,
                        quantity=int(quantity),
                        unit_price=import_price,
                    )
                )

            if not lines:
                QMessageBox.warning(
                    self,
                    "Cảnh báo",
                    "Chưa có sản phẩm hợp lệ!",
                )
                return

            # TODO: thay bằng user đang đăng nhập
            user_id = 1

            dto = CreateImportOrderDTO(
                supplier_id=supplier_id,
                user_id=user_id,
                note=self.txtNote.text().strip(),
                lines=lines,
            )

            self._service.create_import_order(dto)

            QMessageBox.information(
                self,
                "Thành công",
                "Đã nhập hàng và cập nhật tồn kho thành công!",
            )

            self.accept()

        except ValueError as exc:
            QMessageBox.warning(
                self,
                "Cảnh báo",
                str(exc),
            )

        except Exception as exc:
            logger.exception(
                "Lỗi tạo phiếu nhập"
            )

            QMessageBox.critical(
                self,
                "Lỗi",
                f"Không thể tải phiếu nhập:\n{exc}",
            )