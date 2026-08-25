# Form implementation generated from reading ui file 'products.ui'
from PySide6 import QtCore, QtGui, QtWidgets


class Ui_SanPhamTab(object):
    def setupUi(self, SanPhamTab):
        SanPhamTab.setObjectName("SanPhamTab")
        SanPhamTab.resize(1000, 650)
        SanPhamTab.setStyleSheet("background-color: #f8fafc;")

        self.verticalLayout = QtWidgets.QVBoxLayout(SanPhamTab)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")

        # HEADER TITLE SECTION
        self.frameHeader = QtWidgets.QFrame(parent=SanPhamTab)
        self.frameHeader.setStyleSheet("border: none;")
        self.frameHeader.setObjectName("frameHeader")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameHeader)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lblTitle = QtWidgets.QLabel(parent=self.frameHeader)
        self.lblTitle.setStyleSheet("font-size: 24px; font-weight: bold; color: #0f172a;")
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_2.addWidget(self.lblTitle)

        self.lblSubtitle = QtWidgets.QLabel(parent=self.frameHeader)
        self.lblSubtitle.setStyleSheet("color: #64748b; font-size: 14px;")
        self.lblSubtitle.setObjectName("lblSubtitle")
        self.verticalLayout_2.addWidget(self.lblSubtitle)

        self.verticalLayout.addWidget(self.frameHeader)

        # TOOLBAR SECTION
        self.frameToolbar = QtWidgets.QFrame(parent=SanPhamTab)
        self.frameToolbar.setStyleSheet("border: none;")
        self.frameToolbar.setObjectName("frameToolbar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameToolbar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.edtSearch = QtWidgets.QLineEdit(parent=self.frameToolbar)
        self.edtSearch.setMinimumSize(QtCore.QSize(0, 40))
        self.edtSearch.setStyleSheet(
            "QLineEdit { border: 1px solid #cbd5e1; border-radius: 6px; padding: 0 12px; background: #ffffff; color: #0f172a; font-size: 13px; }\n"
            "QLineEdit:focus { border: 1px solid #1d4ed8; }"
        )
        self.edtSearch.setObjectName("edtSearch")
        self.horizontalLayout_3.addWidget(self.edtSearch)

        self.cbDanhMuc = QtWidgets.QComboBox(parent=self.frameToolbar)
        self.cbDanhMuc.setMinimumSize(QtCore.QSize(160, 40))
        self.cbDanhMuc.setStyleSheet(
            "QComboBox { border: 1px solid #cbd5e1; border-radius: 6px; padding: 0 10px; background: #ffffff; color: #334155; font-size: 13px; }\n"
            "QComboBox:hover { border-color: #94a3b8; }"
        )
        self.cbDanhMuc.setObjectName("cbDanhMuc")
        self.cbDanhMuc.addItem("")
        self.horizontalLayout_3.addWidget(self.cbDanhMuc)

        self.btnsua = QtWidgets.QPushButton(parent=self.frameToolbar)
        self.btnsua.setMinimumSize(QtCore.QSize(0, 40))
        self.btnsua.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnsua.setStyleSheet(
            "QPushButton { background-color: #ffffff; border: 1px solid #cbd5e1; color: #334155; border-radius: 6px; padding: 0 16px; font-weight: 600; font-size: 13px; }\n"
            "QPushButton:hover { background-color: #f8fafc; border-color: #94a3b8; color: #0f172a; }"
        )
        self.btnsua.setObjectName("btnsua")
        self.horizontalLayout_3.addWidget(self.btnsua)

        self.btnXoa = QtWidgets.QPushButton(parent=self.frameToolbar)
        self.btnXoa.setMinimumSize(QtCore.QSize(0, 40))
        self.btnXoa.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnXoa.setStyleSheet(
            "QPushButton { background-color: #fef2f2; border: 1px solid #fca5a5; color: #dc2626; border-radius: 6px; padding: 0 16px; font-weight: 600; font-size: 13px; }\n"
            "QPushButton:hover { background-color: #fee2e2; border-color: #f87171; }"
        )
        self.btnXoa.setObjectName("btnXoa")
        self.horizontalLayout_3.addWidget(self.btnXoa)

        self.btnThemdm = QtWidgets.QPushButton(parent=self.frameToolbar)
        self.btnThemdm.setMinimumSize(QtCore.QSize(0, 40))
        self.btnThemdm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnThemdm.setStyleSheet(
            "QPushButton { background-color: #ffffff; border: 1px solid #cbd5e1; color: #0f172a; border-radius: 6px; padding: 0 16px; font-weight: 600; font-size: 13px; }\n"
            "QPushButton:hover { background-color: #f8fafc; border-color: #94a3b8; }"
        )
        self.btnThemdm.setObjectName("btnThemdm")
        self.horizontalLayout_3.addWidget(self.btnThemdm)

        self.btnThem = QtWidgets.QPushButton(parent=self.frameToolbar)
        self.btnThem.setMinimumSize(QtCore.QSize(0, 40))
        self.btnThem.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnThem.setStyleSheet(
            "QPushButton { background-color: #1d4ed8; color: #ffffff; border: none; border-radius: 6px; padding: 0 18px; font-weight: bold; font-size: 13px; }\n"
            "QPushButton:hover { background-color: #1e40af; }"
        )
        self.btnThem.setObjectName("btnThem")
        self.horizontalLayout_3.addWidget(self.btnThem)

        self.verticalLayout.addWidget(self.frameToolbar)

        # TABLE SECTION
        self.frameTable = QtWidgets.QFrame(parent=SanPhamTab)
        self.frameTable.setStyleSheet("#frameTable { background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; }")
        self.frameTable.setObjectName("frameTable")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameTable)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tableSanPham = QtWidgets.QTableWidget(parent=self.frameTable)
        self.tableSanPham.setStyleSheet(
            "QTableWidget { background-color: #ffffff; gridline-color: #f1f5f9; border: none; font-size: 13px; color: #334155; }\n"
            "QTableWidget::item { padding: 8px; border-bottom: 1px solid #f1f5f9; }\n"
            "QTableWidget::item:selected { background-color: #eff6ff; color: #1d4ed8; }\n"
            "QHeaderView::section { background-color: #f8fafc; color: #475569; font-weight: 700; font-size: 11px; text-transform: uppercase; padding: 10px 8px; border: none; border-bottom: 2px solid #e2e8f0; }"
        )
        self.tableSanPham.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableSanPham.setShowGrid(True)
        self.tableSanPham.setAlternatingRowColors(False)
        self.tableSanPham.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableSanPham.setObjectName("tableSanPham")
        self.tableSanPham.setColumnCount(7)
        self.tableSanPham.setRowCount(0)
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableSanPham.setHorizontalHeaderItem(i, item)
        self.tableSanPham.horizontalHeader().setStretchLastSection(True)
        self.tableSanPham.verticalHeader().setVisible(False)
        self.tableSanPham.verticalHeader().setDefaultSectionSize(44)
        self.horizontalLayout_2.addWidget(self.tableSanPham)

        self.verticalLayout.addWidget(self.frameTable)

        # PAGINATION FOOTER SECTION
        self.framePagination = QtWidgets.QFrame(parent=SanPhamTab)
        self.framePagination.setStyleSheet("border: none;")
        self.framePagination.setObjectName("framePagination")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.framePagination)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.lblPage = QtWidgets.QLabel(parent=self.framePagination)
        self.lblPage.setStyleSheet("color: #64748b; font-size: 13px;")
        self.lblPage.setObjectName("lblPage")
        self.horizontalLayout_4.addWidget(self.lblPage)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)

        self.btnPrev = QtWidgets.QPushButton(parent=self.framePagination)
        self.btnPrev.setMinimumSize(QtCore.QSize(36, 32))
        self.btnPrev.setStyleSheet(
            "QPushButton { border: 1px solid #cbd5e1; background: white; border-radius: 4px; color: #334155; }\n"
            "QPushButton:hover { background: #f1f5f9; }"
        )
        self.btnPrev.setObjectName("btnPrev")
        self.horizontalLayout_4.addWidget(self.btnPrev)

        self.horizontalLayout_pageNumbers = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pageNumbers.setSpacing(4)
        self.horizontalLayout_pageNumbers.setObjectName("horizontalLayout_pageNumbers")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_pageNumbers)

        self.btnNext = QtWidgets.QPushButton(parent=self.framePagination)
        self.btnNext.setMinimumSize(QtCore.QSize(36, 32))
        self.btnNext.setStyleSheet(
            "QPushButton { border: 1px solid #cbd5e1; background: white; border-radius: 4px; color: #334155; }\n"
            "QPushButton:hover { background: #f1f5f9; }"
        )
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout_4.addWidget(self.btnNext)

        self.verticalLayout.addWidget(self.framePagination)

        self.retranslateUi(SanPhamTab)
        QtCore.QMetaObject.connectSlotsByName(SanPhamTab)

    def retranslateUi(self, SanPhamTab):
        _translate = QtCore.QCoreApplication.translate
        SanPhamTab.setWindowTitle(_translate("SanPhamTab", "Quản lý Sản phẩm"))
        self.lblTitle.setText(_translate("SanPhamTab", "Quản lý Sản phẩm"))
        self.lblSubtitle.setText(_translate("SanPhamTab", "Danh sách chi tiết và kiểm soát tồn kho toàn hệ thống."))
        self.edtSearch.setPlaceholderText(_translate("SanPhamTab", "Nhập từ khóa tìm kiếm..."))
        self.cbDanhMuc.setItemText(0, _translate("SanPhamTab", "Tất cả danh mục"))
        self.btnsua.setText(_translate("SanPhamTab", "Sửa"))
        self.btnXoa.setText(_translate("SanPhamTab", "Xóa"))
        self.btnThemdm.setText(_translate("SanPhamTab", "+ Thêm danh mục"))
        self.btnThem.setText(_translate("SanPhamTab", "+ Thêm sản phẩm"))
        item = self.tableSanPham.horizontalHeaderItem(0)
        item.setText(_translate("SanPhamTab", "MÃ VẠCH"))
        item = self.tableSanPham.horizontalHeaderItem(1)
        item.setText(_translate("SanPhamTab", "TÊN SẢN PHẨM"))
        item = self.tableSanPham.horizontalHeaderItem(2)
        item.setText(_translate("SanPhamTab", "DANH MỤC"))
        item = self.tableSanPham.horizontalHeaderItem(3)
        item.setText(_translate("SanPhamTab", "ĐƠN VỊ"))
        item = self.tableSanPham.horizontalHeaderItem(4)
        item.setText(_translate("SanPhamTab", "GIÁ BÁN LẺ (VNĐ)"))
        item = self.tableSanPham.horizontalHeaderItem(5)
        item.setText(_translate("SanPhamTab", "TỒN KHO"))
        item = self.tableSanPham.horizontalHeaderItem(6)
        item.setText(_translate("SanPhamTab", "TRẠNG THÁI"))
        self.lblPage.setText(_translate("SanPhamTab", "Hiển thị 1 đến 10 của 0 sản phẩm"))
        self.btnPrev.setText(_translate("SanPhamTab", "‹"))
        self.btnNext.setText(_translate("SanPhamTab", "›"))
