# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgot_password.ui'
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
        self.forgot_card = QFrame(self.centralwidget)
        self.forgot_card.setObjectName(u"forgot_card")
        self.forgot_card.setMinimumSize(QSize(420, 413))
        self.forgot_card.setMaximumSize(QSize(420, 413))
        self.forgot_card.setStyleSheet(u"#forgot_card {\n"
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
"#pushButton_"
                        "accept {\n"
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
        self.forgot_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.forgot_card.setFrameShadow(QFrame.Shadow.Raised)
        self.lblLogo = QLabel(self.forgot_card)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setGeometry(QRect(140, 10, 140, 100))
        self.lblLogo.setMinimumSize(QSize(140, 100))
        self.lblLogo.setMaximumSize(QSize(140, 100))
        self.lblLogo.setPixmap(QPixmap(u"../../assets/images/logo.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTitle = QLabel(self.forgot_card)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setGeometry(QRect(10, 100, 401, 31))
        self.lblTitle.setMinimumSize(QSize(0, 30))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSubtitle = QLabel(self.forgot_card)
        self.lblSubtitle.setObjectName(u"lblSubtitle")
        self.lblSubtitle.setGeometry(QRect(10, 111, 401, 61))
        self.lblSubtitle.setMinimumSize(QSize(0, 21))
        self.lblSubtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dividerLine = QFrame(self.forgot_card)
        self.dividerLine.setObjectName(u"dividerLine")
        self.dividerLine.setGeometry(QRect(40, 173, 341, 1))
        self.dividerLine.setMinimumSize(QSize(0, 1))
        self.dividerLine.setMaximumSize(QSize(16777215, 1))
        self.dividerLine.setFrameShape(QFrame.Shape.HLine)
        self.dividerLine.setFrameShadow(QFrame.Shadow.Sunken)
        self.lblField = QLabel(self.forgot_card)
        self.lblField.setObjectName(u"lblField")
        self.lblField.setGeometry(QRect(40, 190, 35, 31))
        self.lblField.setMinimumSize(QSize(0, 24))
        self.lineEdit_email = QLineEdit(self.forgot_card)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(40, 221, 341, 42))
        self.lineEdit_email.setMinimumSize(QSize(0, 42))
        self.lineEdit_email.setMaximumSize(QSize(16777215, 42))
        self.lineEdit_email.setStyleSheet(u"")
        self.pushButton_accept = QPushButton(self.forgot_card)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        self.pushButton_accept.setGeometry(QRect(40, 290, 341, 61))
        self.pushButton_accept.setMinimumSize(QSize(0, 61))
        self.pushButton_accept.setMaximumSize(QSize(16777215, 61))
        self.pushButton_accept.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblBackLogin = QPushButton(self.forgot_card)
        self.lblBackLogin.setObjectName(u"lblBackLogin")
        self.lblBackLogin.setGeometry(QRect(240, 355, 51, 51))
        self.lblBackLogin.setMinimumSize(QSize(0, 24))
        font = QFont()
        font.setBold(True)
        self.lblBackLogin.setFont(font)
        self.lblBackLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label = QLabel(self.forgot_card)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 350, 111, 61))
        palette = QPalette()
        brush = QBrush(QColor(107, 114, 128, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(107, 114, 128, 128))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        self.label.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #6b7280;\n"
"")

        self.gridLayout.addWidget(self.forgot_card, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RetailPro ERP / Qu\u00ean m\u1eadt kh\u1ea9u", None))
        self.lblLogo.setText("")
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"RetailPro ERP", None))
        self.lblSubtitle.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp email \u0111\u00e3 \u0111\u0103ng k\u00fd \u0111\u1ec3 nh\u1eadn m\u00e3 x\u00e1c th\u1ef1c", None))
        self.lblField.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@example.com", None))
        self.pushButton_accept.setText(QCoreApplication.translate("MainWindow", u"G\u1eedi m\u00e3 x\u00e1c th\u1ef1c", None))
        self.lblBackLogin.setText(QCoreApplication.translate("MainWindow", u"t\u1ea1i \u0111\u00e2y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quay l\u1ea1i \u0111\u0103ng nh\u1eadp", None))
    # retranslateUi

