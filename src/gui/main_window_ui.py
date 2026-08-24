# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
# import app_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1255, 758)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 2, 2, 0)
        self.sidebar_frame = QFrame(self.centralwidget)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_frame.setMaximumSize(QSize(300, 16777215))
        self.sidebar_frame.setStyleSheet(u"/* 1. N\u1ec1n sidebar */\n"
"#sidebar_frame {\n"
"    background-color: #334155;\n"
"}\n"
"\n"
"/* 2. Tr\u1ea1ng th\u00e1i th\u01b0\u1eddng c\u1ee7a n\u00fat menu.\n"
"      border-left trong su\u1ed1t nh\u01b0ng V\u1eaaN r\u1ed9ng 4px \u0111\u1ec3 gi\u1eef ch\u1ed7 s\u1eb5n cho thanh d\u1ecdc,\n"
"      nh\u1edd v\u1eady ch\u1eef kh\u00f4ng b\u1ecb nh\u1ea3y sang ph\u1ea3i khi hover hay khi \u0111\u01b0\u1ee3c ch\u1ecdn.\n"
"      padding-left gi\u1ea3m 30px -> 26px \u0111\u1ec3 b\u00f9 \u0111\u00fang 4px border (4 + 26 = 30),\n"
"      gi\u1eef nguy\u00ean v\u1ecb tr\u00ed ch\u1eef so v\u1edbi giao di\u1ec7n c\u0169. */\n"
"#sidebar_frame QPushButton {\n"
"    background-color: transparent;\n"
"    color: #cbd5e1;\n"
"    text-align: left;\n"
"    padding: 10px 10px 10px 26px;\n"
"    border: none;\n"
"    border-left: 4px solid transparent;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* 3. Hover (r\u00ea chu\u1ed9t v\u00e0o n\u00fat ch\u01b0a ch\u1ecdn): n\u1ec1n s\u00e1ng nh\u1eb9, "
                        "ch\u1eef tr\u1eafng,\n"
"      thanh d\u1ecdc m\u00e0u X\u00c1M mang ngh\u0129a \"xem tr\u01b0\u1edbc\" */\n"
"#sidebar_frame QPushButton:hover {\n"
"    background-color: #475569;\n"
"    color: #ffffff;\n"
"    border-left: 4px solid #94a3b8;\n"
"}\n"
"\n"
"/* 4. Active (n\u00fat c\u1ee7a trang \u0111ang m\u1edf): n\u1ec1n s\u00e1ng nh\u1eb9, ch\u1eef tr\u1eafng \u0111\u1eadm,\n"
"      thanh d\u1ecdc m\u00e0u XANH D\u01af\u01a0NG n\u1ed5i b\u1eadt */\n"
"#sidebar_frame QPushButton:checked {\n"
"    background-color: #475569;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border-left: 4px solid #3b82f6;\n"
"}\n"
"\n"
"/* 5. R\u00ea chu\u1ed9t v\u00e0o ch\u00ednh n\u00fat \u0111ang active th\u00ec V\u1eaaN gi\u1eef thanh xanh d\u01b0\u01a1ng.\n"
"      Rule n\u00e0y b\u1eaft bu\u1ed9c ph\u1ea3i \u0111\u1eb7t SAU rule :hover, v\u00ec khi \u0111\u1ed9 \u0111\u1eb7c hi\u1ec7u ngang\n"
"      nhau th\u00ec Qt \u01b0u ti\u00ean rule \u0111\u1ee9ng sau - \u0111\u00f3 l\u00e0 c\u00e1ch :checked th\u1eafn"
                        "g :hover. */\n"
"#sidebar_frame QPushButton:checked:hover {\n"
"    background-color: #475569;\n"
"    color: #ffffff;\n"
"    border-left: 4px solid #3b82f6;\n"
"}\n"
"\n"
"/* 6. \u0110\u1ed5i m\u00e0u ch\u1eef Logo v\u00e0 Ti\u00eau \u0111\u1ec1 th\u00e0nh tr\u1eafng cho n\u1ed5i b\u1eadt */\n"
"#sidebar_frame QLabel {\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* 7. Ti\u00eau \u0111\u1ec1 nh\u00f3m menu (MAIN / INVENTORY / SYSTEM).\n"
"      3 label n\u00e0y l\u00e0 con c\u1ee7a sidebar_frame n\u00ean d\u00ednh lu\u00f4n rule s\u1ed1 6 \u1edf tr\u00ean v\u00e0\n"
"      b\u1ecb t\u00f4 tr\u1eafng \u0111\u1eadm. Mu\u1ed1n \u0111\u00e8 \u0111\u01b0\u1ee3c rule \u0111\u00f3 th\u00ec selector ph\u1ea3i \u0110\u1eb6C HI\u1ec6U H\u01a0N,\n"
"      v\u00e0 \u1edf \u0111\u00e2y ph\u1ea3i vi\u1ebft \u0111\u1ee7 c\u1ea3 \"#sidebar_frame QLabel#ten_label\":\n"
"        - \"#sidebar_frame QLabel\"        = 1 id + 1 type\n"
"        - \"#lbl_section_main\"            = 1 id + 0 type  -> THUA, kh\u00f4"
                        "ng \u0111\u1ee7\n"
"        - \"#sidebar_frame QLabel#...\"    = 2 id + 1 type  -> TH\u1eaeNG\n"
"      padding-left 30px \u0111\u1ec3 ch\u1eef ti\u00eau \u0111\u1ec1 th\u1eb3ng h\u00e0ng v\u1edbi ch\u1eef tr\u00ean n\u00fat\n"
"      (n\u00fat = border-left 4px + padding-left 26px = 30px).\n"
"      padding-top 12px t\u1ea1o kho\u1ea3ng th\u1edf ng\u0103n c\u00e1ch gi\u1eefa c\u00e1c nh\u00f3m. */\n"
"#sidebar_frame QLabel#lbl_section_main,\n"
"#sidebar_frame QLabel#lbl_section_inventory,\n"
"#sidebar_frame QLabel#lbl_section_system {\n"
"    background-color: transparent;\n"
"    color: #64748b;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    padding: 12px 10px 4px 30px;\n"
"}\n"
"\n"
"/* 8. \u0110\u01b0\u1eddng k\u1ebb ngang m\u1ea3nh ng\u0103n gi\u1eefa ph\u1ea7n header (logo + t\u00ean app) v\u00e0 ph\u1ea7n menu.\n"
"      \u0110\u00e2y l\u00e0 QFrame ph\u1eb3ng (NoFrame) ch\u1ee9 KH\u00d4NG d\u00f9ng frameShape = HLine, v\u00ec HLine\n"
"      v\u1ebd \u0111\u01b0\u1eddng b\u1eb1ng m\u00e0u "
                        "mid/dark/light l\u1ea5y t\u1eeb palette ch\u1ee9 kh\u00f4ng l\u1ea5y t\u1eeb QSS, n\u00ean\n"
"      tr\u00ean n\u1ec1n t\u1ed1i s\u1ebd ra v\u1ea1ch n\u1ed5i 3D sai m\u00e0u v\u00e0 r\u1ea5t kh\u00f3 \u00e9p m\u00e0u.\n"
"      M\u1eb9o \u1edf \u0111\u00e2y l\u00e0 d\u00f9ng box model c\u1ee7a QSS: background-color ch\u1ec9 t\u00f4 ph\u1ea7n N\u1eb0M\n"
"      TRONG l\u1ec1, n\u00ean widget cao 11px v\u1edbi l\u1ec1 tr\u00ean 8px v\u00e0 l\u1ec1 d\u01b0\u1edbi 2px s\u1ebd \u0111\u1ec3 l\u1ea1i\n"
"      \u0111\u00fang 1px \u0111\u01b0\u1ee3c t\u00f4 m\u00e0u (11 = 8 + 1 + 2), th\u1ee5t v\u00e0o 16px m\u1ed7i b\u00ean.\n"
"      L\u1ec1 d\u01b0\u1edbi c\u1ed1 \u00fd nh\u1ecf h\u01a1n l\u1ec1 tr\u00ean v\u00ec nh\u00e3n nh\u00f3m \"MAIN\" ngay b\u00ean d\u01b0\u1edbi \u0111\u00e3 t\u1ef1 c\u00f3\n"
"      s\u1eb5n padding-top 12px r\u1ed3i; \u0111\u1ec3 8px c\u1ea3 hai ph\u00eda s\u1ebd l\u00e0m kho\u1ea3ng d\u01b0\u1edbi r\u1ed9ng g\u1ea5p\n"
"      \u0111\u00f4i kho\u1ea3ng tr\u00ean.\n"
"      Selector vi\u1ebf"
                        "t \u0111\u1ee7 \"#sidebar_frame QFrame#line_header\" (2 id + 1 type) \u0111\u1ec3\n"
"      ch\u1eafc ch\u1eafn th\u1eafng m\u1ecdi rule c\u00f3 s\u1eb5n, gi\u1ed1ng c\u00e1ch \u0111\u00e3 l\u00e0m \u1edf rule s\u1ed1 7. */\n"
"#sidebar_frame QFrame#line_header {\n"
"    background-color: #475569;\n"
"    border: none;\n"
"    margin: 8px 16px 2px 16px;\n"
"}")
        self.sidebar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.sidebar_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 90))
        self.frame.setStyleSheet(u"#frame {\n"
"    background-color: #334155;\n"
"    border: none; \n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(75, 75))
        self.label_4.setMaximumSize(QSize(75, 75))
        self.label_4.setPixmap(QPixmap(u"../../../../Downloads/logo1.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout.setContentsMargins(-1, 14, -1, 14)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(140, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(120, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #AAB4C3;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        self.line_header = QFrame(self.sidebar_frame)
        self.line_header.setObjectName(u"line_header")
        self.line_header.setMinimumSize(QSize(0, 11))
        self.line_header.setMaximumSize(QSize(16777215, 11))
        self.line_header.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_2.addWidget(self.line_header)

        self.lbl_section_main = QLabel(self.sidebar_frame)
        self.lbl_section_main.setObjectName(u"lbl_section_main")

        self.verticalLayout_2.addWidget(self.lbl_section_main)

        self.btn_dashboard = QPushButton(self.sidebar_frame)
        self.btn_dashboard.setObjectName(u"btn_dashboard")

        self.verticalLayout_2.addWidget(self.btn_dashboard)

        self.btn_pos = QPushButton(self.sidebar_frame)
        self.btn_pos.setObjectName(u"btn_pos")

        self.verticalLayout_2.addWidget(self.btn_pos)

        self.btn_products = QPushButton(self.sidebar_frame)
        self.btn_products.setObjectName(u"btn_products")

        self.verticalLayout_2.addWidget(self.btn_products)

        self.btn_customers = QPushButton(self.sidebar_frame)
        self.btn_customers.setObjectName(u"btn_customers")

        self.verticalLayout_2.addWidget(self.btn_customers)

        self.lbl_section_inventory = QLabel(self.sidebar_frame)
        self.lbl_section_inventory.setObjectName(u"lbl_section_inventory")

        self.verticalLayout_2.addWidget(self.lbl_section_inventory)

        self.btn_suppliers = QPushButton(self.sidebar_frame)
        self.btn_suppliers.setObjectName(u"btn_suppliers")

        self.verticalLayout_2.addWidget(self.btn_suppliers)

        self.btn_importing = QPushButton(self.sidebar_frame)
        self.btn_importing.setObjectName(u"btn_importing")

        self.verticalLayout_2.addWidget(self.btn_importing)

        self.lbl_section_system = QLabel(self.sidebar_frame)
        self.lbl_section_system.setObjectName(u"lbl_section_system")

        self.verticalLayout_2.addWidget(self.lbl_section_system)

        self.btn_analytics = QPushButton(self.sidebar_frame)
        self.btn_analytics.setObjectName(u"btn_analytics")

        self.verticalLayout_2.addWidget(self.btn_analytics)

        self.btn_settings = QPushButton(self.sidebar_frame)
        self.btn_settings.setObjectName(u"btn_settings")

        self.verticalLayout_2.addWidget(self.btn_settings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.sidebar_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3 {\n"
"    background-color: #334155;\n"
"    border: none; \n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_help = QPushButton(self.frame_3)
        self.btn_help.setObjectName(u"btn_help")

        self.verticalLayout_3.addWidget(self.btn_help)

        self.btn_logout = QPushButton(self.frame_3)
        self.btn_logout.setObjectName(u"btn_logout")

        self.verticalLayout_3.addWidget(self.btn_logout)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.sidebar_frame)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 100))
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"    background-color: #ffffff; \n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.lblDateTime = QLabel(self.widget_2)
        self.lblDateTime.setObjectName(u"lblDateTime")
        self.lblDateTime.setStyleSheet(u"#lblDateTime {\n"
"    color: #1e3a8a;\n"
"    font-size: 12px;\n"
"    font-weight: 500;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lblDateTime)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.greetingLayout = QHBoxLayout()
        self.greetingLayout.setSpacing(5)
        self.greetingLayout.setObjectName(u"greetingLayout")
        self.lblGreeting = QLabel(self.widget_2)
        self.lblGreeting.setObjectName(u"lblGreeting")
        self.lblGreeting.setStyleSheet(u"/* Loi dan chao: mau xam nhat, chu thuong de nhuong su chu y cho ten */\n"
"#lblGreeting {\n"
"    color: #64748b;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}")
        self.lblGreeting.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.greetingLayout.addWidget(self.lblGreeting)

        self.lblUserName = QLabel(self.widget_2)
        self.lblUserName.setObjectName(u"lblUserName")
        self.lblUserName.setStyleSheet(u"/* Ten nguoi dung: in dam va to mau xanh thuong hieu cho noi bat */\n"
"#lblUserName {\n"
"    color: #1d4ed8;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")
        self.lblUserName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.greetingLayout.addWidget(self.lblUserName)


        self.horizontalLayout_2.addLayout(self.greetingLayout)

        self.lblAvatar = QLabel(self.widget_2)
        self.lblAvatar.setObjectName(u"lblAvatar")
        self.lblAvatar.setMinimumSize(QSize(30, 30))
        self.lblAvatar.setMaximumSize(QSize(40, 40))
        self.lblAvatar.setStyleSheet(u"QLabel {\n"
"    border-radius: 20px; /* B\u1eaft bu\u1ed9c ph\u1ea3i b\u1eb1ng \u0111\u00fang 1/2 k\u00edch th\u01b0\u1edbc Width/Height b\u1ea1n v\u1eeba set \u1edf L\u1ed7i 1 */\n"
"    border-image: url(:/images/avata.jpg) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent;\n"
"}")
        self.lblAvatar.setScaledContents(False)
        self.lblAvatar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblAvatar)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_4.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1255, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RetaiPro ERP / Trang ch\u1ee7", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RetailPro ERP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enterprise Suite", None))
        self.lbl_section_main.setText(QCoreApplication.translate("MainWindow", u"MAIN", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_pos.setText(QCoreApplication.translate("MainWindow", u"POS", None))
        self.btn_products.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.btn_customers.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.lbl_section_inventory.setText(QCoreApplication.translate("MainWindow", u"INVENTORY", None))
        self.btn_suppliers.setText(QCoreApplication.translate("MainWindow", u"Suppliers", None))
        self.btn_importing.setText(QCoreApplication.translate("MainWindow", u"Importing", None))
        self.lbl_section_system.setText(QCoreApplication.translate("MainWindow", u"SYSTEM", None))
        self.btn_analytics.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Sytem Settings", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help Center", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lblDateTime.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y gi\u1edd hi\u1ec7n t\u1ea1i", None))
        self.lblGreeting.setText(QCoreApplication.translate("MainWindow", u"Xin ch\u00e0o,", None))
        self.lblUserName.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1eddi d\u00f9ng", None))
        self.lblAvatar.setText("")
    # retranslateUi

