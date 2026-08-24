from PyQt6 import QtWidgets, QtCore
import qtawesome as qta
from src.gui.tabs.personnel_management_ui import Ui_PersonnelManagement
from src.services.impl.UserServiceImpl import UserServiceImpl
from src.controller.UserDialog import UserDialog  # Import Dialog vừa tạo


class PersonnelController:
    def __init__(self):
        self.view = QtWidgets.QWidget()
        self.ui = Ui_PersonnelManagement()
        self.ui.setupUi(self.view)
        self.service = UserServiceImpl()

        # Kết nối sự kiện tìm kiếm và Combobox
        self.ui.txtSearch.textChanged.connect(self.load_data)
        self.ui.cboRole.currentIndexChanged.connect(self.load_data)
        self.ui.cboStatus.currentIndexChanged.connect(self.load_data)

        # Kết nối nút Thêm nhân sự
        self.ui.btnAdd.clicked.connect(self._on_add_new_user)

        self.load_data()

    def get_view(self):
        return self.view

    def load_data(self):
        keyword = self.ui.txtSearch.text()
        role_filter = self.ui.cboRole.currentText()
        status_filter = self.ui.cboStatus.currentText()

        # Lấy dữ liệu từ database
        users, total, active, roles = self.service.get_personnel_dashboard(keyword)

        # =========================================================
        # 1. ÉP KIỂU SỐ VÀ SẮP XẾP ID TĂNG DẦN (1, 2, 3...)
        # =========================================================
        users.sort(key=lambda x: int(x.user_id))

        # Xử lý Lọc (Filter) bằng code Python
        filtered_users = []
        for u in users:
            if role_filter != "Tất cả chức vụ" and u.role_name != role_filter:
                continue

            mapped_status = "Active" if status_filter == "Hoạt động" else "Inactive"
            if status_filter != "Tất cả trạng thái" and u.status != mapped_status:
                continue

            filtered_users.append(u)
            # Căn chỉnh lại kích thước cột dọc để không bị mất số
            self.ui.tblEmployees.verticalHeader().setDefaultSectionSize(40)  # Chiều cao dòng
            self.ui.tblEmployees.verticalHeader().setMinimumWidth(40)  # Chiều rộng cột

        # Cập nhật số liệu hiển thị
        self.ui.lblTotal.setText(str(len(filtered_users)))
        self.ui.lblActive.setText(str(sum(1 for u in filtered_users if u.status == "Active")))

        # Lấy số lượng từng chức vụ (nếu không có thì mặc định là 0)
        self.ui.lblAdminCount.setText(str(roles.get("Admin", 0)))
        self.ui.lblManagerCount.setText(str(roles.get("Manager", 0)))
        self.ui.lblCashierCount.setText(str(roles.get("Cashier", 0)))

        # Đổ dữ liệu vào bảng
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

            status_item = QtWidgets.QTableWidgetItem("Hoạt động" if dto.status == "Active" else "Đã khóa")
            status_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            status_item.setForeground(
                QtCore.Qt.GlobalColor.darkGreen if dto.status == "Active" else QtCore.Qt.GlobalColor.darkRed)
            self.ui.tblEmployees.setItem(row_idx, 4, status_item)

            # CỘT ACTIONS: Sửa (Bút chì) và Xóa (Thùng rác)
            action_widget = QtWidgets.QWidget()
            action_layout = QtWidgets.QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_layout.setSpacing(15)
            action_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            # Nút Sửa
            btn_edit = QtWidgets.QPushButton()
            btn_edit.setIcon(qta.icon('fa5s.pen', color='#475569'))
            btn_edit.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn_edit.setStyleSheet("background: transparent; border: none;")
            btn_edit.setToolTip("Chỉnh sửa")

            # Nút Xóa
            btn_delete = QtWidgets.QPushButton()
            btn_delete.setIcon(qta.icon('fa5s.trash-alt', color='#ef4444'))
            btn_delete.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn_delete.setStyleSheet("background: transparent; border: none;")
            btn_delete.setToolTip("Xóa nhân viên")

            action_layout.addWidget(btn_edit)
            action_layout.addWidget(btn_delete)
            self.ui.tblEmployees.setCellWidget(row_idx, 5, action_widget)

            # Ép các cột giãn đều cho vừa khít màn hình
            header = self.ui.tblEmployees.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

            # BẮT SỰ KIỆN CLICK
            btn_edit.clicked.connect(lambda checked=False, user_dto=dto: self._on_edit_user(user_dto))
            btn_delete.clicked.connect(lambda checked=False, uid=dto.user_id: self._on_delete_user(uid))

    # ================= CÁC HÀM XỬ LÝ SỰ KIỆN CHUẨN =================

    def _on_add_new_user(self):
        dialog = UserDialog(mode="add", parent=self.view)
        if dialog.exec():
            new_data = dialog.get_data()

            # --- BẮT LỖI KHÔNG ĐƯỢC BỎ TRỐNG ---
            username = new_data.get("username", "").strip()
            full_name = new_data.get("full_name", "").strip()
            email = new_data.get("email", "").strip()
            password = new_data.get("password", "").strip()

            if not username or not full_name or not email or not password:
                QtWidgets.QMessageBox.warning(self.view, "Cảnh báo",
                                              "Vui lòng nhập đầy đủ thông tin, không được để trống ô nào!")
                return

            # =========================================================
            # 2. KIỂM TRA TRÙNG TÊN ĐĂNG NHẬP
            # =========================================================
            existing_users, _, _, _ = self.service.get_personnel_dashboard("")
            for u in existing_users:
                if u.username.lower() == username.lower():
                    QtWidgets.QMessageBox.warning(
                        self.view,
                        "Trùng lặp dữ liệu",
                        f"Tên đăng nhập '{username}' đã có người sử dụng!\nVui lòng chọn tên đăng nhập khác."
                    )
                    return  # Dừng lại ngay, không cho lưu xuống CSDL
            # =========================================================

            # GỌI SERVICE ĐỂ LƯU THẬT VÀO SQL SERVER
            success = self.service.add_user(new_data)

            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Đã lưu nhân viên mới vào cơ sở dữ liệu!")
                self.load_data()
            else:
                # Đổi câu thông báo lỗi ở đây vì đã rào lỗi trùng lặp ở trên rồi
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Lưu thất bại! Vui lòng thử lại sau.")

    def _on_edit_user(self, user_dto):
        user_data = {
            "username": user_dto.username,
            "full_name": user_dto.full_name,
            "role_name": user_dto.role_name,
            "status": user_dto.status,
            "email": getattr(user_dto, 'email', '')
        }

        dialog = UserDialog(mode="edit", user_data=user_data, parent=self.view)
        if dialog.exec():
            updated_data = dialog.get_data()

            # --- BẮT LỖI KHÔNG ĐƯỢC BỎ TRỐNG KHI SỬA ---
            full_name = updated_data.get("full_name", "").strip()
            email = updated_data.get("email", "").strip()

            if not full_name or not email:
                QtWidgets.QMessageBox.warning(self.view, "Cảnh báo",
                                              "Vui lòng không để trống thông tin Họ tên và Email!")
                return
            # ---------------------------------------------

            # GỌI SERVICE ĐỂ CẬP NHẬT XUỐNG SQL SERVER
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
            # GỌI SERVICE XÓA KHỎI SQL SERVER
            success = self.service.delete_user(user_id)

            if success:
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Đã xóa khỏi hệ thống!")
                self.load_data()
            else:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", "Xóa thất bại!")