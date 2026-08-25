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
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"#frame_topbar {\n"
"    background-color: #ffffff;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"#lblScanSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"#lblCashierName {\n"
"    color: #64748b;\n"
"}\n"
"\n"
"#frame_filters {\n"
"    background-color: #ffffff;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 4px 12px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"#CategoryChip {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 16px;\n"
"    padding: 4px 16px;\n"
"    fo"
                        "nt-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#CategoryChip:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"#CategoryChip:checked {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff;\n"
"    border: 1px solid #1e3a8a;\n"
"}\n"
"\n"
"#btnFilter,\n"
"#btnAddCustomer {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnFilter:hover,\n"
"#btnAddCustomer:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"#btnClearCart {\n"
"    background-color: #ffffff;\n"
"    color: #dc2626;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnClearCart:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: transpare"
                        "nt;\n"
"    border: none;\n"
"}\n"
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
"    background-color: #64748b;\n"
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
"QScrollBar:horizontal {\n"
"    background-color: #f8fafc;\n"
"    "
                        "height: 10px;\n"
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
"QScrollBar::add-line:horizontal,\n"
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
"}\n"
"\n"
"#ProductCard {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#ProductCard:hover {\n"
""
                        "    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"#lblCardThumbnail {\n"
"    background-color: #fbfcfd;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    color: #64748b;\n"
"}\n"
"\n"
"#lblCardName {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#lblCardBarcode {\n"
"    color: #64748b;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"#lblCardPrice {\n"
"    color: #1d4ed8;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnCardAdd {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnCardAdd:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"\n"
"#frame_shortcuts {\n"
"    background-color: #ffffff;\n"
"    border-top: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"#frame_order {\n"
"    background-color: #ffffff;\n"
"    border-left: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"#frame_order_header {\n"
"    background-color: #ffffff;\n"
"    border-bottom"
                        ": 1px solid #e2e8f0;\n"
"}\n"
"\n"
"#lblCustomerBadge {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border-radius: 12px;\n"
"    padding: 4px 12px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#lblCartEmpty {\n"
"    color: #64748b;\n"
"}\n"
"\n"
"#CartRow {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    border-bottom: 1px solid #f1f5f9;\n"
"}\n"
"\n"
"#lblCartItemName,\n"
"#lblCartItemTotal {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#lblCartItemUnitPrice {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#lblCartItemQuantity {\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#btnCartMinus,\n"
"#btnCartPlus {\n"
"    background-color: #ffffff;\n"
"    color: #0f172a;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnCartMinus:hover,\n"
"#btnCartPlus:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    "
                        "color: #1d4ed8;\n"
"}\n"
"\n"
"#btnCartRemove {\n"
"    background-color: #ffffff;\n"
"    color: #94a3b8;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnCartRemove:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"    color: #dc2626;\n"
"}\n"
"\n"
"#frame_summary {\n"
"    background-color: #ffffff;\n"
"    border-top: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"#lblSubTotalCaption,\n"
"#lblTaxCaption {\n"
"    color: #64748b;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#lblSubTotal,\n"
"#lblTax {\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#lblDiscount {\n"
"    color: #dc2626;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#btnEditDiscount {\n"
"    background-color: transparent;\n"
"    color: #64748b;\n"
"    border: none;\n"
"    text-align: left;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#btnEditDiscount:hover {\n"
"    color: #1d4ed8;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"#line_summary {\n"
"    col"
                        "or: #e2e8f0;\n"
"    background-color: #e2e8f0;\n"
"}\n"
"\n"
"#lblGrandTotal {\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"#btnPayCash,\n"
"#btnPayCard,\n"
"#btnPayTransfer {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnPayCash:hover,\n"
"#btnPayCard:hover,\n"
"#btnPayTransfer:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"#btnPayCash:checked,\n"
"#btnPayCard:checked,\n"
"#btnPayTransfer:checked {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"#btnCheckout {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnCheckout:hover {\n"
"    background-color: #1d4ed8;\n"
"}\n"
"\n"
"#btnCheckout:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: "
                        "#f8fafc;\n"
"}")
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
        self.gridLayout.setContentsMargins(0, 2, 0, 6)
        self.lblScanSubtitle = QLabel(self.frame_topbar)
        self.lblScanSubtitle.setObjectName(u"lblScanSubtitle")

        self.gridLayout.addWidget(self.lblScanSubtitle, 4, 0, 1, 1)

        self.lblScanCaption = QLabel(self.frame_topbar)
        self.lblScanCaption.setObjectName(u"lblScanCaption")
        font = QFont()
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
        self.txtSearch.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_search_row.addWidget(self.txtSearch)

        self.btnFilter = QPushButton(self.frame_search_row)
        self.btnFilter.setObjectName(u"btnFilter")
        self.btnFilter.setMinimumSize(QSize(46, 40))
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
        font1.setPointSize(15)
        font1.setBold(True)
        self.lblOrderCode.setFont(font1)

        self.gridLayout_order_header.addWidget(self.lblOrderCode, 0, 0, 1, 1)

        self.btnAddCustomer = QPushButton(self.frame_order_header)
        self.btnAddCustomer.setObjectName(u"btnAddCustomer")
        self.btnAddCustomer.setMinimumSize(QSize(99, 36))
        self.btnAddCustomer.setMaximumSize(QSize(40, 36))
        self.btnAddCustomer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddCustomer.setStyleSheet(u"")

        self.gridLayout_order_header.addWidget(self.btnAddCustomer, 0, 1, 1, 1)

        self.btnClearCart = QPushButton(self.frame_order_header)
        self.btnClearCart.setObjectName(u"btnClearCart")
        self.btnClearCart.setMinimumSize(QSize(40, 36))
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
        self.widget_cart.setGeometry(QRect(0, 0, 420, 421))
        self.verticalLayout_cart = QVBoxLayout(self.widget_cart)
        self.verticalLayout_cart.setSpacing(0)
        self.verticalLayout_cart.setObjectName(u"verticalLayout_cart")
        self.verticalLayout_cart.setContentsMargins(0, 0, 0, 0)
        self.lblCartEmpty = QLabel(self.widget_cart)
        self.lblCartEmpty.setObjectName(u"lblCartEmpty")
        self.lblCartEmpty.setMinimumSize(QSize(0, 120))
        font2 = QFont()
        font2.setPointSize(10)
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
        self.gridLayout_summary.setContentsMargins(20, 16, 20, 16)
        self.lblSubTotalCaption = QLabel(self.frame_summary)
        self.lblSubTotalCaption.setObjectName(u"lblSubTotalCaption")

        self.gridLayout_summary.addWidget(self.lblSubTotalCaption, 0, 0, 1, 1)

        self.lblSubTotal = QLabel(self.frame_summary)
        self.lblSubTotal.setObjectName(u"lblSubTotal")
        self.lblSubTotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_summary.addWidget(self.lblSubTotal, 0, 1, 1, 1)

        self.btnEditDiscount = QPushButton(self.frame_summary)
        self.btnEditDiscount.setObjectName(u"btnEditDiscount")
        self.btnEditDiscount.setMinimumSize(QSize(0, 26))

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
        font3.setPointSize(12)
        font3.setBold(True)
        self.lblGrandTotalCaption.setFont(font3)

        self.gridLayout_summary.addWidget(self.lblGrandTotalCaption, 4, 0, 1, 1)

        self.lblGrandTotal = QLabel(self.frame_summary)
        self.lblGrandTotal.setObjectName(u"lblGrandTotal")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.lblGrandTotal.setFont(font4)
        self.lblGrandTotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_summary.addWidget(self.lblGrandTotal, 4, 1, 1, 1)

        self.frame_payment_methods = QFrame(self.frame_summary)
        self.frame_payment_methods.setObjectName(u"frame_payment_methods")
        self.frame_payment_methods.setMinimumSize(QSize(0, 66))
        self.frame_payment_methods.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_payment_methods = QHBoxLayout(self.frame_payment_methods)
        self.horizontalLayout_payment_methods.setSpacing(10)
        self.horizontalLayout_payment_methods.setObjectName(u"horizontalLayout_payment_methods")
        self.horizontalLayout_payment_methods.setContentsMargins(0, 6, 0, 0)
        self.btnPayCash = QPushButton(self.frame_payment_methods)
        self.btnPayCash.setObjectName(u"btnPayCash")
        self.btnPayCash.setMinimumSize(QSize(0, 58))
        self.btnPayCash.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPayCash.setCheckable(True)
        self.btnPayCash.setChecked(True)

        self.horizontalLayout_payment_methods.addWidget(self.btnPayCash)

        self.btnPayCard = QPushButton(self.frame_payment_methods)
        self.btnPayCard.setObjectName(u"btnPayCard")
        self.btnPayCard.setMinimumSize(QSize(0, 58))
        self.btnPayCard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPayCard.setCheckable(True)

        self.horizontalLayout_payment_methods.addWidget(self.btnPayCard)

        self.btnPayTransfer = QPushButton(self.frame_payment_methods)
        self.btnPayTransfer.setObjectName(u"btnPayTransfer")
        self.btnPayTransfer.setMinimumSize(QSize(0, 58))
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
        self.verticalLayout_checkout.setObjectName(u"verticalLayout_checkout")
        self.verticalLayout_checkout.setContentsMargins(20, 14, 20, 18)
        self.btnCheckout = QPushButton(self.frame_checkout)
        self.btnCheckout.setObjectName(u"btnCheckout")
        self.btnCheckout.setMinimumSize(QSize(0, 54))
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

