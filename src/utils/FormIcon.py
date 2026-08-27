import logging
import os
from typing import Optional

import qtawesome as qta

from PySide6.QtCore import QEvent, QObject, QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QAbstractButton, QHBoxLayout, QLabel, QLineEdit, QToolButton, QWidget,
)


logger = logging.getLogger(__name__)

LEFT_ICON_SIZE = 30
EYE_ICON_SIZE = 24
RIGHT_MARGIN = 10

AWESOME_SIZE = QSize(14, 14)
BUTTON_ICON_SIZE = QSize(16, 16)
CARD_ICON_SIZE = QSize(20, 20)
SEARCH_ICON_COLOR = "#94a3b8"

ICONS = {
    "add": "fa5s.plus",
    "add-category": "fa5s.folder-plus",
    "add-customer": "fa5s.user-plus",
    "add-row": "fa5s.plus",
    "analytics": "fa5s.chart-line",
    "back": "fa5s.chevron-left",
    "barcode": "fa5s.barcode",
    "card": "fa5s.credit-card",
    "cart": "fa5s.shopping-cart",
    "cash": "fa5s.money-bill-wave",
    "category": "fa5s.tags",
    "check": "fa5s.check",
    "clear": "fa5s.times",
    "customers": "fa5s.users",
    "dashboard": "fa5s.th-large",
    "database": "fa5s.database",
    "delete": "fa5s.trash-alt",
    "detail": "fa5s.list-ul",
    "discount": "fa5s.percent",
    "edit": "fa5s.edit",
    "collapse": "fa5s.chevron-down",
    "email": "fa5s.envelope",
    "expand": "fa5s.chevron-right",
    "export": "fa5s.file-export",
    "filter": "fa5s.filter",
    "forward": "fa5s.chevron-right",
    "github": "fa5b.github",
    "guide": "fa5s.book-open",
    "help": "fa5s.question-circle",
    "history": "fa5s.history",
    "import": "fa5s.file-import",
    "invoice": "fa5s.file-invoice",
    "keyboard": "fa5s.keyboard",
    "linkedin": "fa5b.linkedin",
    "lock": "fa5s.lock",
    "logout": "fa5s.sign-out-alt",
    "minus": "fa5s.minus",
    "next": "fa5s.chevron-right",
    "pos": "fa5s.shopping-cart",
    "previous": "fa5s.chevron-left",
    "print": "fa5s.print",
    "products": "fa5s.box",
    "revenue": "fa5s.chart-line",
    "receipt": "fa5s.receipt",
    "refresh": "fa5s.sync-alt",
    "role": "fa5s.user-shield",
    "save": "fa5s.save",
    "search": "fa5s.search",
    "send": "fa5s.paper-plane",
    "server": "fa5s.server",
    "settings": "fa5s.cog",
    "stock": "fa5s.exclamation-triangle",
    "supplier": "fa5s.truck",
    "tag": "fa5s.tag",
    "tools": "fa5s.tools",
    "transfer": "fa5s.university",
    "user": "fa5s.user",
    "user-active": "fa5s.user-check",
    "user-group": "fa5s.user-friends",
    "version": "fa5s.code-branch",
}

TONES = {
    "default": "#64748b",
    "primary": "#1d4ed8",
    "on-primary": "#ffffff",
    "text": "#0f172a",
    "muted": "#94a3b8",
    "danger": "#dc2626",
    "success": "#10b981",
    "warning": "#f59e0b",
    "sidebar": "#cbd5e1",
    "sidebar-active": "#ffffff",
    "sidebar-disabled": "#475569",
}

HOVER_OFF = "none"

HOVER_TONES = {
    "edit": "primary",
    "delete": "danger",
}

def resolve(name: str) -> str:
    return ICONS.get(name, name)

def icon(
    name: str,
    tone: str = "default",
    color: Optional[str] = None,
    color_active: Optional[str] = None,
    color_disabled: Optional[str] = None,
) -> QIcon:
    options = {"color": color or TONES.get(tone, tone)}
    if color_active is None:
        color_active = HOVER_TONES.get(name)
    if color_active and color_active != HOVER_OFF:
        options["color_active"] = TONES.get(color_active, color_active)
    if color_disabled:
        options["color_disabled"] = TONES.get(color_disabled, color_disabled)
    try:
        return qta.icon(resolve(name), **options)
    except Exception as error:
        logger.error("Khong tai duoc icon '%s': %s", name, error)
        return QIcon()


class _HoverIconFilter(QObject):
    def __init__(self, button: QAbstractButton, normal: QIcon, hover: QIcon) -> None:
        super().__init__(button)
        self._button = button
        self._normal = normal
        self._hover = hover

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if watched is self._button:
            if event.type() == QEvent.Type.Enter:
                self._button.setIcon(self._hover)
            elif event.type() == QEvent.Type.Leave:
                self._button.setIcon(self._normal)
        return False


def _install_hover_icon(button: QAbstractButton, normal: QIcon, hover: QIcon) -> None:
    for child in button.findChildren(_HoverIconFilter):
        button.removeEventFilter(child)
        child.setParent(None)
    button.installEventFilter(_HoverIconFilter(button, normal, hover))


def apply_icon(
    widget: QWidget,
    name: str,
    tone: str = "default",
    size: QSize = BUTTON_ICON_SIZE,
    color: Optional[str] = None,
    color_active: Optional[str] = None,
    color_disabled: Optional[str] = None,
    hover: Optional[str] = None,
) -> None:
    hover_tone = HOVER_TONES.get(name) if hover is None else hover

    if color_active is None and hover_tone == HOVER_OFF:
        color_active = HOVER_OFF

    built = icon(name, tone, color, color_active, color_disabled)
    if built.isNull():
        return
    if isinstance(widget, QLabel):
        widget.setPixmap(built.pixmap(size))
    elif isinstance(widget, QAbstractButton):
        widget.setIcon(built)
        widget.setIconSize(size)

        if hover_tone and hover_tone != HOVER_OFF:
            hovered = icon(name, tone, color=TONES.get(hover_tone, hover_tone))
            if not hovered.isNull():
                _install_hover_icon(widget, built, hovered)


def apply_awesome_icons(root: QWidget, default_size: QSize = AWESOME_SIZE) -> None:
    for widget in root.findChildren(QWidget):
        icon_name = widget.property("iconName")
        if not icon_name:
            continue

        raw_px = widget.property("iconPx")
        size = QSize(int(raw_px), int(raw_px)) if raw_px else default_size
        tone = widget.property("iconColor") or "primary"
        hover = widget.property("iconHover")
        apply_icon(
            widget,
            str(icon_name),
            tone=str(tone),
            size=size,
            hover=str(hover) if hover else None,
        )


def add_awesome_left_icon(line_edit: QLineEdit, icon_name: str = "search", color: str = SEARCH_ICON_COLOR) -> None:
    built = icon(icon_name, color=color)
    if not built.isNull():
        line_edit.addAction(built, QLineEdit.ActionPosition.LeadingPosition)


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