# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_management.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_CustomerManagement(object):
    def setupUi(self, CustomerManagement):
        if not CustomerManagement.objectName():
            CustomerManagement.setObjectName(u"CustomerManagement")
        CustomerManagement.resize(1280, 860)
        CustomerManagement.setStyleSheet(u"QWidget#CustomerManagement {\n"
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
"QLabel[badge=\"bronze\"] {\n"
"    background-color: #f6e5d5;\n"
"    color: #a1622c;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"gold\"] {\n"
"    background-color: "
                        "#fef9c3;\n"
"    color: #a16207;\n"
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
"QLabel[state=\"warning\"]"
                        " {\n"
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
"QScrollBar::"
                        "down-arrow:vertical {\n"
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
""
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
"QLab"
                        "el#lblSubtitle {\n"
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
"QPushButton#btnDelete:dis"
                        "abled {\n"
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
"    max-width: 34px;\n"
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
"    bo"
                        "rder-radius: 8px;\n"
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
"QPushButton#"
                        "btnPrevPage,\n"
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
"QPushButton#btnNextPage:hover {\n"
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
"QLabel#lblTotalCaption,\n"
"QLabel#lblActiveCaption,\n"
"QLabel#lblPointsCaption {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#lblTotalVal,\n"
"QLabel#lblActiveVal,\n"
"QLabel#lblPointsVal {\n"
"    color: #0f172a;\n"
"    font-size: 27px;\n"
"    font-weight: 700;\n"
""
                        "}\n"
"\n"
"QLabel#badgeTotal,\n"
"QLabel#badgeActive,\n"
"QLabel#badgePoints {\n"
"    background-color: #eff6ff;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLabel#lblTotalTrend,\n"
"QLabel#lblActiveTrend,\n"
"QLabel#lblPointsTrend {\n"
"    background-color: transparent;\n"
"    color: #64748b;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"    padding: 2px 0px;\n"
"}\n"
"\n"
"QLabel#lblTotalTrend[trend=\"up\"],\n"
"QLabel#lblActiveTrend[trend=\"up\"],\n"
"QLabel#lblPointsTrend[trend=\"up\"] {\n"
"    background-color: #ecfdf5;\n"
"    color: #059669;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QLabel#lblTotalTrend[trend=\"down\"],\n"
"QLabel#lblActiveTrend[trend=\"down\"],\n"
"QLabel#lblPointsTrend[trend=\"down\"] {\n"
"    background-color: #fef2f2;\n"
"    color: #dc2626;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QLabel#lblTotalTrend[trend=\"flat\"],\n"
"QLabel#lblActiveTrend[trend=\"flat\"],\n"
"QLabel#lblPointsTrend[trend=\"flat\"] {\n"
"    bac"
                        "kground-color: #f1f5f9;\n"
"    color: #64748b;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QFrame#cardTotal,\n"
"QFrame#cardActive,\n"
"QFrame#cardPoints,\n"
"QFrame#cardTableContainer {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"QLabel#badgeActive {\n"
"    background-color: #d1fae5;\n"
"}\n"
"QLabel#badgePoints {\n"
"    background-color: #ffedd5;\n"
"}\n"
"QPushButton#btnAddCustomer {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnAddCustomer:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnAddCustomer:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnAddCustomer:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"QPushButton#btnDeleteCustomer {\n"
"    background"
                        "-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnDeleteCustomer:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"    color: #dc2626;\n"
"}\n"
"QPushButton#btnDeleteCustomer:pressed {\n"
"    background-color: #fee2e2;\n"
"    border: 1px solid #dc2626;\n"
"    color: #dc2626;\n"
"}\n"
"QPushButton#btnDeleteCustomer:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"QPushButton#btnFilter {\n"
"    padding: 0px;\n"
"    min-width: 38px;\n"
"    max-width: 38px;\n"
"}\n"
"QPushButton#btnLoadMore {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"}\n"
"QPushButton#btnLoadMore:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px "
                        "solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnLoadMore:pressed {\n"
"    background-color: #dbeafe;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"")
        self.rootLayout = QVBoxLayout(CustomerManagement)
        self.rootLayout.setSpacing(16)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(12, 10, 12, 12)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(0)
        self.titleLayout.setObjectName(u"titleLayout")
        self.lblTitle = QLabel(CustomerManagement)
        self.lblTitle.setObjectName(u"lblTitle")

        self.titleLayout.addWidget(self.lblTitle)

        self.lblSubtitle = QLabel(CustomerManagement)
        self.lblSubtitle.setObjectName(u"lblSubtitle")

        self.titleLayout.addWidget(self.lblSubtitle)


        self.headerLayout.addLayout(self.titleLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.btnPurchaseHistory = QPushButton(CustomerManagement)
        self.btnPurchaseHistory.setObjectName(u"btnPurchaseHistory")
        self.btnPurchaseHistory.setMinimumSize(QSize(190, 40))
        self.btnPurchaseHistory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.headerLayout.addWidget(self.btnPurchaseHistory)

        self.btnAddCustomer = QPushButton(CustomerManagement)
        self.btnAddCustomer.setObjectName(u"btnAddCustomer")
        self.btnAddCustomer.setMinimumSize(QSize(180, 38))
        self.btnAddCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.headerLayout.addWidget(self.btnAddCustomer)


        self.rootLayout.addLayout(self.headerLayout)

        self.cardsLayout = QHBoxLayout()
        self.cardsLayout.setSpacing(16)
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.cardTotal = QFrame(CustomerManagement)
        self.cardTotal.setObjectName(u"cardTotal")
        self.cardTotal.setMinimumSize(QSize(0, 120))
        self.cardTotal.setFrameShape(QFrame.Shape.NoFrame)
        self.cardTotalLayout = QVBoxLayout(self.cardTotal)
        self.cardTotalLayout.setSpacing(0)
        self.cardTotalLayout.setObjectName(u"cardTotalLayout")
        self.cardTotalLayout.setContentsMargins(16, 14, 16, 14)
        self.cardTotalTopRow = QHBoxLayout()
        self.cardTotalTopRow.setSpacing(6)
        self.cardTotalTopRow.setObjectName(u"cardTotalTopRow")
        self.lblTotalCaption = QLabel(self.cardTotal)
        self.lblTotalCaption.setObjectName(u"lblTotalCaption")

        self.cardTotalTopRow.addWidget(self.lblTotalCaption)

        self.cardTotalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardTotalTopRow.addItem(self.cardTotalSpacer)

        self.badgeTotal = QLabel(self.cardTotal)
        self.badgeTotal.setObjectName(u"badgeTotal")
        self.badgeTotal.setMinimumSize(QSize(32, 32))
        self.badgeTotal.setMaximumSize(QSize(32, 32))
        self.badgeTotal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardTotalTopRow.addWidget(self.badgeTotal)


        self.cardTotalLayout.addLayout(self.cardTotalTopRow)

        self.lblTotalVal = QLabel(self.cardTotal)
        self.lblTotalVal.setObjectName(u"lblTotalVal")

        self.cardTotalLayout.addWidget(self.lblTotalVal)

        self.cardTotalTrendRow = QHBoxLayout()
        self.cardTotalTrendRow.setObjectName(u"cardTotalTrendRow")
        self.cardTotalTrendRow.setContentsMargins(-1, 10, -1, -1)
        self.lblTotalTrend = QLabel(self.cardTotal)
        self.lblTotalTrend.setObjectName(u"lblTotalTrend")

        self.cardTotalTrendRow.addWidget(self.lblTotalTrend)

        self.cardTotalTrendSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardTotalTrendRow.addItem(self.cardTotalTrendSpacer)


        self.cardTotalLayout.addLayout(self.cardTotalTrendRow)


        self.cardsLayout.addWidget(self.cardTotal)

        self.cardActive = QFrame(CustomerManagement)
        self.cardActive.setObjectName(u"cardActive")
        self.cardActive.setMinimumSize(QSize(0, 120))
        self.cardActive.setFrameShape(QFrame.Shape.NoFrame)
        self.cardActiveLayout = QVBoxLayout(self.cardActive)
        self.cardActiveLayout.setSpacing(0)
        self.cardActiveLayout.setObjectName(u"cardActiveLayout")
        self.cardActiveLayout.setContentsMargins(16, 14, 16, 14)
        self.cardActiveTopRow = QHBoxLayout()
        self.cardActiveTopRow.setObjectName(u"cardActiveTopRow")
        self.lblActiveCaption = QLabel(self.cardActive)
        self.lblActiveCaption.setObjectName(u"lblActiveCaption")

        self.cardActiveTopRow.addWidget(self.lblActiveCaption)

        self.cardActiveSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardActiveTopRow.addItem(self.cardActiveSpacer)

        self.badgeActive = QLabel(self.cardActive)
        self.badgeActive.setObjectName(u"badgeActive")
        self.badgeActive.setMinimumSize(QSize(32, 32))
        self.badgeActive.setMaximumSize(QSize(32, 32))
        self.badgeActive.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardActiveTopRow.addWidget(self.badgeActive)


        self.cardActiveLayout.addLayout(self.cardActiveTopRow)

        self.lblActiveVal = QLabel(self.cardActive)
        self.lblActiveVal.setObjectName(u"lblActiveVal")

        self.cardActiveLayout.addWidget(self.lblActiveVal)

        self.cardActiveTrendRow = QHBoxLayout()
        self.cardActiveTrendRow.setObjectName(u"cardActiveTrendRow")
        self.cardActiveTrendRow.setContentsMargins(-1, 10, -1, -1)
        self.lblActiveTrend = QLabel(self.cardActive)
        self.lblActiveTrend.setObjectName(u"lblActiveTrend")

        self.cardActiveTrendRow.addWidget(self.lblActiveTrend)

        self.cardActiveTrendSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardActiveTrendRow.addItem(self.cardActiveTrendSpacer)


        self.cardActiveLayout.addLayout(self.cardActiveTrendRow)


        self.cardsLayout.addWidget(self.cardActive)

        self.cardPoints = QFrame(CustomerManagement)
        self.cardPoints.setObjectName(u"cardPoints")
        self.cardPoints.setMinimumSize(QSize(0, 120))
        self.cardPoints.setFrameShape(QFrame.Shape.NoFrame)
        self.cardPointsLayout = QVBoxLayout(self.cardPoints)
        self.cardPointsLayout.setSpacing(0)
        self.cardPointsLayout.setObjectName(u"cardPointsLayout")
        self.cardPointsLayout.setContentsMargins(16, 14, 16, 14)
        self.cardPointsTopRow = QHBoxLayout()
        self.cardPointsTopRow.setObjectName(u"cardPointsTopRow")
        self.lblPointsCaption = QLabel(self.cardPoints)
        self.lblPointsCaption.setObjectName(u"lblPointsCaption")

        self.cardPointsTopRow.addWidget(self.lblPointsCaption)

        self.cardPointsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardPointsTopRow.addItem(self.cardPointsSpacer)

        self.badgePoints = QLabel(self.cardPoints)
        self.badgePoints.setObjectName(u"badgePoints")
        self.badgePoints.setMinimumSize(QSize(32, 32))
        self.badgePoints.setMaximumSize(QSize(32, 32))
        self.badgePoints.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardPointsTopRow.addWidget(self.badgePoints)


        self.cardPointsLayout.addLayout(self.cardPointsTopRow)

        self.lblPointsVal = QLabel(self.cardPoints)
        self.lblPointsVal.setObjectName(u"lblPointsVal")

        self.cardPointsLayout.addWidget(self.lblPointsVal)

        self.cardPointsTrendRow = QHBoxLayout()
        self.cardPointsTrendRow.setObjectName(u"cardPointsTrendRow")
        self.cardPointsTrendRow.setContentsMargins(-1, 10, -1, -1)
        self.lblPointsTrend = QLabel(self.cardPoints)
        self.lblPointsTrend.setObjectName(u"lblPointsTrend")

        self.cardPointsTrendRow.addWidget(self.lblPointsTrend)

        self.cardPointsTrendSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cardPointsTrendRow.addItem(self.cardPointsTrendSpacer)


        self.cardPointsLayout.addLayout(self.cardPointsTrendRow)


        self.cardsLayout.addWidget(self.cardPoints)


        self.rootLayout.addLayout(self.cardsLayout)

        self.cardTableContainer = QFrame(CustomerManagement)
        self.cardTableContainer.setObjectName(u"cardTableContainer")
        self.cardTableContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.tableContainerLayout = QVBoxLayout(self.cardTableContainer)
        self.tableContainerLayout.setSpacing(12)
        self.tableContainerLayout.setObjectName(u"tableContainerLayout")
        self.tableContainerLayout.setContentsMargins(12, 12, 12, 12)
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setSpacing(8)
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.txtSearch = QLineEdit(self.cardTableContainer)
        self.txtSearch.setObjectName(u"txtSearch")
        self.txtSearch.setMinimumSize(QSize(240, 40))
        self.txtSearch.setClearButtonEnabled(True)

        self.toolbarLayout.addWidget(self.txtSearch)

        self.btnFilter = QPushButton(self.cardTableContainer)
        self.btnFilter.setObjectName(u"btnFilter")
        self.btnFilter.setMinimumSize(QSize(40, 40))
        self.btnFilter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btnFilter)

        self.btnEditCustomer = QPushButton(self.cardTableContainer)
        self.btnEditCustomer.setObjectName(u"btnEditCustomer")
        self.btnEditCustomer.setMinimumSize(QSize(85, 40))
        self.btnEditCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btnEditCustomer)

        self.btnDeleteCustomer = QPushButton(self.cardTableContainer)
        self.btnDeleteCustomer.setObjectName(u"btnDeleteCustomer")
        self.btnDeleteCustomer.setMinimumSize(QSize(85, 40))
        self.btnDeleteCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btnDeleteCustomer)


        self.tableContainerLayout.addLayout(self.toolbarLayout)

        self.tblCustomers = QTableWidget(self.cardTableContainer)
        if (self.tblCustomers.columnCount() < 6):
            self.tblCustomers.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCustomers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCustomers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblCustomers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblCustomers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblCustomers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblCustomers.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblCustomers.setObjectName(u"tblCustomers")
        self.tblCustomers.setAutoFillBackground(False)
        self.tblCustomers.setFrameShape(QFrame.Shape.NoFrame)
        self.tblCustomers.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblCustomers.setAlternatingRowColors(False)
        self.tblCustomers.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblCustomers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblCustomers.setShowGrid(False)
        self.tblCustomers.horizontalHeader().setMinimumSectionSize(90)
        self.tblCustomers.horizontalHeader().setDefaultSectionSize(130)
        self.tblCustomers.horizontalHeader().setHighlightSections(False)
        self.tblCustomers.horizontalHeader().setStretchLastSection(True)
        self.tblCustomers.verticalHeader().setVisible(False)
        self.tblCustomers.verticalHeader().setMinimumSectionSize(46)
        self.tblCustomers.verticalHeader().setDefaultSectionSize(46)

        self.tableContainerLayout.addWidget(self.tblCustomers)

        self.framePagination = QFrame(self.cardTableContainer)
        self.framePagination.setObjectName(u"framePagination")
        self.framePagination.setFrameShape(QFrame.Shape.NoFrame)
        self.paginationLayout = QHBoxLayout(self.framePagination)
        self.paginationLayout.setSpacing(6)
        self.paginationLayout.setObjectName(u"paginationLayout")
        self.paginationLayout.setContentsMargins(0, 0, 0, 0)
        self.lblPaginationInfo = QLabel(self.framePagination)
        self.lblPaginationInfo.setObjectName(u"lblPaginationInfo")

        self.paginationLayout.addWidget(self.lblPaginationInfo)

        self.paginationSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.paginationLayout.addItem(self.paginationSpacer)

        self.btnLoadMore = QPushButton(self.framePagination)
        self.btnLoadMore.setObjectName(u"btnLoadMore")
        self.btnLoadMore.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.paginationLayout.addWidget(self.btnLoadMore)

        self.btnPrevPage = QPushButton(self.framePagination)
        self.btnPrevPage.setObjectName(u"btnPrevPage")
        self.btnPrevPage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrevPage.setProperty(u"iconPx", 12)

        self.paginationLayout.addWidget(self.btnPrevPage)

        self.btnNextPage = QPushButton(self.framePagination)
        self.btnNextPage.setObjectName(u"btnNextPage")
        self.btnNextPage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNextPage.setProperty(u"iconPx", 12)

        self.paginationLayout.addWidget(self.btnNextPage)


        self.tableContainerLayout.addWidget(self.framePagination)


        self.rootLayout.addWidget(self.cardTableContainer)


        self.retranslateUi(CustomerManagement)

        QMetaObject.connectSlotsByName(CustomerManagement)
    # setupUi

    def retranslateUi(self, CustomerManagement):
        self.lblTitle.setText(QCoreApplication.translate("CustomerManagement", u"Qu\u1ea3n l\u00fd Kh\u00e1ch h\u00e0ng", None))
        self.lblSubtitle.setText(QCoreApplication.translate("CustomerManagement", u"Qu\u1ea3n l\u00fd th\u00f4ng tin li\u00ean l\u1ea1c, l\u1ecbch s\u1eed mua h\u00e0ng v\u00e0 c\u1ea5p \u0111\u1ed9 th\u00e0nh vi\u00ean.", None))
        self.btnPurchaseHistory.setText(QCoreApplication.translate("CustomerManagement", u"  Xem l\u1ecbch s\u1eed mua h\u00e0ng", None))
        self.btnAddCustomer.setText(QCoreApplication.translate("CustomerManagement", u"+ Th\u00eam kh\u00e1ch m\u1edbi", None))
        self.lblTotalCaption.setText(QCoreApplication.translate("CustomerManagement", u"T\u1ed5ng kh\u00e1ch h\u00e0ng", None))
        self.badgeTotal.setText("")
        self.lblTotalVal.setText(QCoreApplication.translate("CustomerManagement", u"0", None))
        self.lblTotalTrend.setText("")
        self.lblActiveCaption.setText(QCoreApplication.translate("CustomerManagement", u"Kh\u00e1ch h\u00e0ng ho\u1ea1t \u0111\u1ed9ng", None))
        self.badgeActive.setText("")
        self.lblActiveVal.setText(QCoreApplication.translate("CustomerManagement", u"0", None))
        self.lblActiveTrend.setText("")
        self.lblPointsCaption.setText(QCoreApplication.translate("CustomerManagement", u"T\u1ed5ng \u0111i\u1ec3m t\u00edch l\u0169y", None))
        self.badgePoints.setText("")
        self.lblPointsVal.setText(QCoreApplication.translate("CustomerManagement", u"0", None))
        self.lblPointsTrend.setText("")
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("CustomerManagement", u"T\u00ecm ki\u1ebfm theo t\u00ean kh\u00e1ch h\u00e0ng ho\u1eb7c s\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.btnFilter.setText("")
        self.btnEditCustomer.setText(QCoreApplication.translate("CustomerManagement", u"  S\u1eeda", None))
        self.btnDeleteCustomer.setText(QCoreApplication.translate("CustomerManagement", u"  X\u00f3a", None))
        ___qtablewidgetitem = self.tblCustomers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CustomerManagement", u"S\u1ed0 \u0110I\u1ec6N THO\u1ea0I", None))
        ___qtablewidgetitem1 = self.tblCustomers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CustomerManagement", u"T\u00caN KH\u00c1CH H\u00c0NG", None))
        ___qtablewidgetitem2 = self.tblCustomers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CustomerManagement", u"NG\u00c0Y SINH", None))
        ___qtablewidgetitem3 = self.tblCustomers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CustomerManagement", u"T\u1ed4NG \u0110I\u1ec2M", None))
        ___qtablewidgetitem4 = self.tblCustomers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CustomerManagement", u"H\u1ea0NG", None))
        ___qtablewidgetitem5 = self.tblCustomers.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CustomerManagement", u"T\u1ed4NG CHI TI\u00caU", None))
        self.lblPaginationInfo.setText(QCoreApplication.translate("CustomerManagement", u"Hi\u1ec3n th\u1ecb 0 c\u1ee7a 0 kh\u00e1ch h\u00e0ng", None))
        self.btnLoadMore.setText(QCoreApplication.translate("CustomerManagement", u"T\u1ea3i th\u00eam d\u1eef li\u1ec7u", None))
        self.btnPrevPage.setText("")
        self.btnPrevPage.setProperty(u"iconName", QCoreApplication.translate("CustomerManagement", u"previous", None))
        self.btnPrevPage.setProperty(u"iconColor", QCoreApplication.translate("CustomerManagement", u"default", None))
        self.btnNextPage.setText("")
        self.btnNextPage.setProperty(u"iconName", QCoreApplication.translate("CustomerManagement", u"next", None))
        self.btnNextPage.setProperty(u"iconColor", QCoreApplication.translate("CustomerManagement", u"default", None))
        pass
    # retranslateUi

