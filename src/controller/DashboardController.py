import logging
import math
from datetime import datetime
from typing import List, Optional

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget,
                             QTableWidgetItem, QHeaderView, QAbstractItemView)
from PyQt6.QtCore import QEvent, QObject, QThread, pyqtSignal, Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QFont, QPen, QLinearGradient, QPixmap

import qtawesome as qta

from src.gui.tabs.dashboard_ui import Ui_Form
from src.dtos.DashboardDTO import DashboardDTO, RecentTransactionDTO
from src.services.impl.DashboardServiceImpl import DashboardServiceImpl

logger = logging.getLogger(__name__)

CARD_ICON_SIZE = QtCore.QSize(16, 16)
QUICK_ACTION_ICON_SIZE = QtCore.QSize(24, 24)
REFRESH_ICON_SIZE = QtCore.QSize(14, 14)

# Huy hiệu icon trên 4 thẻ thống kê: ô vuông bo góc, icon nằm chính giữa.
# Màu nền và bo góc của huy hiệu nằm trong QSS của dashboard.ui.
ICON_BADGE_SIZE = QtCore.QSize(32, 32)
ICON_BADGE_TEXT_GAP = 10

# Chiều cao dải tiêu đề của 2 khối hàng dưới (biểu đồ / giao dịch gần đây).
# Phải khớp với minimumSize/maximumSize của frame_18 trong dashboard.ui.
TITLE_BAR_HEIGHT = 32


class DashboardWorker(QThread):
    data_fetched = pyqtSignal(DashboardDTO)
    error_occurred = pyqtSignal(str)

    def __init__(self, low_stock_threshold: int = 10, parent: Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent)
        self.low_stock_threshold = low_stock_threshold
        self._service = DashboardServiceImpl()

    def run(self) -> None:
        try:
            logger.info("Starting dashboard background data fetch...")
            data = self._service.get_dashboard_data(self.low_stock_threshold)
            self.data_fetched.emit(data)
        except Exception as e:
            logger.exception("Error occurred in DashboardWorker thread: %s", e)
            self.error_occurred.emit(str(e))


class DashboardChartWidget(QWidget):
    """Vẽ biểu đồ cột doanh thu theo tuần bằng QPainter, không cần matplotlib hay QtCharts."""
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.weekly_revenue: List[float] = [0.0, 0.0, 0.0, 0.0]

    def set_data(self, weekly_revenue: List[float]) -> None:
        self.weekly_revenue = weekly_revenue
        self.update()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()

        padding_left = 60
        padding_right = 20
        padding_top = 40
        padding_bottom = 40

        plot_height = height - padding_top - padding_bottom
        plot_width = width - padding_left - padding_right

        if plot_height <= 0 or plot_width <= 0:
            return

        max_val = max(self.weekly_revenue) if self.weekly_revenue else 0.0
        if max_val <= 0.0:
            max_val = 1000000.0  # Chưa có doanh thu vẫn phải có thang đo, tránh chia cho 0

        # Làm tròn trần lên số đẹp để vạch chia trục Y không lẻ
        magnitude = 10 ** math.floor(math.log10(max_val)) if max_val > 0 else 1
        if magnitude == 0:
            magnitude = 1
        max_scale = math.ceil(max_val / magnitude) * magnitude

        # Lưới ngang và nhãn trục Y
        painter.setPen(QPen(QColor("#e2e8f0"), 1))
        num_grid_lines = 4
        for i in range(num_grid_lines + 1):
            y = padding_top + plot_height - (i * plot_height / num_grid_lines)
            painter.drawLine(int(padding_left), int(y), int(width - padding_right), int(y))
            
            val = (i * max_scale / num_grid_lines)
            if val >= 1000000:
                val_str = f"{val/1000000:,.1f}M"
            elif val >= 1000:
                val_str = f"{val/1000:,.0f}k"
            else:
                val_str = f"{val:,.0f}"
            
            painter.setPen(QPen(QColor("#64748b"), 1))
            painter.setFont(QFont("Arial", 8))
            painter.drawText(
                QRectF(5, y - 10, padding_left - 10, 20),
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
                val_str
            )
            painter.setPen(QPen(QColor("#e2e8f0"), 1))

        # Cột doanh thu từng tuần
        num_bars = len(self.weekly_revenue)
        if num_bars > 0:
            bar_gap = 40
            total_gaps_width = bar_gap * (num_bars + 1)
            bar_width = (plot_width - total_gaps_width) / num_bars
            if bar_width <= 0:
                bar_width = 10

            for i, val in enumerate(self.weekly_revenue):
                x = padding_left + bar_gap + i * (bar_width + bar_gap)
                bar_h = (val / max_scale) * plot_height if max_scale > 0 else 0
                y = padding_top + plot_height - bar_h

                rect = QRectF(x, y, bar_width, bar_h)
                gradient = QLinearGradient(rect.topLeft(), rect.bottomLeft())
                gradient.setColorAt(0.0, QColor("#3b82f6"))
                gradient.setColorAt(1.0, QColor("#60a5fa"))

                painter.fillRect(rect, gradient)

                painter.setPen(QPen(QColor("#2563eb"), 1))
                painter.drawRect(rect)

                painter.setPen(QPen(QColor("#1e293b"), 1))
                painter.setFont(QFont("Arial", 9, QFont.Weight.Bold))
                val_text = f"{val/1000:,.0f}k" if val >= 1000 else f"{val:,.0f}"
                painter.drawText(
                    QRectF(x - 20, y - 22, bar_width + 40, 20),
                    Qt.AlignmentFlag.AlignCenter,
                    val_text
                )

                painter.setFont(QFont("Arial", 9))
                painter.drawText(
                    QRectF(x - 20, padding_top + plot_height + 8, bar_width + 40, 20),
                    Qt.AlignmentFlag.AlignCenter,
                    f"Tuần {i+1}"
                )


class DashboardController(QWidget, Ui_Form):
    """Điều khiển màn hình Dashboard: dựng giao diện, tải dữ liệu nền và vẽ đồ họa."""

    # Phát khi bấm một ô thao tác nhanh, kèm mã hành động
    quick_action_requested = pyqtSignal(str)

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        self.chart_widget: Optional[DashboardChartWidget] = None
        self.table_widget: Optional[QTableWidget] = None
        self.worker: Optional[DashboardWorker] = None

        self.quick_action_keys: dict = {}

        # Chỉ bật khi người dùng tự bấm nút, để lần tải lúc chuyển tab không hiện hộp thoại
        self._bao_khi_tai_xong = False

        self._setup_custom_ui()
        self._show_today()
        self._setup_card_icons()
        self._setup_quick_actions()
        self._setup_connections()

    def _setup_custom_ui(self) -> None:
        """Dựng biểu đồ và bảng giao dịch gần đây vào các frame trống của dashboard.ui."""
        if not self.chart_container.layout():
            chart_layout = QVBoxLayout(self.chart_container)
            chart_layout.setContentsMargins(0, 0, 0, 0)
        else:
            chart_layout = self.chart_container.layout()

        self.chart_widget = DashboardChartWidget(self)
        chart_layout.addWidget(self.chart_widget)

        table_layout = QVBoxLayout(self.frame_table)
        table_layout.setContentsMargins(15, 15, 15, 15)
        table_layout.setSpacing(10)

        table_title = QLabel("Giao dịch gần đây", self)
        table_title.setObjectName("lblTableTitle")
        table_title.setFixedHeight(TITLE_BAR_HEIGHT)
        table_layout.addWidget(table_title)

        self.table_widget = QTableWidget(self)
        self.table_widget.setObjectName("tblRecentTransactions")
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Mã hóa đơn", "Thời gian", "Tổng tiền"])
        
        # Bảng chỉ để xem: không sửa, không chọn, không nhận focus
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        self.table_widget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table_widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        table_layout.addWidget(self.table_widget)

    def _show_today(self) -> None:
        """Ghi ngày hôm nay lên tiêu đề, đè ngày mẫu trong file .ui để không hiện ngày cũ."""
        today = datetime.now()
        self.label_2.setText(f"Hôm nay, ngày {today.day} tháng {today.month} năm {today.year}")

    def _setup_card_icons(self) -> None:
        """Gắn icon Font Awesome trước tiêu đề của 4 thẻ thống kê."""
        # Mỗi thẻ: (tên icon Font Awesome, màu icon, objectName của huy hiệu).
        # Màu nền huy hiệu tra theo objectName trong QSS của dashboard.ui.
        icon_map = {
            self.label_4: ("fa5s.chart-line", "#3b82f6", "badgeRevenue"),
            self.label_6: ("fa5s.file-invoice", "#8b5cf6", "badgeInvoice"),
            self.label_8: ("fa5s.exclamation-triangle", "#b45309", "badgeStock"),
            self.label_10: ("fa5s.user-plus", "#10b981", "badgeCustomer"),
        }

        for title_label, (icon_name, icon_color, badge_name) in icon_map.items():
            try:
                pixmap = qta.icon(icon_name, color=icon_color).pixmap(CARD_ICON_SIZE)
            except Exception as e:
                logger.error("Could not load dashboard card icon '%s': %s", icon_name, e)
                continue
            self._put_icon_before_title(title_label, pixmap, badge_name)

    def _put_icon_before_title(self, title_label: QLabel, pixmap: QPixmap,
                               badge_name: str) -> None:
        """Bọc tiêu đề thẻ vào một hàng gồm huy hiệu icon và chữ."""
        card = title_label.parentWidget()
        card_layout = card.layout()

        # Nhớ vị trí cũ rồi gỡ nhãn ra, để chèn lại đúng chỗ đó dưới dạng một hàng
        position = card_layout.indexOf(title_label)
        card_layout.removeWidget(title_label)

        badge = self._create_icon_badge(card, pixmap, badge_name)

        title_row = QHBoxLayout()
        title_row.setContentsMargins(0, 0, 0, 0)
        title_row.setSpacing(ICON_BADGE_TEXT_GAP)
        title_row.addWidget(badge)
        title_row.addWidget(title_label)
        title_row.addStretch()

        card_layout.insertLayout(position, title_row)

    def _create_icon_badge(self, parent: QWidget, pixmap: QPixmap, badge_name: str) -> QLabel:
        """Tạo ô nền bo góc nằm sau icon của thẻ thống kê."""
        badge = QLabel(parent)
        badge.setPixmap(pixmap)

        # Nền nhạt bo góc mềm lấy từ QSS trong dashboard.ui
        badge.setObjectName(badge_name)

        badge.setFixedSize(ICON_BADGE_SIZE)
        badge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        return badge

    def _setup_quick_actions(self) -> None:
        """Đổ icon và nhãn vào 4 ô thao tác nhanh; bấm vào ô sẽ phát quick_action_requested."""
        tiles = [
            (self.frame_7, "pos", "Bán hàng", "fa5s.shopping-cart"),
            (self.frame_11, "products", "Sản phẩm", "fa5s.box"),
            (self.frame_9, "importing", "Nhập hàng", "fa5s.download"),
            (self.frame_8, "customers", "Khách hàng", "fa5s.users"),
        ]

        for frame, action_key, caption, icon_name in tiles:
            self._build_quick_action_tile(frame, caption, icon_name)
            self.quick_action_keys[frame] = action_key
            frame.setCursor(Qt.CursorShape.PointingHandCursor)
            frame.installEventFilter(self)

    def _build_quick_action_tile(self, frame: QWidget, caption: str, icon_name: str) -> None:
        """Vẽ nội dung cho một ô thao tác nhanh."""
        tile_layout = frame.layout() or QVBoxLayout(frame)
        tile_layout.setContentsMargins(8, 10, 8, 10)
        tile_layout.setSpacing(6)

        icon_label = QLabel(frame)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        try:
            icon_label.setPixmap(qta.icon(icon_name, color="#3b82f6").pixmap(QUICK_ACTION_ICON_SIZE))
        except Exception as e:
            logger.error("Could not load quick action icon '%s': %s", icon_name, e)

        caption_label = QLabel(caption, frame)
        caption_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Kiểu chữ lấy từ QSS #lblQuickActionCaption trong dashboard.ui
        caption_label.setObjectName("lblQuickActionCaption")

        tile_layout.addWidget(icon_label)
        tile_layout.addWidget(caption_label)

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        """Biến cú click lên ô thao tác nhanh thành tín hiệu quick_action_requested."""
        if event.type() == QEvent.Type.MouseButtonRelease and source in self.quick_action_keys:
            self.quick_action_requested.emit(self.quick_action_keys[source])

        return super().eventFilter(source, event)

    def _setup_connections(self) -> None:
        """Nối các tín hiệu tương tác của màn hình."""
        self._setup_refresh_button()
        self.pushButton.clicked.connect(self._on_refresh_clicked)

    def _setup_refresh_button(self) -> None:
        """Gắn icon vòng xoay vào nút Tải lại dữ liệu."""
        # Màu nền, bo góc và kích thước nút nằm trong QSS #pushButton của dashboard.ui
        try:
            icon = qta.icon("fa5s.sync-alt", color="#ffffff", color_disabled="#f8fafc")
        except Exception as e:
            logger.error("Could not load dashboard refresh icon: %s", e)
            return

        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(REFRESH_ICON_SIZE)

    def _on_refresh_clicked(self) -> None:
        """Bấm nút Tải lại dữ liệu: bật cờ để báo kết quả khi tải xong."""
        # MainWindowController cũng gọi load_data khi chuyển tab, cờ này phân biệt hai đường vào
        self._bao_khi_tai_xong = True
        self.load_data()

    def load_data(self) -> None:
        """Chạy luồng nền lấy dữ liệu dashboard."""
        if self.worker and self.worker.isRunning():
            logger.warning("Dashboard fetch already running, ignoring reload request.")
            self._bao_khi_tai_xong = False
            return

        self.pushButton.setEnabled(False)
        self.pushButton.setText("Đang tải...")

        self.worker = DashboardWorker(low_stock_threshold=10)
        self.worker.data_fetched.connect(self._on_data_fetched)
        self.worker.error_occurred.connect(self._on_error)
        self.worker.finished.connect(self._on_worker_finished)
        self.worker.start()

    def _on_data_fetched(self, data: DashboardDTO) -> None:
        """Đổ dữ liệu lấy được lên các thẻ, biểu đồ và bảng giao dịch."""
        logger.info("Dashboard stats successfully received. Rendering UI elements...")

        self._show_today()

        # 1. Doanh thu hôm nay
        revenue_str = f"{data.today_revenue:,.0f} đ"
        self.label_5.setText(revenue_str)
        self._format_growth_label(self.label_12, data.revenue_growth_rate)

        # 2. Số hóa đơn hôm nay
        self.label_14.setText(f"{data.today_invoice_count:,}")
        self._format_growth_label(self.label_7, data.invoice_growth_rate)

        # 3. Cảnh báo sắp hết hàng
        self.label_9.setText(f"{data.low_stock_count}")
        if data.low_stock_count > 0:
            self.label_13.setText("Cần nhập hàng ngay!")
            self._apply_state(self.label_13, "canhBao")
        else:
            self.label_13.setText("Kho hàng an toàn")
            self._apply_state(self.label_13, "anToan")

        # 4. Khách hàng mới
        self.label_11.setText(f"{data.new_customer_count}")
        self._format_growth_label(self.label_15, data.customer_growth_rate)

        # 5. Biểu đồ doanh thu theo tuần
        if self.chart_widget:
            self.chart_widget.set_data(data.weekly_revenue)

        # 6. Bảng giao dịch gần đây
        if self.table_widget:
            self.table_widget.setRowCount(0)
            for idx, tx in enumerate(data.recent_transactions):
                self.table_widget.insertRow(idx)
                
                code_item = QTableWidgetItem(tx.invoice_code)
                code_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 0, code_item)
                
                time_item = QTableWidgetItem(tx.formatted_time)
                time_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 1, time_item)
                
                total_item = QTableWidgetItem(f"{tx.final_total:,.0f} đ")
                total_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 2, total_item)

        # Đặt cuối cùng: hộp thoại chặn luồng giao diện, hiện sớm thì người dùng
        # bấm OK xong mới thấy số liệu mới nhảy vào
        if self._bao_khi_tai_xong:
            self._bao_khi_tai_xong = False
            QtWidgets.QMessageBox.information(
                self,
                "Tải lại dữ liệu",
                f"Đã cập nhật số liệu mới vào lúc {datetime.now():%H:%M:%S}.",
            )

    def _format_growth_label(self, label: QLabel, rate: float) -> None:
        """Đặt ký hiệu tăng/giảm cho nhãn tỉ lệ; màu do QSS đọc thuộc tính trangThai."""
        if rate > 0:
            label.setText(f"▲ +{rate:,.1f}%")
            self._apply_state(label, "tang")
        elif rate < 0:
            label.setText(f"▼ {rate:,.1f}%")
            self._apply_state(label, "giam")
        else:
            label.setText(f"■ {rate:,.1f}%")
            self._apply_state(label, "giu")

    @staticmethod
    def _apply_state(label: QLabel, state: str) -> None:
        """Gán thuộc tính trangThai rồi ép Qt vẽ lại nhãn theo QSS trong dashboard.ui."""
        # Không unpolish/polish thì Qt giữ nguyên màu cũ khi trạng thái đổi
        label.setProperty("trangThai", state)
        label.style().unpolish(label)
        label.style().polish(label)

    def _on_error(self, error_message: str) -> None:
        """Báo lỗi cho người dùng khi tải dữ liệu thất bại."""
        logger.error("Failed to load dashboard data: %s", error_message)
        self._bao_khi_tai_xong = False
        QtWidgets.QMessageBox.warning(
            self,
            "Lỗi",
            f"Không thể tải dữ liệu Dashboard: {error_message}"
        )

    def _on_worker_finished(self) -> None:
        """Bật lại nút Tải lại dữ liệu khi luồng nền kết thúc."""
        self.pushButton.setEnabled(True)
        self.pushButton.setText("Tải lại dữ liệu")