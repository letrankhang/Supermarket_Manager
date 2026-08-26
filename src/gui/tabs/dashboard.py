# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1536, 924)
        Form.setStyleSheet(u"""QWidget#Form {
    background-color: #f1f5f9;
    color: #0f172a;
    font-family: "Segoe UI", Arial, sans-serif;
}
QWidget {
    font-family: "Segoe UI", Arial, sans-serif;
}
QLabel {
    background-color: transparent;
    border: none;
    color: #0f172a;
}

QLineEdit,
QComboBox,
QDateEdit,
QSpinBox,
QDoubleSpinBox {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0px 9px;
    min-height: 30px;
    font-size: 13px;
    color: #0f172a;
    selection-background-color: #1d4ed8;
    selection-color: #ffffff;
}
QTextEdit {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 8px 10px;
    font-size: 13px;
    color: #0f172a;
    selection-background-color: #1d4ed8;
    selection-color: #ffffff;
}
QLineEdit:hover,
QComboBox:hover,
QDateEdit:hover,
QSpinBox:hover,
QDoubleSpinBox:hover,
QTextEdit:hover {
    border: 1px solid #cbd5e1;
}
QLineEdit:focus,
QComboBox:focus,
QDateEdit:focus,
QSpinBox:focus,
QDoubleSpinBox:focus,
QTextEdit:focus {
    border: 1px solid #1d4ed8;
}
QLineEdit:disabled,
QComboBox:disabled,
QDateEdit:disabled,
QSpinBox:disabled,
QDoubleSpinBox:disabled {
    background-color: #f8fafc;
    color: #94a3b8;
}

QComboBox {
    background-color: #f1f5f9;
    color: #334155;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding-left: 17px;
    padding-right: 3px;  
    font-weight: 600;
}
QComboBox:hover {
    background-color: #e2e8f0;
    border-color: #94a3b8;
    color: #0f172a;
}
QComboBox:on {
    background-color: #ffffff;
    border-color: #1d4ed8;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: center right;
    border: none;
    background-color: transparent;
    width: 26px;
}
QComboBox::down-arrow {
    image: url(assets/images/chevron-down.png);
    width: 10px;
    height: 10px;
}
QComboBox::down-arrow:on {
    image: url(assets/images/chevron-up.png);
}
QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 4px;
    outline: none;
    selection-background-color: #eff6ff;
    selection-color: #1d4ed8;
}
QComboBox QAbstractItemView::item {
    color: #0f172a;
    min-height: 30px;
    padding: 4px 10px;
    border-radius: 6px;
}
QComboBox QAbstractItemView::item:hover {
    background-color: #eff6ff;
    color: #1d4ed8;
}
QComboBox QAbstractItemView::item:selected {
    background-color: #eff6ff;
    color: #1d4ed8;
}

QSpinBox::up-button,
QSpinBox::down-button,
QDoubleSpinBox::up-button,
QDoubleSpinBox::down-button,
QDateEdit::up-button,
QDateEdit::down-button {
    subcontrol-origin: border;
    width: 20px;
    border: none;
    background-color: transparent;
}
QSpinBox::up-button,
QDoubleSpinBox::up-button,
QDateEdit::up-button {
    subcontrol-position: top right;
}
QSpinBox::down-button,
QDoubleSpinBox::down-button,
QDateEdit::down-button {
    subcontrol-position: bottom right;
}
QSpinBox::up-button:hover,
QSpinBox::down-button:hover,
QDoubleSpinBox::up-button:hover,
QDoubleSpinBox::down-button:hover,
QDateEdit::up-button:hover,
QDateEdit::down-button:hover {
    background-color: #f1f5f9;
}
QSpinBox::up-arrow,
QDoubleSpinBox::up-arrow,
QDateEdit::up-arrow {
    image: url(assets/images/chevron-up.png);
    width: 9px;
    height: 9px;
}
QSpinBox::down-arrow,
QDoubleSpinBox::down-arrow,
QDateEdit::down-arrow {
    image: url(assets/images/chevron-down.png);
    width: 9px;
    height: 9px;
}
QCheckBox {
    background-color: transparent;
    color: #334155;
    font-size: 13px;
    font-weight: bold;
    spacing: 8px;
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    background-color: #ffffff;
}
QCheckBox::indicator:hover {
    border: 1px solid #1d4ed8;
}
QCheckBox::indicator:checked {
    background-color: #1d4ed8;
    border: 1px solid #1d4ed8;
}

QPushButton {
    background-color: #ffffff;
    color: #64748b;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0px 16px;
    min-height: 38px;
    font-size: 12px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #1d4ed8;
}
QPushButton:pressed {
    background-color: #dbeafe;
}
QPushButton:disabled {
    background-color: #f8fafc;
    color: #cbd5e1;
    border: 1px solid #e2e8f0;
}
QPushButton#RowActionButton {
    background-color: transparent;
    border: none;
    border-radius: 6px;
    padding: 0px;
    min-width: 28px;
    max-width: 28px;
    min-height: 28px;
    max-height: 28px;
}
QPushButton#RowActionButton:hover {
    background-color: #eff6ff;
}
QPushButton#RowActionButton:pressed {
    background-color: #dbeafe;
}

QTableWidget {
    background-color: transparent;
    border: none;
    gridline-color: #f1f5f9;
    font-size: 13px;
    color: #334155;
    outline: none;
}
QTableWidget::item {
    padding: 8px;
    border-bottom: 1px solid #f1f5f9;
}
QTableWidget::item:selected {
    background-color: #eff6ff;
    color: #1d4ed8;
}
QHeaderView {
    background-color: #f8fafc;
    border: none;
    border-bottom: 1px solid #e2e8f0;
}
QHeaderView::section {
    background-color: #f8fafc;
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    padding: 10px 8px;
    border: none;
    border-bottom: 1px solid #e2e8f0;
}
QTableCornerButton::section {
    background-color: #f8fafc;
    border: none;
}

QLabel[badge="info"] {
    background-color: #dbeafe;
    color: #1d4ed8;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[badge="success"] {
    background-color: #d1fae5;
    color: #059669;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[badge="warning"] {
    background-color: #ffedd5;
    color: #ea580c;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[badge="danger"] {
    background-color: #fee2e2;
    color: #dc2626;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[badge="neutral"] {
    background-color: #e2e8f0;
    color: #64748b;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[badge="violet"] {
    background-color: #ede9fe;
    color: #6d28d9;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[trend="up"] {
    background-color: #ecfdf5;
    color: #059669;
    border-radius: 4px;
    padding: 2px 6px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[trend="down"] {
    background-color: #fef2f2;
    color: #dc2626;
    border-radius: 4px;
    padding: 2px 6px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[trend="flat"] {
    background-color: #f1f5f9;
    color: #64748b;
    border-radius: 4px;
    padding: 2px 6px;
    font-size: 11px;
    font-weight: 700;
}
QLabel[state="up"] {
    color: #10b981;
    font-weight: bold;
}
QLabel[state="down"] {
    color: #ef4444;
    font-weight: bold;
}
QLabel[state="flat"] {
    color: #64748b;
    font-weight: bold;
}
QLabel[state="warning"] {
    color: #eab308;
    font-weight: bold;
}
QLabel[state="safe"] {
    color: #10b981;
}

QScrollArea {
    background-color: transparent;
    border: none;
}
QScrollArea > QWidget > QWidget {
    background-color: transparent;
}
QAbstractScrollArea::viewport {
    background-color: transparent;
}
QScrollBar:vertical {
    background-color: transparent;
    width: 10px;
    margin: 0px;
    border: none;
}
QScrollBar::handle:vertical {
    background-color: #cbd5e1;
    min-height: 35px;
    border-radius: 5px;
}
QScrollBar::handle:vertical:hover {
    background-color: #94a3b8;
}
QScrollBar::handle:vertical:pressed {
    background-color: #64748b;
}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
    width: 0px;
    background: transparent;
    border: none;
}
QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    width: 0px;
    height: 0px;
    background: transparent;
    border: none;
}
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: transparent;
}
QScrollBar:horizontal {
    background-color: transparent;
    height: 10px;
    margin: 0px;
    border: none;
}
QScrollBar::handle:horizontal {
    background-color: #cbd5e1;
    min-width: 35px;
    border-radius: 5px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #94a3b8;
}
QScrollBar::handle:horizontal:pressed {
    background-color: #64748b;
}
QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
    height: 0px;
    background: transparent;
    border: none;
}
QScrollBar::left-arrow:horizontal,
QScrollBar::right-arrow:horizontal {
    width: 0px;
    height: 0px;
    background: transparent;
    border: none;
}
QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {
    background: transparent;
}

QMenu {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 6px;
}
QMenu::item {
    background-color: transparent;
    color: #334155;
    border-radius: 6px;
    padding: 7px 18px;
    font-size: 13px;
}
QMenu::item:selected {
    background-color: #eff6ff;
    color: #1d4ed8;
}
QMenu::separator {
    height: 1px;
    background-color: #e2e8f0;
    margin: 6px 4px;
}

QFrame#frame,
QFrame#frame_2,
QFrame#frame_3,
QFrame#frame_4,
QFrame#frame_5,
QFrame#frame_10,
QFrame#frame_12,
QFrame#frame_13,
QFrame#frame_18 {
    background-color: transparent;
    border: none;
}

QFrame#frame_14,
QFrame#frame_15,
QFrame#frame_16,
QFrame#frame_17 {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 3px 8px;
}

QFrame#frame_6,
QFrame#frame_chart,
QFrame#frame_table {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
}

QFrame#frame_7,
QFrame#frame_8,
QFrame#frame_9,
QFrame#frame_11 {
    background-color: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
}
QFrame#frame_7:hover,
QFrame#frame_8:hover,
QFrame#frame_9:hover,
QFrame#frame_11:hover {
    background-color: #e2e8f0;
    border: 1px solid #cbd5e1;
}

QLabel#lblDashboardTitle {
    color: #0f172a;
    padding: 0px;
    margin: 0px;
}

QLabel#lblDashboardSubtitle {
    color: #6b7280;
    font-size: 12px;
    font-weight: normal;
    margin-top: 4px;
}

QLabel#lblTableTitle {
    color: #0f172a;
    font-size: 14px;
    font-weight: bold;
}

QPushButton#btnRefresh {
    background-color: #1d4ed8;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 0px 20px;
    min-height: 38px;
    font-size: 13px;
    font-weight: 700;
}
QPushButton#btnRefresh:hover {
    background-color: #1e3a8a;
}
QPushButton#btnRefresh:pressed {
    background-color: #1e40af;
}
QPushButton#btnRefresh:disabled {
    background-color: #cbd5e1;
    color: #f8fafc;
}

QLabel#badgeRevenue {
    background-color: #dbeafe;
    border-radius: 8px;
}
QLabel#badgeInvoice {
    background-color: #ede9fe;
    border-radius: 8px;
}
QLabel#badgeStock {
    background-color: #fef3c7;
    border-radius: 8px;
}
QLabel#badgeCustomer {
    background-color: #d1fae5;
    border-radius: 8px;
}

QLabel#lblQuickActionCaption {
    font-size: 12px;
    font-weight: bold;
    color: #334155;
}""")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 64))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_10)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 2, 0, 12)
        self.lblDashboardTitle = QLabel(self.frame_10)
        self.lblDashboardTitle.setObjectName(u"lblDashboardTitle")
        self.lblDashboardTitle.setMinimumSize(QSize(90, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.lblDashboardTitle.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblDashboardTitle)

        self.lblDashboardSubtitle = QLabel(self.frame_10)
        self.lblDashboardSubtitle.setObjectName(u"lblDashboardSubtitle")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDashboardSubtitle)

        self.lblDashboardSubtitle.raise_()
        self.lblDashboardTitle.raise_()

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnRefresh = QPushButton(self.frame)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(140, 38))
        self.btnRefresh.setMaximumSize(QSize(140, 40))
        self.btnRefresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnRefresh)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(4)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(7)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(14, 12, 14, 14)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_8, 2, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy5.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy5)
        self.frame_9.setMinimumSize(QSize(150, 0))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_9, 2, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.gridLayout_2.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy5.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy5)
        self.frame_11.setMinimumSize(QSize(150, 0))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(3)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_13)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy5.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy5)
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_17)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(20)
        self.label_14.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_14)

        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)


        self.gridLayout_4.addWidget(self.frame_17, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy5.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy5)
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)


        self.gridLayout_4.addWidget(self.frame_16, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy5.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy5)
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(20)
        font4.setBold(False)
        self.label_11.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_11)

        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)


        self.gridLayout_4.addWidget(self.frame_15, 1, 1, 1, 1)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy5.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy5)
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_5.raise_()
        self.label_12.raise_()
        self.label_4.raise_()

        self.gridLayout_4.addWidget(self.frame_14, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_13)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(5)
        sizePolicy7.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy7)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_bottom = QHBoxLayout(self.frame_2)
        self.horizontalLayout_bottom.setSpacing(12)
        self.horizontalLayout_bottom.setObjectName(u"horizontalLayout_bottom")
        self.horizontalLayout_bottom.setContentsMargins(0, 0, 0, 0)
        self.frame_chart = QFrame(self.frame_2)
        self.frame_chart.setObjectName(u"frame_chart")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(6)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_chart.sizePolicy().hasHeightForWidth())
        self.frame_chart.setSizePolicy(sizePolicy8)
        self.frame_chart.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_8 = QVBoxLayout(self.frame_chart)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.frame_18 = QFrame(self.frame_chart)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 32))
        self.frame_18.setMaximumSize(QSize(16777215, 32))
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.frame_18)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.chart_container = QWidget(self.frame_chart)
        self.chart_container.setObjectName(u"chart_container")

        self.verticalLayout_8.addWidget(self.chart_container)


        self.horizontalLayout_bottom.addWidget(self.frame_chart)

        self.frame_table = QFrame(self.frame_2)
        self.frame_table.setObjectName(u"frame_table")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(4)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_table.sizePolicy().hasHeightForWidth())
        self.frame_table.setSizePolicy(sizePolicy9)
        self.frame_table.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_bottom.addWidget(self.frame_table)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblDashboardTitle.setText(QCoreApplication.translate("Form", u"T\u1ed5ng quan h\u1ec7 th\u1ed1ng", None))
        self.lblDashboardSubtitle.setText(QCoreApplication.translate("Form", u"Theo d\u00f5i doanh thu, h\u00f3a \u0111\u01a1n v\u00e0 ho\u1ea1t \u0111\u1ed9ng kinh doanh trong ng\u00e0y", None))
        self.btnRefresh.setText(QCoreApplication.translate("Form", u"T\u1ea3i l\u1ea1i d\u1eef li\u1ec7u", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Thao t\u00e1c nhanh", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"T\u1ed5ng h\u00f3a \u0111\u01a1n", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"S\u1ed1 h\u00f3a \u0111\u01a1n", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"t\u1ec9 l\u1ec7 t\u0103ng tr\u01b0\u1edfng", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"S\u1eafp h\u1ebft h\u00e0ng", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"s\u1ed1 h\u00e0ng s\u1eafp h\u1ebft", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"C\u1ea7n c\u1eadp nh\u1eadt ngay", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Kh\u00e1ch h\u00e0ng m\u1edbi", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"S\u1ed1 kh\u00e1ch h\u00e0ng m\u1edbi", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"t\u1ec9 l\u1ec7 t\u0103ng tr\u01b0\u1edfng", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Doanh thu h\u00f4m nay", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"s\u1ed1 ti\u1ec1n h\u00f4m nay", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"t\u1ec9 l\u1ec7 t\u0103ng tr\u01b0\u1edfng", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Doanh thu th\u00e1ng n\u00e0y", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Th\u00e1ng 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Th\u00e1ng 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Th\u00e1ng 3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Th\u00e1ng 4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"Th\u00e1ng 5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"Th\u00e1ng 6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"Th\u00e1ng 7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"Th\u00e1ng 8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"Th\u00e1ng 9", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"Th\u00e1ng 10", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"Th\u00e1ng 11", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Form", u"Th\u00e1ng 12", None))

    # retranslateUi

