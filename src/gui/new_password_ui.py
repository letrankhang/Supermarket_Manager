# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_password.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

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
        self.newpass_card = QFrame(self.centralwidget)
        self.newpass_card.setObjectName(u"newpass_card")
        self.newpass_card.setMinimumSize(QSize(420, 483))
        self.newpass_card.setMaximumSize(QSize(420, 483))
        self.newpass_card.setStyleSheet(u"#newpass_card {\n"
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
"#lblField1, #lblField2 {\n"
"    color: #374151;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#lblHint {\n"
"    color: #9ca3af;\n"
"    font-size: 12px;\n"
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
""
                        "\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0c2b82;\n"
"}\n"
"\n"
"QToolButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"#pushButton_accept {\n"
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
"#lblBackLogin {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0c2b82;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#lblBackLogin:hover {\n"
"    color: #081d59;\n"
"    text-decoration: underline;\n"
"}")
        self.newpass_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.newpass_card.setFrameShadow(QFrame.Shadow.Raised)
        self.lblLogo = QLabel(self.newpass_card)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setGeometry(QRect(140, 10, 140, 100))
        self.lblLogo.setMinimumSize(QSize(140, 100))
        self.lblLogo.setMaximumSize(QSize(112, 80))
        self.lblLogo.setPixmap(QPixmap(u"../../assets/images/logo.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitle = QLabel(self.newpass_card)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setGeometry(QRect(10, 101, 401, 30))
        self.lblTitle.setMinimumSize(QSize(0, 30))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSubtitle = QLabel(self.newpass_card)
        self.lblSubtitle.setObjectName(u"lblSubtitle")
        self.lblSubtitle.setGeometry(QRect(2, 131, 411, 21))
        self.lblSubtitle.setMinimumSize(QSize(0, 21))
        self.lblSubtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dividerLine = QFrame(self.newpass_card)
        self.dividerLine.setObjectName(u"dividerLine")
        self.dividerLine.setGeometry(QRect(40, 167, 341, 1))
        self.dividerLine.setMinimumSize(QSize(0, 1))
        self.dividerLine.setMaximumSize(QSize(16777215, 1))
        self.dividerLine.setFrameShape(QFrame.Shape.HLine)
        self.dividerLine.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblField1 = QLabel(self.newpass_card)
        self.lblField1.setObjectName(u"lblField1")
        self.lblField1.setGeometry(QRect(40, 179, 86, 31))
        self.lblField1.setMinimumSize(QSize(0, 24))
        self.lineEdit_newpassword = QLineEdit(self.newpass_card)
        self.lineEdit_newpassword.setObjectName(u"lineEdit_newpassword")
        self.lineEdit_newpassword.setGeometry(QRect(40, 210, 341, 42))
        self.lineEdit_newpassword.setMinimumSize(QSize(0, 42))
        self.lineEdit_newpassword.setMaximumSize(QSize(16777215, 42))
        self.lineEdit_newpassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.lblField2 = QLabel(self.newpass_card)
        self.lblField2.setObjectName(u"lblField2")
        self.lblField2.setGeometry(QRect(40, 260, 138, 31))
        self.lblField2.setMinimumSize(QSize(0, 24))
        self.lineEdit_againpassword = QLineEdit(self.newpass_card)
        self.lineEdit_againpassword.setObjectName(u"lineEdit_againpassword")
        self.lineEdit_againpassword.setGeometry(QRect(40, 291, 341, 42))
        self.lineEdit_againpassword.setMinimumSize(QSize(0, 42))
        self.lineEdit_againpassword.setMaximumSize(QSize(16777215, 42))
        self.lineEdit_againpassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_accept = QPushButton(self.newpass_card)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        self.pushButton_accept.setGeometry(QRect(40, 360, 341, 61))
        self.pushButton_accept.setMinimumSize(QSize(0, 61))
        self.pushButton_accept.setMaximumSize(QSize(16777215, 61))
        self.pushButton_accept.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBackToLogin = QPushButton(self.newpass_card)
        self.btnBackToLogin.setObjectName(u"btnBackToLogin")
        self.btnBackToLogin.setGeometry(QRect(240, 420, 51, 61))
        self.btnBackToLogin.setMinimumSize(QSize(0, 24))
        self.btnBackToLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBackToLogin.setStyleSheet(u"QPushButton#btnBackToLogin {\n"
"    background-color: transparent;\n"
"    color: #002b9a;\n"
"    border: none;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QPushButton#btnBackToLogin:hover {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton#btnBackToLogin:pressed {\n"
"    color: #1e40af;\n"
"}")
        self.label = QLabel(self.newpass_card)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 420, 121, 61))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #6b7280;")

        self.gridLayout.addWidget(self.newpass_card, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RetailPro ERP / \u0110\u1eb7t m\u1eadt kh\u1ea9u m\u1edbi", None))
        self.lblLogo.setText("")
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"RetailPro ERP", None))
        self.lblSubtitle.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1eb7t m\u1eadt kh\u1ea9u m\u1edbi cho t\u00e0i kho\u1ea3n c\u1ee7a b\u1ea1n", None))
        self.lblField1.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u m\u1edbi:", None))
        self.lineEdit_newpassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u1ed1i thi\u1ec3u 8 k\u00fd t\u1ef1, g\u1ed3m c\u1ea3 ch\u1eef v\u00e0 s\u1ed1", None))
        self.lblField2.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp l\u1ea1i m\u1eadt kh\u1ea9u m\u1edbi:", None))
        self.lineEdit_againpassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.pushButton_accept.setText(QCoreApplication.translate("MainWindow", u"X\u00e1c nh\u1eadn", None))
        self.btnBackToLogin.setText(QCoreApplication.translate("MainWindow", u"t\u1ea1i \u0111\u00e2y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quay l\u1ea1i \u0111\u0103ng nh\u1eadp", None))
    # retranslateUi

