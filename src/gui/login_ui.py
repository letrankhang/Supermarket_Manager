# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

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
        self.login_card = QFrame(self.centralwidget)
        self.login_card.setObjectName(u"login_card")
        self.login_card.setMinimumSize(QSize(420, 520))
        self.login_card.setMaximumSize(QSize(420, 520))
        self.login_card.setStyleSheet(u"#login_card {\n"
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
"/* N\u00fat con m\u1eaft \u1ea9n/hi\u1ec7n m\u1eadt kh\u1ea9u n\u1eb1m b\u00ean trong \u00f4 m\u1eadt kh\u1ea9u */\n"
"QToolButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    background-color: transparent;\n"
"    color: #4b5563;\n"
"    font-size: 13px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    b"
                        "order: 1px solid #d1d5db;\n"
"    border-radius: 4px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border-color: #0c2b82;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #0c2b82;\n"
"    border-color: #0c2b82;\n"
"    image: url(assets/images/check.png);\n"
"}\n"
"\n"
"#pushButton_forgotpassword {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0c2b82;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#pushButton_forgotpassword:hover {\n"
"    color: #081d59;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"#pushButton_login {\n"
"    background-color: #002b9a;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#pushButton_login:hover {\n"
"    background-color: #00227b;\n"
"}\n"
"\n"
"#pushButton_login:pressed {\n"
"    background-color: #001857;\n"
"}")
        self.login_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_card.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.login_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 10, 140, 100))
        self.label_4.setMinimumSize(QSize(140, 100))
        self.label_4.setMaximumSize(QSize(17, 17))
        self.label_4.setStyleSheet(u"background-color: transparent; border: none;")
        self.label_4.setPixmap(QPixmap(u"../../assets/images/logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.login_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 100, 140, 30))
        self.label_3.setStyleSheet(u"color: #0c2b82; font-size: 22px; font-weight: bold;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.login_card)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 130, 401, 21))
        self.label.setStyleSheet(u"color: #6b7280; font-size: 13px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dividerLine = QFrame(self.login_card)
        self.dividerLine.setObjectName(u"dividerLine")
        self.dividerLine.setGeometry(QRect(41, 174, 340, 1))
        self.dividerLine.setMinimumSize(QSize(0, 1))
        self.dividerLine.setMaximumSize(QSize(16777215, 1))
        self.dividerLine.setStyleSheet(u"background-color: #e5e7eb; border: none;")
        self.dividerLine.setFrameShape(QFrame.Shape.HLine)
        self.dividerLine.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_5 = QLabel(self.login_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 190, 91, 31))
        self.label_5.setStyleSheet(u"color: #374151; font-size: 13px; font-weight: 600;")
        self.lineEdit_username = QLineEdit(self.login_card)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(40, 220, 341, 42))
        self.lineEdit_username.setMinimumSize(QSize(0, 42))
        self.label_6 = QLabel(self.login_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 270, 59, 31))
        self.label_6.setStyleSheet(u"color: #374151; font-size: 13px; font-weight: 600;")
        self.lineEdit_passwprd = QLineEdit(self.login_card)
        self.lineEdit_passwprd.setObjectName(u"lineEdit_passwprd")
        self.lineEdit_passwprd.setGeometry(QRect(40, 300, 341, 42))
        self.lineEdit_passwprd.setMinimumSize(QSize(0, 42))
        self.lineEdit_passwprd.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_login = QPushButton(self.login_card)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(40, 400, 341, 61))
        self.pushButton_login.setMinimumSize(QSize(0, 44))
        self.pushButton_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblCopyright = QLabel(self.login_card)
        self.lblCopyright.setObjectName(u"lblCopyright")
        self.lblCopyright.setGeometry(QRect(130, 470, 169, 41))
        self.lblCopyright.setStyleSheet(u"color: #9ca3af; font-size: 12px;")
        self.lblCopyright.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(self.login_card)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 350, 341, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_forgotpassword = QPushButton(self.layoutWidget)
        self.pushButton_forgotpassword.setObjectName(u"pushButton_forgotpassword")
        self.pushButton_forgotpassword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton_forgotpassword)


        self.gridLayout.addWidget(self.login_card, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RetailPro ERP / \u0110\u0103ng nh\u1eadp", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RetailPro ERP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Vui l\u00f2ng nh\u1eadp th\u00f4ng tin \u0111\u1ec3 truy c\u1eadp h\u1ec7 th\u1ed1ng</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111\u0103ng nh\u1eadp:", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email ho\u1eb7c t\u00ean \u0111\u0103ng nh\u1eadp", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u:", None))
        self.lineEdit_passwprd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.lblCopyright.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2026 RetailPro ERP", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Ghi nh\u1edb t\u00f4i", None))
        self.pushButton_forgotpassword.setText(QCoreApplication.translate("MainWindow", u"Qu\u00ean m\u1eadt kh\u1ea9u?", None))
    # retranslateUi

