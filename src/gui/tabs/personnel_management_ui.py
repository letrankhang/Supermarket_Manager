# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'personnel_management.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PersonnelManagement(object):
    def setupUi(self, PersonnelManagement):
        if not PersonnelManagement.objectName():
            PersonnelManagement.setObjectName(u"PersonnelManagement")
        PersonnelManagement.resize(1000, 700)
        PersonnelManagement.setStyleSheet(u"QWidget#PersonnelManagement {\n"
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
"QDateEd"
                        "it:hover,\n"
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
""
                        "    padding: 4px;\n"
"    outline: none;\n"
"    selection-background-color: #f1f5f9;\n"
"    selection-color: #0f172a;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    color: #0f172a;\n"
"    min-height: 30px;\n"
"    padding: 4px 10px;\n"
"    border-radius: 6px;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #f1f5f9;\n"
"    color: #0f172a;\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #e2e8f0;\n"
"    color: #0f172a;\n"
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
"    sub"
                        "control-position: bottom right;\n"
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
"    bor"
                        "der: 1px solid #1d4ed8;\n"
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
"    font-weight: bold;\n"
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
"    color: #64748b;\n"
"}\n"
"QPushButton#RowActionButton:h"
                        "over {\n"
"    background-color: #f1f5f9;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"QPushButton#RowActionButton:pressed {\n"
"    background-color: #e2e8f0;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QPushButton#btnEditRow:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton#btnDeleteRow:hover {\n"
"    background-color: #fef2f2;\n"
"    color: #dc2626;\n"
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
"    border-bottom: 1px solid #f1f5f9;\n"
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
"    color: "
                        "#64748b;\n"
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
"    font-si"
                        "ze: 11px;\n"
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
"    font-we"
                        "ight: 700;\n"
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
"Q"
                        "ScrollBar::handle:vertical:pressed {\n"
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
"QScrollBar::"
                        "sub-line:horizontal {\n"
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
"QFrame#frameHeader,\n"
"QFrame#frameToolbar,\n"
"QFrame#framePagination {\n"
"    ba"
                        "ckground-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame#frameTable {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"    color: #0f172a;\n"
"    font-size: 24px;\n"
"    font-weight: 700;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QLabel#lblSubtitle,\n"
"QLabel#lblSub {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QPushButton#btnAdd {\n"
"    background-color: #1d4ed8;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 20px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnAdd:hover {\n"
"    background-color: #1e3a8a;\n"
"}\n"
"QPushButton#btnAdd:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"QPushButton#btnAdd:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #f8fafc;\n"
"}\n"
"\n"
"QPushButton#btnDelete "
                        "{\n"
"    background-color: #ffffff;\n"
"    color: #dc2626;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnDelete:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"}\n"
"QPushButton#btnDelete:disabled {\n"
"    background-color: #f8fafc;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"\n"
"QLabel#lblPaginationInfo,\n"
"QLabel#lblPage {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton#btnPrev,\n"
"QPushButton#btnNext,\n"
"QPushButton#btnPrevPage,\n"
"QPushButton#btnNextPage {\n"
"    background-color: #ffffff;\n"
"    color: #334155;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 34px;\n"
"    max-width: 34px;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"    padding: 0px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButto"
                        "n#btnPrev:hover,\n"
"QPushButton#btnNext:hover,\n"
"QPushButton#btnPrevPage:hover,\n"
"QPushButton#btnNextPage:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnPrev:disabled,\n"
"QPushButton#btnNext:disabled,\n"
"QPushButton#btnPrevPage:disabled,\n"
"QPushButton#btnNextPage:disabled {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    color: #cbd5e1;\n"
"}\n"
"\n"
"QPushButton#PageNumberButton {\n"
"    background-color: #ffffff;\n"
"    color: #334155;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 32px;\n"
"    max-width: 32px;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"    padding: 0px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#PageNumberButton:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#PageNumberButton:checked {\n"
"    background-color: #1d4ed8"
                        ";\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton#PageNumberButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #94a3b8;\n"
"}\n"
"\n"
"QLabel#lblTotalTitle,\n"
"QLabel#lblActiveTitle,\n"
"QLabel#lblRolesTitle {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#lblTotal,\n"
"QLabel#lblActive,\n"
"QLabel#lblAdminCount,\n"
"QLabel#lblManagerCount,\n"
"QLabel#lblCashierCount {\n"
"    color: #0f172a;\n"
"    font-size: 27px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#lblAdminText,\n"
"QLabel#lblManagerText,\n"
"QLabel#lblCashierText {\n"
"    color: #6b7280;\n"
"    font-size: 11px;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"QLabel#lblTotalDesc,\n"
"QLabel#lblActiveDesc {\n"
"    color: #94a3b8;\n"
"    font-size: 11px;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"QLabel#badgeTotal,\n"
"QLabel#badgeActive,\n"
"QLabel#badgeRoles {\n"
"    background-color: #eff6ff;\n"
"    border-radius: 9"
                        "px;\n"
"}\n"
"\n"
"QFrame#cardTotal,\n"
"QFrame#cardActive,\n"
"QFrame#cardRoles {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"QFrame#line1,\n"
"QFrame#line2 {\n"
"    background-color: #e2e8f0;\n"
"    border: none;\n"
"    max-width: 1px;\n"
"}\n"
"QLineEdit#txtSearch {\n"
"    min-width: 260px;\n"
"}\n"
"QComboBox#cboRole,\n"
"QComboBox#cboStatus {\n"
"    min-width: 170px;\n"
"}")
        self.verticalLayout = QVBoxLayout(PersonnelManagement)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 10, 12, 12)
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(3)
        self.titleLayout.setObjectName(u"titleLayout")
        self.lblTitle = QLabel(PersonnelManagement)
        self.lblTitle.setObjectName(u"lblTitle")

        self.titleLayout.addWidget(self.lblTitle)

        self.lblSub = QLabel(PersonnelManagement)
        self.lblSub.setObjectName(u"lblSub")

        self.titleLayout.addWidget(self.lblSub)


        self.verticalLayout.addLayout(self.titleLayout)

        self.statsLayout = QHBoxLayout()
        self.statsLayout.setSpacing(16)
        self.statsLayout.setObjectName(u"statsLayout")
        self.cardTotal = QFrame(PersonnelManagement)
        self.cardTotal.setObjectName(u"cardTotal")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardTotal.sizePolicy().hasHeightForWidth())
        self.cardTotal.setSizePolicy(sizePolicy)
        self.cardTotal.setMinimumSize(QSize(0, 132))
        self.cardTotal.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutTotal = QVBoxLayout(self.cardTotal)
        self.layoutTotal.setSpacing(6)
        self.layoutTotal.setObjectName(u"layoutTotal")
        self.layoutTotal.setContentsMargins(16, 14, 16, 14)
        self.rowTotalTop = QHBoxLayout()
        self.rowTotalTop.setSpacing(8)
        self.rowTotalTop.setObjectName(u"rowTotalTop")
        self.lblTotalTitle = QLabel(self.cardTotal)
        self.lblTotalTitle.setObjectName(u"lblTotalTitle")

        self.rowTotalTop.addWidget(self.lblTotalTitle)

        self.spacerTotalTop = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowTotalTop.addItem(self.spacerTotalTop)

        self.badgeTotal = QLabel(self.cardTotal)
        self.badgeTotal.setObjectName(u"badgeTotal")
        self.badgeTotal.setMinimumSize(QSize(34, 34))
        self.badgeTotal.setMaximumSize(QSize(34, 34))
        self.badgeTotal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badgeTotal.setProperty(u"iconPx", 17)

        self.rowTotalTop.addWidget(self.badgeTotal)


        self.layoutTotal.addLayout(self.rowTotalTop)

        self.lblTotal = QLabel(self.cardTotal)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setMinimumSize(QSize(0, 25))
        self.lblTotal.setMaximumSize(QSize(16777215, 25))

        self.layoutTotal.addWidget(self.lblTotal)

        self.lblTotalDesc = QLabel(self.cardTotal)
        self.lblTotalDesc.setObjectName(u"lblTotalDesc")
        self.lblTotalDesc.setMinimumSize(QSize(0, 25))

        self.layoutTotal.addWidget(self.lblTotalDesc)

        self.spacerTotal = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutTotal.addItem(self.spacerTotal)


        self.statsLayout.addWidget(self.cardTotal)

        self.cardActive = QFrame(PersonnelManagement)
        self.cardActive.setObjectName(u"cardActive")
        sizePolicy.setHeightForWidth(self.cardActive.sizePolicy().hasHeightForWidth())
        self.cardActive.setSizePolicy(sizePolicy)
        self.cardActive.setMinimumSize(QSize(0, 132))
        self.cardActive.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutActive = QVBoxLayout(self.cardActive)
        self.layoutActive.setSpacing(6)
        self.layoutActive.setObjectName(u"layoutActive")
        self.layoutActive.setContentsMargins(16, 14, 16, 14)
        self.rowActiveTop = QHBoxLayout()
        self.rowActiveTop.setSpacing(8)
        self.rowActiveTop.setObjectName(u"rowActiveTop")
        self.lblActiveTitle = QLabel(self.cardActive)
        self.lblActiveTitle.setObjectName(u"lblActiveTitle")

        self.rowActiveTop.addWidget(self.lblActiveTitle)

        self.spacerActiveTop = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowActiveTop.addItem(self.spacerActiveTop)

        self.badgeActive = QLabel(self.cardActive)
        self.badgeActive.setObjectName(u"badgeActive")
        self.badgeActive.setMinimumSize(QSize(34, 34))
        self.badgeActive.setMaximumSize(QSize(34, 34))
        self.badgeActive.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badgeActive.setProperty(u"iconPx", 17)

        self.rowActiveTop.addWidget(self.badgeActive)


        self.layoutActive.addLayout(self.rowActiveTop)

        self.lblActive = QLabel(self.cardActive)
        self.lblActive.setObjectName(u"lblActive")
        self.lblActive.setMinimumSize(QSize(0, 25))
        self.lblActive.setMaximumSize(QSize(16777215, 25))

        self.layoutActive.addWidget(self.lblActive)

        self.lblActiveDesc = QLabel(self.cardActive)
        self.lblActiveDesc.setObjectName(u"lblActiveDesc")
        self.lblActiveDesc.setMinimumSize(QSize(0, 25))

        self.layoutActive.addWidget(self.lblActiveDesc)

        self.spacerActive = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutActive.addItem(self.spacerActive)


        self.statsLayout.addWidget(self.cardActive)

        self.cardRoles = QFrame(PersonnelManagement)
        self.cardRoles.setObjectName(u"cardRoles")
        sizePolicy.setHeightForWidth(self.cardRoles.sizePolicy().hasHeightForWidth())
        self.cardRoles.setSizePolicy(sizePolicy)
        self.cardRoles.setMinimumSize(QSize(0, 132))
        self.cardRoles.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutRoles = QVBoxLayout(self.cardRoles)
        self.layoutRoles.setSpacing(0)
        self.layoutRoles.setObjectName(u"layoutRoles")
        self.layoutRoles.setContentsMargins(16, 14, 16, 14)
        self.rowRolesTop = QHBoxLayout()
        self.rowRolesTop.setSpacing(8)
        self.rowRolesTop.setObjectName(u"rowRolesTop")
        self.lblRolesTitle = QLabel(self.cardRoles)
        self.lblRolesTitle.setObjectName(u"lblRolesTitle")
        self.lblRolesTitle.setMaximumSize(QSize(16777215, 25))

        self.rowRolesTop.addWidget(self.lblRolesTitle)

        self.spacerRolesTop = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowRolesTop.addItem(self.spacerRolesTop)

        self.badgeRoles = QLabel(self.cardRoles)
        self.badgeRoles.setObjectName(u"badgeRoles")
        self.badgeRoles.setMinimumSize(QSize(34, 34))
        self.badgeRoles.setMaximumSize(QSize(34, 34))
        self.badgeRoles.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badgeRoles.setProperty(u"iconPx", 17)

        self.rowRolesTop.addWidget(self.badgeRoles)


        self.layoutRoles.addLayout(self.rowRolesTop)

        self.layoutRolesData = QHBoxLayout()
        self.layoutRolesData.setSpacing(12)
        self.layoutRolesData.setObjectName(u"layoutRolesData")
        self.layoutAdmin = QVBoxLayout()
        self.layoutAdmin.setSpacing(0)
        self.layoutAdmin.setObjectName(u"layoutAdmin")
        self.lblAdminCount = QLabel(self.cardRoles)
        self.lblAdminCount.setObjectName(u"lblAdminCount")
        self.lblAdminCount.setMinimumSize(QSize(0, 29))
        self.lblAdminCount.setMaximumSize(QSize(16777215, 29))

        self.layoutAdmin.addWidget(self.lblAdminCount)

        self.lblAdminText = QLabel(self.cardRoles)
        self.lblAdminText.setObjectName(u"lblAdminText")
        self.lblAdminText.setMinimumSize(QSize(0, 36))
        self.lblAdminText.setMaximumSize(QSize(16777215, 36))

        self.layoutAdmin.addWidget(self.lblAdminText)


        self.layoutRolesData.addLayout(self.layoutAdmin)

        self.line1 = QFrame(self.cardRoles)
        self.line1.setObjectName(u"line1")
        self.line1.setFrameShape(QFrame.Shape.VLine)

        self.layoutRolesData.addWidget(self.line1)

        self.layoutManager = QVBoxLayout()
        self.layoutManager.setSpacing(0)
        self.layoutManager.setObjectName(u"layoutManager")
        self.lblManagerCount = QLabel(self.cardRoles)
        self.lblManagerCount.setObjectName(u"lblManagerCount")
        self.lblManagerCount.setMinimumSize(QSize(0, 29))
        self.lblManagerCount.setMaximumSize(QSize(16777215, 29))

        self.layoutManager.addWidget(self.lblManagerCount)

        self.lblManagerText = QLabel(self.cardRoles)
        self.lblManagerText.setObjectName(u"lblManagerText")
        self.lblManagerText.setMinimumSize(QSize(0, 36))
        self.lblManagerText.setMaximumSize(QSize(16777215, 36))

        self.layoutManager.addWidget(self.lblManagerText)


        self.layoutRolesData.addLayout(self.layoutManager)

        self.line2 = QFrame(self.cardRoles)
        self.line2.setObjectName(u"line2")
        self.line2.setFrameShape(QFrame.Shape.VLine)

        self.layoutRolesData.addWidget(self.line2)

        self.layoutCashier = QVBoxLayout()
        self.layoutCashier.setSpacing(0)
        self.layoutCashier.setObjectName(u"layoutCashier")
        self.lblCashierCount = QLabel(self.cardRoles)
        self.lblCashierCount.setObjectName(u"lblCashierCount")
        self.lblCashierCount.setMinimumSize(QSize(0, 29))
        self.lblCashierCount.setMaximumSize(QSize(16777215, 29))

        self.layoutCashier.addWidget(self.lblCashierCount)

        self.lblCashierText = QLabel(self.cardRoles)
        self.lblCashierText.setObjectName(u"lblCashierText")
        self.lblCashierText.setMinimumSize(QSize(0, 36))
        self.lblCashierText.setMaximumSize(QSize(16777215, 36))

        self.layoutCashier.addWidget(self.lblCashierText)


        self.layoutRolesData.addLayout(self.layoutCashier)


        self.layoutRoles.addLayout(self.layoutRolesData)

        self.spacerRoles = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutRoles.addItem(self.spacerRoles)


        self.statsLayout.addWidget(self.cardRoles)


        self.verticalLayout.addLayout(self.statsLayout)

        self.frameTable = QFrame(PersonnelManagement)
        self.frameTable.setObjectName(u"frameTable")
        self.frameTable.setFrameShape(QFrame.Shape.NoFrame)
        self.tableFrameLayout = QVBoxLayout(self.frameTable)
        self.tableFrameLayout.setSpacing(12)
        self.tableFrameLayout.setObjectName(u"tableFrameLayout")
        self.tableFrameLayout.setContentsMargins(12, 12, 12, 12)
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setSpacing(8)
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.txtSearch = QLineEdit(self.frameTable)
        self.txtSearch.setObjectName(u"txtSearch")

        self.toolbarLayout.addWidget(self.txtSearch)

        self.cboRole = QComboBox(self.frameTable)
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.addItem("")
        self.cboRole.setObjectName(u"cboRole")

        self.toolbarLayout.addWidget(self.cboRole)

        self.cboStatus = QComboBox(self.frameTable)
        self.cboStatus.addItem("")
        self.cboStatus.addItem("")
        self.cboStatus.addItem("")
        self.cboStatus.setObjectName(u"cboStatus")

        self.toolbarLayout.addWidget(self.cboStatus)

        self.btnAdd = QPushButton(self.frameTable)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toolbarLayout.addWidget(self.btnAdd)


        self.tableFrameLayout.addLayout(self.toolbarLayout)

        self.tblEmployees = QTableWidget(self.frameTable)
        if (self.tblEmployees.columnCount() < 6):
            self.tblEmployees.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblEmployees.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblEmployees.setObjectName(u"tblEmployees")
        self.tblEmployees.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tblEmployees.setFrameShape(QFrame.Shape.NoFrame)
        self.tblEmployees.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblEmployees.setAlternatingRowColors(False)
        self.tblEmployees.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblEmployees.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblEmployees.setShowGrid(False)
        self.tblEmployees.horizontalHeader().setMinimumSectionSize(90)
        self.tblEmployees.horizontalHeader().setDefaultSectionSize(130)
        self.tblEmployees.horizontalHeader().setHighlightSections(False)
        self.tblEmployees.horizontalHeader().setStretchLastSection(True)
        self.tblEmployees.verticalHeader().setVisible(False)
        self.tblEmployees.verticalHeader().setMinimumSectionSize(44)
        self.tblEmployees.verticalHeader().setDefaultSectionSize(44)

        self.tableFrameLayout.addWidget(self.tblEmployees)


        self.verticalLayout.addWidget(self.frameTable)


        self.retranslateUi(PersonnelManagement)

        QMetaObject.connectSlotsByName(PersonnelManagement)
    # setupUi

    def retranslateUi(self, PersonnelManagement):
        PersonnelManagement.setWindowTitle(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n l\u00fd Nh\u00e2n s\u1ef1", None))
        self.lblTitle.setText(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n l\u00fd Nh\u00e2n s\u1ef1", None))
        self.lblSub.setText(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n l\u00fd th\u00f4ng tin nh\u00e2n vi\u00ean v\u00e0 ph\u00e2n quy\u1ec1n truy c\u1eadp h\u1ec7 th\u1ed1ng.", None))
        self.lblTotalTitle.setText(QCoreApplication.translate("PersonnelManagement", u"T\u1ed5ng s\u1ed1 nh\u00e2n vi\u00ean", None))
        self.badgeTotal.setText("")
        self.badgeTotal.setProperty(u"iconName", QCoreApplication.translate("PersonnelManagement", u"customers", None))
        self.badgeTotal.setProperty(u"iconColor", QCoreApplication.translate("PersonnelManagement", u"#1d4ed8", None))
        self.lblTotal.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.lblTotalDesc.setText(QCoreApplication.translate("PersonnelManagement", u"T\u00e0i kho\u1ea3n nh\u00e2n s\u1ef1 trong h\u1ec7 th\u1ed1ng", None))
        self.lblActiveTitle.setText(QCoreApplication.translate("PersonnelManagement", u"\u0110ang ho\u1ea1t \u0111\u1ed9ng", None))
        self.badgeActive.setText("")
        self.badgeActive.setProperty(u"iconName", QCoreApplication.translate("PersonnelManagement", u"user-active", None))
        self.badgeActive.setProperty(u"iconColor", QCoreApplication.translate("PersonnelManagement", u"#1d4ed8", None))
        self.lblActive.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.lblActiveDesc.setText(QCoreApplication.translate("PersonnelManagement", u"T\u00e0i kho\u1ea3n \u0111\u01b0\u1ee3c ph\u00e9p \u0111\u0103ng nh\u1eadp", None))
        self.lblRolesTitle.setText(QCoreApplication.translate("PersonnelManagement", u"Ph\u00e2n b\u1ed5 vai tr\u00f2", None))
        self.badgeRoles.setText("")
        self.badgeRoles.setProperty(u"iconName", QCoreApplication.translate("PersonnelManagement", u"role", None))
        self.badgeRoles.setProperty(u"iconColor", QCoreApplication.translate("PersonnelManagement", u"#1d4ed8", None))
        self.lblAdminCount.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.lblAdminText.setText(QCoreApplication.translate("PersonnelManagement", u"Qu\u1ea3n tr\u1ecb vi\u00ean", None))
        self.lblManagerCount.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.lblManagerText.setText(QCoreApplication.translate("PersonnelManagement", u"B\u00e1n h\u00e0ng", None))
        self.lblCashierCount.setText(QCoreApplication.translate("PersonnelManagement", u"0", None))
        self.lblCashierText.setText(QCoreApplication.translate("PersonnelManagement", u"Kho", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("PersonnelManagement", u"T\u00ecm ki\u1ebfm theo h\u1ecd t\u00ean ho\u1eb7c t\u00ean \u0111\u0103ng nh\u1eadp", None))
        self.cboRole.setItemText(0, QCoreApplication.translate("PersonnelManagement", u"T\u1ea5t c\u1ea3 ch\u1ee9c v\u1ee5", None))
        self.cboRole.setItemText(1, QCoreApplication.translate("PersonnelManagement", u"Admin", None))
        self.cboRole.setItemText(2, QCoreApplication.translate("PersonnelManagement", u"Cashier", None))
        self.cboRole.setItemText(3, QCoreApplication.translate("PersonnelManagement", u"Warehouse", None))

        self.cboStatus.setItemText(0, QCoreApplication.translate("PersonnelManagement", u"T\u1ea5t c\u1ea3 tr\u1ea1ng th\u00e1i", None))
        self.cboStatus.setItemText(1, QCoreApplication.translate("PersonnelManagement", u"Ho\u1ea1t \u0111\u1ed9ng", None))
        self.cboStatus.setItemText(2, QCoreApplication.translate("PersonnelManagement", u"Kh\u00f3a", None))

        self.btnAdd.setText(QCoreApplication.translate("PersonnelManagement", u"+ Th\u00eam nh\u00e2n s\u1ef1", None))
        ___qtablewidgetitem = self.tblEmployees.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PersonnelManagement", u"M\u00c3 T\u00c0I KHO\u1ea2N", None))
        ___qtablewidgetitem1 = self.tblEmployees.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PersonnelManagement", u"H\u1ecc T\u00caN", None))
        ___qtablewidgetitem2 = self.tblEmployees.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PersonnelManagement", u"T\u00caN \u0110\u0102NG NH\u1eacP", None))
        ___qtablewidgetitem3 = self.tblEmployees.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PersonnelManagement", u"VAI TR\u00d2", None))
        ___qtablewidgetitem4 = self.tblEmployees.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PersonnelManagement", u"TR\u1ea0NG TH\u00c1I", None))
        ___qtablewidgetitem5 = self.tblEmployees.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PersonnelManagement", u"THAO T\u00c1C", None))
    # retranslateUi

