# File: D:\Python\Supermarket_Manager\src\controller\MainWindowController.py

import logging
import os
from typing import List, Optional
from PyQt6.QtWidgets import (
    QMainWindow, QStackedWidget, QVBoxLayout, QMessageBox,
    QPushButton, QButtonGroup
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, QDateTime, Qt, QSize, QEvent
import qtawesome as qta
from src.gui.main_window_ui import Ui_MainWindow
from src.utils.Session import Session
from config.database import Database
from src.entities.user import User
from src.controller.DashboardController import DashboardController
from src.controller.POSController import POSController

logger = logging.getLogger(__name__)


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._fix_logo()
        self._setup_ui()
        self._setup_event()
        self._load_user_data()
        self._block_admin_features_for_cashier()
        # Default to showing the dashboard tab
        self._show_dashboard()

    def _fix_logo(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Sửa đường dẫn ảnh logo
        logo_path = os.path.abspath(os.path.join(current_dir, "..", "..", "assets", "images", "logo2.png"))
        if os.path.exists(logo_path):
            self.label_4.setPixmap(QPixmap(logo_path))
        else:
            logger.error("Logo not found at path: %s", logo_path)

        # Sửa đường dẫn ảnh đại diện (avatar)
        avatar_path = os.path.abspath(os.path.join(current_dir, "..", "..", "assets", "images", "user.png"))
        if os.path.exists(avatar_path):
            avatar_path_url = avatar_path.replace("\\", "/")
            self.lblAvatar.setStyleSheet(f"""
                QLabel {{
                    border-radius: 20px;
                    border-image: url({avatar_path_url}) 0 0 0 0 stretch stretch;
                    background-color: transparent;
                }}
            """)
        else:
            logger.error("Avatar not found at path: %s", avatar_path)

    def _setup_ui(self) -> None:
        """
        Cấu hình giao diện ban đầu, khởi tạo Timer cập nhật ngày giờ và thiết lập QStackedWidget.
        """
        # Khởi tạo Timer để cập nhật ngày giờ thời gian thực (mỗi 1 giây)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_datetime)
        self.timer.start(1000)
        self._update_datetime()

        # Cấu hình layout cho widget_3 và thêm QStackedWidget quản lý các tab nội dung
        if not self.widget_3.layout():
            layout = QVBoxLayout(self.widget_3)
            layout.setContentsMargins(0, 0, 0, 0)
            self.widget_3.setLayout(layout)
        else:
            layout = self.widget_3.layout()

        self.stacked_widget = QStackedWidget(self.widget_3)
        layout.addWidget(self.stacked_widget)

        # Khởi tạo DashboardController và thêm vào stacked widget
        self.dashboard_controller = DashboardController(self)
        self.stacked_widget.addWidget(self.dashboard_controller)

<<<<<<< Updated upstream
=======
        # Khởi tạo POSController (màn hình bán hàng) và thêm vào stacked widget
        self.pos_controller = POSController(self)
        self.stacked_widget.addWidget(self.pos_controller)

        # Cấu hình menu điều hướng (hiệu ứng hover và trạng thái đang chọn)
        self._setup_navigation()

    def _setup_navigation(self) -> None:
        """
        Biến các nút menu thành nhóm nút loại trừ lẫn nhau để mục đang mở
        luôn giữ trạng thái sáng, đồng thời áp dụng hiệu ứng hover.
        """
        self.nav_buttons: List[QPushButton] = [
            self.btn_dashboard,
            self.btn_products,
            self.btn_suppliers,
            self.btn_importing,
            self.btn_customers,
            self.btn_pos,
            self.btn_analytics,
            self.btn_settings,
        ]

        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        for button in self.nav_buttons:
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.nav_group.addButton(button)

        # Các nút phụ ở cuối menu không thuộc nhóm tab nội dung
        for button in (self.btn_help, self.btn_logout):
            button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Nút đang được chọn hiện tại, dùng để khôi phục khi mở tính năng chưa có
        self.active_nav_button: Optional[QPushButton] = None

        # Gán icon cho menu (đặt cuối hàm vì cần setCheckable đã chạy xong)
        self._setup_sidebar_icons()

    def _setup_sidebar_icons(self) -> None:
        """
        Gán icon qtawesome cho toàn bộ nút menu sidebar và cho icon đổi màu
        đồng bộ với chữ theo trạng thái.

        Dùng bộ Font Awesome 5 Solid (prefix "fa5s") cho cả 10 nút để đồng bộ
        nét vẽ, không cần file ảnh icon rời.

        Icon và chữ LUÔN CÙNG MÀU ở mọi trạng thái:
          - Bình thường       : xám nhạt #cbd5e1
          - Hover hoặc active : trắng #ffffff

        qtawesome vẽ icon thành pixmap với màu đã cố định lúc tạo, nên QSS
        :hover / :checked KHÔNG đổi được màu icon. Vì vậy mỗi nút được dựng
        sẵn 2 phiên bản QIcon rồi đổi qua lại bằng code.

        Lưu ý: KHÔNG dùng tham số color_active của qtawesome, vì nó ánh xạ vào
        QIcon.Mode.Active - trạng thái mà Qt chỉ dùng khi nút đang GIỮ FOCUS
        bàn phím, chứ không phải khi rê chuột. Dùng nó sẽ vừa không sáng lúc
        hover, vừa sáng sai lúc nhấn Tab tới nút.
        """
        # Map từng nút menu với tên icon trong bộ Font Awesome 5 Solid
        icon_map = {
            self.btn_dashboard: "fa5s.th-large",         # Lưới ô vuông - tổng quan
            self.btn_products:  "fa5s.box",              # Thùng hàng - sản phẩm
            self.btn_suppliers: "fa5s.truck",            # Xe tải - nhà cung cấp
            self.btn_importing: "fa5s.download",         # Mũi tên xuống - nhập hàng
            self.btn_customers: "fa5s.users",            # Nhóm người - khách hàng
            self.btn_pos:       "fa5s.shopping-cart",    # Giỏ hàng - bán hàng (POS)
            self.btn_analytics: "fa5s.chart-bar",        # Biểu đồ cột - báo cáo thống kê
            self.btn_settings:  "fa5s.cog",              # Bánh răng - cài đặt hệ thống
            self.btn_help:      "fa5s.question-circle",  # Dấu hỏi - trung tâm trợ giúp
            self.btn_logout:    "fa5s.sign-out-alt",     # Mũi tên đi ra - đăng xuất
        }

        # Kích thước icon dùng chung cho mọi nút menu
        icon_size = QSize(20, 20)

        # Hai màu icon phải khớp với "color" của #sidebar_frame QPushButton
        # trong QSS (đặt ở MainWindow.ui) tại trạng thái tương ứng. Nếu đổi màu
        # chữ trong QSS thì nhớ đổi cả 2 hằng dưới đây.
        color_normal = "#cbd5e1"   # Khớp rule QPushButton thường
        color_active = "#ffffff"   # Khớp rule QPushButton:hover và :checked

        # Cache sẵn icon cho từng nút. Bắt buộc phải cache vì qta.icon() render
        # lại font mỗi lần gọi - nếu gọi trong handler hover thì rê chuột nhanh
        # qua sidebar sẽ bị giật.
        self._nav_icon_normal = {}
        self._nav_icon_active = {}

        for button, icon_name in icon_map.items():
            try:
                self._nav_icon_normal[button] = qta.icon(icon_name, color=color_normal)
                self._nav_icon_active[button] = qta.icon(icon_name, color=color_active)
            except Exception as e:
                # Thiếu icon không được phép làm sập giao diện, chỉ ghi log cảnh báo
                logger.error("Không tải được icon '%s' cho nút menu: %s", icon_name, e)
                continue

            button.setIconSize(icon_size)

            # Thêm khoảng đệm giữa icon và chữ. Qt không có thuộc tính QSS nào
            # chỉnh riêng khoảng cách icon - chữ của QPushButton (padding đẩy cả
            # cụm), nên chèn 2 dấu cách vào đầu text. Có kiểm tra startswith để
            # gọi lại hàm này cũng không bị cộng dồn khoảng trắng.
            if not button.text().startswith("  "):
                button.setText("  " + button.text())

            # Nguồn tín hiệu 1: chuột vào / rời khỏi nút -> bắt qua eventFilter()
            button.installEventFilter(self)

            # Nguồn tín hiệu 2: nút được chọn / bỏ chọn. Connect cho cả 10 nút mà
            # không cần kiểm tra isCheckable(): nút không checkable thì đơn giản
            # là không bao giờ phát tín hiệu này.
            button.toggled.connect(
                lambda checked, b=button: self._update_nav_icon(b, hovered=False)
            )

            # Đặt icon khớp trạng thái ban đầu của nút
            self._update_nav_icon(button, hovered=False)

    def _update_nav_icon(self, button: QPushButton, hovered: bool) -> None:
        """
        Chọn phiên bản icon (xám / trắng) đúng với trạng thái hiện tại của nút.

        Icon sáng trắng khi nút đang hover HOẶC đang active (checked). Chính vế
        "hoặc" này giữ cho nút đang active vẫn có icon trắng sau khi chuột rời
        đi, vì lúc đó hovered=False nhưng isChecked() vẫn là True.

        Args:
            button (QPushButton): Nút menu cần cập nhật icon.
            hovered (bool): Chuột có đang nằm trên nút hay không.
        """
        # Nút có thể chưa dựng được icon (lỗi ở _setup_sidebar_icons)
        if button not in self._nav_icon_normal:
            return

        if hovered or button.isChecked():
            button.setIcon(self._nav_icon_active[button])
        else:
            button.setIcon(self._nav_icon_normal[button])

    def eventFilter(self, obj, event):
        """
        Bắt sự kiện chuột vào (Enter) / rời khỏi (Leave) các nút menu sidebar
        để đổi màu icon cho khớp với màu chữ mà QSS đang áp dụng.
        """
        if obj in self._nav_icon_normal:
            if event.type() == QEvent.Type.Enter:
                self._update_nav_icon(obj, hovered=True)
            elif event.type() == QEvent.Type.Leave:
                # Truyền hovered=False tường minh thay vì đọc obj.underMouse(),
                # vì tại thời điểm xử lý Leave thì underMouse() vẫn còn True.
                self._update_nav_icon(obj, hovered=False)

        # Luôn trả sự kiện về cho lớp cha xử lý tiếp, không chặn
        return super().eventFilter(obj, event)

    def _set_active_nav_button(self, button: QPushButton) -> None:
        """
        Đánh dấu nút menu đang được mở và ghi nhớ để khôi phục khi cần.

        Args:
            button (QPushButton): Nút menu tương ứng với tab đang hiển thị.
        """
        button.setChecked(True)
        self.active_nav_button = button
>>>>>>> Stashed changes

    def _update_datetime(self) -> None:
        """
        Cập nhật ngày giờ hiện tại lên giao diện.
        """
        current_time = QDateTime.currentDateTime().toString("dd/MM/yyyy HH:mm:ss")
        self.lblDateTime.setText(current_time)

    def _setup_event(self) -> None:
        """
        Đăng ký sự kiện (Event) cho các nút bấm trên giao diện.
        """
        # Kết nối sự kiện click của nút Dashboard
        self.btn_dashboard.clicked.connect(self._show_dashboard)
<<<<<<< Updated upstream
        self.btn_logout.clicked.connect(self._show_logout)
=======

        # Kết nối sự kiện click của nút Bán hàng (POS)
        self.btn_pos.clicked.connect(self._show_pos)

        # Kết nối các nút bấm khác đến thông báo phát triển tính năng (Đã loại bỏ btn_pos)
        other_buttons = [
            (self.btn_products, "Sản phẩm"),
            (self.btn_suppliers, "Nhà cung cấp"),
            (self.btn_importing, "Nhập hàng"),
            (self.btn_customers, "Khách hàng"),
            (self.btn_analytics, "Báo cáo thống kê"),
            (self.btn_settings, "Cài đặt hệ thống"),
            (self.btn_help, "Trung tâm trợ giúp"),
        ]
        for btn, name in other_buttons:
            btn.clicked.connect(lambda checked=False, n=name: self._show_feature_placeholder(n))
>>>>>>> Stashed changes

        # Các ô "Thao tác nhanh" trên Dashboard điều hướng như nút menu tương ứng
        self.dashboard_controller.quick_action_requested.connect(self._on_quick_action)

    def _on_quick_action(self, action_key: str) -> None:
        """
        Điều hướng khi người dùng bấm một ô Thao tác nhanh trên Dashboard.

        Args:
            action_key (str): Mã thao tác do DashboardController gửi lên.
        """
        if action_key == "pos":
            self._show_pos()
            return

        feature_names = {
            "products": "Sản phẩm",
            "importing": "Nhập hàng",
            "customers": "Khách hàng",
        }
        self._show_feature_placeholder(feature_names.get(action_key, action_key))

    def _show_dashboard(self) -> None:
<<<<<<< Updated upstream
        self.stacked_widget.setCurrentWidget(self.dashboard_controller)
        self.dashboard_controller.load_data()

    def _show_logout(self) -> None:
        logger.info("Đang đăng xuất khỏi tài khoản %s", Session.get_username())
        Session.clear_session()
        from src.controller.LoginController import LoginController
        self.showlogin = LoginController()
        self.showlogin.show()
        self.close()
=======
        """
        Hiển thị tab Dashboard và tải dữ liệu mới.
        """
        self._set_active_nav_button(self.btn_dashboard)
        self.stacked_widget.setCurrentWidget(self.dashboard_controller)
        self.dashboard_controller.load_data()

    def _show_pos(self) -> None:
        """
        Hiển thị màn hình Bán hàng (POS) và nạp danh sách sản phẩm.
        """
        self._set_active_nav_button(self.btn_pos)
        self.stacked_widget.setCurrentWidget(self.pos_controller)
        self.pos_controller.load_data()
>>>>>>> Stashed changes

    def _show_feature_placeholder(self, feature_name: str) -> None:
        """
        Hiển thị hộp thoại thông báo tính năng đang phát triển và trả trạng thái
        sáng của menu về đúng tab đang mở.
        """
        if self.active_nav_button is not None:
            self.active_nav_button.setChecked(True)

        QMessageBox.information(
            self,
            "Tính năng đang phát triển",
            f"Tính năng '{feature_name}' hiện tại đang được phát triển và sẽ sớm được cập nhật."
        )

    def _load_user_data(self) -> None:
        """
        Tải thông tin người dùng từ Session và Cơ sở dữ liệu để hiển thị câu chào.
        """
        if not Session.is_active():
            self.lblGreeting.setText("Xin chào, Khách!")
            return

        user_id = Session.get_user_id()
        fullname = ""

        try:
            with Database.get_session_ctx() as session:
                user = session.query(User).filter_by(user_id=user_id).first()
                if user and user.full_name:
                    fullname = user.full_name
        except Exception as e:
            logger.error("Lỗi khi truy vấn thông tin người dùng từ cơ sở dữ liệu: %s", e)

        # Fallback về username nếu không có fullname
        if not fullname:
            fullname = Session.get_username() or "Người dùng"
        self.lblGreeting.setText(f"Xin chào, {fullname}!")

    def _block_admin_features_for_cashier(self) -> None:
        """
        Phân quyền và hạn chế tính năng đối với nhân viên thu ngân (nếu cần).
        """
        # Sẽ bổ sung logic phân quyền chi tiết tại đây
        pass