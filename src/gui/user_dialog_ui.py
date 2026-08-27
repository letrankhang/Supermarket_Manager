# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_UserDialog(object):
    def setupUi(self, UserDialog):
        if not UserDialog.objectName():
            UserDialog.setObjectName(u"UserDialog")
        UserDialog.resize(400, 550)
        UserDialog.setStyleSheet(u"QDialog#UserDialog {\n"
"    background-color: #ffffff;\n"
"    color: #0f172a;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QWidget {\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QLineEdit,\n"
"QComboBox,\n"
"QDateEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 12px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"    selection-background-color: #1d4ed8;\n"
"    selection-color: #ffffff;\n"
"}\n"
"QTextEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"    selection-background-color: #1d4ed8;\n"
"    selection-color: #ffffff;\n"
"}\n"
"QLineEdit:hover,\n"
"QComboBox:hover,\n"
"QDateEdit:hover,"
                        "\n"
"QSpinBox:hover,\n"
"QDoubleSpinBox:hover,\n"
"QTextEdit:hover {\n"
"    border: 1px solid #cbd5e1;\n"
"}\n"
"QLineEdit:focus,\n"
"QComboBox:focus,\n"
"QDateEdit:focus,\n"
"QSpinBox:focus,\n"
"QDoubleSpinBox:focus,\n"
"QTextEdit:focus {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QLineEdit:disabled,\n"
"QComboBox:disabled,\n"
"QDateEdit:disabled,\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #94a3b8;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 26px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(assets/images/chevron-down.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"    image: url(assets/images/chevron-up.png);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    pad"
                        "ding: 4px;\n"
"    outline: none;\n"
"    selection-background-color: #eff6ff;\n"
"    selection-color: #1d4ed8;\n"
"}\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button,\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button {\n"
"    subcontrol-origin: border;\n"
"    width: 20px;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDateEdit::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button,\n"
"QDateEdit::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover,\n"
"QDoubleSpinBox::down-button:hover,\n"
"QDateEdit::up-button:hover,\n"
"QDateEdit::down-button:hover {\n"
"    background-color: #f1f5f9;\n"
"}\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QDateEdit::up-arrow {\n"
"    image: ur"
                        "l(assets/images/chevron-up.png);\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QDateEdit::down-arrow {\n"
"    image: url(assets/images/chevron-down.png);\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"QCheckBox {\n"
"    background-color: transparent;\n"
"    color: #334155;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    spacing: 8px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 4px;\n"
"    background-color: #ffffff;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight"
                        ": bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #dbeafe;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"QPushButton#RowActionButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0px;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"    min-height: 28px;\n"
"    max-height: 28px;\n"
"}\n"
"QPushButton#RowActionButton:hover {\n"
"    background-color: #eff6ff;\n"
"}\n"
"QPushButton#RowActionButton:pressed {\n"
"    background-color: #dbeafe;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: #f1f5f9;\n"
"    font-size: 13px;\n"
"    color: #334155;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid "
                        "#f1f5f9;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"QHeaderView {\n"
"    background-color: #f8fafc;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc;\n"
"    color: #64748b;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"    padding: 10px 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #f8fafc;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel[badge=\"info\"] {\n"
"    background-color: #dbeafe;\n"
"    color: #1d4ed8;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"success\"] {\n"
"    background-color: #d1fae5;\n"
"    color: #059669;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"warning\"] {\n"
"    backgroun"
                        "d-color: #ffedd5;\n"
"    color: #ea580c;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"danger\"] {\n"
"    background-color: #fee2e2;\n"
"    color: #dc2626;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"neutral\"] {\n"
"    background-color: #e2e8f0;\n"
"    color: #64748b;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[badge=\"violet\"] {\n"
"    background-color: #ede9fe;\n"
"    color: #6d28d9;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[trend=\"up\"] {\n"
"    background-color: #ecfdf5;\n"
"    color: #059669;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[trend=\"down\"] {\n"
"    background-color: #fef2f2;\n"
""
                        "    color: #dc2626;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[trend=\"flat\"] {\n"
"    background-color: #f1f5f9;\n"
"    color: #64748b;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[state=\"up\"] {\n"
"    color: #10b981;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"down\"] {\n"
"    color: #ef4444;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"flat\"] {\n"
"    color: #64748b;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"warning\"] {\n"
"    color: #eab308;\n"
"    font-weight: bold;\n"
"}\n"
"QLabel[state=\"safe\"] {\n"
"    color: #10b981;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollArea > QWidget > QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"QAbstractScrollArea::viewport {\n"
"    background-color: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    bac"
                        "kground-color: transparent;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #cbd5e1;\n"
"    min-height: 35px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #94a3b8;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: #64748b;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: transparent;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
""
                        "    background-color: #cbd5e1;\n"
"    min-width: 35px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #94a3b8;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: #64748b;\n"
"}\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::left-arrow:horizontal,\n"
"QScrollBar::right-arrow:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    color: #334155;\n"
"    border-radius: 6px;\n"
"    padding: 7px 18px;\n"
"    font-si"
                        "ze: 13px;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #e2e8f0;\n"
"    margin: 6px 4px;\n"
"}\n"
"\n"
"QLabel#lblHeaderTitle {\n"
"    color: #0f172a;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QLabel#lblHeaderSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QLabel#lblUsername,\n"
"QLabel#lblFullName,\n"
"QLabel#lblEmail,\n"
"QLabel#lblPassword,\n"
"QLabel#lblRole,\n"
"QLabel#lblStatus {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* O tich trang thai: hinh tron, tich vao thi ca o lan chu deu xanh la */\n"
"QCheckBox#chkStatus {\n"
"    color: #64748b;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    spacing: 8px;\n"
"}\n"
"QCheckBox#chkStatus::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 1px solid #cbd5e1;\n"
"   "
                        " border-radius: 9px;\n"
"    background-color: #ffffff;\n"
"}\n"
"QCheckBox#chkStatus::indicator:hover {\n"
"    border: 1px solid #059669;\n"
"}\n"
"QCheckBox#chkStatus::indicator:checked {\n"
"    background-color: #059669;\n"
"    border: 1px solid #059669;\n"
"    image: url(assets/images/check-white.png);\n"
"}\n"
"QCheckBox#chkStatus:checked {\n"
"    color: #059669;\n"
"}\n"
"QCheckBox#chkStatus:!checked {\n"
"    color: #dc2626;\n"
"}\n"
"\n"
"QPushButton#btnSave {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnSave:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnSave:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnSave:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(UserDialog)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.verticalLayout_header = QVBoxLayout()
        self.verticalLayout_header.setSpacing(0)
        self.verticalLayout_header.setObjectName(u"verticalLayout_header")
        self.verticalLayout_header.setContentsMargins(-1, -1, -1, 5)
        self.lblHeaderTitle = QLabel(UserDialog)
        self.lblHeaderTitle.setObjectName(u"lblHeaderTitle")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lblHeaderTitle.setFont(font)

        self.verticalLayout_header.addWidget(self.lblHeaderTitle)

        self.lblHeaderSubtitle = QLabel(UserDialog)
        self.lblHeaderSubtitle.setObjectName(u"lblHeaderSubtitle")
        self.lblHeaderSubtitle.setWordWrap(True)

        self.verticalLayout_header.addWidget(self.lblHeaderSubtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_header)


        self.verticalLayout.addLayout(self.horizontalLayout_header)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
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

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_bottom = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_bottom)

        self.btnCancel = QPushButton(UserDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 38))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(UserDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(140, 38))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(UserDialog)
        self.btnCancel.clicked.connect(UserDialog.reject)
        self.btnSave.clicked.connect(UserDialog.accept)

        QMetaObject.connectSlotsByName(UserDialog)
    # setupUi

    def retranslateUi(self, UserDialog):
        UserDialog.setWindowTitle(QCoreApplication.translate("UserDialog", u"Th\u00eam t\u00e0i kho\u1ea3n", None))
        self.lblHeaderTitle.setText(QCoreApplication.translate("UserDialog", u"Th\u00eam t\u00e0i kho\u1ea3n", None))
        self.lblHeaderSubtitle.setText(QCoreApplication.translate("UserDialog", u"\u0110i\u1ec1n th\u00f4ng tin \u0111\u0103ng nh\u1eadp v\u00e0 ph\u00e2n quy\u1ec1n truy c\u1eadp h\u1ec7 th\u1ed1ng.", None))
        self.lblUsername.setText(QCoreApplication.translate("UserDialog", u"T\u00ean \u0111\u0103ng nh\u1eadp:", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp t\u00ean \u0111\u0103ng nh\u1eadp", None))
        self.lblFullName.setText(QCoreApplication.translate("UserDialog", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.txtFullName.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp h\u1ecd v\u00e0 t\u00ean", None))
        self.lblEmail.setText(QCoreApplication.translate("UserDialog", u"Email:", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 email", None))
        self.lblPassword.setText(QCoreApplication.translate("UserDialog", u"M\u1eadt kh\u1ea9u:", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("UserDialog", u"Nh\u1eadp m\u1eadt kh\u1ea9u", None))
        self.lblRole.setText(QCoreApplication.translate("UserDialog", u"Ch\u1ee9c v\u1ee5:", None))
        self.cboRole.setItemText(0, QCoreApplication.translate("UserDialog", u"Admin", None))
        self.cboRole.setItemText(1, QCoreApplication.translate("UserDialog", u"Cashier", None))
        self.cboRole.setItemText(2, QCoreApplication.translate("UserDialog", u"Warehouse", None))

        self.lblStatus.setText(QCoreApplication.translate("UserDialog", u"Tr\u1ea1ng th\u00e1i:", None))
        self.chkStatus.setText(QCoreApplication.translate("UserDialog", u"Ho\u1ea1t \u0111\u1ed9ng", None))
        self.btnCancel.setText(QCoreApplication.translate("UserDialog", u"H\u1ee7y", None))
        self.btnSave.setText(QCoreApplication.translate("UserDialog", u"L\u01b0u", None))
    # retranslateUi

