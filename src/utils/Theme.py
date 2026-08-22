import logging
from typing import Dict

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication

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
