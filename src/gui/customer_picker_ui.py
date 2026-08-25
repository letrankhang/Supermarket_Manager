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
        Dialog.setStyleSheet(u"/* ===== To\u00e0n b\u1ed9 m\u00e0u s\u1eafc c\u1ee7a dialog n\u00e0y n\u1eb1m \u1edf \u0111\u00e2y =====\n"
"   S\u1eeda tr\u1ef1c ti\u1ebfp trong Qt Designer: ch\u1ecdn Dialog r\u1ed3i m\u1edf styleSheet.\n"
"   B\u1ea3ng m\u00e0u l\u1ea5y \u0111\u00fang theo m\u00e0n h\u00ecnh POS (pos.ui). */\n"
"\n"
"QDialog {\n"
"	background-color: #f8fafc;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	color: #0f172a;\n"
"}\n"
"\n"
"QLineEdit#txtSearchCustomer {\n"
"	background-color: #ffffff;\n"
"	border: 1px solid #cbd5e1;\n"
"	border-radius: 6px;\n"
"	padding: 8px 10px;\n"
"	font-size: 13px;\n"
"	color: #0f172a;\n"
"}\n"
"QLineEdit#txtSearchCustomer:focus {\n"
"	border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"QTableWidget#tblCustomers {\n"
"	background-color: #ffffff;\n"
"	border: 1px solid #e2e8f0;\n"
"	border-radius: 6px;\n"
"	gridline-color: #f1f5f9;\n"
"	color: #0f172a;\n"
"}\n"
"QTableWidget#tblCustomers::item {\n"
"	padding: 6px;\n"
"}\n"
"QTableWidget#tblCustomers::item:selected "
                        "{\n"
"	background-color: #dbeafe;\n"
"	color: #0f172a;\n"
"}\n"
"QTableWidget#tblCustomers QHeaderView::section {\n"
"	background-color: #f1f5f9;\n"
"	padding: 8px;\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	color: #475569;\n"
"}\n"
"\n"
"QLabel#lblStatus {\n"
"	font-size: 12px;\n"
"	color: #64748b;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 6px;\n"
"	padding: 8px 16px;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnSelect {\n"
"	background-color: #2563eb;\n"
"	color: #ffffff;\n"
"	border: none;\n"
"}\n"
"QPushButton#btnSelect:hover {\n"
"	background-color: #1d4ed8;\n"
"}\n"
"QPushButton#btnSelect:disabled {\n"
"	background-color: #cbd5e1;\n"
"	color: #f8fafc;\n"
"}\n"
"\n"
"QPushButton#btnClearCustomer {\n"
"	background-color: #ffffff;\n"
"	color: #b45309;\n"
"	border: 1px solid #fcd34d;\n"
"}\n"
"QPushButton#btnClearCustomer:hover {\n"
"	background-color: #fef3c7;\n"
"}\n"
"\n"
"QPushButton#btnCancel {\n"
"	background-color: #ffffff;\n"
"	color: #475569;\n"
"	border: 1"
                        "px solid #cbd5e1;\n"
"}\n"
"QPushButton#btnCancel:hover {\n"
"	background-color: #e2e8f0;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   Thanh cu\u1ed9n - gi\u1eef gi\u1ed1ng h\u1ec7t pos.ui cho \u0111\u1ed3ng b\u1ed9 to\u00e0n app\n"
"   Tay k\u00e9o bo tr\u00f2n #cbd5e1, hover #94a3b8, r\u1ed9ng 10px, b\u1ecf m\u0169i t\u00ean.\n"
"   N\u1ebfu \u0111\u1ed5i \u1edf \u0111\u00e2y th\u00ec nh\u1edb s\u1eeda c\u1ea3 pos.ui cho kh\u1edbp.\n"
"   ========================================================= */\n"
"\n"
"\n"
"/* ===== Vertical scrollbar ===== */\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #f8fafc;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #cbd5e1;\n"
"    min-height: 35px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #94a3b8;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: #"
                        "64748b;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"/* ===== Horizontal scrollbar ===== */\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #f8fafc;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #cbd5e1;\n"
"    min-width: 35px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #94a3b8;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: #64748b;\n"
"}\n"
"\n"
"QScrollBar::add-line:hor"
                        "izontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal,\n"
"QScrollBar::right-arrow:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.lblTitle = QLabel(Dialog)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout.addWidget(self.lblTitle)

        self.txtSearchCustomer = QLineEdit(Dialog)
        self.txtSearchCustomer.setObjectName(u"txtSearchCustomer")
        self.txtSearchCustomer.setMinimumSize(QSize(0, 38))
        self.txtSearchCustomer.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.txtSearchCustomer)

        self.tblCustomers = QTableWidget(Dialog)
        self.tblCustomers.setObjectName(u"tblCustomers")
        self.tblCustomers.setStyleSheet(u"QTableWidget::item {\n"
"    padding: 8px 12px;\n"
"    border-bottom: 1px solid #f1f5f9;\n"
"    color: #1e293b;\n"
"    outline: none; \n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f8fafc;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;         \n"
"    font-weight: 600;\n"
"}")
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
        self.btnClearCustomer.setMinimumSize(QSize(0, 38))
        self.btnClearCustomer.setStyleSheet(u"QPushButton {\n"
"    background-color: #f1f5f9;\n"
"    color: #475569;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e2e8f0;\n"
"    color: #1e293b;\n"
"    border-color: #94a3b8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #cbd5e1;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border-color: #e2e8f0;\n"
"}")

        self.horizontalLayout_buttons.addWidget(self.btnClearCustomer)

        self.horizontalSpacer_buttons = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer_buttons)

        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(90, 38))

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
        self.txtSearchCustomer.setPlaceholderText(QCoreApplication.translate("Dialog", u"T\u00ecm theo t\u00ean ho\u1eb7c s\u1ed1 \u0111i\u1ec7n tho\u1ea1i...", None))
        self.lblStatus.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearCustomer.setToolTip(QCoreApplication.translate("Dialog", u"G\u1ee1 kh\u00e1ch kh\u1ecfi h\u00f3a \u0111\u01a1n, quay l\u1ea1i Kh\u00e1ch l\u1ebb", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearCustomer.setText(QCoreApplication.translate("Dialog", u"B\u1ecf ch\u1ecdn (Kh\u00e1ch l\u1ebb)", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"H\u1ee7y", None))
        self.btnSelect.setText(QCoreApplication.translate("Dialog", u"Ch\u1ecdn kh\u00e1ch", None))
    # retranslateUi

