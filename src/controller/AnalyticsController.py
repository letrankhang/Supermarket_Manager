import logging
import math
from typing import List, Optional

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar,
    QTableWidgetItem, QHeaderView, QAbstractItemView, QButtonGroup,
    QPushButton,
)
from PySide6.QtCore import Qt, QSize, QThread, Signal, QRectF
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush

import qtawesome as qta

from src.gui.tabs.analytics_ui import Ui_Analytics
from src.dtos.AnalyticsDTO import AnalyticsDTO, DailyRevenueDTO, CategorySalesDTO
from src.services.impl.AnalyticsServiceImpl import AnalyticsServiceImpl
from src.utils.Theme import repolish, set_trend


logger = logging.getLogger(__name__)

ICON_SIZE = QSize(18, 18)

class AnalyticsWorker(QThread):
    data_fetched = Signal(AnalyticsDTO)
    error_occurred = Signal(str)


    def __init__(
        self, period_type: str = "week", parent: Optional[QtCore.QObject] = None
    ) -> None:
        super().__init__(parent)
        self._period_type = period_type
        self._service = AnalyticsServiceImpl()


    def run(self) -> None:
        try:
            logger.info("Bắt đầu tải dữ liệu Analytics cho kỳ '%s'…", self._period_type)
            data = self._service.get_analytics_by_period(self._period_type)
            self.data_fetched.emit(data)
        except Exception as e:
            logger.exception("Lỗi trong AnalyticsWorker: %s", e)
            self.error_occurred.emit(str(e))


class DotMatrixBarChart(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._data: List[DailyRevenueDTO] = []


    def set_data(self, data: List[DailyRevenueDTO]) -> None:
        self._data = data
        self.update()


    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w, h = self.width(), self.height()
        pl, pr, pt, pb = 20, 20, 20, 32
        pw, ph = w - pl - pr, h - pt - pb
        if pw <= 0 or ph <= 0:
            return

        painter.setPen(QPen(QColor("#e2e8f0"), 1, Qt.PenStyle.DashLine))
        painter.drawRect(QRectF(pl, pt, pw, ph))

        dot_rows = 6
        dot_cols = 14
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor("#cbd5e1")))
        for r in range(1, dot_rows):
            dot_y = pt + r * (ph / dot_rows)
            for c in range(1, dot_cols):
                dot_x = pl + c * (pw / dot_cols)
                painter.drawEllipse(QtCore.QPointF(dot_x, dot_y), 1.2, 1.2)

        days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "CN"]
        values = [25.0, 45.0, 32.0, 70.0, 52.0, 95.0, 60.0]

        if self._data:
            data_map = {d.day_label: d.revenue for d in self._data}
            if any(v > 0 for v in data_map.values()):
                values = [data_map.get(day, 0.0) for day in days]

        max_val = max(values) if values and max(values) > 0 else 100.0
        max_idx = values.index(max(values)) if values else -1

        n = len(days)
        bar_width = max(16.0, pw / (n * 2.8))
        step = pw / n

        for i, (day, val) in enumerate(zip(days, values)):
            cx = pl + (i + 0.5) * step
            bx = cx - bar_width / 2

            bar_ratio = (val / max_val) if max_val > 0 else 0.1
            bar_height = max(8.0, bar_ratio * (ph - 15))
            by = pt + ph - bar_height

            if i == max_idx and val > 0:
                bar_color = QColor("#002d72")
            else:
                bar_color = QColor("#819dc7")

            painter.setBrush(QBrush(bar_color))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(QRectF(bx, by, bar_width, bar_height))

            painter.setPen(QPen(QColor("#64748b"), 1))
            painter.setFont(QFont("Segoe UI", 8))
            painter.drawText(
                QRectF(cx - 25, pt + ph + 8, 50, 18),
                Qt.AlignmentFlag.AlignCenter,
                day
            )


class AnalyticsController(QWidget, Ui_Analytics):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._worker: Optional[AnalyticsWorker] = None
        self._current_period = "week"

        self._setup_period_toggle()
        self._setup_chart()
        self._setup_icons()
        self._setup_table()
        self._setup_connections()

        repolish(self)


    def _setup_period_toggle(self) -> None:
        self._period_group = QButtonGroup(self)
        self._period_group.setExclusive(True)
        self._period_group.addButton(self.btnPeriodToday)
        self._period_group.addButton(self.btnPeriodWeek)
        self._period_group.addButton(self.btnPeriodMonth)


    def _setup_chart(self) -> None:
        if not hasattr(self, "containerTimeChart"):
            self.containerTimeChart = QWidget(self.cardTimeChart)
            if self.cardTimeChart.layout():
                self.cardTimeChart.layout().addWidget(self.containerTimeChart)
            else:
                layout = QVBoxLayout(self.cardTimeChart)
                layout.addWidget(self.containerTimeChart)

        chart_layout = QVBoxLayout(self.containerTimeChart)
        chart_layout.setContentsMargins(0, 0, 0, 0)
        self._time_chart = DotMatrixBarChart(self.containerTimeChart)
        chart_layout.addWidget(self._time_chart)


    def _setup_icons(self) -> None:
        for badge_attr, icon_name in (
            ("badgeRevenue", "fa5s.money-bill-wave"),
            ("badgeOrders", "fa5s.shopping-cart"),
            ("badgeAov", "fa5s.receipt"),
            ("badgeReturn", "fa5s.user-friends"),
        ):
            if hasattr(self, badge_attr):
                try:
                    badge_widget = getattr(self, badge_attr)
                    if isinstance(badge_widget, QLabel):
                        badge_widget.setPixmap(qta.icon(icon_name, color="#2563eb").pixmap(ICON_SIZE))
                except Exception as e:
                    logger.debug("Bỏ qua icon %s: %s", icon_name, e)

        if hasattr(self, "btnDetailLink"):
            self.btnDetailLink.setIcon(qta.icon("fa5s.sync-alt", color="#1d4ed8"))

    def _setup_table(self) -> None:
        header_view = self.tblTopProducts.horizontalHeader()
        header_view.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header_view.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)


    def _setup_connections(self) -> None:
        self.btnPeriodToday.clicked.connect(lambda: self._on_period_changed("today"))
        self.btnPeriodWeek.clicked.connect(lambda: self._on_period_changed("week"))
        self.btnPeriodMonth.clicked.connect(lambda: self._on_period_changed("month"))
        
        if hasattr(self, "btnDetailLink"):
            self.btnDetailLink.clicked.connect(lambda: self.load_data())


    def _on_period_changed(self, period_type: str) -> None:
        self._current_period = period_type
        self.load_data()


    def load_data(self) -> None:
        if self._worker and self._worker.isRunning():
            return

        self._worker = AnalyticsWorker(self._current_period)
        self._worker.data_fetched.connect(self._on_data_fetched)
        self._worker.error_occurred.connect(self._on_error)
        self._worker.start()


    def _format_currency_short(self, amount: float) -> str:
        if amount >= 1_000_000_000:
            return f"₫{amount / 1_000_000_000:,.2f}B"
        elif amount >= 1_000_000:
            return f"₫{amount / 1_000_000:,.0f}M"
        elif amount >= 1_000:
            return f"₫{amount / 1_000:,.0f}K"
        return f"₫{amount:,.0f}"


    def _apply_trend(self, label_attr: str, growth: float, suffix: str = "%") -> None:
        if not hasattr(self, label_attr):
            return

        label = getattr(self, label_attr)
        if growth > 0:
            arrow, direction, sign = "↗", "up", "+"
        elif growth < 0:
            arrow, direction, sign = "↘", "down", ""
        else:
            arrow, direction, sign = "→", "flat", ""

        label.setText(f"{arrow} {sign}{growth}{suffix}")
        set_trend(label, direction)


    def _on_data_fetched(self, data: AnalyticsDTO) -> None:
        logger.info("Analytics data loaded successfully for %s", data.period_label)

        if hasattr(self, "lblRevenueVal"):
            self.lblRevenueVal.setText(self._format_currency_short(data.total_revenue))
        self._apply_trend("lblRevenueTrend", data.revenue_growth)

        if hasattr(self, "lblOrdersVal"):
            self.lblOrdersVal.setText(f"{data.total_invoices:,}")
        self._apply_trend("lblOrdersTrend", data.invoices_growth)

        if hasattr(self, "lblAovVal"):
            self.lblAovVal.setText(self._format_currency_short(data.avg_order_value))
        self._apply_trend("lblAovTrend", data.aov_growth)

        if hasattr(self, "lblReturnVal"):
            self.lblReturnVal.setText(f"{data.returning_rate:.1f}%")
        self._apply_trend("lblReturnTrend", data.returning_growth)

        self._time_chart.set_data(data.daily_revenues)
        self._render_category_breakdown(data.categories)
        self._render_top_products(data.top_products)


    def _render_category_breakdown(self, categories: List[CategorySalesDTO]) -> None:
        if not hasattr(self, "containerCategoryList"):
            return

        while self.containerCategoryList.count():
            item = self.containerCategoryList.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        display_cats = categories if categories else [
            CategorySalesDTO(category_name="Thực phẩm khô", total_revenue=45000000.0, percentage=50.0),
            CategorySalesDTO(category_name="Hóa phẩm", total_revenue=22500000.0, percentage=25.0),
            CategorySalesDTO(category_name="Đồ uống", total_revenue=12600000.0, percentage=14.0),
            CategorySalesDTO(category_name="Sữa và chế phẩm", total_revenue=9000000.0, percentage=10.0),
        ]

        for cat in display_cats[:4]:
            cat_widget = QWidget()
            cat_layout = QVBoxLayout(cat_widget)
            cat_layout.setContentsMargins(0, 2, 0, 4)
            cat_layout.setSpacing(4)

            lbl_row = QHBoxLayout()
            lbl_name = QLabel(cat.category_name)
            lbl_name.setFont(QFont("Segoe UI", 9))
            lbl_row.addWidget(lbl_name)
            lbl_row.addStretch()

            lbl_pct = QLabel(f"{int(cat.percentage)}%")
            lbl_pct.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
            lbl_row.addWidget(lbl_pct)
            cat_layout.addLayout(lbl_row)

            pbar = QProgressBar()
            pbar.setFixedHeight(7)
            pbar.setTextVisible(False)
            pbar.setRange(0, 100)
            pbar.setValue(int(cat.percentage))
            cat_layout.addWidget(pbar)

            self.containerCategoryList.addWidget(cat_widget)


    def _render_top_products(self, products) -> None:
        self.tblTopProducts.setRowCount(0)
        display_products = products if products else [
            type("TopProd", (), {"product_name": "Mì Hảo Hảo tôm chua cay", "total_quantity": 24, "total_revenue": 108000.0})(),
            type("TopProd", (), {"product_name": "Bia Tiger lon 330ml", "total_quantity": 19, "total_revenue": 342000.0})(),
        ]

        for idx, p in enumerate(display_products):
            self.tblTopProducts.insertRow(idx)
            self.tblTopProducts.setRowHeight(idx, 42)

            name_item = QTableWidgetItem(p.product_name)
            name_item.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
            name_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.tblTopProducts.setItem(idx, 0, name_item)

            qty_item = QTableWidgetItem(f"{p.total_quantity:,}")
            qty_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.tblTopProducts.setItem(idx, 1, qty_item)

            rev_str = self._format_currency_short(p.total_revenue)
            rev_item = QTableWidgetItem(rev_str)
            rev_item.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
            rev_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.tblTopProducts.setItem(idx, 2, rev_item)


    def _on_error(self, msg: str) -> None:
        logger.error("Analytics load error: %s", msg)