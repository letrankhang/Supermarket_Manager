# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_UserDialog(object):
    def setupUi(self, UserDialog):
        if not UserDialog.objectName():
            UserDialog.setObjectName(u"UserDialog")
        UserDialog.resize(400, 550)
        self.verticalLayout = QVBoxLayout(UserDialog)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.lblUsername = QLabel(UserDialog)
        self.lblUsername.setObjectName(u"lblUsername")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUsername)

        self.txtUsername = QLineEdit(UserDialog)
        self.txtUsername.setObjectName(u"txtUsername")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtUsername)

        self.lblFullName = QLabel(UserDialog)
        self.lblFullName.setObjectName(u"lblFullName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFullName)

        self.txtFullName = QLineEdit(UserDialog)
        self.txtFullName.setObjectName(u"txtFullName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtFullName)

        self.lblEmail = QLabel(UserDialog)
        self.lblEmail.setObjectName(u"lblEmail")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblEmail)

        self.txtEmail = QLineEdit(UserDialog)
        self.txtEmail.setObjectName(u"txtEmail")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtEmail)

        self.lblPassword = QLabel(UserDialog)
        self.lblPassword.setObjectName(u"lblPassword")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblPassword)

        self.txtPassword = QLineEdit(UserDialog)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtPassword)

        self.lblRole = QLabel(UserDialog)
        self.lblRole.setObjectName(u"lblRole")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblRole)

        self.cboRole = QComboBox(UserDialog)
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.setObjectName(u"cboRole")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cboRole)

        self.lblStatus = QLabel(UserDialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.chkStatus = QCheckBox(UserDialog)
        self.chkStatus.setObjectName(u"chkStatus")
        self.chkStatus.setChecked(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.chkStatus)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(UserDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(UserDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(UserDialog)
        self.btnCancel.clicked.connect(UserDialog.reject)
        self.btnSave.clicked.connect(UserDialog.accept)

        QMetaObject.connectSlotsByName(UserDialog)
    # setupUi

    def retranslateUi(self, UserDialog):
        UserDialog.setWindowTitle(QCoreApplication.translate("UserDialog", u"Th\u00eam t\u00e0i kho\u1ea3n", None))
        UserDialog.setStyleSheet(QCoreApplication.translate("UserDialog", u"/* QSS g\u1ed1c t\u1eeb RetailPro ERP */\n"
"QDialog {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-weight: bold;\n"
"    color: #334155;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit, QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QLineEdit:focus, QComboBox:focus {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f1f5f9;\n"
"    color: #64748b;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-weight: bold;\n"
"    border-radius: 6px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton#btnSave {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"}\n"
"QPushButton#btnSave:hover { background-color: #2563eb; }\n"
"\n"
"QPushButton#btnCancel {\n"
"    background-color: #e2e8f0;\n"
"    color: #475569;\n"
"}\n"
"QPushButton#btnCancel:hover { background-color: #cbd5"
                        "e1; }\n"
"", None))
        self.lblUsername.setText(QCoreApplication.translate("UserDialog", u"T\u00ean \u0111\u0103ng nh\u1eadp:", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp t\u00ean \u0111\u0103ng nh\u1eadp...", None))
        self.lblFullName.setText(QCoreApplication.translate("UserDialog", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.txtFullName.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp h\u1ecd v\u00e0 t\u00ean...", None))
        self.lblEmail.setText(QCoreApplication.translate("UserDialog", u"Email:", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp email...", None))
        self.lblPassword.setText(QCoreApplication.translate("UserDialog", u"M\u1eadt kh\u1ea9u:", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp m\u1eadt kh\u1ea9u...", None))
        self.lblRole.setText(QCoreApplication.translate("UserDialog", u"Ch\u1ee9c v\u1ee5:", None))
        self.cboRole.setItemText(0, QCoreApplication.translate("UserDialog", u"Admin", None))
        self.cboRole.setItemText(1, QCoreApplication.translate("UserDialog", u"Cashier", None))
        self.cboRole.setItemText(2, QCoreApplication.translate("UserDialog", u"Warehouse", None))

        self.lblStatus.setText(QCoreApplication.translate("UserDialog", u"Tr\u1ea1ng th\u00e1i:", None))
        self.chkStatus.setStyleSheet(QCoreApplication.translate("UserDialog", u"QCheckBox { color: #10b981; font-weight: bold; }", None))
        self.chkStatus.setText(QCoreApplication.translate("UserDialog", u"Ho\u1ea1t \u0111\u1ed9ng", None))
        self.btnCancel.setText(QCoreApplication.translate("UserDialog", u"H\u1ee6Y", None))
        self.btnSave.setText(QCoreApplication.translate("UserDialog", u"L\u01afU", None))
    # retranslateUi

