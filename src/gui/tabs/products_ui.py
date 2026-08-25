# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products.ui'
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

class Ui_SanPhamTab(object):
    def setupUi(self, SanPhamTab):
        if not SanPhamTab.objectName():
            SanPhamTab.setObjectName(u"SanPhamTab")
        SanPhamTab.resize(1000, 650)
        SanPhamTab.setStyleSheet(u"\n"
"QWidget#SanPhamTab {\n"
"    background-color: #f1f5f9;\n"
"    color: #0f172a;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #0f172a;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"    color: #0f172a;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"QLabel#lblSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"QFrame#frameHeader,\n"
"QFrame#frameToolbar,\n"
"QFrame#framePagination {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit#edtSearch {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 12px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    color: #0f172a;\n"
"}\n"
"QLineEdit#edtSearch:focus {\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"QComboBox#cbDanhMuc {\n"
"    background-color: #ffffff;\n"
"    border: 1px s"
                        "olid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 12px;\n"
"    min-width: 150px;\n"
"    min-height: 38px;\n"
"    font-size: 13px;\n"
"    color: #334155;\n"
"}\n"
"QComboBox#cbDanhMuc:hover {\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QComboBox#cbDanhMuc QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: none;\n"
"    selection-background-color: #eff6ff;\n"
"    selection-color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton#btnsua,\n"
"QPushButton#btnThemdm {\n"
"    background-color: #ffffff;\n"
"    color: #64748b;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnsua:hover,\n"
"QPushButton#btnThemdm:hover {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"}\n"
"\n"
"QPushButton#btnXo"
                        "a {\n"
"    background-color: #ffffff;\n"
"    color: #dc2626;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    padding: 0px 16px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnXoa:hover {\n"
"    background-color: #fef2f2;\n"
"    border: 1px solid #dc2626;\n"
"}\n"
"\n"
"QPushButton#btnThem {\n"
"    background-color: #2563eb;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0px 18px;\n"
"    min-height: 38px;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnThem:hover {\n"
"    background-color: #1d4ed8;\n"
"}\n"
"QPushButton#btnThem:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"\n"
"QFrame#frameTable {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"QTableWidget#tableSanPham {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: #f1f5f9;\n"
"    font-size: 13px"
                        ";\n"
"    color: #334155;\n"
"    outline: none;\n"
"}\n"
"QTableWidget#tableSanPham::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f1f5f9;\n"
"}\n"
"QTableWidget#tableSanPham::item:selected {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
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
"QLabel[class=\"badgeSuccess\"] {\n"
"    background-color: #dbeafe;\n"
"    color: #1d4ed8;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[class=\"badgeWarning\"] {\n"
"    background-color: #ffedd5;\n"
"    color: #ea580c;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
""
                        "}\n"
"QLabel[class=\"badgeDanger\"] {\n"
"    background-color: #fee2e2;\n"
"    color: #dc2626;\n"
"    border-radius: 6px;\n"
"    padding: 3px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#lblPage {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton#btnPrev,\n"
"QPushButton#btnNext {\n"
"    background-color: #ffffff;\n"
"    color: #334155;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 34px;\n"
"    max-width: 34px;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnPrev:hover,\n"
"QPushButton#btnNext:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#btnPrev:disabled,\n"
"QPushButton#btnNext:disabled {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    color: #cbd5e1;\n"
"}\n"
"\n"
"QPushButton#PageNumberButton {\n"
"    background-color: #fff"
                        "fff;\n"
"    color: #334155;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 32px;\n"
"    max-width: 32px;\n"
"    min-height: 32px;\n"
"    max-height: 32px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#PageNumberButton:hover {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #1d4ed8;\n"
"}\n"
"QPushButton#PageNumberButton:checked {\n"
"    background-color: #1d4ed8;\n"
"    border: 1px solid #1d4ed8;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton#PageNumberButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #94a3b8;\n"
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
""
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
"QScrollBar:"
                        ":sub-line:horizontal {\n"
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
        self.verticalLayout = QVBoxLayout(SanPhamTab)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 10, 12, 12)
        self.frameHeader = QFrame(SanPhamTab)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frameHeader)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.lblTitle = QLabel(self.frameHeader)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout_2.addWidget(self.lblTitle)

        self.lblSubtitle = QLabel(self.frameHeader)
        self.lblSubtitle.setObjectName(u"lblSubtitle")

        self.verticalLayout_2.addWidget(self.lblSubtitle)


        self.verticalLayout.addWidget(self.frameHeader)

        self.frameToolbar = QFrame(SanPhamTab)
        self.frameToolbar.setObjectName(u"frameToolbar")
        self.frameToolbar.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frameToolbar)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.edtSearch = QLineEdit(self.frameToolbar)
        self.edtSearch.setObjectName(u"edtSearch")
        self.edtSearch.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.edtSearch)

        self.cbDanhMuc = QComboBox(self.frameToolbar)
        self.cbDanhMuc.addItem("")
        self.cbDanhMuc.setObjectName(u"cbDanhMuc")
        self.cbDanhMuc.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.cbDanhMuc)

        self.btnsua = QPushButton(self.frameToolbar)
        self.btnsua.setObjectName(u"btnsua")
        self.btnsua.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btnsua)

        self.btnXoa = QPushButton(self.frameToolbar)
        self.btnXoa.setObjectName(u"btnXoa")
        self.btnXoa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btnXoa)

        self.btnThemdm = QPushButton(self.frameToolbar)
        self.btnThemdm.setObjectName(u"btnThemdm")
        self.btnThemdm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btnThemdm)

        self.btnThem = QPushButton(self.frameToolbar)
        self.btnThem.setObjectName(u"btnThem")
        self.btnThem.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btnThem)


        self.verticalLayout.addWidget(self.frameToolbar)

        self.frameTable = QFrame(SanPhamTab)
        self.frameTable.setObjectName(u"frameTable")
        self.frameTable.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTable)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.tableSanPham = QTableWidget(self.frameTable)
        if (self.tableSanPham.columnCount() < 7):
            self.tableSanPham.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableSanPham.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableSanPham.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableSanPham.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableSanPham.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableSanPham.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableSanPham.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableSanPham.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableSanPham.setObjectName(u"tableSanPham")
        self.tableSanPham.setFrameShape(QFrame.Shape.NoFrame)
        self.tableSanPham.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableSanPham.setAlternatingRowColors(False)
        self.tableSanPham.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableSanPham.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableSanPham.setShowGrid(False)
        self.tableSanPham.horizontalHeader().setMinimumSectionSize(90)
        self.tableSanPham.horizontalHeader().setDefaultSectionSize(130)
        self.tableSanPham.horizontalHeader().setHighlightSections(False)
        self.tableSanPham.horizontalHeader().setStretchLastSection(True)
        self.tableSanPham.verticalHeader().setVisible(False)
        self.tableSanPham.verticalHeader().setDefaultSectionSize(44)

        self.horizontalLayout_2.addWidget(self.tableSanPham)


        self.verticalLayout.addWidget(self.frameTable)

        self.framePagination = QFrame(SanPhamTab)
        self.framePagination.setObjectName(u"framePagination")
        self.framePagination.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.framePagination)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lblPage = QLabel(self.framePagination)
        self.lblPage.setObjectName(u"lblPage")

        self.horizontalLayout_4.addWidget(self.lblPage)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btnPrev = QPushButton(self.framePagination)
        self.btnPrev.setObjectName(u"btnPrev")
        self.btnPrev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrev.setProperty(u"iconPx", 12)

        self.horizontalLayout_4.addWidget(self.btnPrev)

        self.horizontalLayout_pageNumbers = QHBoxLayout()
        self.horizontalLayout_pageNumbers.setSpacing(6)
        self.horizontalLayout_pageNumbers.setObjectName(u"horizontalLayout_pageNumbers")

        self.horizontalLayout_4.addLayout(self.horizontalLayout_pageNumbers)

        self.btnNext = QPushButton(self.framePagination)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNext.setProperty(u"iconPx", 12)

        self.horizontalLayout_4.addWidget(self.btnNext)


        self.verticalLayout.addWidget(self.framePagination)


        self.retranslateUi(SanPhamTab)

        QMetaObject.connectSlotsByName(SanPhamTab)
    # setupUi

    def retranslateUi(self, SanPhamTab):
        SanPhamTab.setWindowTitle(QCoreApplication.translate("SanPhamTab", u"Qu\u1ea3n l\u00fd S\u1ea3n ph\u1ea9m", None))
        self.lblTitle.setText(QCoreApplication.translate("SanPhamTab", u"Qu\u1ea3n l\u00fd S\u1ea3n ph\u1ea9m", None))
        self.lblSubtitle.setText(QCoreApplication.translate("SanPhamTab", u"Danh s\u00e1ch chi ti\u1ebft v\u00e0 ki\u1ec3m so\u00e1t t\u1ed3n kho to\u00e0n h\u1ec7 th\u1ed1ng.", None))
        self.edtSearch.setPlaceholderText(QCoreApplication.translate("SanPhamTab", u"Nh\u1eadp t\u1eeb kh\u00f3a t\u00ecm ki\u1ebfm...", None))
        self.cbDanhMuc.setItemText(0, QCoreApplication.translate("SanPhamTab", u"T\u1ea5t c\u1ea3 danh m\u1ee5c", None))

        self.btnsua.setText(QCoreApplication.translate("SanPhamTab", u"S\u1eeda", None))
        self.btnsua.setProperty(u"iconName", QCoreApplication.translate("SanPhamTab", u"fa5s.pen", None))
        self.btnsua.setProperty(u"iconColor", QCoreApplication.translate("SanPhamTab", u"#64748b", None))
        self.btnXoa.setText(QCoreApplication.translate("SanPhamTab", u"X\u00f3a", None))
        self.btnXoa.setProperty(u"iconName", QCoreApplication.translate("SanPhamTab", u"fa5s.trash-alt", None))
        self.btnXoa.setProperty(u"iconColor", QCoreApplication.translate("SanPhamTab", u"#dc2626", None))
        self.btnThemdm.setText(QCoreApplication.translate("SanPhamTab", u"Th\u00eam danh m\u1ee5c", None))
        self.btnThemdm.setProperty(u"iconName", QCoreApplication.translate("SanPhamTab", u"fa5s.folder-plus", None))
        self.btnThemdm.setProperty(u"iconColor", QCoreApplication.translate("SanPhamTab", u"#64748b", None))
        self.btnThem.setText(QCoreApplication.translate("SanPhamTab", u"Th\u00eam s\u1ea3n ph\u1ea9m", None))
        self.btnThem.setProperty(u"iconName", QCoreApplication.translate("SanPhamTab", u"fa5s.plus", None))
        self.btnThem.setProperty(u"iconColor", QCoreApplication.translate("SanPhamTab", u"#ffffff", None))
        ___qtablewidgetitem = self.tableSanPham.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SanPhamTab", u"M\u00c3 V\u1ea0CH", None))
        ___qtablewidgetitem1 = self.tableSanPham.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SanPhamTab", u"T\u00caN S\u1ea2N PH\u1ea8M", None))
        ___qtablewidgetitem2 = self.tableSanPham.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SanPhamTab", u"DANH M\u1ee4C", None))
        ___qtablewidgetitem3 = self.tableSanPham.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SanPhamTab", u"\u0110\u01a0N V\u1eca", None))
        ___qtablewidgetitem4 = self.tableSanPham.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SanPhamTab", u"GI\u00c1 B\u00c1N L\u1eba (VN\u0110)", None))
        ___qtablewidgetitem5 = self.tableSanPham.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SanPhamTab", u"T\u1ed2N KHO", None))
        ___qtablewidgetitem6 = self.tableSanPham.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SanPhamTab", u"TR\u1ea0NG TH\u00c1I", None))
        self.lblPage.setText(QCoreApplication.translate("SanPhamTab", u"Hi\u1ec3n th\u1ecb 1 \u0111\u1ebfn 10 c\u1ee7a 0 s\u1ea3n ph\u1ea9m", None))
        self.btnPrev.setText("")
        self.btnPrev.setProperty(u"iconName", QCoreApplication.translate("SanPhamTab", u"fa5s.chevron-left", None))
        self.btnPrev.setProperty(u"iconColor", QCoreApplication.translate("SanPhamTab", u"#334155", None))
        self.btnNext.setText("")
        self.btnNext.setProperty(u"iconName", QCoreApplication.translate("SanPhamTab", u"fa5s.chevron-right", None))
        self.btnNext.setProperty(u"iconColor", QCoreApplication.translate("SanPhamTab", u"#334155", None))
    # retranslateUi

