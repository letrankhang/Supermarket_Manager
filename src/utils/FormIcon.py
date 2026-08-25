import logging
import os
from typing import Optional

import qtawesome as qta

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QAbstractButton, QHBoxLayout, QLabel, QLineEdit, QToolButton, QWidget,
)

logger = logging.getLogger(__name__)

LEFT_ICON_SIZE = 30
EYE_ICON_SIZE = 24
RIGHT_MARGIN = 10

# Icon qtawesome khai bao san trong file .ui, giong cach help_center dang lam.
AWESOME_SIZE = QSize(14, 14)
AWESOME_COLOR = "#2563eb"
SEARCH_ICON_COLOR = "#94a3b8"


def apply_awesome_icons(root: QWidget, default_size: QSize = AWESOME_SIZE) -> None:
    """Duyet cay widget cua 'root', gan icon qtawesome cho moi widget co khai bao
    thuoc tinh dong 'iconName' trong file .ui. Mau lay tu 'iconColor', kich thuoc
    rieng lay tu 'iconPx' (so nguyen, don vi px).

    Dat ten la 'iconPx' chu khong phai 'iconSize' vi QAbstractButton da co san
    thuoc tinh 'iconSize' cua Qt, dung trung ten se doc nham gia tri cua Qt."""
    for widget in root.findChildren(QWidget):
        icon_name = widget.property("iconName")
        if not icon_name:
            continue

        color = widget.property("iconColor") or AWESOME_COLOR
        raw_px = widget.property("iconPx")
        size = QSize(int(raw_px), int(raw_px)) if raw_px else default_size

        try:
            icon = qta.icon(str(icon_name), color=str(color))
        except Exception as error:
            logger.error(
                "Khong tai duoc icon '%s' cua widget '%s': %s",
                icon_name, widget.objectName(), error,
            )
            continue

        if isinstance(widget, QLabel):
            widget.setPixmap(icon.pixmap(size))
        elif isinstance(widget, QAbstractButton):
            widget.setIcon(icon)
            widget.setIconSize(size)


def add_awesome_left_icon(
    line_edit: QLineEdit,
    icon_name: str,
    color: str = SEARCH_ICON_COLOR,
) -> None:
    """Gan icon qtawesome vao dau o nhap (vi du icon kinh lup cho o tim kiem)."""
    try:
        line_edit.addAction(
            qta.icon(icon_name, color=color),
            QLineEdit.ActionPosition.LeadingPosition,
        )
    except Exception as error:
        logger.error("Khong tai duoc icon '%s' cho o nhap: %s", icon_name, error)

def get_image_path(file_name: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.abspath(
        os.path.join(current_dir, "..", "..", "assets", "images", file_name)
    )
    if not os.path.exists(image_path):
        logger.error("Image path not found: %s", image_path)
        return ""
    return image_path.replace("\\", "/")


def create_icon(file_name: str, size: int) -> QIcon:
    path = get_image_path(file_name)
    if not path:
        return QIcon()

    pixmap = QPixmap(path)
    if pixmap.isNull():
        return QIcon()

    scaled = pixmap.scaled(
        size,
        size,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )
    return QIcon(scaled)


def show_logo(label: QLabel, file_name: str = "logo.png"):
    path = get_image_path(file_name)
    if not path:
        return

    pixmap = QPixmap(path)
    if pixmap.isNull():
        logger.error("Failed to read logo file: %s", path)
        return

    label.setScaledContents(False)
    label.setPixmap(
        pixmap.scaled(
            label.width(),
            label.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
    )

def add_left_icon(line_edit: QLineEdit, *file_names: str, size: int = LEFT_ICON_SIZE):
    for file_name in file_names:
        icon = create_icon(file_name, size)
        if not icon.isNull():
            line_edit.addAction(icon, QLineEdit.ActionPosition.LeadingPosition)
            return

def add_toggle_password_button(line_edit: QLineEdit, size: int = EYE_ICON_SIZE, margin_right: int = RIGHT_MARGIN) -> Optional[QToolButton]:
    icon_view = QIcon(get_image_path("view.png"))
    icon_hide = QIcon(get_image_path("hide.png"))

    if icon_view.isNull() or icon_hide.isNull():
        logger.warning("Missing eye icons (view/hide.png), skipping toggle button.")
        return None

    button = QToolButton(line_edit)
    button.setIconSize(QSize(size, size))
    button.setFixedSize(size, size)
    button.setCursor(Qt.CursorShape.PointingHandCursor)
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def update_icon():
        is_hidden = line_edit.echoMode() == QLineEdit.EchoMode.Password
        button.setIcon(icon_view if is_hidden else icon_hide)
        button.setToolTip("Show password" if is_hidden else "Hide password")

    def toggle_visibility():
        is_hidden = line_edit.echoMode() == QLineEdit.EchoMode.Password
        line_edit.setEchoMode(
            QLineEdit.EchoMode.Normal if is_hidden else QLineEdit.EchoMode.Password
        )
        update_icon()

    button.clicked.connect(toggle_visibility)

    layout = line_edit.layout()
    if layout is None:
        layout = QHBoxLayout(line_edit)

    layout.setContentsMargins(0, 0, int(margin_right), 0)
    layout.addStretch()
    layout.addWidget(button)

    line_edit.setTextMargins(0, 0, int(size + margin_right), 0)
    update_icon()
    return button