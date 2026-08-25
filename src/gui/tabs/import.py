# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_NhapHangTab(object):
    def setupUi(self, NhapHangTab):
        if not NhapHangTab.objectName():
            NhapHangTab.setObjectName(u"NhapHangTab")
        NhapHangTab.resize(940, 680)
        NhapHangTab.setStyleSheet(u"background-color: #f8fafc;")
        self.verticalLayout = QVBoxLayout(NhapHangTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.verticalLayout_title = QVBoxLayout()
        self.verticalLayout_title.setObjectName(u"verticalLayout_title")
        self.lblTitle = QLabel(NhapHangTab)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setStyleSheet(u"font-size:22px; font-weight:bold; color:#0f172a;")

        self.verticalLayout_title.addWidget(self.lblTitle)

        self.lblSubtitle = QLabel(NhapHangTab)
        self.lblSubtitle.setObjectName(u"lblSubtitle")
        self.lblSubtitle.setStyleSheet(u"color:#64748b; font-size:12px;")

        self.verticalLayout_title.addWidget(self.lblSubtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_title)

        self.horizontalSpacer_header = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)

        self.btnTaoPhieu = QPushButton(NhapHangTab)
        self.btnTaoPhieu.setObjectName(u"btnTaoPhieu")
        self.btnTaoPhieu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnTaoPhieu.setStyleSheet(u"QPushButton { background-color:#1d4ed8; color:white; border-radius:6px; padding:10px 18px; font-weight:bold; }\n"
"QPushButton:hover { background-color:#1e40af; }")

        self.horizontalLayout_header.addWidget(self.btnTaoPhieu)


        self.verticalLayout.addLayout(self.horizontalLayout_header)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cardTongChi = QFrame(NhapHangTab)
        self.cardTongChi.setObjectName(u"cardTongChi")
        self.cardTongChi.setStyleSheet(u"QFrame#cardTongChi { background:white; border-radius:8px; border:1px solid #e2e8f0; }")
        self.verticalLayout_card1 = QVBoxLayout(self.cardTongChi)
        self.verticalLayout_card1.setObjectName(u"verticalLayout_card1")
        self.verticalLayout_card1.setContentsMargins(16, 16, 16, 16)
        self.lblTongChiTitle = QLabel(self.cardTongChi)
        self.lblTongChiTitle.setObjectName(u"lblTongChiTitle")
        self.lblTongChiTitle.setStyleSheet(u"color:#64748b; font-size:11px; font-weight:bold;")

        self.verticalLayout_card1.addWidget(self.lblTongChiTitle)

        self.lblTongChi = QLabel(self.cardTongChi)
        self.lblTongChi.setObjectName(u"lblTongChi")
        self.lblTongChi.setStyleSheet(u"font-size:24px; font-weight:bold; color:#0f172a;")

        self.verticalLayout_card1.addWidget(self.lblTongChi)

        self.lblTongChiSub = QLabel(self.cardTongChi)
        self.lblTongChiSub.setObjectName(u"lblTongChiSub")
        self.lblTongChiSub.setStyleSheet(u"color:#16a34a; font-size:11px;")

        self.verticalLayout_card1.addWidget(self.lblTongChiSub)


        self.horizontalLayout.addWidget(self.cardTongChi)

        self.cardGanDay = QFrame(NhapHangTab)
        self.cardGanDay.setObjectName(u"cardGanDay")
        self.cardGanDay.setStyleSheet(u"QFrame#cardGanDay { background:white; border-radius:8px; border:1px solid #e2e8f0; }")
        self.verticalLayout_card3 = QVBoxLayout(self.cardGanDay)
        self.verticalLayout_card3.setObjectName(u"verticalLayout_card3")
        self.verticalLayout_card3.setContentsMargins(16, 16, 16, 16)
        self.lblGanDayTitle = QLabel(self.cardGanDay)
        self.lblGanDayTitle.setObjectName(u"lblGanDayTitle")
        self.lblGanDayTitle.setStyleSheet(u"color:#64748b; font-size:11px; font-weight:bold;")

        self.verticalLayout_card3.addWidget(self.lblGanDayTitle)

        self.lblGanDay = QLabel(self.cardGanDay)
        self.lblGanDay.setObjectName(u"lblGanDay")
        self.lblGanDay.setStyleSheet(u"font-size:24px; font-weight:bold; color:#0f172a;")

        self.verticalLayout_card3.addWidget(self.lblGanDay)

        self.lblGanDaySub = QLabel(self.cardGanDay)
        self.lblGanDaySub.setObjectName(u"lblGanDaySub")
        self.lblGanDaySub.setStyleSheet(u"color:#64748b; font-size:11px;")

        self.verticalLayout_card3.addWidget(self.lblGanDaySub)


        self.horizontalLayout.addWidget(self.cardGanDay)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frameTable = QFrame(NhapHangTab)
        self.frameTable.setObjectName(u"frameTable")
        self.frameTable.setStyleSheet(u"#frameTable { background:white; border-radius:8px; border:1px solid #e2e8f0; }")
        self.verticalLayout_table = QVBoxLayout(self.frameTable)
        self.verticalLayout_table.setObjectName(u"verticalLayout_table")
        self.horizontalLayout_tableHeader = QHBoxLayout()
        self.horizontalLayout_tableHeader.setObjectName(u"horizontalLayout_tableHeader")
        self.horizontalLayout_tableHeader.setContentsMargins(12, 12, 12, -1)
        self.lblDanhSach = QLabel(self.frameTable)
        self.lblDanhSach.setObjectName(u"lblDanhSach")
        self.lblDanhSach.setStyleSheet(u"font-weight:bold; font-size:14px;")

        self.horizontalLayout_tableHeader.addWidget(self.lblDanhSach)

        self.horizontalSpacer_tbl = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_tableHeader.addItem(self.horizontalSpacer_tbl)

        self.cbTrangThai = QComboBox(self.frameTable)
        self.cbTrangThai.addItem("")
        self.cbTrangThai.addItem("")
        self.cbTrangThai.addItem("")
        self.cbTrangThai.setObjectName(u"cbTrangThai")

        self.horizontalLayout_tableHeader.addWidget(self.cbTrangThai)


        self.verticalLayout_table.addLayout(self.horizontalLayout_tableHeader)

        self.tablePhieuNhap = QTableWidget(self.frameTable)
        if (self.tablePhieuNhap.columnCount() < 6):
            self.tablePhieuNhap.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePhieuNhap.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePhieuNhap.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePhieuNhap.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablePhieuNhap.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablePhieuNhap.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablePhieuNhap.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tablePhieuNhap.setObjectName(u"tablePhieuNhap")
        self.tablePhieuNhap.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePhieuNhap.setAlternatingRowColors(True)
        self.tablePhieuNhap.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tablePhieuNhap.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_table.addWidget(self.tablePhieuNhap)


        self.verticalLayout.addWidget(self.frameTable)

        self.horizontalLayout_pagination = QHBoxLayout()
        self.horizontalLayout_pagination.setObjectName(u"horizontalLayout_pagination")
        self.lblPage = QLabel(NhapHangTab)
        self.lblPage.setObjectName(u"lblPage")
        self.lblPage.setStyleSheet(u"color:#64748b; font-size:12px;")

        self.horizontalLayout_pagination.addWidget(self.lblPage)

        self.horizontalSpacer_pg = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_pagination.addItem(self.horizontalSpacer_pg)

        self.btnPrev = QPushButton(NhapHangTab)
        self.btnPrev.setObjectName(u"btnPrev")
        self.btnPrev.setMaximumSize(QSize(36, 32))

        self.horizontalLayout_pagination.addWidget(self.btnPrev)

        self.btnNext = QPushButton(NhapHangTab)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setMaximumSize(QSize(36, 32))

        self.horizontalLayout_pagination.addWidget(self.btnNext)


        self.verticalLayout.addLayout(self.horizontalLayout_pagination)


        self.retranslateUi(NhapHangTab)

        QMetaObject.connectSlotsByName(NhapHangTab)
    # setupUi

    def retranslateUi(self, NhapHangTab):
        self.lblTitle.setText(QCoreApplication.translate("NhapHangTab", u"Qu\u1ea3n l\u00fd Nh\u1eadp h\u00e0ng", None))
        self.lblSubtitle.setText(QCoreApplication.translate("NhapHangTab", u"Theo d\u00f5i v\u00e0 qu\u1ea3n l\u00fd c\u00e1c phi\u1ebfu nh\u1eadp kho t\u1eeb nh\u00e0 cung c\u1ea5p.", None))
        self.btnTaoPhieu.setText(QCoreApplication.translate("NhapHangTab", u"+  T\u1ea1o Phi\u1ebfu Nh\u1eadp", None))
        self.lblTongChiTitle.setText(QCoreApplication.translate("NhapHangTab", u"T\u1ed4NG CHI TH\u00c1NG N\u00c0Y", None))
        self.lblTongChi.setText(QCoreApplication.translate("NhapHangTab", u"\u0111 0", None))
        self.lblTongChiSub.setText(QCoreApplication.translate("NhapHangTab", u"so v\u1edbi th\u00e1ng tr\u01b0\u1edbc", None))
        self.lblGanDayTitle.setText(QCoreApplication.translate("NhapHangTab", u"L\u01af\u1ee2T NH\u1eacP G\u1ea6N \u0110\u00c2Y", None))
        self.lblGanDay.setText(QCoreApplication.translate("NhapHangTab", u"0", None))
        self.lblGanDaySub.setText(QCoreApplication.translate("NhapHangTab", u"Trong 7 ng\u00e0y qua", None))
        self.lblDanhSach.setText(QCoreApplication.translate("NhapHangTab", u"Danh s\u00e1ch Phi\u1ebfu Nh\u1eadp", None))
        self.cbTrangThai.setItemText(0, QCoreApplication.translate("NhapHangTab", u"T\u1ea5t c\u1ea3 tr\u1ea1ng th\u00e1i", None))
        self.cbTrangThai.setItemText(1, QCoreApplication.translate("NhapHangTab", u"Ho\u00e0n th\u00e0nh", None))
        self.cbTrangThai.setItemText(2, QCoreApplication.translate("NhapHangTab", u"Ch\u1edd x\u1eed l\u00fd", None))

        ___qtablewidgetitem = self.tablePhieuNhap.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NhapHangTab", u"M\u00e3 nh\u1eadp", None))
        ___qtablewidgetitem1 = self.tablePhieuNhap.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NhapHangTab", u"Nh\u00e0 cung c\u1ea5p", None))
        ___qtablewidgetitem2 = self.tablePhieuNhap.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NhapHangTab", u"Ng\u00e0y nh\u1eadp", None))
        ___qtablewidgetitem3 = self.tablePhieuNhap.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NhapHangTab", u"T\u1ed5ng ti\u1ec1n", None))
        ___qtablewidgetitem4 = self.tablePhieuNhap.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NhapHangTab", u"Tr\u1ea1ng th\u00e1i", None))
        ___qtablewidgetitem5 = self.tablePhieuNhap.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("NhapHangTab", u"Ng\u01b0\u1eddi t\u1ea1o", None))
        self.lblPage.setText(QCoreApplication.translate("NhapHangTab", u"Hi\u1ec3n th\u1ecb 1-10 c\u1ee7a 0 m\u1ee5c", None))
        self.btnPrev.setText(QCoreApplication.translate("NhapHangTab", u"\u2039", None))
        self.btnNext.setText(QCoreApplication.translate("NhapHangTab", u"\u203a", None))
        pass
    # retranslateUi

