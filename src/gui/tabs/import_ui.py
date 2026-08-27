# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ImportTab(object):
    def setupUi(self, ImportTab):
        if not ImportTab.objectName():
            ImportTab.setObjectName(u"ImportTab")
        ImportTab.resize(940, 680)
        ImportTab.setStyleSheet(u"QWidget#ImportTab {\n"
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
"QDateEdit:hover,\n"
""
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
"    padding:"
                        " 4px;\n"
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
"    image: url(ass"
                        "ets/images/chevron-up.png);\n"
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
"    font-weight: bol"
                        "d;\n"
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
"    border-bottom: 1px solid #f1f5"
                        "f9;\n"
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
"    background-col"
                        "or: #ffedd5;\n"
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
"    background-color: #fef2f2;\n"
"    "
                        "color: #dc2626;\n"
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
"    backgro"
                        "und-color: transparent;\n"
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
"QScrollBar::handle:horizontal {\n"
"  "
                        "  background-color: #cbd5e1;\n"
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
"    font-size"
                        ": 13px;\n"
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
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QLabel#lblSubtitle {\n"
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
"  "
                        "  background-color: #1e3a8a;\n"
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
"    color: #dc2626;\n"
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
"QLabel#lblPage {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton#btnPrev,\n"
"QPushButton#btnNext {\n"
"    background-color: #ffffff;\n"
"    color: #334155;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 34px;\n"
"    max-width: 3"
                        "4px;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"    padding: 0px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnPrev:hover,\n"
"QPushButton#btnNext:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnPrev:disabled,\n"
"QPushButton#btnNext:disabled {\n"
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
"    background-color: #1"
                        "d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton#PageNumberButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #94a3b8;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"    color: #0f172a;\n"
"    font-size: 24px;\n"
"    font-weight: 700;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"QLabel#lblSubtitle,\n"
"QLabel#lblSub {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"QLabel#lblPaginationInfo {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
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
"QPushButton#btnPrevPage:hover,\n"
"QPushButton#btnNextPage:ho"
                        "ver {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnPrevPage:disabled,\n"
"QPushButton#btnNextPage:disabled {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    color: #cbd5e1;\n"
"}\n"
"\n"
"QLabel#lblTotalSpendTitle,\n"
"QLabel#lblRecentTitle {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#lblTotalSpend,\n"
"QLabel#lblRecent {\n"
"    color: #0f172a;\n"
"    font-size: 27px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#lblTotalSpendSub,\n"
"QLabel#lblRecentSub {\n"
"    color: #6b7280;\n"
"    font-size: 11px;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"QFrame#cardTotalSpend,\n"
"QFrame#cardRecent {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"QLabel#badgeTotalSpend,\n"
"QLabel#badgeRecent {\n"
"    background-color: #eff6ff;\n"
"    border-radius: 9px;\n"
"}\n"
"QLineEdit#txtSearch {\n"
"    m"
                        "in-width: 280px;\n"
"}\n"
"QComboBox#cboDate {\n"
"    min-width: 170px;\n"
"    max-width: 170px;\n"
"}\n"
"QPushButton#btnCreateOrder {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnCreateOrder:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnCreateOrder:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnCreateOrder:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(ImportTab)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 10, 12, 12)
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.verticalLayout_title = QVBoxLayout()
        self.verticalLayout_title.setSpacing(0)
        self.verticalLayout_title.setObjectName(u"verticalLayout_title")
        self.lblTitle = QLabel(ImportTab)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout_title.addWidget(self.lblTitle)

        self.lblSubtitle = QLabel(ImportTab)
        self.lblSubtitle.setObjectName(u"lblSubtitle")

        self.verticalLayout_title.addWidget(self.lblSubtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_title)

        self.horizontalSpacer_header = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)

        self.btnCreateOrder = QPushButton(ImportTab)
        self.btnCreateOrder.setObjectName(u"btnCreateOrder")
        self.btnCreateOrder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_header.addWidget(self.btnCreateOrder)


        self.verticalLayout.addLayout(self.horizontalLayout_header)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cardTotalSpend = QFrame(ImportTab)
        self.cardTotalSpend.setObjectName(u"cardTotalSpend")
        self.cardTotalSpend.setMinimumSize(QSize(0, 132))
        self.cardTotalSpend.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_card1 = QVBoxLayout(self.cardTotalSpend)
        self.verticalLayout_card1.setSpacing(6)
        self.verticalLayout_card1.setObjectName(u"verticalLayout_card1")
        self.verticalLayout_card1.setContentsMargins(16, 14, 16, 20)
        self.rowTotalSpendTop = QHBoxLayout()
        self.rowTotalSpendTop.setSpacing(8)
        self.rowTotalSpendTop.setObjectName(u"rowTotalSpendTop")
        self.lblTotalSpendTitle = QLabel(self.cardTotalSpend)
        self.lblTotalSpendTitle.setObjectName(u"lblTotalSpendTitle")

        self.rowTotalSpendTop.addWidget(self.lblTotalSpendTitle)

        self.spacerTotalSpendTop = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowTotalSpendTop.addItem(self.spacerTotalSpendTop)

        self.badgeTotalSpend = QLabel(self.cardTotalSpend)
        self.badgeTotalSpend.setObjectName(u"badgeTotalSpend")
        self.badgeTotalSpend.setMinimumSize(QSize(34, 34))
        self.badgeTotalSpend.setMaximumSize(QSize(34, 34))
        self.badgeTotalSpend.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badgeTotalSpend.setProperty(u"iconPx", 17)

        self.rowTotalSpendTop.addWidget(self.badgeTotalSpend)


        self.verticalLayout_card1.addLayout(self.rowTotalSpendTop)

        self.lblTotalSpend = QLabel(self.cardTotalSpend)
        self.lblTotalSpend.setObjectName(u"lblTotalSpend")
        self.lblTotalSpend.setMinimumSize(QSize(0, 25))
        self.lblTotalSpend.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_card1.addWidget(self.lblTotalSpend)

        self.lblTotalSpendSub = QLabel(self.cardTotalSpend)
        self.lblTotalSpendSub.setObjectName(u"lblTotalSpendSub")

        self.verticalLayout_card1.addWidget(self.lblTotalSpendSub)


        self.horizontalLayout.addWidget(self.cardTotalSpend)

        self.cardRecent = QFrame(ImportTab)
        self.cardRecent.setObjectName(u"cardRecent")
        self.cardRecent.setMinimumSize(QSize(0, 132))
        self.cardRecent.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_card3 = QVBoxLayout(self.cardRecent)
        self.verticalLayout_card3.setSpacing(6)
        self.verticalLayout_card3.setObjectName(u"verticalLayout_card3")
        self.verticalLayout_card3.setContentsMargins(16, 14, 16, 20)
        self.rowRecentTop = QHBoxLayout()
        self.rowRecentTop.setSpacing(8)
        self.rowRecentTop.setObjectName(u"rowRecentTop")
        self.lblRecentTitle = QLabel(self.cardRecent)
        self.lblRecentTitle.setObjectName(u"lblRecentTitle")

        self.rowRecentTop.addWidget(self.lblRecentTitle)

        self.spacerRecentTop = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowRecentTop.addItem(self.spacerRecentTop)

        self.badgeRecent = QLabel(self.cardRecent)
        self.badgeRecent.setObjectName(u"badgeRecent")
        self.badgeRecent.setMinimumSize(QSize(34, 34))
        self.badgeRecent.setMaximumSize(QSize(34, 34))
        self.badgeRecent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badgeRecent.setProperty(u"iconPx", 17)

        self.rowRecentTop.addWidget(self.badgeRecent)


        self.verticalLayout_card3.addLayout(self.rowRecentTop)

        self.lblRecent = QLabel(self.cardRecent)
        self.lblRecent.setObjectName(u"lblRecent")
        self.lblRecent.setMinimumSize(QSize(0, 25))
        self.lblRecent.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_card3.addWidget(self.lblRecent)

        self.lblRecentSub = QLabel(self.cardRecent)
        self.lblRecentSub.setObjectName(u"lblRecentSub")

        self.verticalLayout_card3.addWidget(self.lblRecentSub)


        self.horizontalLayout.addWidget(self.cardRecent)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frameTable = QFrame(ImportTab)
        self.frameTable.setObjectName(u"frameTable")
        self.frameTable.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_table = QVBoxLayout(self.frameTable)
        self.verticalLayout_table.setSpacing(2)
        self.verticalLayout_table.setObjectName(u"verticalLayout_table")
        self.verticalLayout_table.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_tableHeader = QHBoxLayout()
        self.horizontalLayout_tableHeader.setSpacing(8)
        self.horizontalLayout_tableHeader.setObjectName(u"horizontalLayout_tableHeader")
        self.horizontalLayout_tableHeader.setContentsMargins(0, 0, 0, 10)
        self.txtSearch = QLineEdit(self.frameTable)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout_tableHeader.addWidget(self.txtSearch)

        self.cboDate = QComboBox(self.frameTable)
        self.cboDate.addItem("")
        self.cboDate.addItem("")
        self.cboDate.addItem("")
        self.cboDate.addItem("")
        self.cboDate.setObjectName(u"cboDate")

        self.horizontalLayout_tableHeader.addWidget(self.cboDate)


        self.verticalLayout_table.addLayout(self.horizontalLayout_tableHeader)

        self.tblImportOrders = QTableWidget(self.frameTable)
        if (self.tblImportOrders.columnCount() < 6):
            self.tblImportOrders.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblImportOrders.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblImportOrders.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblImportOrders.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter)
        self.tblImportOrders.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblImportOrders.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblImportOrders.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblImportOrders.setObjectName(u"tblImportOrders")
        self.tblImportOrders.setFrameShape(QFrame.Shape.NoFrame)
        self.tblImportOrders.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblImportOrders.setAlternatingRowColors(False)
        self.tblImportOrders.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblImportOrders.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblImportOrders.setShowGrid(False)
        self.tblImportOrders.horizontalHeader().setMinimumSectionSize(90)
        self.tblImportOrders.horizontalHeader().setDefaultSectionSize(130)
        self.tblImportOrders.horizontalHeader().setHighlightSections(False)
        self.tblImportOrders.horizontalHeader().setStretchLastSection(True)
        self.tblImportOrders.verticalHeader().setVisible(False)
        self.tblImportOrders.verticalHeader().setMinimumSectionSize(44)
        self.tblImportOrders.verticalHeader().setDefaultSectionSize(44)

        self.verticalLayout_table.addWidget(self.tblImportOrders)


        self.verticalLayout.addWidget(self.frameTable)

        self.horizontalLayout_pagination = QHBoxLayout()
        self.horizontalLayout_pagination.setSpacing(5)
        self.horizontalLayout_pagination.setObjectName(u"horizontalLayout_pagination")
        self.lblPage = QLabel(ImportTab)
        self.lblPage.setObjectName(u"lblPage")

        self.horizontalLayout_pagination.addWidget(self.lblPage)

        self.horizontalSpacer_pg = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_pagination.addItem(self.horizontalSpacer_pg)

        self.btnPrev = QPushButton(ImportTab)
        self.btnPrev.setObjectName(u"btnPrev")
        self.btnPrev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrev.setProperty(u"iconPx", 12)

        self.horizontalLayout_pagination.addWidget(self.btnPrev)

        self.btnNext = QPushButton(ImportTab)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNext.setProperty(u"iconPx", 12)

        self.horizontalLayout_pagination.addWidget(self.btnNext)


        self.verticalLayout.addLayout(self.horizontalLayout_pagination)


        self.retranslateUi(ImportTab)

        QMetaObject.connectSlotsByName(ImportTab)
    # setupUi

    def retranslateUi(self, ImportTab):
        self.lblTitle.setText(QCoreApplication.translate("ImportTab", u"Qu\u1ea3n l\u00fd Nh\u1eadp h\u00e0ng", None))
        self.lblSubtitle.setText(QCoreApplication.translate("ImportTab", u"Theo d\u00f5i v\u00e0 qu\u1ea3n l\u00fd c\u00e1c phi\u1ebfu nh\u1eadp kho t\u1eeb nh\u00e0 cung c\u1ea5p.", None))
        self.btnCreateOrder.setText(QCoreApplication.translate("ImportTab", u"+  T\u1ea1o Phi\u1ebfu Nh\u1eadp", None))
        self.lblTotalSpendTitle.setText(QCoreApplication.translate("ImportTab", u"T\u1ed5ng chi th\u00e1ng n\u00e0y", None))
        self.badgeTotalSpend.setText("")
        self.badgeTotalSpend.setProperty(u"iconName", QCoreApplication.translate("ImportTab", u"cash", None))
        self.badgeTotalSpend.setProperty(u"iconColor", QCoreApplication.translate("ImportTab", u"#1d4ed8", None))
        self.lblTotalSpend.setText(QCoreApplication.translate("ImportTab", u"\u0111 0", None))
        self.lblTotalSpendSub.setText(QCoreApplication.translate("ImportTab", u"So v\u1edbi th\u00e1ng tr\u01b0\u1edbc", None))
        self.lblRecentTitle.setText(QCoreApplication.translate("ImportTab", u"L\u01b0\u1ee3t nh\u1eadp g\u1ea7n \u0111\u00e2y", None))
        self.badgeRecent.setText("")
        self.badgeRecent.setProperty(u"iconName", QCoreApplication.translate("ImportTab", u"import", None))
        self.badgeRecent.setProperty(u"iconColor", QCoreApplication.translate("ImportTab", u"#1d4ed8", None))
        self.lblRecent.setText(QCoreApplication.translate("ImportTab", u"0", None))
        self.lblRecentSub.setText(QCoreApplication.translate("ImportTab", u"Trong 7 ng\u00e0y qua", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("ImportTab", u"T\u00ecm theo m\u00e3 phi\u1ebfu ho\u1eb7c nh\u00e0 cung c\u1ea5p", None))
        self.cboDate.setItemText(0, QCoreApplication.translate("ImportTab", u"T\u1ea5t c\u1ea3 th\u1eddi gian", None))
        self.cboDate.setItemText(1, QCoreApplication.translate("ImportTab", u"H\u00f4m nay", None))
        self.cboDate.setItemText(2, QCoreApplication.translate("ImportTab", u"7 ng\u00e0y qua", None))
        self.cboDate.setItemText(3, QCoreApplication.translate("ImportTab", u"30 ng\u00e0y qua", None))

        ___qtablewidgetitem = self.tblImportOrders.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ImportTab", u"M\u00c3 NH\u1eacP", None))
        ___qtablewidgetitem1 = self.tblImportOrders.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ImportTab", u"NH\u00c0 CUNG C\u1ea4P", None))
        ___qtablewidgetitem2 = self.tblImportOrders.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ImportTab", u"NG\u00c0Y NH\u1eacP", None))
        ___qtablewidgetitem3 = self.tblImportOrders.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ImportTab", u"T\u1ed4NG TI\u1ec0N", None))
        ___qtablewidgetitem4 = self.tblImportOrders.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ImportTab", u"TR\u1ea0NG TH\u00c1I", None))
        ___qtablewidgetitem5 = self.tblImportOrders.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ImportTab", u"NG\u01af\u1edcI T\u1ea0O", None))
        self.lblPage.setText(QCoreApplication.translate("ImportTab", u"Hi\u1ec3n th\u1ecb 1-10 c\u1ee7a 0 m\u1ee5c", None))
        self.btnPrev.setText("")
        self.btnPrev.setProperty(u"iconName", QCoreApplication.translate("ImportTab", u"previous", None))
        self.btnPrev.setProperty(u"iconColor", QCoreApplication.translate("ImportTab", u"default", None))
        self.btnNext.setText("")
        self.btnNext.setProperty(u"iconName", QCoreApplication.translate("ImportTab", u"next", None))
        self.btnNext.setProperty(u"iconColor", QCoreApplication.translate("ImportTab", u"default", None))
        pass
    # retranslateUi

