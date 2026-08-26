# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplier_management.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_SupplierManagement(object):
    def setupUi(self, SupplierManagement):
        if not SupplierManagement.objectName():
            SupplierManagement.setObjectName(u"SupplierManagement")
        SupplierManagement.resize(1000, 700)
        SupplierManagement.setStyleSheet(u"QWidget#SupplierManagement {\n"
"    background-color: #f1f5f9;\n"
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
"QDateEdi"
                        "t:hover,\n"
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
"\n"
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
"    border-radius: 8px"
                        ";\n"
"    padding: 4px;\n"
"    outline: none;\n"
"    selection-background-color: #f1f5f9;\n"
"    selection-color: #0f172a;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    color: #0f172a;\n"
"    min-height: 30px;\n"
"    padding: 4px 10px;\n"
"    border-radius: 6px;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #f1f5f9;\n"
"    color: #0f172a;\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #e2e8f0;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
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
""
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
"    image: url(assets/images/chevron-up.png);\n"
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
"\n"
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
"QCheckBox::indicator:hover {"
                        "\n"
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
"    font-weight: bold;\n"
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
"\n"
"QPushButton#RowActionButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0px;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"    min-height: 28px;\n"
"    max-height: 28px;\n"
"    color: #64748b;\n"
"}\n"
"QPushButton#"
                        "RowActionButton:hover {\n"
"    background-color: #f1f5f9;\n"
"    color: #0f172a;\n"
"}\n"
"QPushButton#RowActionButton:pressed {\n"
"    background-color: #e2e8f0;\n"
"}\n"
"\n"
"QPushButton#btnEditRow:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton#btnDeleteRow:hover {\n"
"    background-color: #fef2f2;\n"
"    color: #dc2626;\n"
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
"    border-bottom: 1px solid #f1f5f9;\n"
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
"    font-weig"
                        "ht: 700;\n"
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
"    background-color: #ffedd5;\n"
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
"QLabe"
                        "l[badge=\"neutral\"] {\n"
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
"    background-color: #fef2f2;\n"
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
"   "
                        " color: #10b981;\n"
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
"    backgr"
                        "ound-color: #64748b;\n"
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
"QScrollBar::handle:horizontal {\n"
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
"    h"
                        "eight: 0px;\n"
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
"    font-size: 13px;\n"
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
"QFrame#frameHeader,\n"
"QFrame#frameToolbar,\n"
"QFrame#framePagination {\n"
"    background-color: transparent;\n"
"    border: none;\n"
""
                        "}\n"
"\n"
"QFrame#frameTable {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"    color: #0f172a;\n"
"    font-size: 24px;\n"
"    font-weight: 700;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QLabel#lblSubtitle,\n"
"QLabel#lblSub {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QPushButton#btnAdd {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnAdd:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnAdd:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnAdd:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"\n"
"QPushButton#btnDelete {\n"
"    background-color: #ffffff;\n"
"    color: #dc"
                        "2626;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnDelete:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"}\n"
"QPushButton#btnDelete:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QLabel#lblPaginationInfo,\n"
"QLabel#lblPage {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton#btnPrev,\n"
"QPushButton#btnNext,\n"
"QPushButton#btnPrevPage,\n"
"QPushButton#btnNextPage {\n"
"    background-color: #ffffff;\n"
"    color: #334155;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 34px;\n"
"    max-width: 34px;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"    padding: 0px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnPrev:hover,\n"
"QPushButton#btnNext:hover,\n"
"QPu"
                        "shButton#btnPrevPage:hover,\n"
"QPushButton#btnNextPage:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnPrev:disabled,\n"
"QPushButton#btnNext:disabled,\n"
"QPushButton#btnPrevPage:disabled,\n"
"QPushButton#btnNextPage:disabled {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    color: #cbd5e1;\n"
"}\n"
"\n"
"QPushButton#PageNumberButton {\n"
"    background-color: #ffffff;\n"
"    color: #334155;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 32px;\n"
"    max-width: 32px;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"    padding: 0px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#PageNumberButton:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#PageNumberButton:checked {\n"
"    background-color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #ff"
                        "ffff;\n"
"}\n"
"QPushButton#PageNumberButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #94a3b8;\n"
"}\n"
"\n"
"QLineEdit#txtSearch {\n"
"    min-width: 260px;\n"
"}\n"
"QComboBox#cboFilter {\n"
"    min-width: 180px;\n"
"}\n"
"QPushButton#btnExport {\n"
"    min-width: 140px;\n"
"}")
        self.verticalLayout = QVBoxLayout(SupplierManagement)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 10, 12, 12)
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(3)
        self.titleLayout.setObjectName(u"titleLayout")
        self.lblTitle = QLabel(SupplierManagement)
        self.lblTitle.setObjectName(u"lblTitle")

        self.titleLayout.addWidget(self.lblTitle)

        self.lblSub = QLabel(SupplierManagement)
        self.lblSub.setObjectName(u"lblSub")

        self.titleLayout.addWidget(self.lblSub)


        self.verticalLayout.addLayout(self.titleLayout)

        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setSpacing(8)
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.txtSearch = QLineEdit(SupplierManagement)
        self.txtSearch.setObjectName(u"txtSearch")

        self.toolbarLayout.addWidget(self.txtSearch)

        self.cboFilter = QComboBox(SupplierManagement)
        self.cboFilter.addItem("")
        self.cboFilter.addItem("")
        self.cboFilter.addItem("")
        self.cboFilter.setObjectName(u"cboFilter")

        self.toolbarLayout.addWidget(self.cboFilter)

        self.btnExport = QPushButton(SupplierManagement)
        self.btnExport.setObjectName(u"btnExport")
        self.btnExport.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btnExport)

        self.btnAdd = QPushButton(SupplierManagement)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btnAdd)


        self.verticalLayout.addLayout(self.toolbarLayout)

        self.frameTable = QFrame(SupplierManagement)
        self.frameTable.setObjectName(u"frameTable")
        self.frameTable.setFrameShape(QFrame.Shape.NoFrame)
        self.tableFrameLayout = QVBoxLayout(self.frameTable)
        self.tableFrameLayout.setSpacing(0)
        self.tableFrameLayout.setObjectName(u"tableFrameLayout")
        self.tableFrameLayout.setContentsMargins(12, 12, 12, 12)
        self.tblSuppliers = QTableWidget(self.frameTable)
        if (self.tblSuppliers.columnCount() < 7):
            self.tblSuppliers.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tblSuppliers.setObjectName(u"tblSuppliers")
        self.tblSuppliers.setFrameShape(QFrame.Shape.NoFrame)
        self.tblSuppliers.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblSuppliers.setAlternatingRowColors(False)
        self.tblSuppliers.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblSuppliers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblSuppliers.setShowGrid(False)
        self.tblSuppliers.horizontalHeader().setMinimumSectionSize(90)
        self.tblSuppliers.horizontalHeader().setDefaultSectionSize(150)
        self.tblSuppliers.horizontalHeader().setHighlightSections(False)
        self.tblSuppliers.horizontalHeader().setStretchLastSection(True)
        self.tblSuppliers.verticalHeader().setVisible(False)
        self.tblSuppliers.verticalHeader().setMinimumSectionSize(44)
        self.tblSuppliers.verticalHeader().setDefaultSectionSize(44)

        self.tableFrameLayout.addWidget(self.tblSuppliers)


        self.verticalLayout.addWidget(self.frameTable)


        self.retranslateUi(SupplierManagement)

        QMetaObject.connectSlotsByName(SupplierManagement)
    # setupUi

    def retranslateUi(self, SupplierManagement):
        self.lblTitle.setText(QCoreApplication.translate("SupplierManagement", u"Qu\u1ea3n l\u00fd Nh\u00e0 cung c\u1ea5p", None))
        self.lblSub.setText(QCoreApplication.translate("SupplierManagement", u"Qu\u1ea3n l\u00fd v\u00e0 \u0111\u00e1nh gi\u00e1 c\u00e1c \u0111\u1ed1i t\u00e1c cung \u1ee9ng c\u1ee7a h\u1ec7 th\u1ed1ng.", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("SupplierManagement", u"T\u00ecm ki\u1ebfm theo t\u00ean NCC ho\u1eb7c s\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.cboFilter.setItemText(0, QCoreApplication.translate("SupplierManagement", u"T\u1ea5t c\u1ea3 ti\u00eau ch\u00ed", None))
        self.cboFilter.setItemText(1, QCoreApplication.translate("SupplierManagement", u"T\u00ean c\u00f4ng ty", None))
        self.cboFilter.setItemText(2, QCoreApplication.translate("SupplierManagement", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))

        self.btnExport.setText(QCoreApplication.translate("SupplierManagement", u"Xu\u1ea5t b\u00e1o c\u00e1o", None))
        self.btnAdd.setText(QCoreApplication.translate("SupplierManagement", u"+ Th\u00eam \u0111\u1ed1i t\u00e1c", None))
        ___qtablewidgetitem = self.tblSuppliers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SupplierManagement", u"ID", None))
        ___qtablewidgetitem1 = self.tblSuppliers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SupplierManagement", u"T\u00caN C\u00d4NG TY", None))
        ___qtablewidgetitem2 = self.tblSuppliers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SupplierManagement", u"NG\u01af\u1edcI LI\u00caN H\u1ec6", None))
        ___qtablewidgetitem3 = self.tblSuppliers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SupplierManagement", u"S\u1ed0 \u0110I\u1ec6N THO\u1ea0I", None))
        ___qtablewidgetitem4 = self.tblSuppliers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SupplierManagement", u"EMAIL", None))
        ___qtablewidgetitem5 = self.tblSuppliers.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SupplierManagement", u"\u0110\u1ecaA CH\u1ec8", None))
        ___qtablewidgetitem6 = self.tblSuppliers.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SupplierManagement", u"THAO T\u00c1C", None))
        pass
    # retranslateUi

