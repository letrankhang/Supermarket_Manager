import logging
import os
from typing import List, Optional

from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QVBoxLayout, QMessageBox,
    QPushButton, QButtonGroup
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, QDateTime, Qt, QSize, QEvent
from src.utils.FormIcon import icon

from src.gui.main_window_ui import Ui_MainWindow
from src.utils.Session import Session
from config.database import Database
from src.entities.user import User
from src.controller.DashboardController import DashboardController
from src.controller.POSController import POSController
from src.controller.PersonnelController import PersonnelController
from src.controller.SupplierController import SupplierController
from src.controller.HelpCenterController import HelpCenterController
from src.controller.Productcontroller import ProductController
from src.controller.Importcontroller import ImportController
from src.controller.CustomerManagementController import CustomerManagementController
from src.controller.AnalyticsController import AnalyticsController


logger = logging.getLogger(__name__)

class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._fix_logo()
        self._setup_ui()
        self._setup_event()
        self._load_user_data()
        self._apply_role_permissions()


    def _fix_logo(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.abspath(os.path.join(current_dir, "..", "..", "assets", "images", "logo3.png"))

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

        self.personnel_controller = PersonnelController()
        self.stacked_widget.addWidget(self.personnel_controller.get_view())

        self.supplier_controller = SupplierController()
        self.stacked_widget.addWidget(self.supplier_controller.get_view())
        self.help_center_controller = HelpCenterController()
        self.stacked_widget.addWidget(self.help_center_controller)

        self.product_controller = ProductController(self)
        self.stacked_widget.addWidget(self.product_controller)

        self.import_controller = ImportController(self)
        self.stacked_widget.addWidget(self.import_controller)

        self.customer_controller = CustomerManagementController()
        self.stacked_widget.addWidget(self.customer_controller)

        self.analytics_controller = AnalyticsController()
        self.stacked_widget.addWidget(self.analytics_controller)

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
        icon_map = {
            self.btn_dashboard: "dashboard",
            self.btn_products: "products",
            self.btn_suppliers: "supplier",
            self.btn_importing: "import",
            self.btn_customers: "customers",
            self.btn_pos: "pos",
            self.btn_analytics: "analytics",
            self.btn_settings: "settings",
            self.btn_help: "help",
            self.btn_logout: "logout",
        }

        icon_size = QSize(20, 20)

        self._nav_icon_normal = {}
        self._nav_icon_active = {}
        self._nav_icon_disabled = {}

        for button, icon_name in icon_map.items():
            normal = icon(icon_name, "sidebar")
            if normal.isNull():
                continue
            self._nav_icon_normal[button] = normal
            self._nav_icon_active[button] = icon(icon_name, "sidebar-active")
            self._nav_icon_disabled[button] = icon(icon_name, "sidebar-disabled")

            button.setIconSize(icon_size)

            if not button.text().startswith("  "):
                button.setText("  " + button.text())

            button.installEventFilter(self)
            button.toggled.connect(
                lambda checked, b=button: self._update_nav_icon(b, hovered=False)
            )
            self._update_nav_icon(button, hovered=False)


    def _update_nav_icon(self, button: QPushButton, hovered: bool) -> None:
        if button not in self._nav_icon_normal:
            return

        if not button.isEnabled():
            button.setIcon(self._nav_icon_disabled.get(button, self._nav_icon_normal[button]))
        elif hovered or button.isChecked():
            button.setIcon(self._nav_icon_active[button])
        else:
            button.setIcon(self._nav_icon_normal[button])


    def eventFilter(self, obj: object, event: QEvent) -> bool:
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

        self.btn_products.clicked.connect(self._show_products)
        self.btn_importing.clicked.connect(self._show_importing)
        self.btn_customers.clicked.connect(self._show_customers)
        self.btn_analytics.clicked.connect(self._show_analytics)
        self.btn_settings.clicked.connect(self._show_settings)
        self.btn_suppliers.clicked.connect(self._show_suppliers)

        self.dashboard_controller.quick_action_requested.connect(self._on_quick_action)


    def _on_quick_action(self, action_key: str) -> None:
        if action_key == "pos":
            self._show_pos()
        elif action_key == "products":
            self._show_products()
        elif action_key == "importing":
            self._show_importing()
        elif action_key == "customers":
            self._show_customers()


    def _show_dashboard(self) -> None:
        self._set_active_nav_button(self.btn_dashboard)
        self.stacked_widget.setCurrentWidget(self.dashboard_controller)
        self.dashboard_controller.load_data()


    def _show_pos(self) -> None:
        self._set_active_nav_button(self.btn_pos)
        self.stacked_widget.setCurrentWidget(self.pos_controller)
        self.pos_controller.load_data()


    def _show_customers(self) -> None:
        self._set_active_nav_button(self.btn_customers)
        self.stacked_widget.setCurrentWidget(self.customer_controller)
        self.customer_controller.load_data()


    def _show_analytics(self) -> None:
        self._set_active_nav_button(self.btn_analytics)
        self.stacked_widget.setCurrentWidget(self.analytics_controller)
        self.analytics_controller.load_data()


    def _show_settings(self) -> None:
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


    def _show_products(self) -> None:
        self._set_active_nav_button(self.btn_products)
        self.stacked_widget.setCurrentWidget(self.product_controller)
        self.product_controller.load_data()


    def _show_importing(self) -> None:
        self._set_active_nav_button(self.btn_importing)
        self.stacked_widget.setCurrentWidget(self.import_controller)
        self.import_controller.load_data()

        
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


    def _apply_role_permissions(self) -> None:
        raw_role = Session.get_role_name() or "Admin"
        role = raw_role.strip().lower()
        logger.info("Áp dụng phân quyền giao diện cho vai trò: %s", raw_role)

        all_nav_buttons: List[QPushButton] = [
            self.btn_dashboard,
            self.btn_products,
            self.btn_suppliers,
            self.btn_importing,
            self.btn_customers,
            self.btn_pos,
            self.btn_analytics,
            self.btn_settings,
            self.btn_help,
            self.btn_logout,
        ]

        if role == "admin":
            allowed_buttons = set(all_nav_buttons)
            default_show = self._show_dashboard
        elif role in ("cashier", "thu ngân"):
            allowed_buttons = {
                self.btn_pos,
                self.btn_products,
                self.btn_customers,
                self.btn_help,
                self.btn_logout,
            }
            default_show = self._show_pos
        elif role in ("warehouse", "nhân viên kho", "kho"):
            allowed_buttons = {
                self.btn_importing,
                self.btn_products,
                self.btn_suppliers,
                self.btn_help,
                self.btn_logout,
            }
            default_show = self._show_importing
        else:
            allowed_buttons = {self.btn_pos, self.btn_help, self.btn_logout}
            default_show = self._show_pos

        for btn in all_nav_buttons:
            if btn in allowed_buttons:
                btn.setEnabled(True)
                btn.setCursor(Qt.CursorShape.PointingHandCursor)
                btn.setToolTip("")
                self._update_nav_icon(btn, hovered=False)
            else:
                btn.setEnabled(False)
                btn.setCursor(Qt.CursorShape.ForbiddenCursor)
                btn.setToolTip("Bạn không có quyền truy cập chức năng này.")
                self._update_nav_icon(btn, hovered=False)

        default_show()
