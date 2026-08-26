import logging
from typing import Dict

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QWidget


logger = logging.getLogger(__name__)

LIGHT_COLORS: Dict[str, str] = {
    "window": "#f0f4f8",
    "base": "#ffffff",
    "alternate_base": "#f8fafc",
    "text": "#0f172a",
    "placeholder": "#94a3b8",
    "button": "#f0f4f8",
    "highlight": "#0c2b82",
    "highlighted_text": "#ffffff",
    "tooltip_base": "#ffffff",
    "disabled_text": "#94a3b8",
}


def build_light_palette() -> QPalette:
    palette: QPalette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(LIGHT_COLORS["window"]))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(LIGHT_COLORS["text"]))
    palette.setColor(QPalette.ColorRole.Base, QColor(LIGHT_COLORS["base"]))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(LIGHT_COLORS["alternate_base"]))
    palette.setColor(QPalette.ColorRole.Text, QColor(LIGHT_COLORS["text"]))
    palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(LIGHT_COLORS["placeholder"]))
    palette.setColor(QPalette.ColorRole.Button, QColor(LIGHT_COLORS["button"]))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(LIGHT_COLORS["text"]))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(LIGHT_COLORS["tooltip_base"]))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(LIGHT_COLORS["text"]))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(LIGHT_COLORS["highlight"]))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(LIGHT_COLORS["highlighted_text"]))

    disabled: QPalette.ColorGroup = QPalette.ColorGroup.Disabled
    palette.setColor(disabled, QPalette.ColorRole.Text, QColor(LIGHT_COLORS["disabled_text"]))
    palette.setColor(disabled, QPalette.ColorRole.ButtonText, QColor(LIGHT_COLORS["disabled_text"]))
    palette.setColor(disabled, QPalette.ColorRole.WindowText, QColor(LIGHT_COLORS["disabled_text"]))
    return palette


def apply_light_theme(app: QApplication):
    try:
        app.setStyle("Fusion")
        app.setPalette(build_light_palette())
        logger.info("Đã áp dụng light theme.")
    except Exception as e:
        logger.error("Không thể áp dụng light theme: %s", e)


def set_dynamic_property(widget: QWidget, name: str, value: str) -> None:
    widget.setProperty(name, value)
    style = widget.style()
    style.unpolish(widget)
    style.polish(widget)
    widget.update()


def set_badge(widget: QWidget, variant: str) -> None:
    set_dynamic_property(widget, "badge", variant)


def set_trend(widget: QWidget, direction: str) -> None:
    set_dynamic_property(widget, "trend", direction)


def set_state(widget: QWidget, state: str) -> None:
    set_dynamic_property(widget, "state", state)


def repolish(root: QWidget) -> None:
    root.setStyleSheet(root.styleSheet())
    for widget in root.findChildren(QWidget):
        style = widget.style()
        style.unpolish(widget)
        style.polish(widget)
    root.update()


def badge_cell(text: str, variant: str, min_width: int = 88) -> QWidget:
    container = QWidget()
    layout = QHBoxLayout(container)
    layout.setContentsMargins(4, 4, 4, 4)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    label = QLabel(text)
    label.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setFixedHeight(24)
    label.setMinimumWidth(min_width)
    set_badge(label, variant)

    layout.addWidget(label)
    return container
