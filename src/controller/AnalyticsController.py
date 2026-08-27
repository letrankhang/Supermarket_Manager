import logging
import math
from typing import List, Optional

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar,
    QTableWidgetItem, QHeaderView, QButtonGroup,
)
from PySide6.QtCore import Qt, QSize, QThread, Signal, QRectF
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush, QLinearGradient

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


BAR_TOP = "#86d6b4"
BAR_BOTTOM = "#c4ecdb"
BAR_TOP_MAX = "#34b881"
BAR_BOTTOM_MAX = "#86d6b4"
AXIS_LINE = "#cbd5e1"
GRID_LINE = "#eef2f7"
AXIS_TEXT = "#64748b"
AXIS_TITLE = "#94a3b8"
REVENUE_TEXT = "#059669"


def _vn_number(value: float, decimals: int = 0) -> str:
    text = f"{value:,.{decimals}f}"
    return text.replace(",", "_").replace(".", ",").replace("_", ".")


def _format_money_tick(value: float) -> str:
    for unit, suffix in ((1_000_000_000, " tỷ"), (1_000_000, " tr"), (1_000, " N")):
        if value >= unit:
            scaled = value / unit
            decimals = 0 if abs(scaled - round(scaled)) < 0.05 else 1
            return _vn_number(scaled, decimals) + suffix
    return _vn_number(value)


def _nice_ceiling(value: float, ticks: int = 4) -> float:
    if value <= 0:
        return 100.0
    raw = value / ticks
    magnitude = 10 ** math.floor(math.log10(raw))
    for step in (1, 1.5, 2, 2.5, 3, 4, 5, 10):
        if raw <= step * magnitude:
            return step * magnitude * ticks
    return 10 * magnitude * ticks


class DotMatrixBarChart(QWidget):
    Y_TICKS = 4


    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._data: List[DailyRevenueDTO] = []


    def set_data(self, data: List[DailyRevenueDTO]) -> None:
        self._data = data
        self.update()


    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "CN"]
        values = [25.0, 45.0, 32.0, 70.0, 52.0, 95.0, 60.0]

        if self._data:
            data_map = {d.day_label: d.revenue for d in self._data}
            if any(v > 0 for v in data_map.values()):
                values = [data_map.get(day, 0.0) for day in days]

        axis_max = _nice_ceiling(max(values) if values else 0.0, self.Y_TICKS)

        tick_font = QFont("Segoe UI", 8)
        title_font = QFont("Segoe UI", 8, QFont.Weight.DemiBold)
        metrics = QtGui.QFontMetrics(tick_font)
        label_width = max(
            metrics.horizontalAdvance(_format_money_tick(axis_max * i / self.Y_TICKS))
            for i in range(self.Y_TICKS + 1)
        )

        pl = 22 + label_width + 10
        pr, pt, pb = 18, 16, 46
        pw, ph = self.width() - pl - pr, self.height() - pt - pb
        if pw <= 0 or ph <= 0:
            return

        painter.setFont(tick_font)
        for i in range(self.Y_TICKS + 1):
            tick_value = axis_max * i / self.Y_TICKS
            y = pt + ph - (ph * i / self.Y_TICKS)

            if i > 0:
                painter.setPen(QPen(QColor(GRID_LINE), 1))
                painter.drawLine(QtCore.QPointF(pl, y), QtCore.QPointF(pl + pw, y))

            painter.setPen(QPen(QColor(AXIS_TEXT), 1))
            painter.drawText(
                QRectF(pl - label_width - 10, y - 9, label_width, 18),
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
                _format_money_tick(tick_value),
            )

        painter.setPen(QPen(QColor(AXIS_LINE), 1))
        painter.drawLine(QtCore.QPointF(pl, pt), QtCore.QPointF(pl, pt + ph))
        painter.drawLine(QtCore.QPointF(pl, pt + ph), QtCore.QPointF(pl + pw, pt + ph))

        n = len(days)
        bar_width = max(16.0, min(34.0, pw / (n * 2.0)))
        step = pw / n
        max_idx = values.index(max(values)) if values and max(values) > 0 else -1

        for i, (day, val) in enumerate(zip(days, values)):
            cx = pl + (i + 0.5) * step
            bx = cx - bar_width / 2

            bar_ratio = (val / axis_max) if axis_max > 0 else 0.0
            bar_height = max(3.0, bar_ratio * ph)
            by = pt + ph - bar_height

            gradient = QLinearGradient(bx, by, bx, pt + ph)
            if i == max_idx:
                gradient.setColorAt(0.0, QColor(BAR_TOP_MAX))
                gradient.setColorAt(1.0, QColor(BAR_BOTTOM_MAX))
            else:
                gradient.setColorAt(0.0, QColor(BAR_TOP))
                gradient.setColorAt(1.0, QColor(BAR_BOTTOM))

            painter.setBrush(QBrush(gradient))
            painter.setPen(Qt.PenStyle.NoPen)
            radius = min(5.0, bar_width / 2, bar_height / 2)
            painter.drawRoundedRect(QRectF(bx, by, bar_width, bar_height), radius, radius)

            painter.setPen(QPen(QColor(AXIS_TEXT), 1))
            painter.setFont(tick_font)
            painter.drawText(
                QRectF(cx - step / 2, pt + ph + 6, step, 16),
                Qt.AlignmentFlag.AlignCenter,
                day,
            )

        painter.setFont(title_font)
        painter.setPen(QPen(QColor(AXIS_TITLE), 1))
        painter.drawText(
            QRectF(pl, pt + ph + 24, pw, 16),
            Qt.AlignmentFlag.AlignCenter,
            "Ngày trong tuần",
        )

        painter.save()
        painter.translate(14, pt + ph / 2)
        painter.rotate(-90)
        painter.drawText(
            QRectF(-ph / 2, -8, ph, 16),
            Qt.AlignmentFlag.AlignCenter,
            "Doanh thu (đ)",
        )
        painter.restore()


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
        header_view.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.tblTopProducts.setColumnWidth(0, 52)
        header_view.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header_view.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)


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
        return _format_money_tick(amount)


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

        ranked = sorted(display_cats, key=lambda c: c.total_revenue, reverse=True)
        total_revenue = sum(c.total_revenue for c in ranked)

        rows = [
            (c.category_name, c.total_revenue, c.percentage, str(i))
            for i, c in enumerate(ranked)
        ]

        if hasattr(self, "lblCategorySub"):
            self.lblCategorySub.setText(
                f"{len(ranked)} danh mục · tổng {_format_money_tick(total_revenue)}"
            )

        for name, revenue, percentage, series in rows:
            cat_widget = QWidget()
            cat_layout = QVBoxLayout(cat_widget)
            cat_layout.setContentsMargins(0, 2, 0, 4)
            cat_layout.setSpacing(5)

            lbl_row = QHBoxLayout()
            lbl_row.setSpacing(8)

            dot = QLabel()
            dot.setObjectName("CategoryDot")
            dot.setProperty("series", series)
            lbl_row.addWidget(dot)

            lbl_name = QLabel(name)
            lbl_name.setObjectName("CategoryName")
            lbl_row.addWidget(lbl_name)
            lbl_row.addStretch()

            lbl_amount = QLabel(_format_money_tick(revenue))
            lbl_amount.setObjectName("CategoryAmount")
            lbl_row.addWidget(lbl_amount)

            lbl_pct = QLabel(f"{percentage:.1f}%".replace(".", ","))
            lbl_pct.setObjectName("CategoryPercent")
            lbl_row.addWidget(lbl_pct)
            cat_layout.addLayout(lbl_row)

            pbar = QProgressBar()
            pbar.setObjectName("CategoryBar")
            pbar.setProperty("series", series)
            pbar.setTextVisible(False)
            pbar.setRange(0, 100)
            pbar.setValue(int(round(percentage)))
            cat_layout.addWidget(pbar)

            self.containerCategoryList.addWidget(cat_widget)

        self.containerCategoryList.addStretch()


    def _render_top_products(self, products) -> None:
        self.tblTopProducts.setRowCount(0)
        display_products = products if products else [
            type("TopProd", (), {"product_name": "Mì Hảo Hảo tôm chua cay", "total_quantity": 24, "total_revenue": 108000.0})(),
            type("TopProd", (), {"product_name": "Bia Tiger lon 330ml", "total_quantity": 19, "total_revenue": 342000.0})(),
        ]

        for idx, p in enumerate(display_products):
            self.tblTopProducts.insertRow(idx)
            self.tblTopProducts.setRowHeight(idx, 42)

            stt_item = QTableWidgetItem(str(idx + 1))
            stt_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tblTopProducts.setItem(idx, 0, stt_item)

            name_item = QTableWidgetItem(p.product_name)
            name_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.tblTopProducts.setItem(idx, 1, name_item)

            qty_item = QTableWidgetItem(f"{p.total_quantity:,}")
            qty_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.tblTopProducts.setItem(idx, 2, qty_item)

            rev_str = self._format_currency_short(p.total_revenue)
            rev_item = QTableWidgetItem(rev_str)
            rev_item.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
            rev_item.setForeground(QColor(REVENUE_TEXT))
            rev_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.tblTopProducts.setItem(idx, 3, rev_item)


    def _on_error(self, msg: str) -> None:
        logger.error("Analytics load error: %s", msg)