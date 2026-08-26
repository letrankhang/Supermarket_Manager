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
        CashPaymentDialog.setStyleSheet(u"QDialog#CashPaymentDialog {\n"
"    background-color: #ffffff;\n"
"    color: #0f172a;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QWidget {\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QLineEdit,\n"
"QComboBox,\n"
"QDateEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 12px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"    selection-background-color: #1d4ed8;\n"
"    selection-color: #ffffff;\n"
"}\n"
"QTextEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"    selection-background-color: #1d4ed8;\n"
"    selection-color: #ffffff;\n"
"}\n"
"QLineEdit:hover,\n"
"QComboBox:hover,\n"
"QDateEdit"
                        ":hover,\n"
"QSpinBox:hover,\n"
"QDoubleSpinBox:hover,\n"
"QTextEdit:hover {\n"
"    border: 1px solid #cbd5e1;\n"
"}\n"
"QLineEdit:focus,\n"
"QComboBox:focus,\n"
"QDateEdit:focus,\n"
"QSpinBox:focus,\n"
"QDoubleSpinBox:focus,\n"
"QTextEdit:focus {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QLineEdit:disabled,\n"
"QComboBox:disabled,\n"
"QDateEdit:disabled,\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #94a3b8;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 26px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(assets/images/chevron-down.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"    image: url(assets/images/chevron-up.png);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
""
                        "    padding: 4px;\n"
"    outline: none;\n"
"    selection-background-color: #eff6ff;\n"
"    selection-color: #1d4ed8;\n"
"}\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button,\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button {\n"
"    subcontrol-origin: border;\n"
"    width: 20px;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDateEdit::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button,\n"
"QDateEdit::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover,\n"
"QDoubleSpinBox::down-button:hover,\n"
"QDateEdit::up-button:hover,\n"
"QDateEdit::down-button:hover {\n"
"    background-color: #f1f5f9;\n"
"}\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QDateEdit::up-arrow {\n"
"    im"
                        "age: url(assets/images/chevron-up.png);\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QDateEdit::down-arrow {\n"
"    image: url(assets/images/chevron-down.png);\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"QCheckBox {\n"
"    background-color: transparent;\n"
"    color: #334155;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    spacing: 8px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 4px;\n"
"    background-color: #ffffff;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font"
                        "-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #dbeafe;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"QPushButton#RowActionButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0px;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"    min-height: 28px;\n"
"    max-height: 28px;\n"
"}\n"
"QPushButton#RowActionButton:hover {\n"
"    background-color: #eff6ff;\n"
"}\n"
"QPushButton#RowActionButton:pressed {\n"
"    background-color: #dbeafe;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: #f1f5f9;\n"
"    font-size: 13px;\n"
"    color: #334155;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px"
                        " solid #f1f5f9;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"QHeaderView {\n"
"    background-color: #f8fafc;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc;\n"
"    color: #64748b;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"    padding: 10px 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #f8fafc;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel[badge=\"info\"] {\n"
"    background-color: #dbeafe;\n"
"    color: #1d4ed8;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"success\"] {\n"
"    background-color: #d1fae5;\n"
"    color: #059669;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"warning\"] {\n"
"    ba"
                        "ckground-color: #ffedd5;\n"
"    color: #ea580c;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"danger\"] {\n"
"    background-color: #fee2e2;\n"
"    color: #dc2626;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"neutral\"] {\n"
"    background-color: #e2e8f0;\n"
"    color: #64748b;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"violet\"] {\n"
"    background-color: #ede9fe;\n"
"    color: #6d28d9;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[trend=\"up\"] {\n"
"    background-color: #ecfdf5;\n"
"    color: #059669;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[trend=\"down\"] {\n"
"    background-color: #fef2"
                        "f2;\n"
"    color: #dc2626;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[trend=\"flat\"] {\n"
"    background-color: #f1f5f9;\n"
"    color: #64748b;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[state=\"up\"] {\n"
"    color: #10b981;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"down\"] {\n"
"    color: #ef4444;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"flat\"] {\n"
"    color: #64748b;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"warning\"] {\n"
"    color: #eab308;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"safe\"] {\n"
"    color: #10b981;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollArea > QWidget > QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"QAbstractScrollArea::viewport {\n"
"    background-color: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
""
                        "    background-color: transparent;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #cbd5e1;\n"
"    min-height: 35px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #94a3b8;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: #64748b;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: transparent;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:horizont"
                        "al {\n"
"    background-color: #cbd5e1;\n"
"    min-width: 35px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #94a3b8;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: #64748b;\n"
"}\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::left-arrow:horizontal,\n"
"QScrollBar::right-arrow:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    color: #334155;\n"
"    border-radius: 6px;\n"
"    padding: 7px 18px;\n"
"  "
                        "  font-size: 13px;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #e2e8f0;\n"
"    margin: 6px 4px;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"    color: #0f172a;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#lblSubTitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QFrame#frameTotal {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#lblTotalCaption,\n"
"QLabel#lblCashCaption {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLabel#lblTotalValue {\n"
"    color: #0f172a;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnConfirm {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-si"
                        "ze: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnConfirm:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnConfirm:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnConfirm:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"\n"
"QLineEdit#txtCashReceived {\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"    min-height: 44px;\n"
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
"QPushButton#btnQuick50,\n"
"QPushButton#btnQuick100,\n"
"QPushButton#btnQuick200,\n"
"QPushButton#btnQuick500,\n"
"QPushButton#btnExactAmount {\n"
"    padding: 0px 4px;\n"
" "
                        "   min-height: 34px;\n"
"    font-size: 12px;\n"
"}\n"
"")
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

