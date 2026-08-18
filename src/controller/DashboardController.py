# File: D:\Python\Supermarket_Manager\src\controller\DashboardController.py

import logging
import math
from datetime import datetime
from typing import List, Optional

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QFont, QPen, QLinearGradient

from src.gui.tabs.dashboard import Ui_Form
from src.dtos.DashboardDTO import DashboardDTO, RecentTransactionDTO
from src.services.impl.DashboardServiceImpl import DashboardServiceImpl

logger = logging.getLogger(__name__)


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
    """
    Custom lightweight widget to draw weekly revenue bar charts using QPainter.
    Zero-dependencies alternative to matplotlib/QtCharts.
    """
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.weekly_revenue: List[float] = [0.0, 0.0, 0.0, 0.0]

    def set_data(self, weekly_revenue: List[float]) -> None:
        self.weekly_revenue = weekly_revenue
        self.update()  # Request repaint

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

        # Fallback if dimensions are too small
        if plot_height <= 0 or plot_width <= 0:
            return

        max_val = max(self.weekly_revenue) if self.weekly_revenue else 0.0
        if max_val <= 0.0:
            max_val = 1000000.0  # Default scale helper

        # Calculate a clean scale maximum
        magnitude = 10 ** math.floor(math.log10(max_val)) if max_val > 0 else 1
        if magnitude == 0:
            magnitude = 1
        max_scale = math.ceil(max_val / magnitude) * magnitude

        # Draw gridlines and Y-axis labels
        painter.setPen(QPen(QColor("#e2e8f0"), 1))
        num_grid_lines = 4
        for i in range(num_grid_lines + 1):
            y = padding_top + plot_height - (i * plot_height / num_grid_lines)
            painter.drawLine(int(padding_left), int(y), int(width - padding_right), int(y))
            
            # Y labels
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

        # Draw weekly columns
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
                gradient.setColorAt(0.0, QColor("#3b82f6"))  # Blue-500
                gradient.setColorAt(1.0, QColor("#60a5fa"))  # Blue-400

                # Draw bar fill
                painter.fillRect(rect, gradient)

                # Draw bar outline
                painter.setPen(QPen(QColor("#2563eb"), 1))
                painter.drawRect(rect)

                # Draw value label on top
                painter.setPen(QPen(QColor("#1e293b"), 1))
                painter.setFont(QFont("Arial", 9, QFont.Weight.Bold))
                val_text = f"{val/1000:,.0f}k" if val >= 1000 else f"{val:,.0f}"
                painter.drawText(
                    QRectF(x - 20, y - 22, bar_width + 40, 20),
                    Qt.AlignmentFlag.AlignCenter,
                    val_text
                )

                # Draw week name on bottom
                painter.setFont(QFont("Arial", 9))
                painter.drawText(
                    QRectF(x - 20, padding_top + plot_height + 8, bar_width + 40, 20),
                    Qt.AlignmentFlag.AlignCenter,
                    f"Tuần {i+1}"
                )


class DashboardController(QWidget, Ui_Form):
    """
    Controller responsible for handling dashboard UI elements, background loading,
    and rendering custom UI graphics (SOLID + Model-View separation).
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        self.chart_widget: Optional[DashboardChartWidget] = None
        self.table_widget: Optional[QTableWidget] = None
        self.worker: Optional[DashboardWorker] = None

        self._setup_custom_ui()
        self._setup_connections()

    def _setup_custom_ui(self) -> None:
        """
        Initializes custom elements like the chart layout and transaction table layout.
        """
        # 1. Custom chart widget setup inside self.chart_container
        if not self.chart_container.layout():
            chart_layout = QVBoxLayout(self.chart_container)
            chart_layout.setContentsMargins(0, 0, 0, 0)
        else:
            chart_layout = self.chart_container.layout()

        self.chart_widget = DashboardChartWidget(self)
        chart_layout.addWidget(self.chart_widget)

        # 2. Transaction table setup inside self.frame_table
        table_layout = QVBoxLayout(self.frame_table)
        table_layout.setContentsMargins(15, 15, 15, 15)

        table_title = QLabel("Giao dịch gần đây", self)
        table_title.setStyleSheet("font-weight: bold; font-size: 14px; color: #1e293b; margin-bottom: 5px;")
        table_layout.addWidget(table_title)

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Mã hóa đơn", "Thời gian", "Tổng tiền"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_widget.setStyleSheet("""
            QTableWidget {
                border: none;
                gridline-color: #f1f5f9;
                background-color: white;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #f8fafc;
            }
            QHeaderView::section {
                background-color: #f8fafc;
                padding: 8px;
                font-weight: bold;
                border: none;
                color: #475569;
            }
        """)
        table_layout.addWidget(self.table_widget)

    def _setup_connections(self) -> None:
        """
        Connects interactive events (signals/slots).
        """
        self.pushButton.setText("Tải lại dữ liệu")
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
        """)
        self.pushButton.clicked.connect(self.load_data)

    def load_data(self) -> None:
        """
        Starts the background worker to retrieve dashboard data.
        """
        if self.worker and self.worker.isRunning():
            logger.warning("Dashboard fetch already running, ignoring reload request.")
            return

        self.pushButton.setEnabled(False)
        self.pushButton.setText("Đang tải...")

        # Setup worker thread
        self.worker = DashboardWorker(low_stock_threshold=10)
        self.worker.data_fetched.connect(self._on_data_fetched)
        self.worker.error_occurred.connect(self._on_error)
        self.worker.finished.connect(self._on_worker_finished)
        self.worker.start()

    def _on_data_fetched(self, data: DashboardDTO) -> None:
        """
        Slot fired when dashboard data is retrieved successfully. Updates UI labels.
        """
        logger.info("Dashboard stats successfully received. Rendering UI elements...")

        # Update Greeting Date label
        current_time = datetime.now()
        self.label_2.setText(f"Hôm nay, ngày {current_time.day} tháng {current_time.month} năm {current_time.year}")

        # 1. Today's Revenue
        revenue_str = f"{data.today_revenue:,.0f} đ"
        self.label_5.setText(revenue_str)
        self._format_growth_label(self.label_12, data.revenue_growth_rate)

        # 2. Total Invoices
        self.label_14.setText(f"{data.today_invoice_count:,}")
        self._format_growth_label(self.label_7, data.invoice_growth_rate)

        # 3. Low Stock warning
        self.label_9.setText(f"{data.low_stock_count}")
        if data.low_stock_count > 0:
            self.label_13.setText("Cần nhập hàng ngay!")
            self.label_13.setStyleSheet("color: #eab308; font-weight: bold;")  # Yellow alert
        else:
            self.label_13.setText("Kho hàng an toàn")
            self.label_13.setStyleSheet("color: #10b981;")  # Green status

        # 4. New Customers
        self.label_11.setText(f"{data.new_customer_count}")
        self._format_growth_label(self.label_15, data.customer_growth_rate)

        # 5. Populate Chart
        if self.chart_widget:
            self.chart_widget.set_data(data.weekly_revenue)

        # 6. Populate Recent Transactions Table
        if self.table_widget:
            self.table_widget.setRowCount(0)
            for idx, tx in enumerate(data.recent_transactions):
                self.table_widget.insertRow(idx)
                
                # Invoice Code item
                code_item = QTableWidgetItem(tx.invoice_code)
                code_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 0, code_item)
                
                # Format time item
                time_item = QTableWidgetItem(tx.formatted_time)
                time_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 1, time_item)
                
                # Final Total item
                total_item = QTableWidgetItem(f"{tx.final_total:,.0f} đ")
                total_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(idx, 2, total_item)

    def _format_growth_label(self, label: QLabel, rate: float) -> None:
        """
        Formats a growth rate label with correct positive/negative symbols and theme colors.
        """
        if rate > 0:
            label.setText(f"▲ +{rate:,.1f}%")
            label.setStyleSheet("color: #10b981; font-weight: bold;")  # Emerald Green
        elif rate < 0:
            label.setText(f"▼ {rate:,.1f}%")
            label.setStyleSheet("color: #ef4444; font-weight: bold;")  # Tomato Red
        else:
            label.setText(f"■ {rate:,.1f}%")
            label.setStyleSheet("color: #64748b; font-weight: bold;")  # Slate Gray

    def _on_error(self, error_message: str) -> None:
        """
        Slot fired when data loading fails. Logs error and shows feedback to the user.
        """
        logger.error("Failed to load dashboard data: %s", error_message)
        QtWidgets.QMessageBox.warning(
            self,
            "Lỗi",
            f"Không thể tải dữ liệu Dashboard: {error_message}"
        )

    def _on_worker_finished(self) -> None:
        """
        Enables the refresh button back when the thread completes.
        """
        self.pushButton.setEnabled(True)
        self.pushButton.setText("Tải lại dữ liệu")