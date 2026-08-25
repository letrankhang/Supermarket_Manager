# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verification_code.ui'
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 680)
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"    background-color: #f3f4f6;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.code_card = QFrame(self.centralwidget)
        self.code_card.setObjectName(u"code_card")
        self.code_card.setMinimumSize(QSize(420, 445))
        self.code_card.setMaximumSize(QSize(420, 445))
        self.code_card.setStyleSheet(u"#code_card {\n"
"    background-color: #ffffff;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #e5e7eb;\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"#lblTitle {\n"
"    color: #0c2b82;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#lblSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#dividerLine {\n"
"    background-color: #e5e7eb;\n"
"    border: none;\n"
"}\n"
"\n"
"#lblField {\n"
"    color: #374151;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#lblCopyright {\n"
"    color: #9ca3af;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 6px;\n"
"    padding: 0px 12px;\n"
"    background-color: #ffffff;\n"
"    color: #111827;\n"
"    font-size: 13px;\n"
"    selection-background-color: #0c2b82;\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0c2b82;\n"
"}\n"
"\n"
"#pushButton_ac"
                        "cept {\n"
"    background-color: #002b9a;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#pushButton_accept:hover {\n"
"    background-color: #00227b;\n"
"}\n"
"\n"
"#pushButton_accept:pressed {\n"
"    background-color: #001857;\n"
"}\n"
"\n"
"#pushButton_accept:disabled {\n"
"    background-color: #9ca3af;\n"
"}\n"
"\n"
"#pushButton_resend, #pushButton_2 {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0c2b82;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#pushButton_resend:hover, #pushButton_2:hover {\n"
"    color: #081d59;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"#pushButton_resend:disabled {\n"
"    color: #9ca3af;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"#lblBackLogin {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0c2b82;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#lblBackLogin:hover {\n"
" "
                        "   color: #081d59;\n"
"    text-decoration: underline;\n"
"}")
        self.code_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.code_card.setFrameShadow(QFrame.Shadow.Raised)
        self.lblLogo = QLabel(self.code_card)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setGeometry(QRect(140, 20, 140, 100))
        self.lblLogo.setMinimumSize(QSize(140, 100))
        self.lblLogo.setMaximumSize(QSize(140, 100))
        self.lblLogo.setPixmap(QPixmap(u"../../assets/images/logo.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitle = QLabel(self.code_card)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setGeometry(QRect(10, 121, 401, 30))
        self.lblTitle.setMinimumSize(QSize(0, 30))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSubtitle = QLabel(self.code_card)
        self.lblSubtitle.setObjectName(u"lblSubtitle")
        self.lblSubtitle.setGeometry(QRect(10, 151, 401, 21))
        self.lblSubtitle.setMinimumSize(QSize(0, 21))
        self.lblSubtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dividerLine = QFrame(self.code_card)
        self.dividerLine.setObjectName(u"dividerLine")
        self.dividerLine.setGeometry(QRect(40, 195, 341, 1))
        self.dividerLine.setMinimumSize(QSize(0, 1))
        self.dividerLine.setMaximumSize(QSize(16777215, 1))
        self.dividerLine.setFrameShape(QFrame.Shape.HLine)
        self.dividerLine.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblField = QLabel(self.code_card)
        self.lblField.setObjectName(u"lblField")
        self.lblField.setGeometry(QRect(40, 208, 75, 31))
        self.lblField.setMinimumSize(QSize(0, 24))
        self.lineEdit_code = QLineEdit(self.code_card)
        self.lineEdit_code.setObjectName(u"lineEdit_code")
        self.lineEdit_code.setGeometry(QRect(40, 239, 341, 42))
        self.lineEdit_code.setMinimumSize(QSize(0, 42))
        self.lineEdit_code.setMaximumSize(QSize(16777215, 42))
        self.lineEdit_code.setMaxLength(6)
        self.pushButton_accept = QPushButton(self.code_card)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        self.pushButton_accept.setGeometry(QRect(40, 330, 341, 61))
        self.pushButton_accept.setMinimumSize(QSize(0, 61))
        self.pushButton_accept.setMaximumSize(QSize(16777215, 61))
        self.pushButton_accept.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblBackLogin = QPushButton(self.code_card)
        self.lblBackLogin.setObjectName(u"lblBackLogin")
        self.lblBackLogin.setGeometry(QRect(230, 390, 61, 51))
        self.lblBackLogin.setMinimumSize(QSize(0, 24))
        font = QFont()
        font.setBold(True)
        self.lblBackLogin.setFont(font)
        self.lblBackLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblBackLogin.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.code_card)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 281, 341, 41))
        self.horizontalLayout_resend = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_resend.setSpacing(0)
        self.horizontalLayout_resend.setObjectName(u"horizontalLayout_resend")
        self.horizontalLayout_resend.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_resend.addItem(self.horizontalSpacer)

        self.pushButton_resend = QPushButton(self.layoutWidget)
        self.pushButton_resend.setObjectName(u"pushButton_resend")
        self.pushButton_resend.setMinimumSize(QSize(0, 24))
        self.pushButton_resend.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_resend.addWidget(self.pushButton_resend)

        self.label = QLabel(self.code_card)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 390, 123, 51))
        self.label.setMinimumSize(QSize(123, 0))
        self.label.setMaximumSize(QSize(123, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #6b7280;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogo.raise_()
        self.lblTitle.raise_()
        self.lblSubtitle.raise_()
        self.dividerLine.raise_()
        self.lblField.raise_()
        self.lineEdit_code.raise_()
        self.pushButton_accept.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.lblBackLogin.raise_()

        self.gridLayout.addWidget(self.code_card, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RetailPro ERP / X\u00e1c th\u1ef1c m\u00e3", None))
        self.lblLogo.setText("")
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"RetailPro ERP", None))
        self.lblSubtitle.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp m\u00e3 x\u00e1c th\u1ef1c \u0111\u00e3 g\u1eedi t\u1edbi email c\u1ee7a b\u1ea1n", None))
        self.lblField.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 x\u00e1c th\u1ef1c:", None))
        self.lineEdit_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp 6 ch\u1eef s\u1ed1", None))
        self.pushButton_accept.setText(QCoreApplication.translate("MainWindow", u"X\u00e1c nh\u1eadn", None))
        self.lblBackLogin.setText(QCoreApplication.translate("MainWindow", u"t\u1ea1i \u0111\u00e2y", None))
        self.pushButton_resend.setText(QCoreApplication.translate("MainWindow", u"G\u1eedi l\u1ea1i m\u00e3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quay l\u1ea1i \u0111\u0103ng nh\u1eadp", None))
    # retranslateUi

