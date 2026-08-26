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
        Form.setStyleSheet(u"""QWidget#Form {
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
    color: #ef4444;
    font-weight: bold;
}
QLabel[state="flat"] {
    color: #64748b;
    font-weight: bold;
}
QLabel[state="warning"] {
    color: #eab308;
    font-weight: bold;
}
QLabel[state="safe"] {
    color: #10b981;
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

QFrame#frame_topbar,
QFrame#frame_filters,
QFrame#frame_shortcuts,
QFrame#frame_summary,
QFrame#frame_order_header,
QFrame#frame_search_row,
QFrame#frame_categories,
QFrame#frame_payment_methods,
QFrame#frame_checkout {
    background-color: transparent;
    border: none;
}

QFrame#frame_topbar,
QFrame#frame_filters {
    background-color: #ffffff;
    border-bottom: 1px solid #e2e8f0;
}
QFrame#frame_shortcuts,
QFrame#frame_summary {
    background-color: #ffffff;
    border-top: 1px solid #e2e8f0;
}
QFrame#frame_order {
    background-color: #ffffff;
    border-left: 1px solid #e2e8f0;
}
QFrame#frame_order_header {
    background-color: #ffffff;
    border-bottom: 1px solid #e2e8f0;
}

QLabel#lblScanCaption {
    color: #0f172a;
    padding: 0px;
    margin: 0px;
}

QLabel#lblScanSubtitle {
    color: #6b7280;
    font-size: 12px;
    font-weight: normal;
    margin-top: 4px;
}

QLabel#lblCashierName,
QLabel#lblCartEmpty,
QLabel#lblSubTotalCaption,
QLabel#lblTaxCaption,
QLabel#lblCartItemUnitPrice,
QLabel#lblGrandTotalCaption {
    color: #64748b;
    font-size: 13px;
}

QPushButton#CategoryChip {
    background-color: #ffffff;
    color: #64748b;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 4px 16px;
    min-height: 30px;
    font-size: 12px;
    font-weight: bold;
}
QPushButton#CategoryChip:hover {
    border: 1px solid #1d4ed8;
    color: #1d4ed8;
}
QPushButton#CategoryChip:checked {
    background-color: #1d4ed8;
    color: #ffffff;
    border: 1px solid #1d4ed8;
}

QPushButton#btnCardAdd {
     padding-bottom: 3px;
	 font-size: 18px;
     font-weight: bold;
}

QPushButton#btnClearCart {
    background-color: #ffffff;
    color: #dc2626;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0px 16px;
    min-height: 38px;
    font-size: 12px;
    font-weight: bold;
}
QPushButton#btnClearCart:hover {
    background-color: #fef2f2;
    border: 1px solid #dc2626;
}
QPushButton#btnClearCart:disabled {
    background-color: #f8fafc;
    color: #cbd5e1;
    border: 1px solid #e2e8f0;
}

QPushButton#btnEditDiscount {
    background-color: transparent;
    color: #1d4ed8;
    border: none;
    padding: 0px;
    min-height: 0px;
    font-size: 13px;
    font-weight: bold;
}
QPushButton#btnEditDiscount:hover {
    color: #1e3a8a;
    text-decoration: underline;
}
QPushButton#btnEditDiscount:pressed {
    color: #1e40af;
}
QPushButton#btnEditDiscount:disabled {
    background-color: transparent;
    border: none;
    color: #94a3b8;
    text-decoration: none;
}

QPushButton#btnCheckout {
    background-color: #1d4ed8;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 0px 20px;
    min-height: 38px;
    font-size: 13px;
    font-weight: 700;
}
QPushButton#btnCheckout:hover {
    background-color: #1e3a8a;
}
QPushButton#btnCheckout:pressed {
    background-color: #1e40af;
}
QPushButton#btnCheckout:disabled {
    background-color: #cbd5e1;
    color: #f8fafc;
}

QPushButton#btnPayCash,
QPushButton#btnPayCard,
QPushButton#btnPayTransfer {
    background-color: #ffffff;
    color: #64748b;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0px 16px;
    min-height: 34px;
    font-size: 12px;
    font-weight: bold;
}
QPushButton#btnPayCash:hover,
QPushButton#btnPayCard:hover,
QPushButton#btnPayTransfer:hover {
    border: 1px solid #1d4ed8;
    color: #1d4ed8;
}
QPushButton#btnPayCash:checked,
QPushButton#btnPayCard:checked,
QPushButton#btnPayTransfer:checked {
    background-color: #eff6ff;
    border: 1px solid #1d4ed8;
    color: #1d4ed8;
}

QFrame#ProductCard {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
}
QFrame#ProductCard:hover {
    border: 1px solid #1d4ed8;
}
QFrame#CartRow {
    background-color: #ffffff;
    border: none;
    border-bottom: 1px solid #f1f5f9;
}
QLabel#lblCardThumbnail {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    color: #64748b;
}
QLabel#lblCardName,
QLabel#lblCartItemName,
QLabel#lblCartItemTotal {
    font-size: 13px;
    font-weight: bold;
}
QLabel#lblCardBarcode {
    color: #64748b;
    font-size: 11px;
}
QLabel#lblCardPrice {
    color: #1d4ed8;
    font-size: 13px;
    font-weight: bold;
}
QLabel#lblCustomerBadge {
    background-color: #eff6ff;
    color: #1d4ed8;
    border-radius: 12px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: bold;
}
QLabel#lblDiscount {
    color: #dc2626;
    font-size: 13px;
}
QLabel#lblSubTotal,
QLabel#lblTax,
QLabel#lblCartItemQuantity {
    font-size: 13px;
}
QFrame#line_summary {
    color: #e2e8f0;
    background-color: #e2e8f0;
    border: none;
}

QLabel#lblGrandTotal {
    color: #1d4ed8;
    font-size: 22px;
    font-weight: bold;
}

QPushButton#btnCardAdd {
    background-color: #1d4ed8;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 0px;
    min-height: 0px;
    font-size: 16px;
    font-weight: bold;
}
QPushButton#btnCardAdd:hover {
    background-color: #1e3a8a;
}
QPushButton#btnCartMinus,
QPushButton#btnCartPlus {
    background-color: #ffffff;
    color: #0f172a;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 0px;
    min-height: 0px;
    font-size: 14px;
    font-weight: bold;
}
QPushButton#btnCartMinus:hover,
QPushButton#btnCartPlus:hover {
    background-color: #eff6ff;
    border: 1px solid #1d4ed8;
    color: #1d4ed8;
}
QPushButton#btnCartRemove {
    background-color: #ffffff;
    color: #94a3b8;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 0px;
    min-height: 0px;
    font-size: 13px;
    font-weight: bold;
}
QPushButton#btnCartRemove:hover {
    background-color: #fef2f2;
    border: 1px solid #dc2626;
    color: #dc2626;
}
""")
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
        self.btnFilter.setMinimumSize(QSize(52, 40))
        self.btnFilter.setMaximumSize(QSize(46, 40))
        self.btnFilter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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
        self.btnFilter.setText(QCoreApplication.translate("Form", u"L\u1ecdc", None))
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

