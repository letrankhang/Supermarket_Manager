# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pos.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 860)
        Form.setStyleSheet(u"QWidget#Form {\n"
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
"QDateEdit:hover,\n"
"Q"
                        "SpinBox:hover,\n"
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
"    padding: "
                        "4px;\n"
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
"    image: url(asse"
                        "ts/images/chevron-up.png);\n"
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
"    font-weight: bold"
                        ";\n"
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
"    border-bottom: 1px solid #f1f5f"
                        "9;\n"
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
"    background-colo"
                        "r: #ffedd5;\n"
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
"    c"
                        "olor: #dc2626;\n"
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
"    backgrou"
                        "nd-color: transparent;\n"
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
"   "
                        " background-color: #cbd5e1;\n"
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
"    font-size:"
                        " 13px;\n"
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
"QFrame#frame_topbar,\n"
"QFrame#frame_filters,\n"
"QFrame#frame_shortcuts,\n"
"QFrame#frame_summary,\n"
"QFrame#frame_order_header,\n"
"QFrame#frame_search_row,\n"
"QFrame#frame_categories,\n"
"QFrame#frame_payment_methods,\n"
"QFrame#frame_checkout {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame#frame_topbar,\n"
"QFrame#frame_filters {\n"
"    background-color: #ffffff;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"QFrame#frame_shortcuts,\n"
"QFrame#frame_summary {\n"
"    background-color: #ffffff;\n"
"    border-top: 1px solid #e2e8f0;\n"
"}\n"
"QFrame#frame_order {\n"
"    background-color: #ffffff;\n"
"    border-left: 1px solid #e2e8f0;\n"
"}\n"
"QFrame#frame_order_header {\n"
"    background-color: #ffffff;\n"
"    border-bottom: 1px solid #"
                        "e2e8f0;\n"
"}\n"
"\n"
"QLabel#lblScanCaption {\n"
"    color: #0f172a;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QLabel#lblScanSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QLabel#lblCashierName,\n"
"QLabel#lblCartEmpty,\n"
"QLabel#lblSubTotalCaption,\n"
"QLabel#lblTaxCaption,\n"
"QLabel#lblCartItemUnitPrice,\n"
"QLabel#lblGrandTotalCaption {\n"
"    color: #64748b;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton#CategoryChip {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 16px;\n"
"    padding: 4px 16px;\n"
"    min-height: 30px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#CategoryChip:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#CategoryChip:checked {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"QPushB"
                        "utton#btnCardAdd {\n"
"     padding-bottom: 3px;\n"
"	 font-size: 18px;\n"
"     font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnClearCart {\n"
"    background-color: #ffffff;\n"
"    color: #dc2626;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnClearCart:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"}\n"
"QPushButton#btnClearCart:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QPushButton#btnEditDiscount {\n"
"    background-color: transparent;\n"
"    color: #1d4ed8;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    min-height: 0px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnEditDiscount:hover {\n"
"    color: #1e3a8a;\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton#btnEditDiscount:pressed {\n"
"    color: #1e40"
                        "af;\n"
"}\n"
"QPushButton#btnEditDiscount:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #94a3b8;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton#btnCheckout {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnCheckout:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnCheckout:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnCheckout:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"\n"
"QPushButton#btnPayCash,\n"
"QPushButton#btnPayCard,\n"
"QPushButton#btnPayTransfer {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 34px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPush"
                        "Button#btnPayCash:hover,\n"
"QPushButton#btnPayCard:hover,\n"
"QPushButton#btnPayTransfer:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnPayCash:checked,\n"
"QPushButton#btnPayCard:checked,\n"
"QPushButton#btnPayTransfer:checked {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QFrame#ProductCard {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame#ProductCard:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QFrame#CartRow {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    border-bottom: 1px solid #f1f5f9;\n"
"}\n"
"QLabel#lblCardThumbnail {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    color: #64748b;\n"
"}\n"
"QLabel#lblCardName,\n"
"QLabel#lblCartItemName,\n"
"QLabel#lblCartItemTotal {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel#lblCard"
                        "Barcode {\n"
"    color: #64748b;\n"
"    font-size: 11px;\n"
"}\n"
"QLabel#lblCardPrice {\n"
"    color: #1d4ed8;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel#lblCustomerBadge {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border-radius: 12px;\n"
"    padding: 4px 12px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel#lblDiscount {\n"
"    color: #dc2626;\n"
"    font-size: 13px;\n"
"}\n"
"QLabel#lblSubTotal,\n"
"QLabel#lblTax,\n"
"QLabel#lblCartItemQuantity {\n"
"    font-size: 13px;\n"
"}\n"
"QFrame#line_summary {\n"
"    color: #e2e8f0;\n"
"    background-color: #e2e8f0;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#lblGrandTotal {\n"
"    color: #1d4ed8;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnCardAdd {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0px;\n"
"    min-height: 0px;\n"
"    font-size: 16px;\n"
"    font-weight:"
                        " bold;\n"
"}\n"
"QPushButton#btnCardAdd:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnCartMinus,\n"
"QPushButton#btnCartPlus {\n"
"    background-color: #ffffff;\n"
"    color: #0f172a;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    padding: 0px;\n"
"    min-height: 0px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnCartMinus:hover,\n"
"QPushButton#btnCartPlus:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnCartRemove {\n"
"    background-color: #ffffff;\n"
"    color: #94a3b8;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    padding: 0px;\n"
"    min-height: 0px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnCartRemove:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"    color: #dc2626;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 0, 3)
        self.widget_catalog = QWidget(Form)
        self.widget_catalog.setObjectName(u"widget_catalog")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_catalog.sizePolicy().hasHeightForWidth())
        self.widget_catalog.setSizePolicy(sizePolicy)
        self.verticalLayout_catalog = QVBoxLayout(self.widget_catalog)
        self.verticalLayout_catalog.setSpacing(0)
        self.verticalLayout_catalog.setObjectName(u"verticalLayout_catalog")
        self.verticalLayout_catalog.setContentsMargins(0, 0, 0, 0)
        self.frame_topbar = QFrame(self.widget_catalog)
        self.frame_topbar.setObjectName(u"frame_topbar")
        self.frame_topbar.setMinimumSize(QSize(0, 76))
        self.frame_topbar.setMaximumSize(QSize(16777215, 76))
        self.frame_topbar.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_topbar = QHBoxLayout(self.frame_topbar)
        self.horizontalLayout_topbar.setObjectName(u"horizontalLayout_topbar")
        self.horizontalLayout_topbar.setContentsMargins(20, -1, 20, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 6)
        self.lblScanSubtitle = QLabel(self.frame_topbar)
        self.lblScanSubtitle.setObjectName(u"lblScanSubtitle")

        self.gridLayout.addWidget(self.lblScanSubtitle, 4, 0, 1, 1)

        self.lblScanCaption = QLabel(self.frame_topbar)
        self.lblScanCaption.setObjectName(u"lblScanCaption")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.lblScanCaption.setFont(font)

        self.gridLayout.addWidget(self.lblScanCaption, 3, 0, 1, 1)


        self.horizontalLayout_topbar.addLayout(self.gridLayout)

        self.horizontalSpacer_topbar = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_topbar.addItem(self.horizontalSpacer_topbar)

        self.lblCashierName = QLabel(self.frame_topbar)
        self.lblCashierName.setObjectName(u"lblCashierName")

        self.horizontalLayout_topbar.addWidget(self.lblCashierName)


        self.verticalLayout_catalog.addWidget(self.frame_topbar)

        self.frame_filters = QFrame(self.widget_catalog)
        self.frame_filters.setObjectName(u"frame_filters")
        self.frame_filters.setMinimumSize(QSize(0, 120))
        self.frame_filters.setMaximumSize(QSize(16777215, 120))
        self.frame_filters.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_filters = QVBoxLayout(self.frame_filters)
        self.verticalLayout_filters.setObjectName(u"verticalLayout_filters")
        self.verticalLayout_filters.setContentsMargins(20, 14, 20, -1)
        self.frame_search_row = QFrame(self.frame_filters)
        self.frame_search_row.setObjectName(u"frame_search_row")
        self.frame_search_row.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_search_row = QHBoxLayout(self.frame_search_row)
        self.horizontalLayout_search_row.setObjectName(u"horizontalLayout_search_row")
        self.horizontalLayout_search_row.setContentsMargins(0, 0, 0, 0)
        self.txtSearch = QLineEdit(self.frame_search_row)
        self.txtSearch.setObjectName(u"txtSearch")
        self.txtSearch.setMinimumSize(QSize(123, 40))

        self.horizontalLayout_search_row.addWidget(self.txtSearch)

        self.btnFilter = QPushButton(self.frame_search_row)
        self.btnFilter.setObjectName(u"btnFilter")
        self.btnFilter.setMinimumSize(QSize(46, 40))
        self.btnFilter.setMaximumSize(QSize(46, 40))
        self.btnFilter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnFilter.setProperty(u"iconPx", 16)

        self.horizontalLayout_search_row.addWidget(self.btnFilter)


        self.verticalLayout_filters.addWidget(self.frame_search_row)

        self.frame_categories = QFrame(self.frame_filters)
        self.frame_categories.setObjectName(u"frame_categories")
        self.frame_categories.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_categories = QHBoxLayout(self.frame_categories)
        self.horizontalLayout_categories.setSpacing(8)
        self.horizontalLayout_categories.setObjectName(u"horizontalLayout_categories")
        self.horizontalLayout_categories.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_categories = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_categories.addItem(self.horizontalSpacer_categories)


        self.verticalLayout_filters.addWidget(self.frame_categories)


        self.verticalLayout_catalog.addWidget(self.frame_filters)

        self.scrollProducts = QScrollArea(self.widget_catalog)
        self.scrollProducts.setObjectName(u"scrollProducts")
        self.scrollProducts.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollProducts.setWidgetResizable(True)
        self.widget_products = QWidget()
        self.widget_products.setObjectName(u"widget_products")
        self.widget_products.setGeometry(QRect(0, 0, 860, 612))
        self.gridLayout_products = QGridLayout(self.widget_products)
        self.gridLayout_products.setSpacing(14)
        self.gridLayout_products.setObjectName(u"gridLayout_products")
        self.gridLayout_products.setContentsMargins(20, 10, 20, 20)
        self.scrollProducts.setWidget(self.widget_products)

        self.verticalLayout_catalog.addWidget(self.scrollProducts)

        self.frame_shortcuts = QFrame(self.widget_catalog)
        self.frame_shortcuts.setObjectName(u"frame_shortcuts")
        self.frame_shortcuts.setMinimumSize(QSize(0, 46))
        self.frame_shortcuts.setMaximumSize(QSize(16777215, 46))
        self.frame_shortcuts.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_shortcuts = QHBoxLayout(self.frame_shortcuts)
        self.horizontalLayout_shortcuts.setSpacing(18)
        self.horizontalLayout_shortcuts.setObjectName(u"horizontalLayout_shortcuts")
        self.horizontalLayout_shortcuts.setContentsMargins(20, 0, 20, 0)
        self.lblHintHelp = QLabel(self.frame_shortcuts)
        self.lblHintHelp.setObjectName(u"lblHintHelp")

        self.horizontalLayout_shortcuts.addWidget(self.lblHintHelp)

        self.lblHintDiscount = QLabel(self.frame_shortcuts)
        self.lblHintDiscount.setObjectName(u"lblHintDiscount")

        self.horizontalLayout_shortcuts.addWidget(self.lblHintDiscount)

        self.lblHintQuantity = QLabel(self.frame_shortcuts)
        self.lblHintQuantity.setObjectName(u"lblHintQuantity")

        self.horizontalLayout_shortcuts.addWidget(self.lblHintQuantity)

        self.lblHintPay = QLabel(self.frame_shortcuts)
        self.lblHintPay.setObjectName(u"lblHintPay")

        self.horizontalLayout_shortcuts.addWidget(self.lblHintPay)

        self.horizontalSpacer_shortcuts = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_shortcuts.addItem(self.horizontalSpacer_shortcuts)


        self.verticalLayout_catalog.addWidget(self.frame_shortcuts)


        self.horizontalLayout.addWidget(self.widget_catalog)

        self.frame_order = QFrame(Form)
        self.frame_order.setObjectName(u"frame_order")
        self.frame_order.setMinimumSize(QSize(420, 0))
        self.frame_order.setMaximumSize(QSize(460, 16777215))
        self.frame_order.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_order = QVBoxLayout(self.frame_order)
        self.verticalLayout_order.setSpacing(0)
        self.verticalLayout_order.setObjectName(u"verticalLayout_order")
        self.verticalLayout_order.setContentsMargins(0, 0, 0, 0)
        self.frame_order_header = QFrame(self.frame_order)
        self.frame_order_header.setObjectName(u"frame_order_header")
        self.frame_order_header.setMinimumSize(QSize(0, 110))
        self.frame_order_header.setMaximumSize(QSize(16777215, 110))
        self.frame_order_header.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_order_header = QGridLayout(self.frame_order_header)
        self.gridLayout_order_header.setObjectName(u"gridLayout_order_header")
        self.gridLayout_order_header.setContentsMargins(20, 18, 20, -1)
        self.lblOrderCode = QLabel(self.frame_order_header)
        self.lblOrderCode.setObjectName(u"lblOrderCode")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.lblOrderCode.setFont(font1)

        self.gridLayout_order_header.addWidget(self.lblOrderCode, 0, 0, 1, 1)

        self.btnAddCustomer = QPushButton(self.frame_order_header)
        self.btnAddCustomer.setObjectName(u"btnAddCustomer")
        self.btnAddCustomer.setMinimumSize(QSize(115, 40))
        self.btnAddCustomer.setMaximumSize(QSize(40, 36))
        self.btnAddCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_order_header.addWidget(self.btnAddCustomer, 0, 1, 1, 1)

        self.btnClearCart = QPushButton(self.frame_order_header)
        self.btnClearCart.setObjectName(u"btnClearCart")
        self.btnClearCart.setMinimumSize(QSize(40, 40))
        self.btnClearCart.setMaximumSize(QSize(40, 36))
        self.btnClearCart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_order_header.addWidget(self.btnClearCart, 0, 2, 1, 1)

        self.lblCustomerBadge = QLabel(self.frame_order_header)
        self.lblCustomerBadge.setObjectName(u"lblCustomerBadge")
        self.lblCustomerBadge.setMinimumSize(QSize(0, 28))

        self.gridLayout_order_header.addWidget(self.lblCustomerBadge, 1, 0, 1, 3)


        self.verticalLayout_order.addWidget(self.frame_order_header)

        self.scrollCart = QScrollArea(self.frame_order)
        self.scrollCart.setObjectName(u"scrollCart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.scrollCart.sizePolicy().hasHeightForWidth())
        self.scrollCart.setSizePolicy(sizePolicy1)
        self.scrollCart.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollCart.setWidgetResizable(True)
        self.widget_cart = QWidget()
        self.widget_cart.setObjectName(u"widget_cart")
        self.widget_cart.setGeometry(QRect(0, 0, 420, 446))
        self.verticalLayout_cart = QVBoxLayout(self.widget_cart)
        self.verticalLayout_cart.setSpacing(0)
        self.verticalLayout_cart.setObjectName(u"verticalLayout_cart")
        self.verticalLayout_cart.setContentsMargins(0, 0, 0, 0)
        self.lblCartEmpty = QLabel(self.widget_cart)
        self.lblCartEmpty.setObjectName(u"lblCartEmpty")
        self.lblCartEmpty.setMinimumSize(QSize(0, 120))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.lblCartEmpty.setFont(font2)
        self.lblCartEmpty.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_cart.addWidget(self.lblCartEmpty)

        self.scrollCart.setWidget(self.widget_cart)

        self.verticalLayout_order.addWidget(self.scrollCart)

        self.frame_summary = QFrame(self.frame_order)
        self.frame_summary.setObjectName(u"frame_summary")
        self.frame_summary.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_summary = QGridLayout(self.frame_summary)
        self.gridLayout_summary.setObjectName(u"gridLayout_summary")
        self.gridLayout_summary.setContentsMargins(20, 16, 20, 5)
        self.lblSubTotalCaption = QLabel(self.frame_summary)
        self.lblSubTotalCaption.setObjectName(u"lblSubTotalCaption")

        self.gridLayout_summary.addWidget(self.lblSubTotalCaption, 0, 0, 1, 1)

        self.lblSubTotal = QLabel(self.frame_summary)
        self.lblSubTotal.setObjectName(u"lblSubTotal")
        self.lblSubTotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_summary.addWidget(self.lblSubTotal, 0, 1, 1, 1)

        self.btnEditDiscount = QPushButton(self.frame_summary)
        self.btnEditDiscount.setObjectName(u"btnEditDiscount")
        self.btnEditDiscount.setMinimumSize(QSize(0, 0))
        self.btnEditDiscount.setMaximumSize(QSize(55, 16777215))
        self.btnEditDiscount.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btnEditDiscount.setAutoDefault(False)

        self.gridLayout_summary.addWidget(self.btnEditDiscount, 1, 0, 1, 1)

        self.lblDiscount = QLabel(self.frame_summary)
        self.lblDiscount.setObjectName(u"lblDiscount")
        self.lblDiscount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_summary.addWidget(self.lblDiscount, 1, 1, 1, 1)

        self.lblTaxCaption = QLabel(self.frame_summary)
        self.lblTaxCaption.setObjectName(u"lblTaxCaption")

        self.gridLayout_summary.addWidget(self.lblTaxCaption, 2, 0, 1, 1)

        self.lblTax = QLabel(self.frame_summary)
        self.lblTax.setObjectName(u"lblTax")
        self.lblTax.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_summary.addWidget(self.lblTax, 2, 1, 1, 1)

        self.line_summary = QFrame(self.frame_summary)
        self.line_summary.setObjectName(u"line_summary")
        self.line_summary.setMinimumSize(QSize(0, 1))
        self.line_summary.setMaximumSize(QSize(16777215, 1))
        self.line_summary.setFrameShape(QFrame.Shape.HLine)
        self.line_summary.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout_summary.addWidget(self.line_summary, 3, 0, 1, 2)

        self.lblGrandTotalCaption = QLabel(self.frame_summary)
        self.lblGrandTotalCaption.setObjectName(u"lblGrandTotalCaption")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.lblGrandTotalCaption.setFont(font3)

        self.gridLayout_summary.addWidget(self.lblGrandTotalCaption, 4, 0, 1, 1)

        self.lblGrandTotal = QLabel(self.frame_summary)
        self.lblGrandTotal.setObjectName(u"lblGrandTotal")
        self.lblGrandTotal.setFont(font3)
        self.lblGrandTotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_summary.addWidget(self.lblGrandTotal, 4, 1, 1, 1)

        self.frame_payment_methods = QFrame(self.frame_summary)
        self.frame_payment_methods.setObjectName(u"frame_payment_methods")
        self.frame_payment_methods.setMinimumSize(QSize(0, 66))
        self.frame_payment_methods.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_payment_methods = QHBoxLayout(self.frame_payment_methods)
        self.horizontalLayout_payment_methods.setSpacing(10)
        self.horizontalLayout_payment_methods.setObjectName(u"horizontalLayout_payment_methods")
        self.horizontalLayout_payment_methods.setContentsMargins(0, 0, 0, 0)
        self.btnPayCash = QPushButton(self.frame_payment_methods)
        self.btnPayCash.setObjectName(u"btnPayCash")
        self.btnPayCash.setMinimumSize(QSize(0, 36))
        self.btnPayCash.setMaximumSize(QSize(16777215, 50))
        self.btnPayCash.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPayCash.setCheckable(True)
        self.btnPayCash.setChecked(True)

        self.horizontalLayout_payment_methods.addWidget(self.btnPayCash)

        self.btnPayCard = QPushButton(self.frame_payment_methods)
        self.btnPayCard.setObjectName(u"btnPayCard")
        self.btnPayCard.setMinimumSize(QSize(0, 36))
        self.btnPayCard.setMaximumSize(QSize(16777215, 50))
        self.btnPayCard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPayCard.setCheckable(True)

        self.horizontalLayout_payment_methods.addWidget(self.btnPayCard)

        self.btnPayTransfer = QPushButton(self.frame_payment_methods)
        self.btnPayTransfer.setObjectName(u"btnPayTransfer")
        self.btnPayTransfer.setMinimumSize(QSize(0, 36))
        self.btnPayTransfer.setMaximumSize(QSize(16777215, 50))
        self.btnPayTransfer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPayTransfer.setCheckable(True)

        self.horizontalLayout_payment_methods.addWidget(self.btnPayTransfer)


        self.gridLayout_summary.addWidget(self.frame_payment_methods, 5, 0, 1, 2)


        self.verticalLayout_order.addWidget(self.frame_summary)

        self.frame_checkout = QFrame(self.frame_order)
        self.frame_checkout.setObjectName(u"frame_checkout")
        self.frame_checkout.setMinimumSize(QSize(0, 86))
        self.frame_checkout.setMaximumSize(QSize(16777215, 86))
        self.frame_checkout.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_checkout = QVBoxLayout(self.frame_checkout)
        self.verticalLayout_checkout.setSpacing(0)
        self.verticalLayout_checkout.setObjectName(u"verticalLayout_checkout")
        self.verticalLayout_checkout.setContentsMargins(20, 0, 20, 0)
        self.btnCheckout = QPushButton(self.frame_checkout)
        self.btnCheckout.setObjectName(u"btnCheckout")
        self.btnCheckout.setMinimumSize(QSize(0, 38))
        self.btnCheckout.setMaximumSize(QSize(16777215, 55))
        self.btnCheckout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_checkout.addWidget(self.btnCheckout)


        self.verticalLayout_order.addWidget(self.frame_checkout)


        self.horizontalLayout.addWidget(self.frame_order)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblScanSubtitle.setText(QCoreApplication.translate("Form", u"T\u1ea1o \u0111\u01a1n h\u00e0ng m\u1edbi v\u00e0 thanh to\u00e1n nhanh", None))
        self.lblScanCaption.setText(QCoreApplication.translate("Form", u"B\u00e1n h\u00e0ng", None))
        self.lblCashierName.setText(QCoreApplication.translate("Form", u"Thu ng\u00e2n: ---", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("Form", u"T\u00ecm ki\u1ebfm s\u1ea3n ph\u1ea9m", None))
#if QT_CONFIG(tooltip)
        self.btnFilter.setToolTip(QCoreApplication.translate("Form", u"L\u1ecdc s\u1ea3n ph\u1ea9m theo t\u1eeb kh\u00f3a \u0111ang nh\u1eadp", None))
#endif // QT_CONFIG(tooltip)
        self.btnFilter.setText("")
        self.btnFilter.setProperty(u"iconName", QCoreApplication.translate("Form", u"filter", None))
        self.btnFilter.setProperty(u"iconColor", QCoreApplication.translate("Form", u"default", None))
        self.lblHintHelp.setText(QCoreApplication.translate("Form", u"<span style=\"background-color:#fbfcfd; border:1px solid #e2e8f0; padding:2px 6px; font-weight:bold; color:#0f172a;\">F1</span>&nbsp;<span style=\"color:#64748b;\">Tr\u1ee3 gi\u00fap</span>", None))
        self.lblHintDiscount.setText(QCoreApplication.translate("Form", u"<span style=\"background-color:#fbfcfd; border:1px solid #e2e8f0; padding:2px 6px; font-weight:bold; color:#0f172a;\">F3</span>&nbsp;<span style=\"color:#64748b;\">Gi\u1ea3m gi\u00e1</span>", None))
        self.lblHintQuantity.setText(QCoreApplication.translate("Form", u"<span style=\"background-color:#fbfcfd; border:1px solid #e2e8f0; padding:2px 6px; font-weight:bold; color:#0f172a;\">F4</span>&nbsp;<span style=\"color:#64748b;\">S\u1ed1 l\u01b0\u1ee3ng</span>", None))
        self.lblHintPay.setText(QCoreApplication.translate("Form", u"<span style=\"background-color:#fbfcfd; border:1px solid #e2e8f0; padding:2px 6px; font-weight:bold; color:#0f172a;\">F9</span>&nbsp;<span style=\"color:#64748b;\">Thanh to\u00e1n</span>", None))
        self.lblOrderCode.setText(QCoreApplication.translate("Form", u"\u0110\u01a1n h\u00e0ng m\u1edbi", None))
#if QT_CONFIG(tooltip)
        self.btnAddCustomer.setToolTip(QCoreApplication.translate("Form", u"G\u1eafn kh\u00e1ch h\u00e0ng v\u00e0o h\u00f3a \u0111\u01a1n", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddCustomer.setText(QCoreApplication.translate("Form", u"+ Kh\u00e1ch h\u00e0ng", None))
#if QT_CONFIG(tooltip)
        self.btnClearCart.setToolTip(QCoreApplication.translate("Form", u"X\u00f3a to\u00e0n b\u1ed9 gi\u1ecf h\u00e0ng", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearCart.setText("")
        self.lblCustomerBadge.setText(QCoreApplication.translate("Form", u"Kh\u00e1ch h\u00e0ng l\u1ebb (M\u1eb7c \u0111\u1ecbnh)", None))
        self.lblCartEmpty.setText(QCoreApplication.translate("Form", u"Gi\u1ecf h\u00e0ng \u0111ang tr\u1ed1ng", None))
        self.lblSubTotalCaption.setText(QCoreApplication.translate("Form", u"T\u1ea1m t\u00ednh (0 s\u1ea3n ph\u1ea9m)", None))
        self.lblSubTotal.setText(QCoreApplication.translate("Form", u"0 \u0111", None))
#if QT_CONFIG(tooltip)
        self.btnEditDiscount.setToolTip(QCoreApplication.translate("Form", u"Nh\u1eadp m\u1ee9c gi\u00e1 cho h\u00f3a \u0111\u01a1n", None))
#endif // QT_CONFIG(tooltip)
        self.btnEditDiscount.setText(QCoreApplication.translate("Form", u"Gi\u1ea3m gi\u00e1", None))
        self.lblDiscount.setText(QCoreApplication.translate("Form", u"0 \u0111", None))
        self.lblTaxCaption.setText(QCoreApplication.translate("Form", u"Thu\u1ebf VAT", None))
        self.lblTax.setText(QCoreApplication.translate("Form", u"0 \u0111", None))
        self.lblGrandTotalCaption.setText(QCoreApplication.translate("Form", u"T\u1ed5ng thanh to\u00e1n", None))
        self.lblGrandTotal.setText(QCoreApplication.translate("Form", u"0 \u0111", None))
        self.btnPayCash.setText(QCoreApplication.translate("Form", u"Ti\u1ec1n m\u1eb7t", None))
        self.btnPayCard.setText(QCoreApplication.translate("Form", u"Th\u1ebb", None))
        self.btnPayTransfer.setText(QCoreApplication.translate("Form", u"Chuy\u1ec3n kho\u1ea3n", None))
        self.btnCheckout.setText(QCoreApplication.translate("Form", u"Ho\u00e0n t\u1ea5t \u0111\u01a1n h\u00e0ng", None))
    # retranslateUi

