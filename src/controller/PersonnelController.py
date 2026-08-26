from PySide6 import QtWidgets, QtCore
from src.utils.FormIcon import add_awesome_left_icon, apply_awesome_icons, apply_icon
from src.gui.tabs.personnel_management_ui import Ui_PersonnelManagement
from src.services.impl.UserServiceImpl import UserServiceImpl
from src.controller.UserDialog import UserDialog
from src.utils.Theme import badge_cell


class PersonnelController:
    def __init__(self):
        self.view = QtWidgets.QWidget()
        self.ui = Ui_PersonnelManagement()
        self.ui.setupUi(self.view)
        add_awesome_left_icon(self.ui.txtSearch, "search")
        apply_awesome_icons(self.view)
        self.service = UserServiceImpl()

        self.ui.txtSearch.textChanged.connect(self.load_data)
        self.ui.cboRole.currentIndexChanged.connect(self.load_data)
        self.ui.cboStatus.currentIndexChanged.connect(self.load_data)

        self.ui.btnAdd.clicked.connect(self._on_add_new_user)

        self.load_data()


    def get_view(self):
        return self.view


    def load_data(self):
        keyword = self.ui.txtSearch.text().strip().lower()
        role_filter = self.ui.cboRole.currentText()
        status_filter = self.ui.cboStatus.currentText()

        users, total, active, roles = self.service.get_personnel_dashboard("")

        users.sort(key=lambda x: int(x.user_id))

        self.ui.lblTotal.setText(str(len(users)))
        self.ui.lblActive.setText(str(sum(1 for u in users if u.status == "Active")))
        self.ui.lblAdminCount.setText(str(roles.get("Admin", 0)))
        self.ui.lblManagerCount.setText(str(roles.get("Cashier", 0)))
        self.ui.lblCashierCount.setText(str(roles.get("Warehouse", 0)))

        filtered_users = []
        for u in users:
            if keyword and keyword not in u.username.lower() and keyword not in u.full_name.lower():
                continue

            if role_filter != "Tất cả chức vụ" and u.role_name != role_filter:
                continue

            mapped_status = "Active" if status_filter == "Hoạt động" else "Inactive"
            if status_filter != "Tất cả trạng thái" and u.status != mapped_status:
                continue

            filtered_users.append(u)

        self.ui.tblEmployees.setRowCount(len(filtered_users))
        for row_idx, dto in enumerate(filtered_users):
            id_item = QtWidgets.QTableWidgetItem(str(dto.user_id))
            id_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.tblEmployees.setItem(row_idx, 0, id_item)

            self.ui.tblEmployees.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(dto.full_name))
            self.ui.tblEmployees.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(dto.username))

            role_item = QtWidgets.QTableWidgetItem(dto.role_name)
            role_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.tblEmployees.setItem(row_idx, 3, role_item)

            is_active = dto.status == "Active"
            self.ui.tblEmployees.setCellWidget(
                row_idx,
                4,
                badge_cell(
                    "Hoạt động" if is_active else "Đã khóa",
                    "success" if is_active else "danger",
                ),
            )

            action_widget = QtWidgets.QWidget()
            action_layout = QtWidgets.QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_layout.setSpacing(15)
            action_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            btn_edit = QtWidgets.QPushButton()
            btn_edit.setObjectName("RowActionButton")
            apply_icon(btn_edit, "edit", tone="muted", hover="none")
            btn_edit.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn_edit.setToolTip("Chỉnh sửa")

            btn_delete = QtWidgets.QPushButton()
            btn_delete.setObjectName("RowActionButton")
            apply_icon(btn_delete, "delete", tone="muted", hover="none")
            btn_delete.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn_delete.setToolTip("Xóa nhân viên")

            action_layout.addWidget(btn_edit)
            action_layout.addWidget(btn_delete)
            self.ui.tblEmployees.setCellWidget(row_idx, 5, action_widget)

            header = self.ui.tblEmployees.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Fixed)
            self.ui.tblEmployees.setColumnWidth(4, 130)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

            btn_edit.clicked.connect(lambda checked=False, user_dto=dto: self._on_edit_user(user_dto))
            btn_delete.clicked.connect(lambda checked=False, uid=dto.user_id: self._on_delete_user(uid))


    def _on_add_new_user(self):
        dialog = UserDialog(mode="add", parent=self.view)
        if dialog.exec():
            new_data = dialog.get_data()

            username = new_data.get("username", "").strip()
            full_name = new_data.get("full_name", "").strip()
            email = new_data.get("email", "").strip()
            password = new_data.get("password", "").strip()

            if not username or not full_name or not email or not password:
                QtWidgets.QMessageBox.warning(self.view, "Cảnh báo",
                                              "Vui lòng nhập đầy đủ thông tin, không được để trống ô nào!")
                return
            existing_users, _, _, _ = self.service.get_personnel_dashboard("")
            for u in existing_users:
                if u.username.lower() == username.lower():
                    QtWidgets.QMessageBox.warning(
                        self.view,
                        "Trùng lặp dữ liệu",
                        f"Tên đăng nhập '{username}' đã có người sử dụng!\nVui lòng chọn tên đăng nhập khác."
                    )
                    return

            success = self.service.add_user(new_data)

            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Đã lưu nhân viên mới vào cơ sở dữ liệu!")
                self.load_data()
            else:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Lưu thất bại! Vui lòng thử lại sau.")


    def _on_edit_user(self, user_dto):
        user_email = getattr(user_dto, 'email', '')
        if not user_email:
            try:
                from config.database import Database
                from src.entities.user import User
                with Database.get_session_ctx() as session:
                    db_user = session.query(User).filter_by(username=user_dto.username).first()
                    if db_user and db_user.email:
                        user_email = db_user.email
            except Exception as e:
                print(f"Bỏ qua lỗi truy vấn phụ, dùng email rỗng: {e}")

        user_data = {
            "username": user_dto.username,
            "full_name": user_dto.full_name,
            "role_name": user_dto.role_name,
            "status": user_dto.status,
            "email": user_email
        }

        dialog = UserDialog(mode="edit", user_data=user_data, parent=self.view)
        if dialog.exec():
            updated_data = dialog.get_data()

            full_name = updated_data.get("full_name", "").strip()
            email = updated_data.get("email", "").strip()

            if not full_name or not email:
                QtWidgets.QMessageBox.warning(self.view, "Cảnh báo",
                                              "Vui lòng không để trống thông tin Họ tên và Email!")
                return

            success = self.service.update_user(user_dto.username, updated_data)

            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Cập nhật dữ liệu thành công!")
                self.load_data()
            else:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Không thể cập nhật. Vui lòng thử lại!")


    def _on_delete_user(self, user_id):
        reply = QtWidgets.QMessageBox.question(
            self.view, "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa vĩnh viễn tài khoản ID: {user_id}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            success = self.service.delete_user(user_id)

            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Đã xóa khỏi hệ thống!")
                self.load_data()
            else:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Xóa thất bại!")