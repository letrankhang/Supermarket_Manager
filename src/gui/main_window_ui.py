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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1255, 758)
        MainWindow.setStyleSheet(u"QFrame#sidebar_frame,\n"
"QFrame#frame,\n"
"QFrame#frame_3 {\n"
"    background-color: #334155;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame#sidebar_frame QPushButton {\n"
"    background-color: transparent;\n"
"    color: #cbd5e1;\n"
"    text-align: left;\n"
"    padding: 10px 10px 10px 26px;\n"
"    border: none;\n"
"    border-left: 4px solid transparent;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QFrame#sidebar_frame QPushButton:hover {\n"
"    background-color: #475569;\n"
"    color: #ffffff;\n"
"    border-left: 4px solid #94a3b8;\n"
"}\n"
"QFrame#sidebar_frame QPushButton:checked,\n"
"QFrame#sidebar_frame QPushButton:checked:hover {\n"
"    background-color: #475569;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border-left: 4px solid #3b82f6;\n"
"}\n"
"\n"
"QFrame#sidebar_frame QLabel {\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"QFrame#sidebar_frame QLabel#lbl_section_main,\n"
"QFrame#sidebar_frame QLabel#lbl_section_inventory,\n"
"QFrame#sidebar_frame"
                        " QLabel#lbl_section_system {\n"
"    background-color: transparent;\n"
"    color: #64748b;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    padding: 12px 10px 4px 30px;\n"
"}\n"
"QFrame#sidebar_frame QFrame#line_header {\n"
"    background-color: #475569;\n"
"    border: none;\n"
"    margin: 8px 16px 2px 16px;\n"
"}\n"
"\n"
"QWidget#widget_2 {\n"
"    background-color: #ffffff;\n"
"}\n"
"QLabel#lblDateTime {\n"
"    color: #1e3a8a;\n"
"    font-size: 12px;\n"
"    font-weight: 500;\n"
"}\n"
"QLabel#lblGreeting {\n"
"    color: #64748b;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"QLabel#lblUserName {\n"
"    color: #1d4ed8;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel#lblAvatar {\n"
"    background-color: #f1f5f9;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QFrame#sidebar_frame QPushButton:disabled {\n"
"    color: #475569;\n"
"    background-color: transparent;\n"
"    border-left: 4px solid transparent;\n"
"}\n"
"")
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
        self.sidebar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.sidebar_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 90))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 2)
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
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #94a3b8;\n"
"font-weight: 600;")
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
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.lblDateTime = QLabel(self.widget_2)
        self.lblDateTime.setObjectName(u"lblDateTime")

        self.horizontalLayout_2.addWidget(self.lblDateTime)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.greetingLayout = QHBoxLayout()
        self.greetingLayout.setSpacing(5)
        self.greetingLayout.setObjectName(u"greetingLayout")
        self.lblGreeting = QLabel(self.widget_2)
        self.lblGreeting.setObjectName(u"lblGreeting")
        self.lblGreeting.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.greetingLayout.addWidget(self.lblGreeting)

        self.lblUserName = QLabel(self.widget_2)
        self.lblUserName.setObjectName(u"lblUserName")
        self.lblUserName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.greetingLayout.addWidget(self.lblUserName)


        self.horizontalLayout_2.addLayout(self.greetingLayout)

        self.lblAvatar = QLabel(self.widget_2)
        self.lblAvatar.setObjectName(u"lblAvatar")
        self.lblAvatar.setMinimumSize(QSize(30, 30))
        self.lblAvatar.setMaximumSize(QSize(40, 40))
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
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Personnel", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help Center", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lblDateTime.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y gi\u1edd hi\u1ec7n t\u1ea1i", None))
        self.lblGreeting.setText(QCoreApplication.translate("MainWindow", u"Xin ch\u00e0o,", None))
        self.lblUserName.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1eddi d\u00f9ng", None))
        self.lblAvatar.setText("")
    # retranslateUi

