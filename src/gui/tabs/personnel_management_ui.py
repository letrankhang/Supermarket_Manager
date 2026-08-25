# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'personnel_management.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_PersonnelManagement(object):
    def setupUi(self, PersonnelManagement):
        if not PersonnelManagement.objectName():
            PersonnelManagement.setObjectName(u"PersonnelManagement")
        PersonnelManagement.resize(1000, 700)
        self.verticalLayout = QVBoxLayout(PersonnelManagement)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.lblTitle = QLabel(PersonnelManagement)
        self.lblTitle.setObjectName(u"lblTitle")

        self.titleLayout.addWidget(self.lblTitle)

        self.lblSub = QLabel(PersonnelManagement)
        self.lblSub.setObjectName(u"lblSub")

        self.titleLayout.addWidget(self.lblSub)


        self.verticalLayout.addLayout(self.titleLayout)

        self.statsLayout = QHBoxLayout()
        self.statsLayout.setSpacing(15)
        self.statsLayout.setObjectName(u"statsLayout")
        self.cardTotal = QFrame(PersonnelManagement)
        self.cardTotal.setObjectName(u"cardTotal")
        self.cardTotal.setFrameShape(QFrame.StyledPanel)
        self.cardTotal.setFrameShadow(QFrame.Raised)
        self.layoutTotal = QVBoxLayout(self.cardTotal)
        self.layoutTotal.setObjectName(u"layoutTotal")
        self.lblTotalTitle = QLabel(self.cardTotal)
        self.lblTotalTitle.setObjectName(u"lblTotalTitle")

        self.layoutTotal.addWidget(self.lblTotalTitle)

        self.lblTotal = QLabel(self.cardTotal)
        self.lblTotal.setObjectName(u"lblTotal")

        self.layoutTotal.addWidget(self.lblTotal)


        self.statsLayout.addWidget(self.cardTotal)

        self.cardActive = QFrame(PersonnelManagement)
        self.cardActive.setObjectName(u"cardActive")
        self.cardActive.setFrameShape(QFrame.StyledPanel)
        self.cardActive.setFrameShadow(QFrame.Raised)
        self.layoutActive = QVBoxLayout(self.cardActive)
        self.layoutActive.setObjectName(u"layoutActive")
        self.lblActiveTitle = QLabel(self.cardActive)
        self.lblActiveTitle.setObjectName(u"lblActiveTitle")

        self.layoutActive.addWidget(self.lblActiveTitle)

        self.lblActive = QLabel(self.cardActive)
        self.lblActive.setObjectName(u"lblActive")

        self.layoutActive.addWidget(self.lblActive)


        self.statsLayout.addWidget(self.cardActive)

        self.cardRoles = QFrame(PersonnelManagement)
        self.cardRoles.setObjectName(u"cardRoles")
        self.layoutRoles = QVBoxLayout(self.cardRoles)
        self.layoutRoles.setObjectName(u"layoutRoles")
        self.lblRolesTitle = QLabel(self.cardRoles)
        self.lblRolesTitle.setObjectName(u"lblRolesTitle")

        self.layoutRoles.addWidget(self.lblRolesTitle)

        self.layoutRolesData = QHBoxLayout()
        self.layoutRolesData.setObjectName(u"layoutRolesData")
        self.layoutAdmin = QVBoxLayout()
        self.layoutAdmin.setObjectName(u"layoutAdmin")
        self.lblAdminText = QLabel(self.cardRoles)
        self.lblAdminText.setObjectName(u"lblAdminText")

        self.layoutAdmin.addWidget(self.lblAdminText)

        self.lblAdminCount = QLabel(self.cardRoles)
        self.lblAdminCount.setObjectName(u"lblAdminCount")

        self.layoutAdmin.addWidget(self.lblAdminCount)


        self.layoutRolesData.addLayout(self.layoutAdmin)

        self.line1 = QFrame(self.cardRoles)
        self.line1.setObjectName(u"line1")
        self.line1.setFrameShape(QFrame.VLine)

        self.layoutRolesData.addWidget(self.line1)

        self.layoutManager = QVBoxLayout()
        self.layoutManager.setObjectName(u"layoutManager")
        self.lblManagerText = QLabel(self.cardRoles)
        self.lblManagerText.setObjectName(u"lblManagerText")

        self.layoutManager.addWidget(self.lblManagerText)

        self.lblManagerCount = QLabel(self.cardRoles)
        self.lblManagerCount.setObjectName(u"lblManagerCount")

        self.layoutManager.addWidget(self.lblManagerCount)


        self.layoutRolesData.addLayout(self.layoutManager)

        self.line2 = QFrame(self.cardRoles)
        self.line2.setObjectName(u"line2")
        self.line2.setFrameShape(QFrame.VLine)

        self.layoutRolesData.addWidget(self.line2)

        self.layoutCashier = QVBoxLayout()
        self.layoutCashier.setObjectName(u"layoutCashier")
        self.lblCashierText = QLabel(self.cardRoles)
        self.lblCashierText.setObjectName(u"lblCashierText")

        self.layoutCashier.addWidget(self.lblCashierText)

        self.lblCashierCount = QLabel(self.cardRoles)
        self.lblCashierCount.setObjectName(u"lblCashierCount")

        self.layoutCashier.addWidget(self.lblCashierCount)


        self.layoutRolesData.addLayout(self.layoutCashier)


        self.layoutRoles.addLayout(self.layoutRolesData)


        self.statsLayout.addWidget(self.cardRoles)


        self.verticalLayout.addLayout(self.statsLayout)

        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setSpacing(15)
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.txtSearch = QLineEdit(PersonnelManagement)
        self.txtSearch.setObjectName(u"txtSearch")

        self.toolbarLayout.addWidget(self.txtSearch)

        self.cboRole = QComboBox(PersonnelManagement)
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.setObjectName(u"cboRole")
        self.cboRole.setStyleSheet(u"QComboBox { background-color: white; border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px; font-size: 14px; }\n"
"/* \u0110\u1ecbnh d\u1ea1ng cho danh s\u00e1ch x\u1ed5 xu\u1ed1ng c\u1ee7a ComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white; \n"
"    color: #1e293b; /* M\u00e0u ch\u1eef b\u00ecnh th\u01b0\u1eddng */\n"
"    selection-background-color: #3b82f6; /* M\u00e0u n\u1ec1n xanh khi r\u00ea chu\u1ed9t/ch\u1ecdn */\n"
"    selection-color: white; /* M\u00e0u ch\u1eef tr\u1eafng khi r\u00ea chu\u1ed9t/ch\u1ecdn */\n"
"    border: 1px solid #cbd5e1;\n"
"    outline: none; /* B\u1ecf vi\u1ec1n ch\u1ea5m g\u1ea1ch x\u1ea5u x\u00ed khi click */\n"
"}")

        self.toolbarLayout.addWidget(self.cboRole)

        self.cboStatus = QComboBox(PersonnelManagement)
        self.cboStatus.addItem("")
        self.cboStatus.addItem("")
        self.cboStatus.addItem("")
        self.cboStatus.setObjectName(u"cboStatus")
        self.cboStatus.setStyleSheet(u"QComboBox { background-color: white; border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px; font-size: 14px; }\n"
"/* \u0110\u1ecbnh d\u1ea1ng cho danh s\u00e1ch x\u1ed5 xu\u1ed1ng c\u1ee7a ComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white; \n"
"    color: #1e293b; /* M\u00e0u ch\u1eef b\u00ecnh th\u01b0\u1eddng */\n"
"    selection-background-color: #3b82f6; /* M\u00e0u n\u1ec1n xanh khi r\u00ea chu\u1ed9t/ch\u1ecdn */\n"
"    selection-color: white; /* M\u00e0u ch\u1eef tr\u1eafng khi r\u00ea chu\u1ed9t/ch\u1ecdn */\n"
"    border: 1px solid #cbd5e1;\n"
"    outline: none; /* B\u1ecf vi\u1ec1n ch\u1ea5m g\u1ea1ch x\u1ea5u x\u00ed khi click */\n"
"}")

        self.toolbarLayout.addWidget(self.cboStatus)

        self.btnAdd = QPushButton(PersonnelManagement)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btnAdd)


        self.verticalLayout.addLayout(self.toolbarLayout)

        self.tblEmployees = QTableWidget(PersonnelManagement)
        if (self.tblEmployees.columnCount() < 6):
            self.tblEmployees.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblEmployees.setObjectName(u"tblEmployees")
        self.tblEmployees.setFocusPolicy(Qt.NoFocus)
        self.tblEmployees.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblEmployees.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblEmployees.setShowGrid(False)

        self.verticalLayout.addWidget(self.tblEmployees)


        self.retranslateUi(PersonnelManagement)

        QMetaObject.connectSlotsByName(PersonnelManagement)
    # setupUi

    def retranslateUi(self, PersonnelManagement):
        PersonnelManagement.setWindowTitle(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n l\u00fd Nh\u00e2n s\u1ef1", None))
        PersonnelManagement.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"background-color: #f8fafc;", None))
        self.lblTitle.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"font-size: 24px; font-weight: bold; color: #0f172a;", None))
        self.lblTitle.setText(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n l\u00fd nh\u00e2n s\u1ef1", None))
        self.lblSub.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"color: #64748b; font-size: 14px;", None))
        self.lblSub.setText(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n l\u00fd th\u00f4ng tin nh\u00e2n vi\u00ean v\u00e0 ph\u00e2n quy\u1ec1n truy c\u1eadp h\u1ec7 th\u1ed1ng.", None))
        self.cardTotal.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"background-color: white; border: 1px solid #e2e8f0; border-radius: 8px;", None))
        self.lblTotalTitle.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"color: #64748b; font-weight: bold; border: none;", None))
        self.lblTotalTitle.setText(QCoreApplication.translate("PersonnelManagement", u"T\u1ed4NG S\u1ed0 NH\u00c2N VI\u00caN", None))
        self.lblTotal.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"font-size: 28px; font-weight: bold; color: #0f172a; border: none;", None))
        self.lblTotal.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.cardActive.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"background-color: white; border: 1px solid #e2e8f0; border-radius: 8px;", None))
        self.lblActiveTitle.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"color: #64748b; font-weight: bold; border: none;", None))
        self.lblActiveTitle.setText(QCoreApplication.translate("PersonnelManagement", u"\u0110ANG HO\u1ea0T \u0110\u1ed8NG", None))
        self.lblActive.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"font-size: 28px; font-weight: bold; color: #0f172a; border: none;", None))
        self.lblActive.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.cardRoles.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"background-color: white; border: 1px solid #e2e8f0; border-radius: 8px;", None))
        self.lblRolesTitle.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"color: #64748b; font-weight: bold; border: none;", None))
        self.lblRolesTitle.setText(QCoreApplication.translate("PersonnelManagement", u"PH\u00c2N B\u1ed4 VAI TR\u00d2", None))
        self.lblAdminText.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"color: #475569; font-size: 13px; border: none;", None))
        self.lblAdminText.setText(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n tr\u1ecb vi\u00ean", None))
        self.lblAdminCount.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"font-size: 20px; font-weight: bold; color: #0f172a; border: none;", None))
        self.lblAdminCount.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.line1.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"border: none; border-left: 1px solid #e2e8f0;", None))
        self.lblManagerText.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"color: #475569; font-size: 13px; border: none;", None))
        self.lblManagerText.setText(QCoreApplication.translate("PersonnelManagement", u"B\u00e1n h\u00e0ng", None))
        self.lblManagerCount.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"font-size: 20px; font-weight: bold; color: #0f172a; border: none;", None))
        self.lblManagerCount.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.line2.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"border: none; border-left: 1px solid #e2e8f0;", None))
        self.lblCashierText.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"color: #475569; font-size: 13px; border: none;", None))
        self.lblCashierText.setText(QCoreApplication.translate("PersonnelManagement", u"Kho", None))
        self.lblCashierCount.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"font-size: 20px; font-weight: bold; color: #0f172a; border: none;", None))
        self.lblCashierCount.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.txtSearch.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"QLineEdit { background-color: white; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px; font-size: 14px;}\n"
"QLineEdit:focus { border: 1px solid #3b82f6; }", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("PersonnelManagement", u"T\u00ecm ki\u1ebfm theo t\u00ean ho\u1eb7c username...", None))
        self.cboRole.setItemText(0, QCoreApplication.translate("PersonnelManagement", u"T\u1ea5t c\u1ea3 ch\u1ee9c v\u1ee5", None))
        self.cboRole.setItemText(1, QCoreApplication.translate("PersonnelManagement", u"Admin", None))
        self.cboRole.setItemText(2, QCoreApplication.translate("PersonnelManagement", u"Cashier", None))
        self.cboRole.setItemText(3, QCoreApplication.translate("PersonnelManagement", u"Warehouse", None))

        self.cboStatus.setItemText(0, QCoreApplication.translate("PersonnelManagement", u"T\u1ea5t c\u1ea3 tr\u1ea1ng th\u00e1i", None))
        self.cboStatus.setItemText(1, QCoreApplication.translate("PersonnelManagement", u"Ho\u1ea1t \u0111\u1ed9ng", None))
        self.cboStatus.setItemText(2, QCoreApplication.translate("PersonnelManagement", u"Kh\u00f3a", None))

        self.btnAdd.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"QPushButton { background-color: #2563eb; color: white; border-radius: 6px; padding: 10px 20px; font-weight: bold; font-size: 14px; }\n"
"QPushButton:hover { background-color: #1d4ed8; }", None))
        self.btnAdd.setText(QCoreApplication.translate("PersonnelManagement", u"+ Th\u00eam nh\u00e2n s\u1ef1", None))
        ___qtablewidgetitem = self.tblEmployees.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PersonnelManagement", u"USER ID", None))
        ___qtablewidgetitem1 = self.tblEmployees.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PersonnelManagement", u"H\u1ecc T\u00caN", None))
        ___qtablewidgetitem2 = self.tblEmployees.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PersonnelManagement", u"T\u00caN \u0110\u0102NG NH\u1eacP", None))
        ___qtablewidgetitem3 = self.tblEmployees.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PersonnelManagement", u"VAI TR\u00d2", None))
        ___qtablewidgetitem4 = self.tblEmployees.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PersonnelManagement", u"TR\u1ea0NG TH\u00c1I", None))
        ___qtablewidgetitem5 = self.tblEmployees.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PersonnelManagement", u"ACTIONS", None))
        self.tblEmployees.setStyleSheet(QCoreApplication.translate("PersonnelManagement", u"QTableWidget { background-color: white; border: 1px solid #e2e8f0; border-radius: 8px; color: #1e293b;}\n"
"QHeaderView::section { background-color: #f1f5f9; padding: 12px; font-weight: bold; color: #475569; border: none; border-bottom: 1px solid #e2e8f0;}\n"
"QTableWidget::item { padding: 8px; border-bottom: 1px solid #f1f5f9; }", None))
    # retranslateUi

