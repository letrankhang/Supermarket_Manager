# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_category_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_CategoryManagerDialog(object):
    def setupUi(self, CategoryManagerDialog):
        if not CategoryManagerDialog.objectName():
            CategoryManagerDialog.setObjectName(u"CategoryManagerDialog")
        CategoryManagerDialog.resize(600, 660)
        CategoryManagerDialog.setMinimumSize(QSize(560, 620))
        CategoryManagerDialog.setStyleSheet(u"\n"
"QDialog#CategoryManagerDialog {\n"
"    background-color: #f1f5f9;\n"
"    color: #0f172a;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QWidget#widgetBody {\n"
"    background-color: transparent;\n"
"}\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QLabel#lblHeaderTitle {\n"
"    color: #0f172a;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"QLabel#lblHeaderSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QLabel#lblFormTitle {\n"
"    color: #0f172a;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QFrame#frameTableCard,\n"
"QFrame#frameFormCard {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"QFrame#lineSeparator {\n"
"    color: #e2e8f0;\n"
"    background-color: #e2e8f0;\n"
"    border: none;\n"
"}\n"
"\n"
"QTableWidget#tblCategories {\n"
"    background-co"
                        "lor: transparent;\n"
"    border: none;\n"
"    gridline-color: #f1f5f9;\n"
"    font-size: 13px;\n"
"    color: #334155;\n"
"    outline: none;\n"
"}\n"
"QTableWidget#tblCategories::item {\n"
"    padding: 6px 8px;\n"
"    border-bottom: 1px solid #f1f5f9;\n"
"}\n"
"QTableWidget#tblCategories::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc;\n"
"    color: #64748b;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #f8fafc;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#lblCategoryName,\n"
"QLabel#lblDescription {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLineEdit#txtCategoryName {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 12px;\n"
"    min-height"
                        ": 38px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"}\n"
"QTextEdit#txtDescription {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"}\n"
"QLineEdit#txtCategoryName:focus,\n"
"QTextEdit#txtDescription:focus {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"QPushButton#btnEditCategory {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 34px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnEditCategory:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QPushButton#btnDeleteCategory {\n"
"    background-color: #ffffff;\n"
"    color: #dc2626;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 34px;\n"
"    font-"
                        "size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnDeleteCategory:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"}\n"
"QPushButton#btnEditCategory:disabled,\n"
"QPushButton#btnDeleteCategory:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
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
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
""
                        "    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
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
"QScrollBar::add-page:verti"
                        "cal,\n"
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
"}")
        self.verticalLayout_root = QVBoxLayout(CategoryManagerDialog)
        self.verticalLayout_root.setSpacing(0)
        self.verticalLayout_root.setObjectName(u"verticalLayout_root")
        self.verticalLayout_root.setContentsMargins(0, 0, 0, 0)
        self.widgetBody = QWidget(CategoryManagerDialog)
        self.widgetBody.setObjectName(u"widgetBody")
        self.verticalLayout_body = QVBoxLayout(self.widgetBody)
        self.verticalLayout_body.setSpacing(10)
        self.verticalLayout_body.setObjectName(u"verticalLayout_body")
        self.verticalLayout_body.setContentsMargins(20, 16, 20, 16)
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setSpacing(10)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.verticalLayout_header = QVBoxLayout()
        self.verticalLayout_header.setSpacing(0)
        self.verticalLayout_header.setObjectName(u"verticalLayout_header")
        self.verticalLayout_header.setContentsMargins(-1, -1, -1, 5)
        self.lblHeaderTitle = QLabel(self.widgetBody)
        self.lblHeaderTitle.setObjectName(u"lblHeaderTitle")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lblHeaderTitle.setFont(font)

        self.verticalLayout_header.addWidget(self.lblHeaderTitle)

        self.lblHeaderSubtitle = QLabel(self.widgetBody)
        self.lblHeaderSubtitle.setObjectName(u"lblHeaderSubtitle")

        self.verticalLayout_header.addWidget(self.lblHeaderSubtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_header)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)


        self.verticalLayout_body.addLayout(self.horizontalLayout_header)

        self.frameTableCard = QFrame(self.widgetBody)
        self.frameTableCard.setObjectName(u"frameTableCard")
        self.frameTableCard.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_tableCard = QVBoxLayout(self.frameTableCard)
        self.verticalLayout_tableCard.setSpacing(0)
        self.verticalLayout_tableCard.setObjectName(u"verticalLayout_tableCard")
        self.verticalLayout_tableCard.setContentsMargins(10, 10, 10, 10)
        self.tblCategories = QTableWidget(self.frameTableCard)
        if (self.tblCategories.columnCount() < 2):
            self.tblCategories.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCategories.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCategories.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblCategories.setObjectName(u"tblCategories")
        self.tblCategories.setMinimumSize(QSize(0, 200))
        self.tblCategories.setFrameShape(QFrame.Shape.NoFrame)
        self.tblCategories.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblCategories.setAlternatingRowColors(False)
        self.tblCategories.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblCategories.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblCategories.setShowGrid(False)
        self.tblCategories.horizontalHeader().setDefaultSectionSize(180)
        self.tblCategories.horizontalHeader().setHighlightSections(False)
        self.tblCategories.horizontalHeader().setStretchLastSection(True)
        self.tblCategories.verticalHeader().setVisible(False)
        self.tblCategories.verticalHeader().setDefaultSectionSize(38)

        self.verticalLayout_tableCard.addWidget(self.tblCategories)


        self.verticalLayout_body.addWidget(self.frameTableCard)

        self.horizontalLayout_rowActions = QHBoxLayout()
        self.horizontalLayout_rowActions.setSpacing(8)
        self.horizontalLayout_rowActions.setObjectName(u"horizontalLayout_rowActions")
        self.horizontalSpacer_rowActions = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_rowActions.addItem(self.horizontalSpacer_rowActions)

        self.btnEditCategory = QPushButton(self.widgetBody)
        self.btnEditCategory.setObjectName(u"btnEditCategory")
        self.btnEditCategory.setEnabled(False)
        self.btnEditCategory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_rowActions.addWidget(self.btnEditCategory)

        self.btnDeleteCategory = QPushButton(self.widgetBody)
        self.btnDeleteCategory.setObjectName(u"btnDeleteCategory")
        self.btnDeleteCategory.setEnabled(False)
        self.btnDeleteCategory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_rowActions.addWidget(self.btnDeleteCategory)


        self.verticalLayout_body.addLayout(self.horizontalLayout_rowActions)

        self.lineSeparator = QFrame(self.widgetBody)
        self.lineSeparator.setObjectName(u"lineSeparator")
        self.lineSeparator.setFrameShape(QFrame.Shape.HLine)
        self.lineSeparator.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_body.addWidget(self.lineSeparator)

        self.lblFormTitle = QLabel(self.widgetBody)
        self.lblFormTitle.setObjectName(u"lblFormTitle")

        self.verticalLayout_body.addWidget(self.lblFormTitle)

        self.frameFormCard = QFrame(self.widgetBody)
        self.frameFormCard.setObjectName(u"frameFormCard")
        self.frameFormCard.setFrameShape(QFrame.Shape.NoFrame)
        self.formLayout = QFormLayout(self.frameFormCard)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setHorizontalSpacing(14)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(16, 14, 16, 14)
        self.lblCategoryName = QLabel(self.frameFormCard)
        self.lblCategoryName.setObjectName(u"lblCategoryName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCategoryName)

        self.txtCategoryName = QLineEdit(self.frameFormCard)
        self.txtCategoryName.setObjectName(u"txtCategoryName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtCategoryName)

        self.lblDescription = QLabel(self.frameFormCard)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.txtDescription = QTextEdit(self.frameFormCard)
        self.txtDescription.setObjectName(u"txtDescription")
        self.txtDescription.setMaximumSize(QSize(16777215, 72))
        self.txtDescription.setFrameShape(QFrame.Shape.NoFrame)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtDescription)


        self.verticalLayout_body.addWidget(self.frameFormCard)

        self.horizontalLayout_bottom = QHBoxLayout()
        self.horizontalLayout_bottom.setSpacing(10)
        self.horizontalLayout_bottom.setObjectName(u"horizontalLayout_bottom")
        self.horizontalSpacer_bottom = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_bottom.addItem(self.horizontalSpacer_bottom)

        self.btnCancel = QPushButton(self.widgetBody)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 40))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_bottom.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.widgetBody)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(160, 38))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_bottom.addWidget(self.btnSave)


        self.verticalLayout_body.addLayout(self.horizontalLayout_bottom)


        self.verticalLayout_root.addWidget(self.widgetBody)


        self.retranslateUi(CategoryManagerDialog)

        QMetaObject.connectSlotsByName(CategoryManagerDialog)
    # setupUi

    def retranslateUi(self, CategoryManagerDialog):
        CategoryManagerDialog.setWindowTitle(QCoreApplication.translate("CategoryManagerDialog", u"Qu\u1ea3n l\u00fd danh m\u1ee5c", None))
        self.lblHeaderTitle.setText(QCoreApplication.translate("CategoryManagerDialog", u"Qu\u1ea3n l\u00fd danh m\u1ee5c s\u1ea3n ph\u1ea9m", None))
        self.lblHeaderSubtitle.setText(QCoreApplication.translate("CategoryManagerDialog", u"Ch\u1ecdn m\u1ed9t d\u00f2ng \u0111\u1ec3 s\u1eeda ho\u1eb7c x\u00f3a, ho\u1eb7c th\u00eam danh m\u1ee5c m\u1edbi \u1edf b\u00ean d\u01b0\u1edbi.", None))
        ___qtablewidgetitem = self.tblCategories.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CategoryManagerDialog", u"T\u00caN DANH M\u1ee4C", None))
        ___qtablewidgetitem1 = self.tblCategories.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CategoryManagerDialog", u"M\u00d4 T\u1ea2", None))
        self.btnEditCategory.setText(QCoreApplication.translate("CategoryManagerDialog", u"S\u1eeda", None))
        self.btnDeleteCategory.setText(QCoreApplication.translate("CategoryManagerDialog", u"X\u00f3a", None))
        self.lblFormTitle.setText(QCoreApplication.translate("CategoryManagerDialog", u"Th\u00eam danh m\u1ee5c m\u1edbi", None))
        self.lblCategoryName.setText(QCoreApplication.translate("CategoryManagerDialog", u"T\u00ean danh m\u1ee5c:", None))
        self.txtCategoryName.setPlaceholderText(QCoreApplication.translate("CategoryManagerDialog", u"V\u00ed d\u1ee5: \u0110\u1ed3 u\u1ed1ng, B\u00e1nh k\u1eb9o...", None))
        self.lblDescription.setText(QCoreApplication.translate("CategoryManagerDialog", u"M\u00f4 t\u1ea3 danh m\u1ee5c:", None))
        self.txtDescription.setPlaceholderText(QCoreApplication.translate("CategoryManagerDialog", u"Nh\u1eadp m\u00f4 t\u1ea3 danh m\u1ee5c", None))
        self.btnCancel.setText(QCoreApplication.translate("CategoryManagerDialog", u"H\u1ee7y", None))
        self.btnSave.setText(QCoreApplication.translate("CategoryManagerDialog", u"L\u01b0u danh m\u1ee5c", None))
    # retranslateUi

