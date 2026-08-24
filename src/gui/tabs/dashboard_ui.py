# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1536, 924)
        Form.setStyleSheet(u"/* ===== QSS t\u1eadp trung c\u1ee7a Dashboard =====\n"
"   Tr\u01b0\u1edbc \u0111\u00e2y n\u1eb1m r\u1ea3i r\u00e1c trong DashboardController.py.\n"
"   Gom v\u1ec1 \u0111\u00e2y \u0111\u1ec3 ch\u1ec9nh giao di\u1ec7n tr\u1ef1c ti\u1ebfp trong Qt Designer.\n"
"   QSS \u0111\u1eb7t \u1edf widget g\u1ed1c s\u1ebd lan xu\u1ed1ng m\u1ecdi widget con, k\u1ec3 c\u1ea3\n"
"   widget \u0111\u01b0\u1ee3c t\u1ea1o l\u00fac ch\u1ea1y (b\u1ea3ng, huy hi\u1ec7u icon, nh\u00e3n \u00f4 thao t\u00e1c). */\n"
"\n"
"/* N\u00fat \"T\u1ea3i l\u1ea1i d\u1eef li\u1ec7u\" tr\u00ean thanh ti\u00eau \u0111\u1ec1.\n"
"   D\u00f9ng chung b\u1ea3ng m\u00e0u v\u1edbi n\u00fat ch\u00ednh c\u1ee7a tab POS (#btnCheckout, #btnCardAdd)\n"
"   \u0111\u1ec3 hai tab nh\u00ecn \u0111\u1ed3ng b\u1ed9. */\n"
"QPushButton#pushButton {\n"
"	background-color: #1d4ed8;\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	padding: 0px 14px;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton#pushButton:hover {\n"
"	backg"
                        "round-color: #1e3a8a;\n"
"}\n"
"QPushButton#pushButton:pressed {\n"
"	background-color: #1e40af;\n"
"}\n"
"/* Tr\u1ea1ng th\u00e1i \"\u0110ang t\u1ea3i...\" khi controller t\u1ea1m kho\u00e1 n\u00fat */\n"
"QPushButton#pushButton:disabled {\n"
"	background-color: #cbd5e1;\n"
"	color: #f8fafc;\n"
"}\n"
"\n"
"/* Dong mo ta phu ngay duoi tieu de \"Tong quan he thong\" */\n"
"QLabel#lblDashboardSubtitle {\n"
"	color: #6b7280;\n"
"	font-size: 12px;\n"
"	font-weight: normal;\n"
"	margin-top: 4px;\n"
"}\n"
"\n"
"/* Ti\u00eau \u0111\u1ec1 kh\u1ed1i \"Giao d\u1ecbch g\u1ea7n \u0111\u00e2y\" */\n"
"QLabel#lblTableTitle {\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	color: #1e293b;\n"
"}\n"
"\n"
"/* B\u1ea3ng giao d\u1ecbch g\u1ea7n \u0111\u00e2y */\n"
"QTableWidget#tblRecentTransactions {\n"
"	border: none;\n"
"	gridline-color: #f1f5f9;\n"
"	background-color: white;\n"
"}\n"
"QTableWidget#tblRecentTransactions::item {\n"
"	padding: 10px;\n"
"	border-bottom: 1px solid #f8fafc;\n"
"}\n"
"QTableWidget#tblRecentTransa"
                        "ctions QHeaderView::section {\n"
"	background-color: #f8fafc;\n"
"	padding: 8px;\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	color: #475569;\n"
"}\n"
"\n"
"/* Ch\u1eef ch\u00fa th\u00edch d\u01b0\u1edbi 4 \u00f4 thao t\u00e1c nhanh */\n"
"QLabel#lblQuickActionCaption {\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	color: #475569;\n"
"}\n"
"\n"
"/* Huy hi\u1ec7u n\u1ec1n bo g\u00f3c ph\u00eda sau icon c\u1ee7a 4 th\u1ebb th\u1ed1ng k\u00ea */\n"
"QLabel#badgeRevenue  { background-color: #dbeafe; border-radius: 8px; }\n"
"QLabel#badgeInvoice  { background-color: #ede9fe; border-radius: 8px; }\n"
"QLabel#badgeStock    { background-color: #fef3c7; border-radius: 8px; }\n"
"QLabel#badgeCustomer { background-color: #d1fae5; border-radius: 8px; }\n"
"\n"
"/* Nh\u00e3n \u0111\u1ed5i m\u00e0u theo d\u1eef li\u1ec7u.\n"
"   Controller ch\u1ec9 g\u00e1n thu\u1ed9c t\u00ednh \u0111\u1ed9ng trangThai, m\u00e0u do QSS d\u01b0\u1edbi \u0111\u00e2y quy\u1ebft \u0111\u1ecbnh. */\n"
"QLabel[trangThai=\"tang\"]    { col"
                        "or: #10b981; font-weight: bold; }\n"
"QLabel[trangThai=\"giam\"]    { color: #ef4444; font-weight: bold; }\n"
"QLabel[trangThai=\"giu\"]     { color: #64748b; font-weight: bold; }\n"
"QLabel[trangThai=\"canhBao\"] { color: #eab308; font-weight: bold; }\n"
"QLabel[trangThai=\"anToan\"]  { color: #10b981; }\n"
"\n"
"/* =========================================================\n"
"   Thanh cu\u1ed9n - gi\u1eef gi\u1ed1ng h\u1ec7t pos.ui cho \u0111\u1ed3ng b\u1ed9 to\u00e0n app\n"
"   Tay k\u00e9o bo tr\u00f2n #cbd5e1, hover #94a3b8, r\u1ed9ng 10px, b\u1ecf m\u0169i t\u00ean.\n"
"   N\u1ebfu \u0111\u1ed5i \u1edf \u0111\u00e2y th\u00ec nh\u1edb s\u1eeda c\u1ea3 pos.ui cho kh\u1edbp.\n"
"   ========================================================= */\n"
"\n"
"\n"
"/* ===== Vertical scrollbar ===== */\n"
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
"    m"
                        "in-height: 35px;\n"
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
"\n"
"/* ===== Horizontal scrollbar ===== */\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #f8fafc;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #cbd5e1;\n"
"    min-width: 35px;\n"
"    border-radius: 5px;\n"
"}\n"
""
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
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 64))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setStyleSheet(u"#frame_10 {\n"
"		background-color: transparent;\n"
"		color: black;\n"
"		border: none;\n"
"		outline: none;\n"
"		padding: 0px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_10)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 2, 0, 12)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lblDashboardSubtitle = QLabel(self.frame_10)
        self.lblDashboardSubtitle.setObjectName(u"lblDashboardSubtitle")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDashboardSubtitle)

        self.lblDashboardSubtitle.raise_()
        self.label.raise_()

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(140, 40))
        self.pushButton.setMaximumSize(QSize(140, 40))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(4)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(7)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setStyleSheet(u"#frame_6 {\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #e2e8f0;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(14, 12, 14, 14)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setStyleSheet(u"QFrame#frame_8 {\n"
"	background-color: #f1f5f9;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QFrame#frame_8:hover {\n"
"	background-color: #e2e8f0;\n"
"	border: 1px solid #cbd5e1;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_8, 2, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy5.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy5)
        self.frame_9.setMinimumSize(QSize(150, 0))
        self.frame_9.setStyleSheet(u"QFrame#frame_9 {\n"
"	background-color: #f1f5f9;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QFrame#frame_9:hover {\n"
"	background-color: #e2e8f0;\n"
"	border: 1px solid #cbd5e1;\n"
"}")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_9, 2, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.gridLayout_2.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy5.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy5)
        self.frame_11.setMinimumSize(QSize(150, 0))
        self.frame_11.setStyleSheet(u"QFrame#frame_11 {\n"
"	background-color: #f1f5f9;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QFrame#frame_11:hover {\n"
"	background-color: #e2e8f0;\n"
"	border: 1px solid #cbd5e1;\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.frame_7.setStyleSheet(u"QFrame#frame_7 {\n"
"	background-color: #f1f5f9;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QFrame#frame_7:hover {\n"
"	background-color: #e2e8f0;\n"
"	border: 1px solid #cbd5e1;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(3)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_13)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy5.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy5)
        self.frame_17.setStyleSheet(u"#frame_17 {\n"
"		background-color: white;\n"
"		border-radius: 10px;\n"
"		padding: 3px 8px;\n"
"		border: 1px solid #e2e8f0; \n"
"}")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_17)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setPointSize(20)
        self.label_14.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_14)

        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)


        self.gridLayout_4.addWidget(self.frame_17, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy5.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy5)
        self.frame_16.setStyleSheet(u"#frame_16 {\n"
"		background-color:  white;\n"
"		border-radius: 10px;\n"
"		padding: 3px 8px;\n"
"		border: 1px solid #e2e8f0; \n"
"}")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)


        self.gridLayout_4.addWidget(self.frame_16, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy5.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy5)
        self.frame_15.setStyleSheet(u"#frame_15 {\n"
"		background-color: white;\n"
"		border-radius: 10px;\n"
"		padding: 3px 8px;\n"
"		border: 1px solid #e2e8f0; \n"
"}")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(False)
        self.label_11.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_11)

        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)


        self.gridLayout_4.addWidget(self.frame_15, 1, 1, 1, 1)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy5.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy5)
        self.frame_14.setStyleSheet(u"#frame_14 {\n"
"		background-color: white;\n"
"		border-radius: 10px;\n"
"		padding: 3px 8px;\n"
"		border: 1px solid #e2e8f0; \n"
"}")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_5.raise_()
        self.label_12.raise_()
        self.label_4.raise_()

        self.gridLayout_4.addWidget(self.frame_14, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_13)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(5)
        sizePolicy7.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy7)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_bottom = QHBoxLayout(self.frame_2)
        self.horizontalLayout_bottom.setSpacing(12)
        self.horizontalLayout_bottom.setObjectName(u"horizontalLayout_bottom")
        self.horizontalLayout_bottom.setContentsMargins(0, 0, 0, 0)
        self.frame_chart = QFrame(self.frame_2)
        self.frame_chart.setObjectName(u"frame_chart")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(6)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_chart.sizePolicy().hasHeightForWidth())
        self.frame_chart.setSizePolicy(sizePolicy8)
        self.frame_chart.setStyleSheet(u"QFrame#frame_chart { \n"
"	background-color: white; \n"
"	border-radius: 10px; \n"
"	border: 1px solid #e2e8f0; \n"
"}")
        self.frame_chart.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_8 = QVBoxLayout(self.frame_chart)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.frame_18 = QFrame(self.frame_chart)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 32))
        self.frame_18.setMaximumSize(QSize(16777215, 32))
        self.frame_18.setStyleSheet(u"#frame_18{\n"
"	padding: 0px;\n"
"}")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.frame_18)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(90, 16777215))
        self.comboBox.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.chart_container = QWidget(self.frame_chart)
        self.chart_container.setObjectName(u"chart_container")

        self.verticalLayout_8.addWidget(self.chart_container)


        self.horizontalLayout_bottom.addWidget(self.frame_chart)

        self.frame_table = QFrame(self.frame_2)
        self.frame_table.setObjectName(u"frame_table")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(4)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_table.sizePolicy().hasHeightForWidth())
        self.frame_table.setSizePolicy(sizePolicy9)
        self.frame_table.setStyleSheet(u"QFrame#frame_table { \n"
"	background-color: white; \n"
"	border-radius: 10px; \n"
"	border: 1px solid #e2e8f0; \n"
"}")
        self.frame_table.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_bottom.addWidget(self.frame_table)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"T\u1ed5ng quan h\u1ec7 th\u1ed1ng", None))
        self.lblDashboardSubtitle.setText(QCoreApplication.translate("Form", u"Theo d\u00f5i doanh thu, h\u00f3a \u0111\u01a1n v\u00e0 ho\u1ea1t \u0111\u1ed9ng kinh doanh trong ng\u00e0y", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"T\u1ea3i l\u1ea1i d\u1eef li\u1ec7u", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Thao t\u00e1c nhanh", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"T\u1ed5ng h\u00f3a \u0111\u01a1n", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"S\u1ed1 h\u00f3a \u0111\u01a1n", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"t\u1ec9 l\u1ec7 t\u0103ng tr\u01b0\u1edfng", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"S\u1eafp h\u1ebft h\u00e0ng", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"s\u1ed1 h\u00e0ng s\u1eafp h\u1ebft", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"C\u1ea7n c\u1eadp nh\u1eadt ngay", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Kh\u00e1ch h\u00e0ng m\u1edbi", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"S\u1ed1 kh\u00e1ch h\u00e0ng m\u1edbi", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"t\u1ec9 l\u1ec7 t\u0103ng tr\u01b0\u1edfng", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Doanh thu h\u00f4m nay", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"s\u1ed1 ti\u1ec1n h\u00f4m nay", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"t\u1ec9 l\u1ec7 t\u0103ng tr\u01b0\u1edfng", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Doanh thu th\u00e1ng n\u00e0y", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Th\u00e1ng 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Th\u00e1ng 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Th\u00e1ng 3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Th\u00e1ng 4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"Th\u00e1ng 5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"Th\u00e1ng 6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"Th\u00e1ng 7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"Th\u00e1ng 8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"Th\u00e1ng 9", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"Th\u00e1ng 10", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"Th\u00e1ng 11", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Form", u"Th\u00e1ng 12", None))

    # retranslateUi

