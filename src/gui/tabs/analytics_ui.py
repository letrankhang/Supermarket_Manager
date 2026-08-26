# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analytics.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Analytics(object):
    def setupUi(self, Analytics):
        if not Analytics.objectName():
            Analytics.setObjectName(u"Analytics")
        Analytics.resize(1280, 860)
        Analytics.setStyleSheet(u"QWidget#Analytics {\n"
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
"QLabel#lblRevenueCaption,\n"
"QLabel#lblOrdersCaption,\n"
"QLabel#lblAovCaption,\n"
"QLabel#lblReturnCaption {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#lblRevenueVal,\n"
"QLabel#lblOrdersVal,\n"
"QLabel#lblAovVal,\n"
"QLabel#lblReturnVal {\n"
"    color: #0f172a;\n"
"    font-size: 27px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#badgeRevenue,\n"
"QLabel#badgeOrders,\n"
"QLabel#badgeAov,\n"
"QLabel#badgeReturn {\n"
"    background-color: #eff6ff;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLabel#lblTimeChartTitle,\n"
"QLabel#lblCategoryTitle,\n"
"QLabel#lblTopProductsTitle {\n"
"    color: #0f172a;\n"
"    font-size: 15px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
""
                        "QLabel#lblRevenueTrend,\n"
"QLabel#lblOrdersTrend,\n"
"QLabel#lblAovTrend,\n"
"QLabel#lblReturnTrend {\n"
"    background-color: transparent;\n"
"    color: #64748b;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"    padding: 2px 0px;\n"
"}\n"
"\n"
"QLabel#lblRevenueTrend[trend=\"up\"],\n"
"QLabel#lblOrdersTrend[trend=\"up\"],\n"
"QLabel#lblAovTrend[trend=\"up\"],\n"
"QLabel#lblReturnTrend[trend=\"up\"] {\n"
"    background-color: #ecfdf5;\n"
"    color: #059669;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QLabel#lblRevenueTrend[trend=\"down\"],\n"
"QLabel#lblOrdersTrend[trend=\"down\"],\n"
"QLabel#lblAovTrend[trend=\"down\"],\n"
"QLabel#lblReturnTrend[trend=\"down\"] {\n"
"    background-color: #fef2f2;\n"
"    color: #dc2626;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QLabel#lblRevenueTrend[trend=\"flat\"],\n"
"QLabel#lblOrdersTrend[trend=\"flat\"],\n"
"QLabel#lblAovTrend[trend=\"flat\"],\n"
"QLabel#lblReturnTrend[trend=\"flat\"] {\n"
"    background"
                        "-color: #f1f5f9;\n"
"    color: #64748b;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QFrame#cardRevenue,\n"
"QFrame#cardOrders,\n"
"QFrame#cardAov,\n"
"QFrame#cardReturn,\n"
"QFrame#cardTimeChart,\n"
"QFrame#cardCategory,\n"
"QFrame#cardTopProducts {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"QFrame#framePeriodToggle {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#btnPeriodToday,\n"
"QPushButton#btnPeriodWeek,\n"
"QPushButton#btnPeriodMonth {\n"
"    background-color: transparent;\n"
"    color: #64748b;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnPeriodToday:hover,\n"
"QPushButton#btnPeriodWeek:hover,\n"
"QPushButton#btnPeriodMonth:hover {\n"
"    background-color: #eff6ff;\n"
"    color"
                        ": #1d4ed8;\n"
"}\n"
"QPushButton#btnPeriodToday:checked,\n"
"QPushButton#btnPeriodWeek:checked,\n"
"QPushButton#btnPeriodMonth:checked {\n"
"    background-color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #ffffff;\n"
"}\n"
"QWidget#containerTimeChart,\n"
"QScrollArea#scrollCategory,\n"
"QWidget#scrollCategoryContent {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"QProgressBar {\n"
"    background-color: #e2e8f0;\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"    max-height: 7px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #1d4ed8;\n"
"    border-radius: 3px;\n"
"}\n"
"QLabel#lblCategorySub {\n"
"    color: #94a3b8;\n"
"    font-size: 11px;\n"
"    font-weight: normal;\n"
"}\n"
"QLabel#CategoryName {\n"
"    color: #334155;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
"QLabel#CategoryAmount {\n"
"    color: #94a3b8;\n"
"    font-size: 11px;\n"
"    font-weight: normal;\n"
"}\n"
"QLabel#CategoryPercent {\n"
""
                        "    color: #0f172a;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#CategoryDot {\n"
"    background-color: #8fbdf7;\n"
"    border-radius: 4px;\n"
"    min-width: 8px;\n"
"    max-width: 8px;\n"
"    min-height: 8px;\n"
"    max-height: 8px;\n"
"}\n"
"QProgressBar#CategoryBar {\n"
"    background-color: #eef2f7;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    min-height: 8px;\n"
"    max-height: 8px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar#CategoryBar::chunk {\n"
"    background-color: #8fbdf7;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#btnDetailLink {\n"
"    background-color: transparent;\n"
"    color: #1d4ed8;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0px 8px;\n"
"    min-height: 26px;\n"
"    max-height: 26px;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnDetailLink:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1e3a8a;\n"
"}\n"
"QPushButton#btnDetailLink:pressed {\n"
"    background-co"
                        "lor: #dbeafe;\n"
"}\n"
"")
        self.rootLayout = QVBoxLayout(Analytics)
        self.rootLayout.setSpacing(16)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(12, 10, 12, 12)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(3)
        self.titleLayout.setObjectName(u"titleLayout")
        self.lblTitle = QLabel(Analytics)
        self.lblTitle.setObjectName(u"lblTitle")

        self.titleLayout.addWidget(self.lblTitle)

        self.lblSubtitle = QLabel(Analytics)
        self.lblSubtitle.setObjectName(u"lblSubtitle")

        self.titleLayout.addWidget(self.lblSubtitle)


        self.headerLayout.addLayout(self.titleLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.framePeriodToggle = QFrame(Analytics)
        self.framePeriodToggle.setObjectName(u"framePeriodToggle")
        self.framePeriodToggle.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleLayout = QHBoxLayout(self.framePeriodToggle)
        self.toggleLayout.setSpacing(4)
        self.toggleLayout.setObjectName(u"toggleLayout")
        self.toggleLayout.setContentsMargins(4, 4, 4, 4)
        self.btnPeriodToday = QPushButton(self.framePeriodToggle)
        self.btnPeriodToday.setObjectName(u"btnPeriodToday")
        self.btnPeriodToday.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPeriodToday.setCheckable(True)

        self.toggleLayout.addWidget(self.btnPeriodToday)

        self.btnPeriodWeek = QPushButton(self.framePeriodToggle)
        self.btnPeriodWeek.setObjectName(u"btnPeriodWeek")
        self.btnPeriodWeek.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPeriodWeek.setCheckable(True)
        self.btnPeriodWeek.setChecked(True)

        self.toggleLayout.addWidget(self.btnPeriodWeek)

        self.btnPeriodMonth = QPushButton(self.framePeriodToggle)
        self.btnPeriodMonth.setObjectName(u"btnPeriodMonth")
        self.btnPeriodMonth.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPeriodMonth.setCheckable(True)

        self.toggleLayout.addWidget(self.btnPeriodMonth)


        self.headerLayout.addWidget(self.framePeriodToggle)


        self.rootLayout.addLayout(self.headerLayout)

        self.cardsLayout = QHBoxLayout()
        self.cardsLayout.setSpacing(16)
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.cardRevenue = QFrame(Analytics)
        self.cardRevenue.setObjectName(u"cardRevenue")
        self.cardRevenue.setMinimumSize(QSize(0, 120))
        self.cardRevenue.setFrameShape(QFrame.Shape.NoFrame)
        self.cardRevenueLayout = QVBoxLayout(self.cardRevenue)
        self.cardRevenueLayout.setSpacing(6)
        self.cardRevenueLayout.setObjectName(u"cardRevenueLayout")
        self.cardRevenueLayout.setContentsMargins(16, 14, 16, 14)
        self.cardRevenueTopRow = QHBoxLayout()
        self.cardRevenueTopRow.setObjectName(u"cardRevenueTopRow")
        self.lblRevenueCaption = QLabel(self.cardRevenue)
        self.lblRevenueCaption.setObjectName(u"lblRevenueCaption")

        self.cardRevenueTopRow.addWidget(self.lblRevenueCaption)

        self.cardRevenueSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardRevenueTopRow.addItem(self.cardRevenueSpacer)

        self.badgeRevenue = QLabel(self.cardRevenue)
        self.badgeRevenue.setObjectName(u"badgeRevenue")
        self.badgeRevenue.setMinimumSize(QSize(32, 32))
        self.badgeRevenue.setMaximumSize(QSize(32, 32))
        self.badgeRevenue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardRevenueTopRow.addWidget(self.badgeRevenue)


        self.cardRevenueLayout.addLayout(self.cardRevenueTopRow)

        self.lblRevenueVal = QLabel(self.cardRevenue)
        self.lblRevenueVal.setObjectName(u"lblRevenueVal")
        self.lblRevenueVal.setMinimumSize(QSize(0, 25))
        self.lblRevenueVal.setMaximumSize(QSize(16777215, 25))

        self.cardRevenueLayout.addWidget(self.lblRevenueVal)

        self.cardRevenueTrendRow = QHBoxLayout()
        self.cardRevenueTrendRow.setObjectName(u"cardRevenueTrendRow")
        self.cardRevenueTrendRow.setContentsMargins(-1, 10, -1, -1)
        self.lblRevenueTrend = QLabel(self.cardRevenue)
        self.lblRevenueTrend.setObjectName(u"lblRevenueTrend")

        self.cardRevenueTrendRow.addWidget(self.lblRevenueTrend)

        self.cardRevenueTrendSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardRevenueTrendRow.addItem(self.cardRevenueTrendSpacer)


        self.cardRevenueLayout.addLayout(self.cardRevenueTrendRow)


        self.cardsLayout.addWidget(self.cardRevenue)

        self.cardOrders = QFrame(Analytics)
        self.cardOrders.setObjectName(u"cardOrders")
        self.cardOrders.setMinimumSize(QSize(0, 120))
        self.cardOrders.setFrameShape(QFrame.Shape.NoFrame)
        self.cardOrdersLayout = QVBoxLayout(self.cardOrders)
        self.cardOrdersLayout.setSpacing(6)
        self.cardOrdersLayout.setObjectName(u"cardOrdersLayout")
        self.cardOrdersLayout.setContentsMargins(16, 14, 16, 14)
        self.cardOrdersTopRow = QHBoxLayout()
        self.cardOrdersTopRow.setObjectName(u"cardOrdersTopRow")
        self.lblOrdersCaption = QLabel(self.cardOrders)
        self.lblOrdersCaption.setObjectName(u"lblOrdersCaption")

        self.cardOrdersTopRow.addWidget(self.lblOrdersCaption)

        self.cardOrdersSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardOrdersTopRow.addItem(self.cardOrdersSpacer)

        self.badgeOrders = QLabel(self.cardOrders)
        self.badgeOrders.setObjectName(u"badgeOrders")
        self.badgeOrders.setMinimumSize(QSize(32, 32))
        self.badgeOrders.setMaximumSize(QSize(32, 32))
        self.badgeOrders.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardOrdersTopRow.addWidget(self.badgeOrders)


        self.cardOrdersLayout.addLayout(self.cardOrdersTopRow)

        self.lblOrdersVal = QLabel(self.cardOrders)
        self.lblOrdersVal.setObjectName(u"lblOrdersVal")
        self.lblOrdersVal.setMinimumSize(QSize(0, 25))
        self.lblOrdersVal.setMaximumSize(QSize(16777215, 25))

        self.cardOrdersLayout.addWidget(self.lblOrdersVal)

        self.cardOrdersTrendRow = QHBoxLayout()
        self.cardOrdersTrendRow.setObjectName(u"cardOrdersTrendRow")
        self.cardOrdersTrendRow.setContentsMargins(-1, 10, -1, -1)
        self.lblOrdersTrend = QLabel(self.cardOrders)
        self.lblOrdersTrend.setObjectName(u"lblOrdersTrend")

        self.cardOrdersTrendRow.addWidget(self.lblOrdersTrend)

        self.cardOrdersTrendSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardOrdersTrendRow.addItem(self.cardOrdersTrendSpacer)


        self.cardOrdersLayout.addLayout(self.cardOrdersTrendRow)


        self.cardsLayout.addWidget(self.cardOrders)

        self.cardAov = QFrame(Analytics)
        self.cardAov.setObjectName(u"cardAov")
        self.cardAov.setMinimumSize(QSize(0, 120))
        self.cardAov.setFrameShape(QFrame.Shape.NoFrame)
        self.cardAovLayout = QVBoxLayout(self.cardAov)
        self.cardAovLayout.setSpacing(6)
        self.cardAovLayout.setObjectName(u"cardAovLayout")
        self.cardAovLayout.setContentsMargins(16, 14, 16, 14)
        self.cardAovTopRow = QHBoxLayout()
        self.cardAovTopRow.setObjectName(u"cardAovTopRow")
        self.lblAovCaption = QLabel(self.cardAov)
        self.lblAovCaption.setObjectName(u"lblAovCaption")

        self.cardAovTopRow.addWidget(self.lblAovCaption)

        self.cardAovSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardAovTopRow.addItem(self.cardAovSpacer)

        self.badgeAov = QLabel(self.cardAov)
        self.badgeAov.setObjectName(u"badgeAov")
        self.badgeAov.setMinimumSize(QSize(32, 32))
        self.badgeAov.setMaximumSize(QSize(32, 32))
        self.badgeAov.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardAovTopRow.addWidget(self.badgeAov)


        self.cardAovLayout.addLayout(self.cardAovTopRow)

        self.lblAovVal = QLabel(self.cardAov)
        self.lblAovVal.setObjectName(u"lblAovVal")
        self.lblAovVal.setMinimumSize(QSize(0, 25))
        self.lblAovVal.setMaximumSize(QSize(16777215, 25))

        self.cardAovLayout.addWidget(self.lblAovVal)

        self.cardAovTrendRow = QHBoxLayout()
        self.cardAovTrendRow.setObjectName(u"cardAovTrendRow")
        self.cardAovTrendRow.setContentsMargins(-1, 10, -1, -1)
        self.lblAovTrend = QLabel(self.cardAov)
        self.lblAovTrend.setObjectName(u"lblAovTrend")

        self.cardAovTrendRow.addWidget(self.lblAovTrend)

        self.cardAovTrendSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardAovTrendRow.addItem(self.cardAovTrendSpacer)


        self.cardAovLayout.addLayout(self.cardAovTrendRow)


        self.cardsLayout.addWidget(self.cardAov)

        self.cardReturn = QFrame(Analytics)
        self.cardReturn.setObjectName(u"cardReturn")
        self.cardReturn.setMinimumSize(QSize(0, 120))
        self.cardReturn.setFrameShape(QFrame.Shape.NoFrame)
        self.cardReturnLayout = QVBoxLayout(self.cardReturn)
        self.cardReturnLayout.setSpacing(6)
        self.cardReturnLayout.setObjectName(u"cardReturnLayout")
        self.cardReturnLayout.setContentsMargins(16, 14, 16, 14)
        self.cardReturnTopRow = QHBoxLayout()
        self.cardReturnTopRow.setObjectName(u"cardReturnTopRow")
        self.lblReturnCaption = QLabel(self.cardReturn)
        self.lblReturnCaption.setObjectName(u"lblReturnCaption")

        self.cardReturnTopRow.addWidget(self.lblReturnCaption)

        self.cardReturnSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardReturnTopRow.addItem(self.cardReturnSpacer)

        self.badgeReturn = QLabel(self.cardReturn)
        self.badgeReturn.setObjectName(u"badgeReturn")
        self.badgeReturn.setMinimumSize(QSize(32, 32))
        self.badgeReturn.setMaximumSize(QSize(32, 32))
        self.badgeReturn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardReturnTopRow.addWidget(self.badgeReturn)


        self.cardReturnLayout.addLayout(self.cardReturnTopRow)

        self.lblReturnVal = QLabel(self.cardReturn)
        self.lblReturnVal.setObjectName(u"lblReturnVal")
        self.lblReturnVal.setMinimumSize(QSize(0, 25))
        self.lblReturnVal.setMaximumSize(QSize(16777215, 25))

        self.cardReturnLayout.addWidget(self.lblReturnVal)

        self.cardReturnTrendRow = QHBoxLayout()
        self.cardReturnTrendRow.setObjectName(u"cardReturnTrendRow")
        self.cardReturnTrendRow.setContentsMargins(-1, 10, -1, -1)
        self.lblReturnTrend = QLabel(self.cardReturn)
        self.lblReturnTrend.setObjectName(u"lblReturnTrend")

        self.cardReturnTrendRow.addWidget(self.lblReturnTrend)

        self.cardReturnTrendSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardReturnTrendRow.addItem(self.cardReturnTrendSpacer)


        self.cardReturnLayout.addLayout(self.cardReturnTrendRow)


        self.cardsLayout.addWidget(self.cardReturn)


        self.rootLayout.addLayout(self.cardsLayout)

        self.middleLayout = QHBoxLayout()
        self.middleLayout.setSpacing(16)
        self.middleLayout.setObjectName(u"middleLayout")
        self.cardTimeChart = QFrame(Analytics)
        self.cardTimeChart.setObjectName(u"cardTimeChart")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardTimeChart.sizePolicy().hasHeightForWidth())
        self.cardTimeChart.setSizePolicy(sizePolicy)
        self.cardTimeChart.setMinimumSize(QSize(0, 280))
        self.cardTimeChart.setFrameShape(QFrame.Shape.NoFrame)
        self.timeChartLayout = QVBoxLayout(self.cardTimeChart)
        self.timeChartLayout.setSpacing(8)
        self.timeChartLayout.setObjectName(u"timeChartLayout")
        self.timeChartLayout.setContentsMargins(18, 16, 18, 16)
        self.lblTimeChartTitle = QLabel(self.cardTimeChart)
        self.lblTimeChartTitle.setObjectName(u"lblTimeChartTitle")

        self.timeChartLayout.addWidget(self.lblTimeChartTitle)

        self.containerTimeChart = QWidget(self.cardTimeChart)
        self.containerTimeChart.setObjectName(u"containerTimeChart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.containerTimeChart.sizePolicy().hasHeightForWidth())
        self.containerTimeChart.setSizePolicy(sizePolicy1)

        self.timeChartLayout.addWidget(self.containerTimeChart)


        self.middleLayout.addWidget(self.cardTimeChart)

        self.cardCategory = QFrame(Analytics)
        self.cardCategory.setObjectName(u"cardCategory")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cardCategory.sizePolicy().hasHeightForWidth())
        self.cardCategory.setSizePolicy(sizePolicy2)
        self.cardCategory.setMinimumSize(QSize(280, 280))
        self.cardCategory.setFrameShape(QFrame.Shape.NoFrame)
        self.categoryCardLayout = QVBoxLayout(self.cardCategory)
        self.categoryCardLayout.setSpacing(8)
        self.categoryCardLayout.setObjectName(u"categoryCardLayout")
        self.categoryCardLayout.setContentsMargins(18, 16, 18, 16)
        self.lblCategoryTitle = QLabel(self.cardCategory)
        self.lblCategoryTitle.setObjectName(u"lblCategoryTitle")
        self.lblCategoryTitle.setMinimumSize(QSize(0, 12))
        self.lblCategoryTitle.setMaximumSize(QSize(16777215, 25))

        self.categoryCardLayout.addWidget(self.lblCategoryTitle)

        self.lblCategorySub = QLabel(self.cardCategory)
        self.lblCategorySub.setObjectName(u"lblCategorySub")
        self.lblCategorySub.setMinimumSize(QSize(0, 5))
        self.lblCategorySub.setMaximumSize(QSize(16777215, 12))

        self.categoryCardLayout.addWidget(self.lblCategorySub)

        self.scrollCategory = QScrollArea(self.cardCategory)
        self.scrollCategory.setObjectName(u"scrollCategory")
        sizePolicy1.setHeightForWidth(self.scrollCategory.sizePolicy().hasHeightForWidth())
        self.scrollCategory.setSizePolicy(sizePolicy1)
        self.scrollCategory.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollCategory.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollCategory.setWidgetResizable(True)
        self.scrollCategoryContent = QWidget()
        self.scrollCategoryContent.setObjectName(u"scrollCategoryContent")
        self.scrollCategoryContent.setGeometry(QRect(0, 0, 280, 200))
        self.containerCategoryList = QVBoxLayout(self.scrollCategoryContent)
        self.containerCategoryList.setSpacing(10)
        self.containerCategoryList.setObjectName(u"containerCategoryList")
        self.containerCategoryList.setContentsMargins(0, 0, 6, 0)
        self.categorySpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.containerCategoryList.addItem(self.categorySpacer)

        self.scrollCategory.setWidget(self.scrollCategoryContent)

        self.categoryCardLayout.addWidget(self.scrollCategory)


        self.middleLayout.addWidget(self.cardCategory)


        self.rootLayout.addLayout(self.middleLayout)

        self.cardTopProducts = QFrame(Analytics)
        self.cardTopProducts.setObjectName(u"cardTopProducts")
        self.cardTopProducts.setFrameShape(QFrame.Shape.NoFrame)
        self.topProductsLayout = QVBoxLayout(self.cardTopProducts)
        self.topProductsLayout.setSpacing(8)
        self.topProductsLayout.setObjectName(u"topProductsLayout")
        self.topProductsLayout.setContentsMargins(18, 16, 18, 16)
        self.topProductsHeaderRow = QHBoxLayout()
        self.topProductsHeaderRow.setObjectName(u"topProductsHeaderRow")
        self.lblTopProductsTitle = QLabel(self.cardTopProducts)
        self.lblTopProductsTitle.setObjectName(u"lblTopProductsTitle")

        self.topProductsHeaderRow.addWidget(self.lblTopProductsTitle)

        self.topProductsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topProductsHeaderRow.addItem(self.topProductsSpacer)

        self.btnDetailLink = QPushButton(self.cardTopProducts)
        self.btnDetailLink.setObjectName(u"btnDetailLink")
        self.btnDetailLink.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.topProductsHeaderRow.addWidget(self.btnDetailLink)


        self.topProductsLayout.addLayout(self.topProductsHeaderRow)

        self.tblTopProducts = QTableWidget(self.cardTopProducts)
        if (self.tblTopProducts.columnCount() < 4):
            self.tblTopProducts.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblTopProducts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblTopProducts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblTopProducts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblTopProducts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblTopProducts.setObjectName(u"tblTopProducts")
        self.tblTopProducts.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tblTopProducts.setFrameShape(QFrame.Shape.NoFrame)
        self.tblTopProducts.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblTopProducts.setAlternatingRowColors(False)
        self.tblTopProducts.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tblTopProducts.setShowGrid(False)
        self.tblTopProducts.horizontalHeader().setMinimumSectionSize(52)
        self.tblTopProducts.horizontalHeader().setDefaultSectionSize(130)
        self.tblTopProducts.horizontalHeader().setHighlightSections(False)
        self.tblTopProducts.horizontalHeader().setStretchLastSection(True)
        self.tblTopProducts.verticalHeader().setVisible(False)
        self.tblTopProducts.verticalHeader().setMinimumSectionSize(42)
        self.tblTopProducts.verticalHeader().setDefaultSectionSize(42)

        self.topProductsLayout.addWidget(self.tblTopProducts)


        self.rootLayout.addWidget(self.cardTopProducts)


        self.retranslateUi(Analytics)

        QMetaObject.connectSlotsByName(Analytics)
    # setupUi

    def retranslateUi(self, Analytics):
        self.lblTitle.setText(QCoreApplication.translate("Analytics", u"Ph\u00e2n t\u00edch B\u00e1n h\u00e0ng", None))
        self.lblSubtitle.setText(QCoreApplication.translate("Analytics", u"T\u1ed5ng quan hi\u1ec7u su\u1ea5t kinh doanh v\u00e0 xu h\u01b0\u1edbng.", None))
        self.btnPeriodToday.setText(QCoreApplication.translate("Analytics", u"H\u00f4m nay", None))
        self.btnPeriodWeek.setText(QCoreApplication.translate("Analytics", u"Tu\u1ea7n n\u00e0y", None))
        self.btnPeriodMonth.setText(QCoreApplication.translate("Analytics", u"Th\u00e1ng n\u00e0y", None))
        self.lblRevenueCaption.setText(QCoreApplication.translate("Analytics", u"Doanh thu", None))
        self.badgeRevenue.setText("")
        self.lblRevenueVal.setText(QCoreApplication.translate("Analytics", u"0", None))
        self.lblRevenueTrend.setText("")
        self.lblOrdersCaption.setText(QCoreApplication.translate("Analytics", u"S\u1ed1 \u0111\u01a1n h\u00e0ng", None))
        self.badgeOrders.setText("")
        self.lblOrdersVal.setText(QCoreApplication.translate("Analytics", u"0", None))
        self.lblOrdersTrend.setText("")
        self.lblAovCaption.setText(QCoreApplication.translate("Analytics", u"Gi\u00e1 tr\u1ecb \u0111\u01a1n TB", None))
        self.badgeAov.setText("")
        self.lblAovVal.setText(QCoreApplication.translate("Analytics", u"0", None))
        self.lblAovTrend.setText("")
        self.lblReturnCaption.setText(QCoreApplication.translate("Analytics", u"Kh\u00e1ch quay l\u1ea1i", None))
        self.badgeReturn.setText("")
        self.lblReturnVal.setText(QCoreApplication.translate("Analytics", u"0", None))
        self.lblReturnTrend.setText("")
        self.lblTimeChartTitle.setText(QCoreApplication.translate("Analytics", u"Doanh thu theo th\u1eddi gian", None))
        self.lblCategoryTitle.setText(QCoreApplication.translate("Analytics", u"Ph\u00e2n b\u1ed5 theo danh m\u1ee5c", None))
        self.lblCategorySub.setText(QCoreApplication.translate("Analytics", u"T\u1ef7 tr\u1ecdng doanh thu theo nh\u00f3m h\u00e0ng", None))
        self.lblTopProductsTitle.setText(QCoreApplication.translate("Analytics", u"Top s\u1ea3n ph\u1ea9m b\u00e1n ch\u1ea1y", None))
        self.btnDetailLink.setText(QCoreApplication.translate("Analytics", u"L\u00e0m m\u1edbi d\u1eef li\u1ec7u", None))
        ___qtablewidgetitem = self.tblTopProducts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Analytics", u"STT", None))
        ___qtablewidgetitem1 = self.tblTopProducts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Analytics", u"S\u1ea2N PH\u1ea8M", None))
        ___qtablewidgetitem2 = self.tblTopProducts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Analytics", u"S\u1ed0 L\u01af\u1ee2NG", None))
        ___qtablewidgetitem3 = self.tblTopProducts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Analytics", u"DOANH THU", None))
        pass
    # retranslateUi

