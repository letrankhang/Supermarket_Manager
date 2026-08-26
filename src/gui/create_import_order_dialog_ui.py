# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_import_order_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CreateImportOrderDialog(object):
    def setupUi(self, CreateImportOrderDialog):
        if not CreateImportOrderDialog.objectName():
            CreateImportOrderDialog.setObjectName(u"CreateImportOrderDialog")
        CreateImportOrderDialog.resize(1030, 644)
        CreateImportOrderDialog.setMinimumSize(QSize(900, 560))
        CreateImportOrderDialog.setStyleSheet(u"QDialog#CreateImportOrderDialog {\n"
"    background-color: #f1f5f9;\n"
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
"QDa"
                        "teEdit:hover,\n"
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
"    border-radius: 8px"
                        ";\n"
"    padding: 4px;\n"
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
""
                        "    image: url(assets/images/chevron-up.png);\n"
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
"  "
                        "  font-weight: bold;\n"
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
"    border-botto"
                        "m: 1px solid #f1f5f9;\n"
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
""
                        "    background-color: #ffedd5;\n"
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
"    background-color:"
                        " #fef2f2;\n"
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
"QScrollBar:vertical"
                        " {\n"
"    background-color: transparent;\n"
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
"QScrollBar::handle:h"
                        "orizontal {\n"
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
"    padding: 7px 18px;"
                        "\n"
"    font-size: 13px;\n"
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
"QFrame#frame_3,\n"
"QFrame#frame_4,\n"
"QFrame#frame_5 {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QFrame#frame,\n"
"QFrame#frame_2 {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#lblDialogTitle {\n"
"    color: #0f172a;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QLabel#lblDialogSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QLabel#lblDetailTitle {\n"
"    color: #0f172a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#lblSupplier,\n"
"QLabel#lblNote {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLa"
                        "bel#lblTotalText {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLabel#lblTotalAmount {\n"
"    color: #1d4ed8;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
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
        self.verticalLayout_root = QVBoxLayout(CreateImportOrderDialog)
        self.verticalLayout_root.setSpacing(12)
        self.verticalLayout_root.setObjectName(u"verticalLayout_root")
        self.verticalLayout_root.setContentsMargins(18, 16, 18, 16)
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setSpacing(10)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.verticalLayout_header = QVBoxLayout()
        self.verticalLayout_header.setSpacing(4)
        self.verticalLayout_header.setObjectName(u"verticalLayout_header")
        self.lblDialogTitle = QLabel(CreateImportOrderDialog)
        self.lblDialogTitle.setObjectName(u"lblDialogTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(15)
        font.setBold(True)
        self.lblDialogTitle.setFont(font)

        self.verticalLayout_header.addWidget(self.lblDialogTitle)

        self.lblDialogSubtitle = QLabel(CreateImportOrderDialog)
        self.lblDialogSubtitle.setObjectName(u"lblDialogSubtitle")

        self.verticalLayout_header.addWidget(self.lblDialogSubtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_header)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)


        self.verticalLayout_root.addLayout(self.horizontalLayout_header)

        self.frame_4 = QFrame(CreateImportOrderDialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 14, 16, 14)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QVBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblSupplier = QLabel(self.frame)
        self.lblSupplier.setObjectName(u"lblSupplier")
        self.lblSupplier.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout.addWidget(self.lblSupplier)

        self.cboSupplier = QComboBox(self.frame)
        self.cboSupplier.setObjectName(u"cboSupplier")
        self.cboSupplier.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.cboSupplier)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QVBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblNote = QLabel(self.frame_2)
        self.lblNote.setObjectName(u"lblNote")

        self.horizontalLayout_2.addWidget(self.lblNote)

        self.txtNote = QLineEdit(self.frame_2)
        self.txtNote.setObjectName(u"txtNote")

        self.horizontalLayout_2.addWidget(self.txtNote)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_root.addWidget(self.frame_4)

        self.frame_3 = QFrame(CreateImportOrderDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 14, 16, 14)
        self.horizontalLayout_detailBar = QHBoxLayout()
        self.horizontalLayout_detailBar.setSpacing(10)
        self.horizontalLayout_detailBar.setObjectName(u"horizontalLayout_detailBar")
        self.lblDetailTitle = QLabel(self.frame_3)
        self.lblDetailTitle.setObjectName(u"lblDetailTitle")

        self.horizontalLayout_detailBar.addWidget(self.lblDetailTitle)

        self.horizontalSpacer_detailBar = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_detailBar.addItem(self.horizontalSpacer_detailBar)

        self.cboProduct = QComboBox(self.frame_3)
        self.cboProduct.setObjectName(u"cboProduct")
        self.cboProduct.setMinimumSize(QSize(280, 40))
        self.cboProduct.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_detailBar.addWidget(self.cboProduct)

        self.btnAddProductRow = QPushButton(self.frame_3)
        self.btnAddProductRow.setObjectName(u"btnAddProductRow")
        self.btnAddProductRow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_detailBar.addWidget(self.btnAddProductRow)


        self.verticalLayout.addLayout(self.horizontalLayout_detailBar)

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
        self.tblImportDetails.setFrameShape(QFrame.Shape.NoFrame)
        self.tblImportDetails.setAlternatingRowColors(False)
        self.tblImportDetails.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblImportDetails.setShowGrid(False)
        self.tblImportDetails.horizontalHeader().setHighlightSections(False)
        self.tblImportDetails.verticalHeader().setVisible(False)
        self.tblImportDetails.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout.addWidget(self.tblImportDetails)


        self.verticalLayout_root.addWidget(self.frame_3)

        self.frame_5 = QFrame(CreateImportOrderDialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(16, 12, 16, 12)
        self.totalLayout = QHBoxLayout()
        self.totalLayout.setSpacing(10)
        self.totalLayout.setObjectName(u"totalLayout")
        self.lblTotalText = QLabel(self.frame_5)
        self.lblTotalText.setObjectName(u"lblTotalText")

        self.totalLayout.addWidget(self.lblTotalText)

        self.lblTotalAmount = QLabel(self.frame_5)
        self.lblTotalAmount.setObjectName(u"lblTotalAmount")

        self.totalLayout.addWidget(self.lblTotalAmount)


        self.horizontalLayout_5.addLayout(self.totalLayout)

        self.horizontalSpacer_footer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_footer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnCancel = QPushButton(self.frame_5)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.frame_5)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btnSave)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_root.addWidget(self.frame_5)


        self.retranslateUi(CreateImportOrderDialog)

        QMetaObject.connectSlotsByName(CreateImportOrderDialog)
    # setupUi

    def retranslateUi(self, CreateImportOrderDialog):
        CreateImportOrderDialog.setWindowTitle(QCoreApplication.translate("CreateImportOrderDialog", u"T\u1ea1o Phi\u1ebfu Nh\u1eadp H\u00e0ng", None))
        self.lblDialogTitle.setText(QCoreApplication.translate("CreateImportOrderDialog", u"T\u1ea1o phi\u1ebfu nh\u1eadp h\u00e0ng", None))
        self.lblDialogSubtitle.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Ch\u1ecdn nh\u00e0 cung c\u1ea5p, th\u00eam s\u1ea3n ph\u1ea9m r\u1ed3i x\u00e1c nh\u1eadn \u0111\u1ec3 ghi t\u0103ng t\u1ed3n kho.", None))
        self.lblSupplier.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Nh\u00e0 cung c\u1ea5p:", None))
        self.lblNote.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Ghi ch\u00fa nh\u1eadp h\u00e0ng:", None))
        self.txtNote.setPlaceholderText(QCoreApplication.translate("CreateImportOrderDialog", u"(Ghi ch\u00fa cho phi\u1ebfu nh\u1eadp n\u1ebfu c\u00f3)", None))
        self.lblDetailTitle.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Danh s\u00e1ch s\u1ea3n ph\u1ea9m nh\u1eadp", None))
        self.cboProduct.setCurrentText("")
        self.btnAddProductRow.setText(QCoreApplication.translate("CreateImportOrderDialog", u"Th\u00eam d\u00f2ng s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem = self.tblImportDetails.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CreateImportOrderDialog", u"M\u00c3 S\u1ea2N PH\u1ea8M", None))
        ___qtablewidgetitem1 = self.tblImportDetails.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CreateImportOrderDialog", u"T\u00caN S\u1ea2N PH\u1ea8M", None))
        ___qtablewidgetitem2 = self.tblImportDetails.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CreateImportOrderDialog", u"S\u1ed0 L\u01af\u1ee2NG", None))
        ___qtablewidgetitem3 = self.tblImportDetails.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CreateImportOrderDialog", u"\u0110\u01a0N GI\u00c1 NH\u1eacP", None))
        ___qtablewidgetitem4 = self.tblImportDetails.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CreateImportOrderDialog", u"TH\u00c0NH TI\u1ec0N", None))
        self.lblTotalText.setText(QCoreApplication.translate("CreateImportOrderDialog", u"T\u1ed5ng ti\u1ec1n nh\u1eadp h\u00e0ng:", None))
        self.lblTotalAmount.setText(QCoreApplication.translate("CreateImportOrderDialog", u"0 VN\u0110", None))
        self.btnCancel.setText(QCoreApplication.translate("CreateImportOrderDialog", u"H\u1ee7y b\u1ecf", None))
        self.btnSave.setText(QCoreApplication.translate("CreateImportOrderDialog", u"X\u00e1c nh\u1eadn nh\u1eadp h\u00e0ng", None))
    # retranslateUi

