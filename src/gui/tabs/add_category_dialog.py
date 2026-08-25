# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_category_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_CategoryManagerDialog(object):
    def setupUi(self, CategoryManagerDialog):
        if not CategoryManagerDialog.objectName():
            CategoryManagerDialog.setObjectName(u"CategoryManagerDialog")
        CategoryManagerDialog.resize(560, 620)
        CategoryManagerDialog.setStyleSheet(u"QDialog { background-color: #ffffff; }")
        self.verticalLayout_root = QVBoxLayout(CategoryManagerDialog)
        self.verticalLayout_root.setSpacing(0)
        self.verticalLayout_root.setObjectName(u"verticalLayout_root")
        self.verticalLayout_root.setContentsMargins(0, 0, 0, 0)
        self.widgetBody = QWidget(CategoryManagerDialog)
        self.widgetBody.setObjectName(u"widgetBody")
        self.verticalLayout_body = QVBoxLayout(self.widgetBody)
        self.verticalLayout_body.setSpacing(14)
        self.verticalLayout_body.setObjectName(u"verticalLayout_body")
        self.verticalLayout_body.setContentsMargins(24, 18, 24, 20)
        self.lblHeaderTitle = QLabel(self.widgetBody)
        self.lblHeaderTitle.setObjectName(u"lblHeaderTitle")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblHeaderTitle.setFont(font)
        self.lblHeaderTitle.setStyleSheet(u"color: #1e3a5f;")
        self.lblHeaderTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_body.addWidget(self.lblHeaderTitle)

        self.tblCategories = QTableWidget(self.widgetBody)
        if (self.tblCategories.columnCount() < 2):
            self.tblCategories.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCategories.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCategories.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblCategories.setObjectName(u"tblCategories")
        self.tblCategories.setMinimumSize(QSize(0, 200))
        self.tblCategories.setStyleSheet(u"QTableWidget { border: 1px solid #e2e8f0; border-radius: 6px; gridline-color: #f1f5f9; }\n"
"QHeaderView::section { background-color: #f8fafc; color: #64748b; font-weight: bold; border: none; padding: 6px; }")
        self.tblCategories.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblCategories.setAlternatingRowColors(True)
        self.tblCategories.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_body.addWidget(self.tblCategories)

        self.horizontalLayout_rowActions = QHBoxLayout()
        self.horizontalLayout_rowActions.setObjectName(u"horizontalLayout_rowActions")
        self.horizontalSpacer_rowActions = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_rowActions.addItem(self.horizontalSpacer_rowActions)

        self.btnEditCategory = QPushButton(self.widgetBody)
        self.btnEditCategory.setObjectName(u"btnEditCategory")
        self.btnEditCategory.setEnabled(False)
        self.btnEditCategory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditCategory.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #334155; border-radius: 6px; padding: 6px 14px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }\n"
"QPushButton:disabled { color: #94a3b8; }")

        self.horizontalLayout_rowActions.addWidget(self.btnEditCategory)

        self.btnDeleteCategory = QPushButton(self.widgetBody)
        self.btnDeleteCategory.setObjectName(u"btnDeleteCategory")
        self.btnDeleteCategory.setEnabled(False)
        self.btnDeleteCategory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDeleteCategory.setStyleSheet(u"QPushButton { background-color: #fee2e2; color: #b91c1c; border-radius: 6px; padding: 6px 14px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #fecaca; }\n"
"QPushButton:disabled { color: #94a3b8; background-color: #e2e8f0; }")

        self.horizontalLayout_rowActions.addWidget(self.btnDeleteCategory)


        self.verticalLayout_body.addLayout(self.horizontalLayout_rowActions)

        self.lineSeparator = QFrame(self.widgetBody)
        self.lineSeparator.setObjectName(u"lineSeparator")
        self.lineSeparator.setFrameShape(QFrame.HLine)
        self.lineSeparator.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_body.addWidget(self.lineSeparator)

        self.lblFormTitle = QLabel(self.widgetBody)
        self.lblFormTitle.setObjectName(u"lblFormTitle")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.lblFormTitle.setFont(font1)
        self.lblFormTitle.setStyleSheet(u"color: #1e293b;")

        self.verticalLayout_body.addWidget(self.lblFormTitle)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.lblCategoryName = QLabel(self.widgetBody)
        self.lblCategoryName.setObjectName(u"lblCategoryName")
        font2 = QFont()
        font2.setPointSize(10)
        self.lblCategoryName.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCategoryName)

        self.txtCategoryName = QLineEdit(self.widgetBody)
        self.txtCategoryName.setObjectName(u"txtCategoryName")
        self.txtCategoryName.setMinimumSize(QSize(0, 32))
        self.txtCategoryName.setStyleSheet(u"QLineEdit { border: 1px solid #cbd5e1; border-radius: 6px; padding: 4px 8px; }\n"
"QLineEdit:focus { border: 1px solid #1d4ed8; }")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtCategoryName)

        self.lblDescription = QLabel(self.widgetBody)
        self.lblDescription.setObjectName(u"lblDescription")
        self.lblDescription.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.txtDescription = QTextEdit(self.widgetBody)
        self.txtDescription.setObjectName(u"txtDescription")
        self.txtDescription.setMaximumSize(QSize(16777215, 90))
        self.txtDescription.setStyleSheet(u"QTextEdit { border: 1px solid #cbd5e1; border-radius: 6px; padding: 4px 8px; }\n"
"QTextEdit:focus { border: 1px solid #1d4ed8; }")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtDescription)


        self.verticalLayout_body.addLayout(self.formLayout)

        self.horizontalLayout_bottom = QHBoxLayout()
        self.horizontalLayout_bottom.setObjectName(u"horizontalLayout_bottom")
        self.horizontalSpacer_bottom = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_bottom.addItem(self.horizontalSpacer_bottom)

        self.btnCancel = QPushButton(self.widgetBody)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(90, 36))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancel.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #334155; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }")

        self.horizontalLayout_bottom.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.widgetBody)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(150, 36))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSave.setStyleSheet(u"QPushButton { background-color: #1e3a8a; color: white; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #1e40af; }")

        self.horizontalLayout_bottom.addWidget(self.btnSave)


        self.verticalLayout_body.addLayout(self.horizontalLayout_bottom)


        self.verticalLayout_root.addWidget(self.widgetBody)


        self.retranslateUi(CategoryManagerDialog)

        QMetaObject.connectSlotsByName(CategoryManagerDialog)
    # setupUi

    def retranslateUi(self, CategoryManagerDialog):
        CategoryManagerDialog.setWindowTitle(QCoreApplication.translate("CategoryManagerDialog", u"Qu\u1ea3n L\u00fd Danh M\u1ee5c", None))
        self.lblHeaderTitle.setText(QCoreApplication.translate("CategoryManagerDialog", u"QU\u1ea2N L\u00dd DANH M\u1ee4C S\u1ea2N PH\u1ea8M", None))
        ___qtablewidgetitem = self.tblCategories.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CategoryManagerDialog", u"T\u00ean danh m\u1ee5c", None))
        ___qtablewidgetitem1 = self.tblCategories.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CategoryManagerDialog", u"M\u00f4 t\u1ea3", None))
        self.btnEditCategory.setText(QCoreApplication.translate("CategoryManagerDialog", u"\u270e  S\u1eeda", None))
        self.btnDeleteCategory.setText(QCoreApplication.translate("CategoryManagerDialog", u"\U0001f5d1  X\U000000f3a", None))
        self.lblFormTitle.setText(QCoreApplication.translate("CategoryManagerDialog", u"Th\u00eam danh m\u1ee5c m\u1edbi", None))
        self.lblCategoryName.setText(QCoreApplication.translate("CategoryManagerDialog", u"T\u00ean danh m\u1ee5c:", None))
        self.txtCategoryName.setPlaceholderText(QCoreApplication.translate("CategoryManagerDialog", u"V\u00ed d\u1ee5: \u0110\u1ed3 u\u1ed1ng, B\u00e1nh k\u1eb9o...", None))
        self.lblDescription.setText(QCoreApplication.translate("CategoryManagerDialog", u"M\u00f4 t\u1ea3 danh m\u1ee5c:", None))
        self.txtDescription.setPlaceholderText(QCoreApplication.translate("CategoryManagerDialog", u"Nh\u1eadp m\u00f4 t\u1ea3 danh m\u1ee5c...", None))
        self.btnCancel.setText(QCoreApplication.translate("CategoryManagerDialog", u"H\u1ee6Y", None))
        self.btnSave.setText(QCoreApplication.translate("CategoryManagerDialog", u"L\u01afU DANH M\u1ee4C", None))
    # retranslateUi

