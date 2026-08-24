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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CashPaymentDialog(object):
    def setupUi(self, CashPaymentDialog):
        if not CashPaymentDialog.objectName():
            CashPaymentDialog.setObjectName(u"CashPaymentDialog")
        CashPaymentDialog.resize(420, 439)
        CashPaymentDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #ffffff;\n"
"}\n"
"QLabel#lblTitle {\n"
"    color: #0f172a;\n"
"    font-size: 16px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#lblSubTitle {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"QFrame#frameTotal {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#lblTotalCaption {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"QLabel#lblTotalValue {\n"
"    color: #0f172a;\n"
"    font-size: 20px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#lblCashCaption {\n"
"    color: #334155;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"QLineEdit#txtCashReceived {\n"
"    background-color: #ffffff;\n"
"    color: #0f172a;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 8px;\n"
"    padding: 10px 12px;\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"    selection-background-color: #2563eb;\n"
"    selection-color: #ffffff;\n"
"}\n"
"QLineEdit#txtCashReceived:hover {\n"
" "
                        "   border: 1px solid #94a3b8;\n"
"}\n"
"QLineEdit#txtCashReceived:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"QPushButton[class=\"quickAmount\"] {\n"
"    background-color: #f8fafc;\n"
"    color: #334155;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 8px;\n"
"    padding: 6px 4px;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton[class=\"quickAmount\"]:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #93c5fd;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton[class=\"quickAmount\"]:pressed {\n"
"    background-color: #dbeafe;\n"
"}\n"
"QFrame#frameChange {\n"
"    background-color: #f0fdf4;\n"
"    border: 1px solid #bbf7d0;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#lblChangeCaption {\n"
"    color: #15803d;\n"
"    font-size: 12px;\n"
"}\n"
"QLabel#lblChangeValue {\n"
"    color: #15803d;\n"
"    font-size: 20px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#lblError {\n"
"    color: #dc2626;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
""
                        "QPushButton#btnConfirm {\n"
"    background-color: #2563eb;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 9px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton#btnConfirm:hover {\n"
"    background-color: #1d4ed8;\n"
"}\n"
"QPushButton#btnConfirm:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnConfirm:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #94a3b8;\n"
"}\n"
"QPushButton#btnCancel {\n"
"    background-color: #f8fafc;\n"
"    color: #475569;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 8px;\n"
"    padding: 9px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #f1f5f9;\n"
"    border: 1px solid #94a3b8;\n"
"    color: #334155;\n"
"}\n"
"QPushButton#btnCancel:pressed {\n"
"    background-color: #e2e8f0;\n"
"}")
        self.mainLayout = QVBoxLayout(CashPaymentDialog)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.headerLayout = QVBoxLayout()
        self.headerLayout.setSpacing(2)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTitle = QLabel(CashPaymentDialog)
        self.lblTitle.setObjectName(u"lblTitle")

        self.headerLayout.addWidget(self.lblTitle)

        self.lblSubTitle = QLabel(CashPaymentDialog)
        self.lblSubTitle.setObjectName(u"lblSubTitle")

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

        self.bottomSpacer = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)

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

