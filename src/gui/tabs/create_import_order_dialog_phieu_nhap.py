# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_import_order_dialog_phieu_nhap.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_CreateImportOrderDialog(object):
    def setupUi(self, CreateImportOrderDialog):
        if not CreateImportOrderDialog.objectName():
            CreateImportOrderDialog.setObjectName(u"CreateImportOrderDialog")
        CreateImportOrderDialog.resize(1030, 644)
        self.frame_5 = QFrame(CreateImportOrderDialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 560, 793, 56))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.totalLayout = QHBoxLayout()
        self.totalLayout.setObjectName(u"totalLayout")
        self.lblTotalText = QLabel(self.frame_5)
        self.lblTotalText.setObjectName(u"lblTotalText")
        font = QFont()
        font.setPointSize(10)
        self.lblTotalText.setFont(font)

        self.totalLayout.addWidget(self.lblTotalText)

        self.lblTotalAmount = QLabel(self.frame_5)
        self.lblTotalAmount.setObjectName(u"lblTotalAmount")
        self.lblTotalAmount.setFont(font)

        self.totalLayout.addWidget(self.lblTotalAmount)


        self.horizontalLayout_5.addLayout(self.totalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnAddProductRow = QPushButton(self.frame_5)
        self.btnAddProductRow.setObjectName(u"btnAddProductRow")
        self.btnAddProductRow.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnAddProductRow)

        self.cbothemsp = QComboBox(self.frame_5)
        self.cbothemsp.setObjectName(u"cbothemsp")
        self.cbothemsp.setFont(font)

        self.horizontalLayout_4.addWidget(self.cbothemsp)

        self.btnSave = QPushButton(self.frame_5)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnSave)

        self.btnCancel = QPushButton(self.frame_5)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnCancel)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.frame_3 = QFrame(CreateImportOrderDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 80, 1021, 471))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblDetailTitle = QLabel(self.frame_3)
        self.lblDetailTitle.setObjectName(u"lblDetailTitle")
        self.lblDetailTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblDetailTitle)

        self.tblImportDetails = QTableWidget(self.frame_3)
        if (self.tblImportDetails.columnCount() < 5):
            self.tblImportDetails.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblImportDetails.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblImportDetails.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblImportDetails.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblImportDetails.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblImportDetails.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblImportDetails.setObjectName(u"tblImportDetails")
        self.tblImportDetails.setFont(font)

        self.verticalLayout.addWidget(self.tblImportDetails)

        self.frame_4 = QFrame(CreateImportOrderDialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 0, 721, 78))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSupplier = QLabel(self.frame)
        self.lblSupplier.setObjectName(u"lblSupplier")
        font1 = QFont()
        font1.setPointSize(12)
        self.lblSupplier.setFont(font1)
        self.lblSupplier.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.lblSupplier)

        self.cboSupplier = QComboBox(self.frame)
        self.cboSupplier.setObjectName(u"cboSupplier")
        self.cboSupplier.setFont(font1)

        self.horizontalLayout.addWidget(self.cboSupplier)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblNote = QLabel(self.frame_2)
        self.lblNote.setObjectName(u"lblNote")
        self.lblNote.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lblNote)

        self.txtNote = QLineEdit(self.frame_2)
        self.txtNote.setObjectName(u"txtNote")
        self.txtNote.setFont(font1)

        self.horizontalLayout_2.addWidget(self.txtNote)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(CreateImportOrderDialog)

        QMetaObject.connectSlotsByName(CreateImportOrderDialog)
    # setupUi

    def retranslateUi(self, CreateImportOrderDialog):
        CreateImportOrderDialog.setWindowTitle(QCoreApplication.translate("CreateImportOrderDialog", u"T\u1ea1o Ph\u1ebfu Nh\u1eadp H\u00e0ng", None))
        self.lblTotalText.setText(QCoreApplication.translate("CreateImportOrderDialog", u"T\u1ed5ng ti\u1ec1n nh\u1eadp h\u00e0ng:", None))
        self.lblTotalAmount.setText(QCoreApplication.translate("CreateImportOrderDialog", u"0 VN\u0110", None))
        self.btnAddProductRow.setText(QCoreApplication.translate("CreateImportOrderDialog", u"+ Th\u00eam d\u00f2ng s\u1ea3n ph\u1ea9m", None))
        self.cbothemsp.setCurrentText("")
        self.btnSave.setText(QCoreApplication.translate("CreateImportOrderDialog", u"X\u00e1c nh\u1eadn nh\u1eadp h\u00e0ng", None))
        self.btnCancel.setText(QCoreApplication.translate("CreateImportOrderDialog", u"H\u1ee7y b\u1ecf", None))
        self.lblDetailTitle.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Danh s\u00e1ch s\u1ea3n ph\u1ea9m nh\u1eadp:", None))
        ___qtablewidgetitem = self.tblImportDetails.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CreateImportOrderDialog", u"M\u00e3 s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem1 = self.tblImportDetails.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CreateImportOrderDialog", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem2 = self.tblImportDetails.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CreateImportOrderDialog", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        ___qtablewidgetitem3 = self.tblImportDetails.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CreateImportOrderDialog", u"\u0110\u01a1n gi\u00e1 nh\u1eadp", None))
        ___qtablewidgetitem4 = self.tblImportDetails.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Th\u00e0nh ti\u1ec1n", None))
        self.lblSupplier.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Nh\u00e0 cung c\u1ea5p:", None))
        self.lblNote.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Ghi ch\u00fa nh\u1eadp h\u00e0ng:", None))
    # retranslateUi

