from PySide6 import QtWidgets, QtCore
from src.utils.FormIcon import add_awesome_left_icon, apply_icon
from src.gui.tabs.supplier_management_ui import Ui_SupplierManagement
from src.services.impl.SupplierServiceImpl import SupplierServiceImpl
from src.controller.SupplierDialog import SupplierDialog


class SupplierController:
    def __init__(self):
        self.view = QtWidgets.QWidget()
        self.ui = Ui_SupplierManagement()
        self.ui.setupUi(self.view)
        add_awesome_left_icon(self.ui.txtSearch, "search")

        self.service = SupplierServiceImpl()

        self.ui.txtSearch.textChanged.connect(self.load_data)
        self.ui.cboFilter.currentIndexChanged.connect(self.load_data)

        self.ui.btnAdd.clicked.connect(self._on_add_new_supplier)

        self.load_data()


    def get_view(self):
        return self.view


    def load_data(self):
        keyword = self.ui.txtSearch.text().lower()
        filter_type = self.ui.cboFilter.currentText()

        all_suppliers = self.service.get_suppliers("")

        all_suppliers.sort(key=lambda x: int(x.supplier_id))

        filtered_suppliers = []

        for dto in all_suppliers:
            match = False
            if filter_type == "Tất cả tiêu chí":
                if keyword in dto.company_name.lower() or keyword in dto.phone or keyword in (
                        dto.contact_name or "").lower():
                    match = True
            elif filter_type == "Tên công ty":
                if keyword in dto.company_name.lower():
                    match = True
            elif filter_type == "Số điện thoại":
                if keyword in dto.phone:
                    match = True

            if match or not keyword:
                filtered_suppliers.append(dto)

        self.ui.tblSuppliers.setRowCount(len(filtered_suppliers))

        header = self.ui.tblSuppliers.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.ui.tblSuppliers.setColumnWidth(6, 100)

        for row_idx, dto in enumerate(filtered_suppliers):
            id_item = QtWidgets.QTableWidgetItem(str(dto.supplier_id))
            id_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.tblSuppliers.setItem(row_idx, 0, id_item)

            self.ui.tblSuppliers.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(str(dto.company_name)))
            self.ui.tblSuppliers.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(dto.contact_name)))
            self.ui.tblSuppliers.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(dto.phone)))
            self.ui.tblSuppliers.setItem(row_idx, 4, QtWidgets.QTableWidgetItem(str(dto.email)))
            self.ui.tblSuppliers.setItem(row_idx, 5, QtWidgets.QTableWidgetItem(str(dto.address)))

            action_widget = QtWidgets.QWidget()
            action_layout = QtWidgets.QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_layout.setSpacing(10)
            action_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            btn_edit = QtWidgets.QPushButton()
            btn_edit.setObjectName("RowActionButton")
            apply_icon(btn_edit, "edit", tone="muted")
            btn_edit.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn_edit.setToolTip("Chỉnh sửa")

            btn_delete = QtWidgets.QPushButton()
            btn_delete.setObjectName("RowActionButton")
            apply_icon(btn_delete, "delete", tone="muted")
            btn_delete.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn_delete.setToolTip("Xóa nhà cung cấp")

            action_layout.addWidget(btn_edit)
            action_layout.addWidget(btn_delete)
            self.ui.tblSuppliers.setCellWidget(row_idx, 6, action_widget)

            btn_edit.clicked.connect(lambda checked=False, s_dto=dto: self._on_edit_supplier(s_dto))
            btn_delete.clicked.connect(lambda checked=False, s_id=dto.supplier_id: self._on_delete_supplier(s_id))


    def _on_add_new_supplier(self):
        dialog = SupplierDialog(mode="add", parent=self.view)

        if dialog.exec():
            new_data = dialog.get_data()

            company_name = new_data.get("company_name", "")
            contact_name = new_data.get("contact_name", "")
            phone = new_data.get("phone", "")
            email = new_data.get("email", "")
            address = new_data.get("address", "")

            if not company_name or not contact_name or not phone or not email or not address:
                QtWidgets.QMessageBox.warning(self.view, "Cảnh báo",
                                              "Vui lòng nhập đầy đủ thông tin, không để trống ô nào!")
                return

            if not phone.isdigit() or len(phone) != 10 or not phone.startswith("0"):
                QtWidgets.QMessageBox.warning(self.view, "Lỗi dữ liệu",
                                              "Số điện thoại không hợp lệ!\nNhập đúng 10 chữ số và bắt đầu bằng số 0.")
                return

            existing_suppliers = self.service.get_suppliers("")
            for s in existing_suppliers:
                if s.phone == phone:
                    QtWidgets.QMessageBox.warning(
                        self.view,
                        "Trùng lặp dữ liệu",
                        f"Số điện thoại '{phone}' đã được sử dụng cho công ty '{s.company_name}'!\nVui lòng kiểm tra và nhập số khác."
                    )
                    return

            success = self.service.add_supplier(new_data)
            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Đã thêm nhà cung cấp mới!")
                self.load_data()
            else:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Lưu thất bại! Vui lòng thử lại sau.")


    def _on_edit_supplier(self, supplier_dto):
        supplier_data = {
            "company_name": supplier_dto.company_name,
            "contact_name": supplier_dto.contact_name,
            "phone": supplier_dto.phone,
            "email": supplier_dto.email,
            "address": supplier_dto.address
        }

        dialog = SupplierDialog(mode="edit", supplier_data=supplier_data, parent=self.view)

        if dialog.exec():
            updated_data = dialog.get_data()

            company_name = updated_data.get("company_name", "")
            contact_name = updated_data.get("contact_name", "")
            phone = updated_data.get("phone", "")
            email = updated_data.get("email", "")
            address = updated_data.get("address", "")

            if not company_name or not contact_name or not phone or not email or not address:
                QtWidgets.QMessageBox.warning(self.view, "Cảnh báo",
                                              "Vui lòng nhập đầy đủ thông tin, không để trống ô nào!")
                return

            if not phone.isdigit() or len(phone) != 10 or not phone.startswith("0"):
                QtWidgets.QMessageBox.warning(self.view, "Lỗi dữ liệu",
                                              "Số điện thoại không hợp lệ!\nNhập đúng 10 chữ số và bắt đầu bằng số 0.")
                return

            success = self.service.update_supplier(supplier_dto.supplier_id, updated_data)

            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Cập nhật dữ liệu thành công!")
                self.load_data()
            else:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Cập nhật thất bại. Vui lòng thử lại!")


    def _on_delete_supplier(self, supplier_id):
        reply = QtWidgets.QMessageBox.question(
            self.view, "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa vĩnh viễn đối tác ID: {supplier_id} không?\nHành động này không thể hoàn tác!",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            success = self.service.delete_supplier(supplier_id)
            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Đã xóa nhà cung cấp khỏi hệ thống!")
                self.load_data()
            else:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Xóa thất bại!")