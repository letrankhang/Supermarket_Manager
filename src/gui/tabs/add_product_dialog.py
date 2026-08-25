# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        if not AddProductDialog.objectName():
            AddProductDialog.setObjectName(u"AddProductDialog")
        AddProductDialog.resize(441, 315)
        self.layoutWidget = QWidget(AddProductDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 402, 259))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblBarcode = QLabel(self.layoutWidget)
        self.lblBarcode.setObjectName(u"lblBarcode")
        font = QFont()
        font.setPointSize(12)
        self.lblBarcode.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblBarcode)

        self.txtBarcode = QLineEdit(self.layoutWidget)
        self.txtBarcode.setObjectName(u"txtBarcode")
        self.txtBarcode.setEnabled(False)
        self.txtBarcode.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtBarcode)

        self.lblProductName = QLabel(self.layoutWidget)
        self.lblProductName.setObjectName(u"lblProductName")
        self.lblProductName.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblProductName)

        self.txtProductName = QLineEdit(self.layoutWidget)
        self.txtProductName.setObjectName(u"txtProductName")
        self.txtProductName.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtProductName)

        self.lblCategory = QLabel(self.layoutWidget)
        self.lblCategory.setObjectName(u"lblCategory")
        self.lblCategory.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCategory)

        self.cboCategory = QComboBox(self.layoutWidget)
        self.cboCategory.setObjectName(u"cboCategory")
        self.cboCategory.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cboCategory)

        self.lblUnit = QLabel(self.layoutWidget)
        self.lblUnit.setObjectName(u"lblUnit")
        self.lblUnit.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblUnit)

        self.txtUnit = QLineEdit(self.layoutWidget)
        self.txtUnit.setObjectName(u"txtUnit")
        self.txtUnit.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtUnit)

        self.lblRetailPrice = QLabel(self.layoutWidget)
        self.lblRetailPrice.setObjectName(u"lblRetailPrice")
        self.lblRetailPrice.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblRetailPrice)

        self.spnRetailPrice = QDoubleSpinBox(self.layoutWidget)
        self.spnRetailPrice.setObjectName(u"spnRetailPrice")
        self.spnRetailPrice.setFont(font)
        self.spnRetailPrice.setMaximum(999999999.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spnRetailPrice)

        self.lblImage = QLabel(self.layoutWidget)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblImage)

        self.txtImage = QLineEdit(self.layoutWidget)
        self.txtImage.setObjectName(u"txtImage")
        self.txtImage.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtImage)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSave = QPushButton(self.layoutWidget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setFont(font)

        self.horizontalLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(self.layoutWidget)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setFont(font)

        self.horizontalLayout.addWidget(self.btnCancel)


        self.formLayout.setLayout(6, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout)


        self.retranslateUi(AddProductDialog)

        QMetaObject.connectSlotsByName(AddProductDialog)
    # setupUi

    def retranslateUi(self, AddProductDialog):
        AddProductDialog.setWindowTitle(QCoreApplication.translate("AddProductDialog", u"Th\u00eam S\u1ea3n Ph\u1ea9m M\u1edbi", None))
        self.lblBarcode.setText(QCoreApplication.translate("AddProductDialog", u"M\u00e3 v\u1ea1ch :", None))
        self.lblProductName.setText(QCoreApplication.translate("AddProductDialog", u"T\u00ean s\u1ea3n ph\u1ea9m:", None))
        self.lblCategory.setText(QCoreApplication.translate("AddProductDialog", u"Danh m\u1ee5c:", None))
        self.lblUnit.setText(QCoreApplication.translate("AddProductDialog", u"\u0110\u01a1n v\u1ecb t\u00ednh:", None))
        self.lblRetailPrice.setText(QCoreApplication.translate("AddProductDialog", u"Gi\u00e1 b\u00e1n l\u1ebb (VN\u0110):", None))
        self.lblImage.setText(QCoreApplication.translate("AddProductDialog", u"\u0110\u01b0\u1eddng d\u1eabn h\u00ecnh \u1ea3nh:", None))
        self.btnSave.setText(QCoreApplication.translate("AddProductDialog", u"L\u01b0u s\u1ea3n ph\u1ea9m", None))
        self.btnCancel.setText(QCoreApplication.translate("AddProductDialog", u"H\u1ee7y b\u1ecf", None))
    # retranslateUi

