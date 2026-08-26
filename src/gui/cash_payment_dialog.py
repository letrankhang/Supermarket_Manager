# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cash_payment_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CashPaymentDialog(object):
    def setupUi(self, CashPaymentDialog):
        if not CashPaymentDialog.objectName():
            CashPaymentDialog.setObjectName(u"CashPaymentDialog")
        CashPaymentDialog.resize(420, 415)
        CashPaymentDialog.setStyleSheet(u"""QDialog#CashPaymentDialog {
    background-color: #ffffff;
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
    color: #dc2626;
    font-weight: bold;
}
QLabel[state="flat"] {
    color: #64748b;
    font-weight: bold;
}
QLabel[state="warning"] {
    color: #ea580c;
    font-weight: bold;
}
QLabel[state="safe"] {
    color: #10b981;
    font-weight: bold;
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

QLabel#lblSubTitle {
    color: #6b7280;
    font-size: 12px;
    font-weight: normal;
    margin-top: 4px;
}

QFrame#frameTotal {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
}

QLabel#lblTotalCaption,
QLabel#lblCashCaption {
    color: #64748b;
    font-size: 12px;
}

QLabel#lblTotalValue {
    color: #0f172a;
    font-size: 20px;
    font-weight: bold;
}

QPushButton#btnConfirm {
    background-color: #1d4ed8;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 0px 20px;
    min-height: 38px;
    font-size: 13px;
    font-weight: 700;
}
QPushButton#btnConfirm:hover {
    background-color: #1e3a8a;
}
QPushButton#btnConfirm:pressed {
    background-color: #1e40af;
}
QPushButton#btnConfirm:disabled {
    background-color: #cbd5e1;
    color: #f8fafc;
}

QLineEdit#txtCashReceived {
    font-size: 18px;
    font-weight: 700;
    min-height: 44px;
}
QFrame#frameChange {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 10px;
}
QLabel#lblChangeCaption {
    color: #15803d;
    font-size: 12px;
}
QLabel#lblChangeValue {
    color: #15803d;
    font-size: 20px;
    font-weight: 700;
}
QLabel#lblError {
    color: #dc2626;
    font-size: 12px;
    font-weight: 600;
}
QPushButton#btnQuick50,
QPushButton#btnQuick100,
QPushButton#btnQuick200,
QPushButton#btnQuick500,
QPushButton#btnExactAmount {
    padding: 0px 4px;
    min-height: 34px;
    font-size: 12px;
}
""")
        self.mainLayout = QVBoxLayout(CashPaymentDialog)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.mainLayout.setContentsMargins(19, 16, 20, 16)
        self.headerLayout = QVBoxLayout()
        self.headerLayout.setSpacing(0)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTitle = QLabel(CashPaymentDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(15)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.headerLayout.addWidget(self.lblTitle)

        self.lblSubTitle = QLabel(CashPaymentDialog)
        self.lblSubTitle.setObjectName(u"lblSubTitle")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(False)
        self.lblSubTitle.setFont(font1)

        self.headerLayout.addWidget(self.lblSubTitle)


        self.mainLayout.addLayout(self.headerLayout)

        self.frameTotal = QFrame(CashPaymentDialog)
        self.frameTotal.setObjectName(u"frameTotal")
        self.frameTotal.setFrameShape(QFrame.Shape.NoFrame)
        self.totalLayout = QHBoxLayout(self.frameTotal)
        self.totalLayout.setSpacing(10)
        self.totalLayout.setObjectName(u"totalLayout")
        self.totalLayout.setContentsMargins(14, 10, 14, 10)
        self.lblTotalCaption = QLabel(self.frameTotal)
        self.lblTotalCaption.setObjectName(u"lblTotalCaption")

        self.totalLayout.addWidget(self.lblTotalCaption)

        self.totalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.totalLayout.addItem(self.totalSpacer)

        self.lblTotalValue = QLabel(self.frameTotal)
        self.lblTotalValue.setObjectName(u"lblTotalValue")
        self.lblTotalValue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.totalLayout.addWidget(self.lblTotalValue)


        self.mainLayout.addWidget(self.frameTotal)

        self.lblCashCaption = QLabel(CashPaymentDialog)
        self.lblCashCaption.setObjectName(u"lblCashCaption")

        self.mainLayout.addWidget(self.lblCashCaption)

        self.txtCashReceived = QLineEdit(CashPaymentDialog)
        self.txtCashReceived.setObjectName(u"txtCashReceived")
        self.txtCashReceived.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.mainLayout.addWidget(self.txtCashReceived)

        self.quickAmountLayout = QHBoxLayout()
        self.quickAmountLayout.setSpacing(6)
        self.quickAmountLayout.setObjectName(u"quickAmountLayout")
        self.btnQuick50 = QPushButton(CashPaymentDialog)
        self.btnQuick50.setObjectName(u"btnQuick50")
        self.btnQuick50.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickAmountLayout.addWidget(self.btnQuick50)

        self.btnQuick100 = QPushButton(CashPaymentDialog)
        self.btnQuick100.setObjectName(u"btnQuick100")
        self.btnQuick100.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickAmountLayout.addWidget(self.btnQuick100)

        self.btnQuick200 = QPushButton(CashPaymentDialog)
        self.btnQuick200.setObjectName(u"btnQuick200")
        self.btnQuick200.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickAmountLayout.addWidget(self.btnQuick200)

        self.btnQuick500 = QPushButton(CashPaymentDialog)
        self.btnQuick500.setObjectName(u"btnQuick500")
        self.btnQuick500.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickAmountLayout.addWidget(self.btnQuick500)

        self.btnExactAmount = QPushButton(CashPaymentDialog)
        self.btnExactAmount.setObjectName(u"btnExactAmount")
        self.btnExactAmount.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.quickAmountLayout.addWidget(self.btnExactAmount)


        self.mainLayout.addLayout(self.quickAmountLayout)

        self.frameChange = QFrame(CashPaymentDialog)
        self.frameChange.setObjectName(u"frameChange")
        self.frameChange.setFrameShape(QFrame.Shape.NoFrame)
        self.changeLayout = QHBoxLayout(self.frameChange)
        self.changeLayout.setSpacing(10)
        self.changeLayout.setObjectName(u"changeLayout")
        self.changeLayout.setContentsMargins(14, 10, 14, 10)
        self.lblChangeCaption = QLabel(self.frameChange)
        self.lblChangeCaption.setObjectName(u"lblChangeCaption")

        self.changeLayout.addWidget(self.lblChangeCaption)

        self.changeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.changeLayout.addItem(self.changeSpacer)

        self.lblChangeValue = QLabel(self.frameChange)
        self.lblChangeValue.setObjectName(u"lblChangeValue")
        self.lblChangeValue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.changeLayout.addWidget(self.lblChangeValue)


        self.mainLayout.addWidget(self.frameChange)

        self.lblError = QLabel(CashPaymentDialog)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setWordWrap(True)

        self.mainLayout.addWidget(self.lblError)

        self.actionLayout = QHBoxLayout()
        self.actionLayout.setSpacing(10)
        self.actionLayout.setObjectName(u"actionLayout")
        self.actionSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionLayout.addItem(self.actionSpacer)

        self.btnCancel = QPushButton(CashPaymentDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionLayout.addWidget(self.btnCancel)

        self.btnConfirm = QPushButton(CashPaymentDialog)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.actionLayout.addWidget(self.btnConfirm)


        self.mainLayout.addLayout(self.actionLayout)


        self.retranslateUi(CashPaymentDialog)

        QMetaObject.connectSlotsByName(CashPaymentDialog)
    # setupUi

    def retranslateUi(self, CashPaymentDialog):
        CashPaymentDialog.setWindowTitle(QCoreApplication.translate("CashPaymentDialog", u"Thanh to\u00e1n ti\u1ec1n m\u1eb7t", None))
        self.lblTitle.setText(QCoreApplication.translate("CashPaymentDialog", u"Thanh to\u00e1n ti\u1ec1n m\u1eb7t", None))
        self.lblSubTitle.setText(QCoreApplication.translate("CashPaymentDialog", u"Nh\u1eadp s\u1ed1 ti\u1ec1n kh\u00e1ch \u0111\u01b0a \u0111\u1ec3 t\u00ednh ti\u1ec1n th\u1ed1i l\u1ea1i", None))
        self.lblTotalCaption.setText(QCoreApplication.translate("CashPaymentDialog", u"T\u1ed5ng thanh to\u00e1n", None))
        self.lblTotalValue.setText(QCoreApplication.translate("CashPaymentDialog", u"0 \u0111", None))
        self.lblCashCaption.setText(QCoreApplication.translate("CashPaymentDialog", u"Ti\u1ec1n kh\u00e1ch \u0111\u01b0a:", None))
        self.txtCashReceived.setPlaceholderText(QCoreApplication.translate("CashPaymentDialog", u"0", None))
        self.btnQuick50.setText(QCoreApplication.translate("CashPaymentDialog", u"50.000", None))
        self.btnQuick50.setProperty(u"class", QCoreApplication.translate("CashPaymentDialog", u"quickAmount", None))
        self.btnQuick100.setText(QCoreApplication.translate("CashPaymentDialog", u"100.000", None))
        self.btnQuick100.setProperty(u"class", QCoreApplication.translate("CashPaymentDialog", u"quickAmount", None))
        self.btnQuick200.setText(QCoreApplication.translate("CashPaymentDialog", u"200.000", None))
        self.btnQuick200.setProperty(u"class", QCoreApplication.translate("CashPaymentDialog", u"quickAmount", None))
        self.btnQuick500.setText(QCoreApplication.translate("CashPaymentDialog", u"500.000", None))
        self.btnQuick500.setProperty(u"class", QCoreApplication.translate("CashPaymentDialog", u"quickAmount", None))
        self.btnExactAmount.setText(QCoreApplication.translate("CashPaymentDialog", u"V\u1eeba \u0111\u1ee7", None))
        self.btnExactAmount.setProperty(u"class", QCoreApplication.translate("CashPaymentDialog", u"quickAmount", None))
        self.lblChangeCaption.setText(QCoreApplication.translate("CashPaymentDialog", u"Ti\u1ec1n th\u1ed1i l\u1ea1i", None))
        self.lblChangeValue.setText(QCoreApplication.translate("CashPaymentDialog", u"0 \u0111", None))
        self.lblError.setText("")
        self.btnCancel.setText(QCoreApplication.translate("CashPaymentDialog", u"H\u1ee7y", None))
        self.btnConfirm.setText(QCoreApplication.translate("CashPaymentDialog", u"X\u00e1c nh\u1eadn thanh to\u00e1n", None))
    # retranslateUi

