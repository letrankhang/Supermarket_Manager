# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        if not AddProductDialog.objectName():
            AddProductDialog.setObjectName(u"AddProductDialog")
        AddProductDialog.resize(518, 470)
        AddProductDialog.setMinimumSize(QSize(460, 450))
        AddProductDialog.setStyleSheet(u"\n"
"QDialog#AddProductDialog {\n"
"    background-color: #f1f5f9;\n"
"    color: #0f172a;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"/* ===== Ti\u00eau \u0111\u1ec1 h\u1ed9p tho\u1ea1i =====\n"
"   C\u00f9ng c\u00f4ng th\u1ee9c v\u1edbi header c\u1ee7a products.ui: m\u1ed9t d\u00f2ng ti\u00eau \u0111\u1ec1 \u0111\u1eadm, ngay d\u01b0\u1edbi\n"
"   l\u00e0 d\u00f2ng m\u00f4 t\u1ea3 m\u00e0u x\u00e1m c\u1ee1 nh\u1ecf. C\u1ee1 ch\u1eef ti\u00eau \u0111\u1ec1 l\u1ea5y t\u1eeb thu\u1ed9c t\u00ednh font. */\n"
"QLabel#lblDialogTitle {\n"
"    color: #0f172a;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"QLabel#lblDialogSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"/* ===== Th\u1ebb ch\u1ee9a bi\u1ec3u m\u1eabu ===== */\n"
"QFrame#frameForm {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0"
                        ";\n"
"    border-radius: 14px;\n"
"}\n"
"QFrame#frameFooter {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"/* Nh\u00e3n c\u1ee7a t\u1eebng \u00f4 nh\u1eadp, c\u00f9ng t\u00f4ng v\u1edbi infoKey b\u00ean help_center.ui. */\n"
"QLabel#lblBarcode,\n"
"QLabel#lblProductName,\n"
"QLabel#lblCategory,\n"
"QLabel#lblUnit,\n"
"QLabel#lblRetailPrice,\n"
"QLabel#lblImage {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
"/* ===== \u00d4 nh\u1eadp li\u1ec7u ===== */\n"
"QLineEdit,\n"
"QComboBox,\n"
"QDoubleSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 12px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"}\n"
"QLineEdit:focus,\n"
"QComboBox:focus,\n"
"QDoubleSpinBox:focus {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QLineEdit:disabled,\n"
"QComboBox:disabled,\n"
"QDoubleSpinBox:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #94a3b8;\n"
""
                        "}\n"
"QComboBox:hover,\n"
"QDoubleSpinBox:hover {\n"
"    border: 1px solid #cbd5e1;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: none;\n"
"    selection-background-color: #eff6ff;\n"
"    selection-color: #1d4ed8;\n"
"}\n"
"/* ===== N\u00fat b\u1ea5m ===== */\n"
"QPushButton#btnSave {\n"
"    background-color: #2563eb;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnSave:hover {\n"
"    background-color: #1d4ed8;\n"
"}\n"
"QPushButton#btnSave:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnSave:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"QPushButton#btnCancel {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-ra"
                        "dius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}")
        self.verticalLayout_root = QVBoxLayout(AddProductDialog)
        self.verticalLayout_root.setSpacing(12)
        self.verticalLayout_root.setObjectName(u"verticalLayout_root")
        self.verticalLayout_root.setContentsMargins(18, 16, 18, 16)
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setSpacing(10)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.verticalLayout_header = QVBoxLayout()
        self.verticalLayout_header.setSpacing(0)
        self.verticalLayout_header.setObjectName(u"verticalLayout_header")
        self.lblDialogTitle = QLabel(AddProductDialog)
        self.lblDialogTitle.setObjectName(u"lblDialogTitle")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lblDialogTitle.setFont(font)

        self.verticalLayout_header.addWidget(self.lblDialogTitle)

        self.lblDialogSubtitle = QLabel(AddProductDialog)
        self.lblDialogSubtitle.setObjectName(u"lblDialogSubtitle")

        self.verticalLayout_header.addWidget(self.lblDialogSubtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_header)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)


        self.verticalLayout_root.addLayout(self.horizontalLayout_header)

        self.frameForm = QFrame(AddProductDialog)
        self.frameForm.setObjectName(u"frameForm")
        self.frameForm.setFrameShape(QFrame.Shape.NoFrame)
        self.formLayout = QFormLayout(self.frameForm)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setHorizontalSpacing(14)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(18, 16, 18, 16)
        self.lblBarcode = QLabel(self.frameForm)
        self.lblBarcode.setObjectName(u"lblBarcode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblBarcode)

        self.txtBarcode = QLineEdit(self.frameForm)
        self.txtBarcode.setObjectName(u"txtBarcode")
        self.txtBarcode.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtBarcode)

        self.lblProductName = QLabel(self.frameForm)
        self.lblProductName.setObjectName(u"lblProductName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblProductName)

        self.txtProductName = QLineEdit(self.frameForm)
        self.txtProductName.setObjectName(u"txtProductName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtProductName)

        self.lblCategory = QLabel(self.frameForm)
        self.lblCategory.setObjectName(u"lblCategory")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCategory)

        self.cboCategory = QComboBox(self.frameForm)
        self.cboCategory.setObjectName(u"cboCategory")
        self.cboCategory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cboCategory)

        self.lblUnit = QLabel(self.frameForm)
        self.lblUnit.setObjectName(u"lblUnit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblUnit)

        self.txtUnit = QLineEdit(self.frameForm)
        self.txtUnit.setObjectName(u"txtUnit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtUnit)

        self.lblRetailPrice = QLabel(self.frameForm)
        self.lblRetailPrice.setObjectName(u"lblRetailPrice")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblRetailPrice)

        self.spnRetailPrice = QDoubleSpinBox(self.frameForm)
        self.spnRetailPrice.setObjectName(u"spnRetailPrice")
        self.spnRetailPrice.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spnRetailPrice.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spnRetailPrice.setDecimals(0)
        self.spnRetailPrice.setMaximum(999999999.000000000000000)
        self.spnRetailPrice.setSingleStep(1000.000000000000000)
        self.spnRetailPrice.setProperty(u"groupSeparatorShown", True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spnRetailPrice)

        self.lblImage = QLabel(self.frameForm)
        self.lblImage.setObjectName(u"lblImage")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblImage)

        self.txtImage = QLineEdit(self.frameForm)
        self.txtImage.setObjectName(u"txtImage")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtImage)


        self.verticalLayout_root.addWidget(self.frameForm)

        self.frameFooter = QFrame(AddProductDialog)
        self.frameFooter.setObjectName(u"frameFooter")
        self.frameFooter.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameFooter)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_footer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_footer)

        self.btnCancel = QPushButton(self.frameFooter)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.frameFooter)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_root.addWidget(self.frameFooter)


        self.retranslateUi(AddProductDialog)

        QMetaObject.connectSlotsByName(AddProductDialog)
    # setupUi

    def retranslateUi(self, AddProductDialog):
        AddProductDialog.setWindowTitle(QCoreApplication.translate("AddProductDialog", u"Th\u00eam S\u1ea3n Ph\u1ea9m M\u1edbi", None))
        self.lblDialogTitle.setText(QCoreApplication.translate("AddProductDialog", u"Th\u00eam s\u1ea3n ph\u1ea9m m\u1edbi", None))
        self.lblDialogSubtitle.setText(QCoreApplication.translate("AddProductDialog", u"\u0110i\u1ec1n th\u00f4ng tin s\u1ea3n ph\u1ea9m, m\u00e3 v\u1ea1ch \u0111\u01b0\u1ee3c sinh t\u1ef1 \u0111\u1ed9ng.", None))
        self.lblBarcode.setText(QCoreApplication.translate("AddProductDialog", u"M\u00e3 v\u1ea1ch", None))
        self.lblProductName.setText(QCoreApplication.translate("AddProductDialog", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        self.txtProductName.setPlaceholderText(QCoreApplication.translate("AddProductDialog", u"V\u00ed d\u1ee5: M\u00ec t\u00f4m H\u1ea3o H\u1ea3o chua cay", None))
        self.lblCategory.setText(QCoreApplication.translate("AddProductDialog", u"Danh m\u1ee5c", None))
        self.lblUnit.setText(QCoreApplication.translate("AddProductDialog", u"\u0110\u01a1n v\u1ecb t\u00ednh", None))
        self.txtUnit.setPlaceholderText(QCoreApplication.translate("AddProductDialog", u"V\u00ed d\u1ee5: G\u00f3i, Chai, Th\u00f9ng", None))
        self.lblRetailPrice.setText(QCoreApplication.translate("AddProductDialog", u"Gi\u00e1 b\u00e1n l\u1ebb (VN\u0110)", None))
        self.lblImage.setText(QCoreApplication.translate("AddProductDialog", u"\u0110\u01b0\u1eddng d\u1eabn h\u00ecnh \u1ea3nh", None))
        self.txtImage.setPlaceholderText(QCoreApplication.translate("AddProductDialog", u"assets/ProductImages/ten-file.png", None))
        self.btnCancel.setText(QCoreApplication.translate("AddProductDialog", u"H\u1ee7y b\u1ecf", None))
        self.btnSave.setText(QCoreApplication.translate("AddProductDialog", u"L\u01b0u s\u1ea3n ph\u1ea9m", None))
    # retranslateUi

