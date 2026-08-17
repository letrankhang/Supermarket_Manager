# File: D:\Python\Supermarket_Manager\src\controller\MainWindowController.py

import logging
import os
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, QDateTime
from src.gui.MainWindow import Ui_MainWindow
from src.utils.Sesion import Session
from config.database import Database
from src.entities.user import User
from src.controller.DashboardController import DashboardController

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
        logo_path = os.path.abspath(os.path.join(current_dir, "..", "..", "assets", "images", "logo.png"))
        if os.path.exists(logo_path):
            self.label.setPixmap(QPixmap(logo_path))
        else:
            logger.error("Logo not found at path: %s", logo_path)

        # Sửa đường dẫn ảnh đại diện (avatar)
        avatar_path = os.path.abspath(os.path.join(current_dir, "..", "..", "assets", "images", "avata.jpg"))
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


        # Kết nối các nút bấm khác đến thông báo phát triển tính năng
        other_buttons = [
            (self.btn_products, "Sản phẩm"),
            (self.btn_suppliers, "Nhà cung cấp"),
            (self.btn_importing, "Nhập hàng"),
            (self.btn_customers, "Khách hàng"),
            (self.btn_pos, "Bán hàng (POS)"),
            (self.btn_analytics, "Báo cáo thống kê"),
            (self.btn_settings, "Cài đặt hệ thống"),
            (self.btn_help, "Trung tâm trợ giúp"),
        ]
        for btn, name in other_buttons:
            # Sử dụng default parameter in lambda to capture value properly
            btn.clicked.connect(lambda checked=False, n=name: self._show_feature_placeholder(n))

    def _show_dashboard(self) -> None:
        """
        Hiển thị tab Dashboard và tải dữ liệu mới.
        """
        self.stacked_widget.setCurrentWidget(self.dashboard_controller)
        self.dashboard_controller.load_data()

    def _show_feature_placeholder(self, feature_name: str) -> None:
        """
        Hiển thị hộp thoại thông báo tính năng đang phát triển.
        """
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