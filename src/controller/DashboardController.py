import logging
import math
from datetime import datetime
from typing import List, Optional

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget,
                             QTableWidgetItem, QHeaderView, QAbstractItemView,
                             QAbstractScrollArea)
from PySide6.QtCore import QEvent, QObject, QThread, Signal, Qt, QRectF
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QLinearGradient, QPixmap

from src.utils.FormIcon import apply_icon, icon
from src.utils.Theme import set_state

from src.gui.tabs.dashboard_ui import Ui_Form
from src.dtos.DashboardDTO import DashboardDTO
from src.services.impl.DashboardServiceImpl import DashboardServiceImpl

logger = logging.getLogger(__name__)

CARD_ICON_SIZE = QtCore.QSize(16, 16)
QUICK_ACTION_ICON_SIZE = QtCore.QSize(24, 24)
REFRESH_ICON_SIZE = QtCore.QSize(14, 14)

ICON_BADGE_SIZE = QtCore.QSize(32, 32)
ICON_BADGE_TEXT_GAP = 10

TITLE_BAR_HEIGHT = 32

INVOICE_CODE_COLUMN_WIDTH = 107
TOTAL_AMOUNT_COLUMN_WIDTH = 96

TRANSACTION_ROW_HEIGHT = 42

class DashboardWorker(QThread):
    data_fetched = Signal(DashboardDTO)
    error_occurred = Signal(str)


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

class WeeklyRevenueWorker(QThread):
    revenue_fetched = Signal(list)
    error_occurred = Signal(str)


    def __init__(self, year: int, month: int, parent: Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent)
        self.year = year
        self.month = month
        self._service = DashboardServiceImpl()


    def run(self) -> None:
        try:
            revenue = self._service.get_weekly_revenue(self.year, self.month)
            self.revenue_fetched.emit(revenue)
        except Exception as e:
            logger.exception("Lỗi khi lấy doanh thu tuần ở luồng nền: %s", e)
            self.error_occurred.emit(str(e))


class DashboardChartWidget(QWidget):
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
            max_val = 1000000.0  

        magnitude = 10 ** math.floor(math.log10(max_val)) if max_val > 0 else 1
        if magnitude == 0:
            magnitude = 1
        max_scale = math.ceil(max_val / magnitude) * magnitude

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
    quick_action_requested = Signal(str)


    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.chart_widget: Optional[DashboardChartWidget] = None
        self._revenue_worker: Optional[WeeklyRevenueWorker] = None
        self._selected_month: int = datetime.now().month
        self.table_widget: Optional[QTableWidget] = None
        self.worker: Optional[DashboardWorker] = None

        self.quick_action_keys: dict = {}

        self._notify_loaded = False

        self._setup_custom_ui()
        self._setup_card_icons()
        self._setup_quick_actions()
        self._setup_connections()


    def _setup_custom_ui(self) -> None:
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
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Mã hóa đơn", "Thời gian", "Thanh toán", "Tổng tiền"])
        
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        self.table_widget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table_widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        header = self.table_widget.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.table_widget.setColumnWidth(0, INVOICE_CODE_COLUMN_WIDTH)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        self.table_widget.setColumnWidth(3, TOTAL_AMOUNT_COLUMN_WIDTH)

        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.table_widget.verticalHeader().setDefaultSectionSize(TRANSACTION_ROW_HEIGHT)
        self.table_widget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.table_widget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        table_layout.addWidget(self.table_widget)


    def _setup_card_icons(self) -> None:
        icon_map = {
            self.label_4: ("revenue", "#3b82f6", "badgeRevenue"),
            self.label_6: ("invoice", "#8b5cf6", "badgeInvoice"),
            self.label_8: ("stock", "#b45309", "badgeStock"),
            self.label_10: ("add-customer", "#10b981", "badgeCustomer"),
        }

        for title_label, (icon_name, tone, badge_name) in icon_map.items():
            built = icon(icon_name, tone)
            if built.isNull():
                continue
            self._put_icon_before_title(title_label, built.pixmap(CARD_ICON_SIZE), badge_name)


    def _put_icon_before_title(self, title_label: QLabel, pixmap: QPixmap, badge_name: str) -> None:
        card = title_label.parentWidget()
        card_layout = card.layout()

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
        badge = QLabel(parent)
        badge.setPixmap(pixmap)

        badge.setObjectName(badge_name)

        badge.setFixedSize(ICON_BADGE_SIZE)
        badge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        return badge


    def _setup_quick_actions(self) -> None:
        tiles = [
            (self.frame_7, "pos", "Bán hàng", "pos"),
            (self.frame_11, "products", "Sản phẩm", "products"),
            (self.frame_9, "importing", "Nhập hàng", "import"),
            (self.frame_8, "customers", "Khách hàng", "customers"),
        ]

        for frame, action_key, caption, icon_name in tiles:
            self._build_quick_action_tile(frame, caption, icon_name)
            self.quick_action_keys[frame] = action_key
            frame.setCursor(Qt.CursorShape.PointingHandCursor)
            frame.installEventFilter(self)


    def _build_quick_action_tile(self, frame: QWidget, caption: str, icon_name: str) -> None:
        tile_layout = frame.layout() or QVBoxLayout(frame)
        tile_layout.setContentsMargins(8, 10, 8, 10)

        tile_layout.setSpacing(5)

        icon_label = QLabel(frame)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        apply_icon(icon_label, icon_name, tone="primary", size=QUICK_ACTION_ICON_SIZE)

        caption_label = QLabel(caption, frame)
        caption_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        caption_label.setObjectName("lblQuickActionCaption")

        tile_layout.addStretch()
        tile_layout.addWidget(icon_label)
        tile_layout.addWidget(caption_label)
        tile_layout.addStretch()


    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.MouseButtonRelease and source in self.quick_action_keys:
            self.quick_action_requested.emit(self.quick_action_keys[source])

        return super().eventFilter(source, event)


    def _setup_connections(self) -> None:
        self._setup_refresh_button()
        self.btnRefresh.clicked.connect(self._on_refresh_clicked)
        self._setup_month_selector()


    def _setup_month_selector(self) -> None:
        current_month = datetime.now().month

        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(current_month - 1)
        self.comboBox.blockSignals(False)

        self._selected_month = current_month
        self.comboBox.currentIndexChanged.connect(self._on_month_changed)


    def _on_month_changed(self, index: int) -> None:
        month = index + 1
        if month < 1 or month > 12:
            return

        self._selected_month = month
        self._load_weekly_revenue(datetime.now().year, month)


    def _load_weekly_revenue(self, year: int, month: int) -> None:
        if self._revenue_worker is not None and self._revenue_worker.isRunning():
            return

        self.comboBox.setEnabled(False)

        self._revenue_worker = WeeklyRevenueWorker(year, month, self)
        self._revenue_worker.revenue_fetched.connect(self._on_weekly_revenue_fetched)
        self._revenue_worker.error_occurred.connect(self._on_weekly_revenue_error)
        self._revenue_worker.finished.connect(lambda: self.comboBox.setEnabled(True))
        self._revenue_worker.start()


    def _on_weekly_revenue_fetched(self, weekly_revenue: list) -> None:
        if self.chart_widget:
            self.chart_widget.set_data(weekly_revenue)


    def _on_weekly_revenue_error(self, message: str) -> None:
        logger.error("Không tải được doanh thu theo tháng: %s", message)
        if self.chart_widget:
            self.chart_widget.set_data([0.0, 0.0, 0.0, 0.0])


    def _setup_refresh_button(self) -> None:
        apply_icon(self.btnRefresh, "refresh", tone="on-primary", size=REFRESH_ICON_SIZE)


    def _on_refresh_clicked(self) -> None:
        self._notify_loaded = True
        self.load_data()


    def load_data(self) -> None:
        if self.worker and self.worker.isRunning():
            logger.warning("Dashboard fetch already running, ignoring reload request.")
            self._notify_loaded = False
            return

        self.btnRefresh.setEnabled(False)
        self.btnRefresh.setText("Đang tải...")

        self.worker = DashboardWorker(low_stock_threshold=10)
        self.worker.data_fetched.connect(self._on_data_fetched)
        self.worker.error_occurred.connect(self._on_error)
        self.worker.finished.connect(self._on_worker_finished)
        self.worker.start()


    def _on_data_fetched(self, data: DashboardDTO) -> None:
        logger.info("Dashboard stats successfully received. Rendering UI elements...")

        revenue_str = f"{data.today_revenue:,.0f} đ"
        self.label_5.setText(revenue_str)
        self._format_growth_label(self.label_12, data.revenue_growth_rate)

        self.label_14.setText(f"{data.today_invoice_count:,}")
        self._format_growth_label(self.label_7, data.invoice_growth_rate)

        self.label_9.setText(f"{data.low_stock_count}")
        if data.low_stock_count > 0:
            self.label_13.setText("Cần nhập hàng ngay!")
            set_state(self.label_13, "warning")
        else:
            self.label_13.setText("Kho hàng an toàn")
            set_state(self.label_13, "safe")

        self.label_11.setText(f"{data.new_customer_count}")
        self._format_growth_label(self.label_15, data.customer_growth_rate)

        if self._selected_month == datetime.now().month:
            if self.chart_widget:
                self.chart_widget.set_data(data.weekly_revenue)
        else:
            self._load_weekly_revenue(datetime.now().year, self._selected_month)

        if self.table_widget:
            self.table_widget.setRowCount(0)
            for idx, tx in enumerate(data.recent_transactions):
                self.table_widget.insertRow(idx)
                
                code_item = QTableWidgetItem(tx.invoice_code)
                code_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 0, code_item)
                
                time_item = QTableWidgetItem(tx.formatted_time)
                time_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 1, time_item)
                
                payment_item = QTableWidgetItem(tx.payment_method)
                payment_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 2, payment_item)

                total_item = QTableWidgetItem(f"{tx.final_total:,.0f} đ")
                total_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 3, total_item)

        if self._notify_loaded:
            self._notify_loaded = False
            QtWidgets.QMessageBox.information(
                self,
                "Tải lại dữ liệu",
                f"Đã cập nhật số liệu mới vào lúc {datetime.now():%H:%M:%S}.",
            )


    def _format_growth_label(self, label: QLabel, rate: float) -> None:
        if rate > 0:
            label.setText(f"▲ +{rate:,.1f}%")
            set_state(label, "up")
        elif rate < 0:
            label.setText(f"▼ {rate:,.1f}%")
            set_state(label, "down")
        else:
            label.setText(f"■ {rate:,.1f}%")
            set_state(label, "flat")


    def _on_error(self, error_message: str) -> None:
        logger.error("Failed to load dashboard data: %s", error_message)
        self._notify_loaded = False
        QtWidgets.QMessageBox.warning(
            self,
            "Lỗi",
            f"Không thể tải dữ liệu Dashboard: {error_message}"
        )


    def _on_worker_finished(self) -> None:
        self.btnRefresh.setEnabled(True)
        self.btnRefresh.setText("Tải lại dữ liệu")