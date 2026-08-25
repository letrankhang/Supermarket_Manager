import logging
import os
from typing import List, Optional

from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QVBoxLayout, QMessageBox,
    QPushButton, QButtonGroup
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, QDateTime, Qt, QSize, QEvent
import qtawesome as qta

from src.gui.main_window_ui import Ui_MainWindow
from src.utils.Session import Session
from config.database import Database
from src.entities.user import User
from src.controller.DashboardController import DashboardController
from src.controller.POSController import POSController
from src.controller.PersonnelController import PersonnelController
from src.controller.SupplierController import SupplierController
from src.controller.HelpCenterController import HelpCenterController

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
        self._show_dashboard()

    def _fix_logo(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.abspath(os.path.join(current_dir, "..", "..", "assets", "images", "logo_sidebar2.png"))

        if os.path.exists(logo_path):
            self.label_4.setPixmap(QPixmap(logo_path))
        else:
            logger.error("Logo not found at path: %s", logo_path)

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
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_datetime)
        self.timer.start(1000)
        self._update_datetime()

        if not self.widget_3.layout():
            layout = QVBoxLayout(self.widget_3)
            layout.setContentsMargins(0, 0, 0, 0)
            self.widget_3.setLayout(layout)
        else:
            layout = self.widget_3.layout()

        self.stacked_widget = QStackedWidget(self.widget_3)
        layout.addWidget(self.stacked_widget)

        self.dashboard_controller = DashboardController()
        self.stacked_widget.addWidget(self.dashboard_controller)

        self.pos_controller = POSController()
        self.stacked_widget.addWidget(self.pos_controller)

        #  Nhân sự
        self.personnel_controller = PersonnelController()
        self.stacked_widget.addWidget(self.personnel_controller.get_view())

        # nhà cung cấp
        self.supplier_controller = SupplierController()
        self.stacked_widget.addWidget(self.supplier_controller.get_view())
        self.help_center_controller = HelpCenterController()
        self.stacked_widget.addWidget(self.help_center_controller)


        self._setup_navigation()


    def _setup_navigation(self) -> None:
        self.nav_buttons: List[QPushButton] = [
            self.btn_dashboard,
            self.btn_products,
            self.btn_suppliers,
            self.btn_importing,
            self.btn_customers,
            self.btn_pos,
            self.btn_analytics,
            self.btn_settings,
            self.btn_help,
        ]

        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        for button in self.nav_buttons:
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.nav_group.addButton(button)

        for button in (self.btn_help, self.btn_logout):
            button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.active_nav_button: Optional[QPushButton] = None

        self._setup_sidebar_icons()

    def _setup_sidebar_icons(self) -> None:
        """Gán icon qtawesome cho toàn bộ nút menu sidebar, đổi màu theo trạng thái."""
        icon_map = {
            self.btn_dashboard: "fa5s.th-large",
            self.btn_products: "fa5s.box",
            self.btn_suppliers: "fa5s.truck",
            self.btn_importing: "fa5s.download",
            self.btn_customers: "fa5s.users",
            self.btn_pos: "fa5s.shopping-cart",
            self.btn_analytics: "fa5s.chart-bar",
            self.btn_settings: "fa5s.cog",
            self.btn_help: "fa5s.question-circle",
            self.btn_logout: "fa5s.sign-out-alt",
        }

        icon_size = QSize(20, 20)
        color_normal = "#cbd5e1"
        color_active = "#ffffff"

        self._nav_icon_normal = {}
        self._nav_icon_active = {}

        for button, icon_name in icon_map.items():
            try:
                self._nav_icon_normal[button] = qta.icon(icon_name, color=color_normal)
                self._nav_icon_active[button] = qta.icon(icon_name, color=color_active)
            except Exception as e:
                logger.error("Không tải được icon '%s' cho nút menu: %s", icon_name, e)
                continue

            button.setIconSize(icon_size)

            if not button.text().startswith("  "):
                button.setText("  " + button.text())

            button.installEventFilter(self)
            button.toggled.connect(
                lambda checked, b=button: self._update_nav_icon(b, hovered=False)
            )
            self._update_nav_icon(button, hovered=False)

    def _update_nav_icon(self, button: QPushButton, hovered: bool) -> None:
        """Chọn phiên bản icon (xám / trắng) đúng trạng thái hiện tại của nút."""
        if button not in self._nav_icon_normal:
            return

        if hovered or button.isChecked():
            button.setIcon(self._nav_icon_active[button])
        else:
            button.setIcon(self._nav_icon_normal[button])

    def eventFilter(self, obj, event):
        if obj in self._nav_icon_normal:
            if event.type() == QEvent.Type.Enter:
                self._update_nav_icon(obj, hovered=True)
            elif event.type() == QEvent.Type.Leave:
                self._update_nav_icon(obj, hovered=False)
        return super().eventFilter(obj, event)

    def _set_active_nav_button(self, button: QPushButton) -> None:
        button.setChecked(True)
        self.active_nav_button = button

    def _update_datetime(self) -> None:
        current_time = QDateTime.currentDateTime().toString("dd/MM/yyyy HH:mm:ss")
        self.lblDateTime.setText(current_time)

    def _setup_event(self) -> None:
        self.btn_dashboard.clicked.connect(self._show_dashboard)
        self.btn_logout.clicked.connect(self._show_logout)
        self.btn_help.clicked.connect(self._show_help_center)
        self.btn_pos.clicked.connect(self._show_pos)

        # --- BỔ SUNG: Gắn sự kiện click cho nút Cài đặt hệ thống ---
        self.btn_settings.clicked.connect(self._show_settings)
        self.btn_suppliers.clicked.connect(self._show_suppliers)

        unimplemented_buttons = [
            self.btn_products,
            self.btn_importing,
            self.btn_customers,
            self.btn_analytics,
        ]
        for btn in unimplemented_buttons:
            btn.clicked.connect(self._revert_nav_button)

        self.dashboard_controller.quick_action_requested.connect(self._on_quick_action)

    def _revert_nav_button(self) -> None:
        """Giữ trạng thái checked của nút menu cũ khi bấm vào tính năng chưa phát triển."""
        if self.active_nav_button is not None:
            self.active_nav_button.setChecked(True)

    def _on_quick_action(self, action_key: str) -> None:
        if action_key == "pos":
            self._show_pos()
            return

    def _show_dashboard(self) -> None:
        self._set_active_nav_button(self.btn_dashboard)
        self.stacked_widget.setCurrentWidget(self.dashboard_controller)
        self.dashboard_controller.load_data()

    def _show_pos(self) -> None:
        self._set_active_nav_button(self.btn_pos)
        self.stacked_widget.setCurrentWidget(self.pos_controller)
        self.pos_controller.load_data()

    # --- BỔ SUNG: Hàm chuyển sang màn hình Cài đặt hệ thống (Nhân sự) ---
    def _show_settings(self) -> None:
        """Hiển thị màn hình Quản lý Nhân sự (System Settings)."""
        self._set_active_nav_button(self.btn_settings)
        self.stacked_widget.setCurrentWidget(self.personnel_controller.get_view())

    def _show_suppliers(self) -> None:
        self._set_active_nav_button(self.btn_suppliers)
        self.stacked_widget.setCurrentWidget(self.supplier_controller.get_view())

    def _show_help_center(self) -> None:
        self._set_active_nav_button(self.btn_help)
        self.stacked_widget.setCurrentWidget(self.help_center_controller)

    def _show_logout(self) -> None:
        reply = QMessageBox.question(
            self,
            "Xác nhận đăng xuất",
            "Bạn có chắc chắn muốn đăng xuất không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self._perform_logout()

    def _perform_logout(self) -> None:
        logger.info("Đang đăng xuất khỏi tài khoản %s", Session.get_username())
        Session.clear_session()

        from src.controller.LoginController import LoginController
        self.logout = LoginController()
        self.logout.show()
        self.close()

    def _load_user_data(self) -> None:
        if not Session.is_active():
            self.lblUserName.setText("Khách")
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

        if not fullname:
            fullname = Session.get_username() or "Người dùng"
        self.lblUserName.setText(fullname)

    def _block_admin_features_for_cashier(self) -> None:
        pass