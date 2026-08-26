# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_picker.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(520, 460)
        Dialog.setStyleSheet(u"""QDialog#Dialog {
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
    padding: 0px 12px;
    min-height: 38px;
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

QLabel#lblTitle {
    color: #0f172a;
    font-weight: bold;
}

QLabel#lblStatus {
    color: #64748b;
    font-size: 12px;
}

QTableWidget#tblCustomers {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
}

QPushButton#btnSelect {
    background-color: #1d4ed8;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 0px 20px;
    min-height: 38px;
    font-size: 13px;
    font-weight: 700;
}
QPushButton#btnSelect:hover {
    background-color: #1e3a8a;
}
QPushButton#btnSelect:pressed {
    background-color: #1e40af;
}
QPushButton#btnSelect:disabled {
    background-color: #cbd5e1;
    color: #f8fafc;
}

QPushButton#btnClearCustomer {
    background-color: #ffffff;
    color: #dc2626;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0px 16px;
    min-height: 38px;
    font-size: 12px;
    font-weight: bold;
}
QPushButton#btnClearCustomer:hover {
    background-color: #fef2f2;
    border: 1px solid #dc2626;
}
QPushButton#btnClearCustomer:disabled {
    background-color: #f8fafc;
    color: #cbd5e1;
    border: 1px solid #e2e8f0;
}
""")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 16, 18, 16)
        self.lblTitle = QLabel(Dialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(15)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.txtSearchCustomer = QLineEdit(Dialog)
        self.txtSearchCustomer.setObjectName(u"txtSearchCustomer")
        self.txtSearchCustomer.setMinimumSize(QSize(0, 40))
        self.txtSearchCustomer.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.txtSearchCustomer)

        self.tblCustomers = QTableWidget(Dialog)
        self.tblCustomers.setObjectName(u"tblCustomers")
        self.tblCustomers.setAlternatingRowColors(False)
        self.tblCustomers.setShowGrid(False)

        self.verticalLayout.addWidget(self.tblCustomers)

        self.lblStatus = QLabel(Dialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setSpacing(10)
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.btnClearCustomer = QPushButton(Dialog)
        self.btnClearCustomer.setObjectName(u"btnClearCustomer")
        self.btnClearCustomer.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_buttons.addWidget(self.btnClearCustomer)

        self.horizontalSpacer_buttons = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer_buttons)

        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(90, 40))

        self.horizontalLayout_buttons.addWidget(self.btnCancel)

        self.btnSelect = QPushButton(Dialog)
        self.btnSelect.setObjectName(u"btnSelect")
        self.btnSelect.setMinimumSize(QSize(110, 38))

        self.horizontalLayout_buttons.addWidget(self.btnSelect)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ch\u1ecdn kh\u00e1ch h\u00e0ng", None))
        self.lblTitle.setText(QCoreApplication.translate("Dialog", u"Ch\u1ecdn kh\u00e1ch h\u00e0ng cho h\u00f3a \u0111\u01a1n", None))
        self.txtSearchCustomer.setPlaceholderText(QCoreApplication.translate("Dialog", u"T\u00ecm theo t\u00ean ho\u1eb7c s\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.lblStatus.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearCustomer.setToolTip(QCoreApplication.translate("Dialog", u"G\u1ee1 kh\u00e1ch kh\u1ecfi h\u00f3a \u0111\u01a1n, quay l\u1ea1i Kh\u00e1ch l\u1ebb", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearCustomer.setText(QCoreApplication.translate("Dialog", u"B\u1ecf ch\u1ecdn (Kh\u00e1ch l\u1ebb)", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"H\u1ee7y", None))
        self.btnSelect.setText(QCoreApplication.translate("Dialog", u"Ch\u1ecdn kh\u00e1ch", None))
    # retranslateUi

