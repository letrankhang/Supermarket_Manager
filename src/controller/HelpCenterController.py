import logging
import os

from typing import Optional

from PySide6.QtCore import QSize, QUrl, Qt
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QAbstractButton, QLabel,
    QToolButton, QWidget,
)

import qtawesome as qta

from src.gui.tabs.help_center_ui import Ui_Form
from src.utils.Session import Session

logger = logging.getLogger(__name__)

VERSION = "1.0.0"

CARD_ICON_SIZE = QSize(15, 15)
AVATAR_ICON_SIZE = QSize(18, 18)
SOCIAL_ICON_SIZE = QSize(15, 15)
ACCORDION_ICON_SIZE = QSize(11, 11)

PRIMARY_COLOR = "#2563eb"
MUTED_COLOR = "#94a3b8"

ROLE_NAMES_VI = {
    "admin": "Quản trị viên",
    "manager": "Quản lý",
    "cashier": "Thu ngân",
}

ICON_SIZES = {
    "cardIcon": CARD_ICON_SIZE,
    "avatar": AVATAR_ICON_SIZE,
    "socialButton": SOCIAL_ICON_SIZE,
    "primaryButton": SOCIAL_ICON_SIZE,
}

class HelpCenterController(QWidget, Ui_Form):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.setupUi(self)

        self.apply_icons()
        self.setup_accordions()
        self.setup_links()
        self.refresh_qss()
        self.update_system_info()

    def apply_icons(self) -> None:
        for widget in self.findChildren(QWidget):
            icon_name = widget.property("iconName")

            if not icon_name:
                continue

            color = widget.property("iconColor") or PRIMARY_COLOR
            size = ICON_SIZES.get(widget.property("class"), CARD_ICON_SIZE)

            try:
                icon = qta.icon(icon_name, color=color)
            except Exception as error:
                logger.error(
                    "Không tải được icon '%s' của widget '%s': %s",
                    icon_name,
                    widget.objectName(),
                    error,
                )
                continue

            if isinstance(widget, QLabel):
                widget.setPixmap(icon.pixmap(size))
            elif isinstance(widget, QAbstractButton):
                widget.setIcon(icon)
                widget.setIconSize(size)

    def setup_accordions(self) -> None:
        for button in self.findChildren(QToolButton):
            if button.property("class") != "accordion":
                continue

            content_name = button.objectName().replace("btn", "content", 1)
            content = self.findChild(QWidget, content_name)

            if content is None:
                logger.error(
                    "Không tìm thấy widget nội dung '%s' cho nút '%s'",
                    content_name,
                    button.objectName(),
                )
                continue

            opened = button.isChecked()

            content.setVisible(opened)
            self.update_accordion_icon(button, opened)

            button.toggled.connect(
                lambda checked, btn=button, widget=content:
                self.toggle_accordion(btn, widget, checked)
            )

    def toggle_accordion(self, button: QToolButton, content: QWidget, opened: bool) -> None:
        content.setVisible(opened)
        self.update_accordion_icon(button, opened)

        layout = self.scrollAreaWidgetContents.layout()

        if layout is not None:
            layout.invalidate()
            layout.activate()

        self.scrollAreaWidgetContents.adjustSize()

    def update_accordion_icon(self, button: QToolButton, opened: bool) -> None:
        icon_name = (
            "fa5s.chevron-down"
            if opened
            else "fa5s.chevron-right"
        )

        icon_color = PRIMARY_COLOR if opened else MUTED_COLOR

        try:
            button.setIcon(
                qta.icon(
                    icon_name,
                    color=icon_color,
                )
            )
            button.setIconSize(ACCORDION_ICON_SIZE)
        except Exception as error:
            logger.error(
                "Không tải được icon '%s' cho mục hướng dẫn: %s",
                icon_name,
                error,
            )

    def setup_links(self) -> None:
        for button in self.findChildren(QAbstractButton):
            email = button.property("email")
            url = self.build_email_link(email) if email else button.property("url")

            if not url:
                continue

            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(
                lambda checked=False, target=url:
                self.open_link(target)
            )

    @staticmethod
    def build_email_link(email: str) -> str:
        return (
            "https://mail.google.com/mail/"
            f"?view=cm&fs=1&to={email}"
        )

    @staticmethod
    def open_link(url: str) -> None:
        QDesktopServices.openUrl(QUrl(url))

    def update_system_info(self) -> None:
        db_type = os.getenv("DB_TYPE", "mysql").strip().lower()

        if db_type == "mssql":
            db_name = os.getenv(
                "MSSQL_NAME",
                "supermarket_db",
            )

            server = (
                f"{os.getenv('MSSQL_SERVER', 'localhost')}:"
                f"{os.getenv('MSSQL_PORT', '1433')}"
            )

            database = f"SQL Server · {db_name}"

        else:
            db_name = os.getenv(
                "DB_NAME",
                "supermarket_db",
            )

            server = (
                f"{os.getenv('DB_HOST', 'localhost')}:"
                f"{os.getenv('DB_PORT', '3306')}"
            )

            database = f"MySQL · {db_name}"

        self.valueVersion.setText(VERSION)
        self.valueDatabase.setText(database)
        self.valueServer.setText(server)
        self.valueCurrentUser.setText(Session.get_username() or "—")

        role_name = Session.get_role_name() or ""
        role_display = ROLE_NAMES_VI.get(role_name.strip().lower(), role_name or "—")
        self.valueRole.setText(role_display)

    def showEvent(self, event) -> None:
        super().showEvent(event)
        self.update_system_info()

    def refresh_qss(self) -> None:
        self.setStyleSheet(self.styleSheet())

        for widget in self.findChildren(QWidget):
            if widget.property("class"):
                widget.style().unpolish(widget)
                widget.style().polish(widget)
