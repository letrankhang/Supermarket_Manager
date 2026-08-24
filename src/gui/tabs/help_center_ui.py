# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_center.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1100, 720)
        Form.setStyleSheet(u"\n"
"QWidget#Form {\n"
"    background-color: #f1f5f9;\n"
"    color: #0f172a;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"/* ===== Ti\u00eau \u0111\u1ec1 trang =====\n"
"   D\u00f9ng chung ki\u1ec3u v\u1edbi header c\u1ee7a dashboard.ui: ti\u00eau \u0111\u1ec1 \u0111\u1eadm c\u1ee1 l\u1edbn,\n"
"   ngay d\u01b0\u1edbi l\u00e0 m\u1ed9t d\u00f2ng m\u00f4 t\u1ea3 m\u00e0u x\u00e1m, ch\u1eef th\u01b0\u1eddng, c\u1ee1 nh\u1ecf h\u01a1n.\n"
"   C\u1ee1 ch\u1eef v\u00e0 \u0111\u1ed9 \u0111\u1eadm c\u1ee7a ti\u00eau \u0111\u1ec1 l\u1ea5y t\u1eeb thu\u1ed9c t\u00ednh font c\u1ee7a lblTitle\n"
"   (pointsize 18, bold) gi\u1ed1ng h\u1ec7t QLabel ti\u00eau \u0111\u1ec1 b\u00ean Dashboard. */\n"
"QLabel#lblTitle {\n"
"    color: #0f172a;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"QLabel#lblSubTitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    margin-top: 4px;\n"
"}\n"
"QScrollArea {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"QWi"
                        "dget#scrollAreaWidgetContents {\n"
"    background: transparent;\n"
"}\n"
"/* ===== Th\u1ebb n\u1ed9i dung ===== */\n"
"QFrame[class=\"card\"] {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 14px;\n"
"}\n"
"QLabel[class=\"cardIcon\"] {\n"
"    background-color: #eff6ff;\n"
"    border-radius: 9px;\n"
"}\n"
"QLabel[class=\"cardTitle\"] {\n"
"    color: #0f172a;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[class=\"cardHint\"] {\n"
"    color: #94a3b8;\n"
"    font-size: 11px;\n"
"}\n"
"QFrame[class=\"divider\"] {\n"
"    background-color: #e2e8f0;\n"
"    border: none;\n"
"    min-height: 1px;\n"
"    max-height: 1px;\n"
"}\n"
"/* ===== M\u1ee5c h\u01b0\u1edbng d\u1eabn thu g\u1ecdn ===== */\n"
"QToolButton[class=\"accordion\"] {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    color: #0f172a;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    padding: 9px 10px;\n"
"    text-align: left;\n"
""
                        "}\n"
"QToolButton[class=\"accordion\"]:hover {\n"
"    background-color: #f1f5f9;\n"
"}\n"
"QToolButton[class=\"accordion\"]:checked {\n"
"    background-color: #eff6ff;\n"
"    color: #1d4ed8;\n"
"}\n"
"QLabel[class=\"bullet\"] {\n"
"    color: #93c5fd;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[class=\"accordionLine\"] {\n"
"    color: #475569;\n"
"    font-size: 12px;\n"
"}\n"
"/* ===== Ph\u00edm t\u1eaft ===== */\n"
"QLabel[class=\"keyCap\"] {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    color: #334155;\n"
"    font-family: Consolas, \"Courier New\", monospace;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"    min-width: 40px;\n"
"    max-width: 40px;\n"
"    min-height: 23px;\n"
"    max-height: 23px;\n"
"}\n"
"QLabel[class=\"keyDesc\"] {\n"
"    color: #475569;\n"
"    font-size: 12px;\n"
"}\n"
"/* ===== Th\u00f4ng tin h\u1ec7 th\u1ed1ng ===== */\n"
"QLabel[class=\"infoKey\"] {\n"
"    color: #94a3b8;\n"
"    f"
                        "ont-size: 11px;\n"
"}\n"
"QLabel[class=\"infoValue\"] {\n"
"    color: #0f172a;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"}\n"
"/* ===== H\u1ed7 tr\u1ee3 nhanh ===== */\n"
"QLabel[class=\"supportText\"] {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton[class=\"primaryButton\"] {\n"
"    background-color: #2563eb;\n"
"    border: none;\n"
"    border-radius: 9px;\n"
"    color: #ffffff;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"    min-height: 36px;\n"
"    padding: 0px 14px;\n"
"}\n"
"QPushButton[class=\"primaryButton\"]:hover {\n"
"    background-color: #1d4ed8;\n"
"}\n"
"QPushButton[class=\"primaryButton\"]:pressed {\n"
"    background-color: #1e40af;\n"
"}\n"
"/* ===== \u0110\u1ed9i ng\u0169 ph\u00e1t tri\u1ec3n ===== */\n"
"QFrame[class=\"memberRow\"] {\n"
"    background-color: transparent;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame[class=\"memberRow\"]:hover {\n"
"    background-color: #f8fafc;\n"
"    border: 1px "
                        "solid #e2e8f0;\n"
"}\n"
"QToolButton[class=\"avatar\"] {\n"
"    background-color: #f1f5f9;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 20px;\n"
"}\n"
"QLabel[class=\"memberName\"] {\n"
"    color: #0f172a;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel[class=\"memberRole\"] {\n"
"    background-color: #eff6ff;\n"
"    border-radius: 8px;\n"
"    color: #2563eb;\n"
"    font-size: 10px;\n"
"    font-weight: 700;\n"
"    padding: 2px 8px;\n"
"}\n"
"QLabel[class=\"memberDesc\"] {\n"
"    color: #64748b;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton[class=\"socialButton\"] {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    min-width: 32px;\n"
"    max-width: 32px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"}\n"
"QPushButton[class=\"socialButton\"]:hover {\n"
"    background-color: #eff6ff;\n"
"    border-color: #93c5fd;\n"
"}\n"
"QPushButton[class=\"socialButton\"]:pressed {\n"
"    background-color: #dbeafe;"
                        "\n"
"}\n"
"/* ===== Thanh cu\u1ed9n ===== */\n"
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
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: transparent;\n"
"    height: 10px;\n"
" "
                        "   margin: 0px;\n"
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
        self.mainLayout = QVBoxLayout(Form)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(15, 15, 15, 15)
        self.headerLayout = QVBoxLayout()
        self.headerLayout.setSpacing(0)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTitle = QLabel(Form)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.headerLayout.addWidget(self.lblTitle)

        self.lblSubTitle = QLabel(Form)
        self.lblSubTitle.setObjectName(u"lblSubTitle")

        self.headerLayout.addWidget(self.lblSubTitle)


        self.mainLayout.addLayout(self.headerLayout)

        self.titleSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.mainLayout.addItem(self.titleSpacer)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1328, 1060, 1944))
        self.contentLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.contentLayout.setSpacing(16)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(0, 0, 4, 8)
        self.bodyLayout = QHBoxLayout()
        self.bodyLayout.setSpacing(16)
        self.bodyLayout.setObjectName(u"bodyLayout")
        self.bodyLayout.setContentsMargins(0, 0, 0, 0)
        self.leftColumn = QWidget(self.scrollAreaWidgetContents)
        self.leftColumn.setObjectName(u"leftColumn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftColumn.sizePolicy().hasHeightForWidth())
        self.leftColumn.setSizePolicy(sizePolicy)
        self.leftColumnLayout = QVBoxLayout(self.leftColumn)
        self.leftColumnLayout.setSpacing(16)
        self.leftColumnLayout.setObjectName(u"leftColumnLayout")
        self.leftColumnLayout.setContentsMargins(0, 0, 0, 0)
        self.guideCard = QFrame(self.leftColumn)
        self.guideCard.setObjectName(u"guideCard")
        self.guideCard.setFrameShape(QFrame.Shape.NoFrame)
        self.guideCardLayout = QVBoxLayout(self.guideCard)
        self.guideCardLayout.setSpacing(12)
        self.guideCardLayout.setObjectName(u"guideCardLayout")
        self.guideCardLayout.setContentsMargins(18, 16, 18, 16)
        self.guideCardTitleLayout = QHBoxLayout()
        self.guideCardTitleLayout.setSpacing(10)
        self.guideCardTitleLayout.setObjectName(u"guideCardTitleLayout")
        self.guideCardTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.guideCardIcon = QLabel(self.guideCard)
        self.guideCardIcon.setObjectName(u"guideCardIcon")
        self.guideCardIcon.setMinimumSize(QSize(30, 30))
        self.guideCardIcon.setMaximumSize(QSize(30, 30))
        self.guideCardIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.guideCardTitleLayout.addWidget(self.guideCardIcon)

        self.guideCardTitle = QLabel(self.guideCard)
        self.guideCardTitle.setObjectName(u"guideCardTitle")

        self.guideCardTitleLayout.addWidget(self.guideCardTitle)

        self.guideCardHint = QLabel(self.guideCard)
        self.guideCardHint.setObjectName(u"guideCardHint")

        self.guideCardTitleLayout.addWidget(self.guideCardHint)

        self.guideCardTitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.guideCardTitleLayout.addItem(self.guideCardTitleSpacer)


        self.guideCardLayout.addLayout(self.guideCardTitleLayout)

        self.guideCardDivider = QFrame(self.guideCard)
        self.guideCardDivider.setObjectName(u"guideCardDivider")
        self.guideCardDivider.setFrameShape(QFrame.Shape.NoFrame)

        self.guideCardLayout.addWidget(self.guideCardDivider)

        self.guideCardContent = QVBoxLayout()
        self.guideCardContent.setSpacing(2)
        self.guideCardContent.setObjectName(u"guideCardContent")
        self.guideCardContent.setContentsMargins(0, 0, 0, 0)
        self.btnGuide1GroupLayout = QVBoxLayout()
        self.btnGuide1GroupLayout.setSpacing(0)
        self.btnGuide1GroupLayout.setObjectName(u"btnGuide1GroupLayout")
        self.btnGuide1GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGuide1 = QToolButton(self.guideCard)
        self.btnGuide1.setObjectName(u"btnGuide1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnGuide1.sizePolicy().hasHeightForWidth())
        self.btnGuide1.setSizePolicy(sizePolicy1)
        self.btnGuide1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuide1.setCheckable(True)
        self.btnGuide1.setChecked(False)
        self.btnGuide1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnGuide1GroupLayout.addWidget(self.btnGuide1)

        self.contentGuide1 = QWidget(self.guideCard)
        self.contentGuide1.setObjectName(u"contentGuide1")
        self.contentGuide1Layout = QVBoxLayout(self.contentGuide1)
        self.contentGuide1Layout.setSpacing(7)
        self.contentGuide1Layout.setObjectName(u"contentGuide1Layout")
        self.contentGuide1Layout.setContentsMargins(18, 4, 4, 10)
        self.contentGuide1Line1Layout = QHBoxLayout()
        self.contentGuide1Line1Layout.setSpacing(9)
        self.contentGuide1Line1Layout.setObjectName(u"contentGuide1Line1Layout")
        self.contentGuide1Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide1Line1Bullet = QLabel(self.contentGuide1)
        self.contentGuide1Line1Bullet.setObjectName(u"contentGuide1Line1Bullet")
        self.contentGuide1Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide1Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide1Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide1Line1Layout.addWidget(self.contentGuide1Line1Bullet)

        self.contentGuide1Line1Text = QLabel(self.contentGuide1)
        self.contentGuide1Line1Text.setObjectName(u"contentGuide1Line1Text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentGuide1Line1Text.sizePolicy().hasHeightForWidth())
        self.contentGuide1Line1Text.setSizePolicy(sizePolicy2)
        self.contentGuide1Line1Text.setWordWrap(True)

        self.contentGuide1Line1Layout.addWidget(self.contentGuide1Line1Text)


        self.contentGuide1Layout.addLayout(self.contentGuide1Line1Layout)

        self.contentGuide1Line2Layout = QHBoxLayout()
        self.contentGuide1Line2Layout.setSpacing(9)
        self.contentGuide1Line2Layout.setObjectName(u"contentGuide1Line2Layout")
        self.contentGuide1Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide1Line2Bullet = QLabel(self.contentGuide1)
        self.contentGuide1Line2Bullet.setObjectName(u"contentGuide1Line2Bullet")
        self.contentGuide1Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide1Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide1Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide1Line2Layout.addWidget(self.contentGuide1Line2Bullet)

        self.contentGuide1Line2Text = QLabel(self.contentGuide1)
        self.contentGuide1Line2Text.setObjectName(u"contentGuide1Line2Text")
        sizePolicy2.setHeightForWidth(self.contentGuide1Line2Text.sizePolicy().hasHeightForWidth())
        self.contentGuide1Line2Text.setSizePolicy(sizePolicy2)
        self.contentGuide1Line2Text.setWordWrap(True)

        self.contentGuide1Line2Layout.addWidget(self.contentGuide1Line2Text)


        self.contentGuide1Layout.addLayout(self.contentGuide1Line2Layout)

        self.contentGuide1Line3Layout = QHBoxLayout()
        self.contentGuide1Line3Layout.setSpacing(9)
        self.contentGuide1Line3Layout.setObjectName(u"contentGuide1Line3Layout")
        self.contentGuide1Line3Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide1Line3Bullet = QLabel(self.contentGuide1)
        self.contentGuide1Line3Bullet.setObjectName(u"contentGuide1Line3Bullet")
        self.contentGuide1Line3Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide1Line3Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide1Line3Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide1Line3Layout.addWidget(self.contentGuide1Line3Bullet)

        self.contentGuide1Line3Text = QLabel(self.contentGuide1)
        self.contentGuide1Line3Text.setObjectName(u"contentGuide1Line3Text")
        sizePolicy2.setHeightForWidth(self.contentGuide1Line3Text.sizePolicy().hasHeightForWidth())
        self.contentGuide1Line3Text.setSizePolicy(sizePolicy2)
        self.contentGuide1Line3Text.setWordWrap(True)

        self.contentGuide1Line3Layout.addWidget(self.contentGuide1Line3Text)


        self.contentGuide1Layout.addLayout(self.contentGuide1Line3Layout)

        self.contentGuide1Line4Layout = QHBoxLayout()
        self.contentGuide1Line4Layout.setSpacing(9)
        self.contentGuide1Line4Layout.setObjectName(u"contentGuide1Line4Layout")
        self.contentGuide1Line4Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide1Line4Bullet = QLabel(self.contentGuide1)
        self.contentGuide1Line4Bullet.setObjectName(u"contentGuide1Line4Bullet")
        self.contentGuide1Line4Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide1Line4Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide1Line4Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide1Line4Layout.addWidget(self.contentGuide1Line4Bullet)

        self.contentGuide1Line4Text = QLabel(self.contentGuide1)
        self.contentGuide1Line4Text.setObjectName(u"contentGuide1Line4Text")
        sizePolicy2.setHeightForWidth(self.contentGuide1Line4Text.sizePolicy().hasHeightForWidth())
        self.contentGuide1Line4Text.setSizePolicy(sizePolicy2)
        self.contentGuide1Line4Text.setWordWrap(True)

        self.contentGuide1Line4Layout.addWidget(self.contentGuide1Line4Text)


        self.contentGuide1Layout.addLayout(self.contentGuide1Line4Layout)

        self.contentGuide1Line5Layout = QHBoxLayout()
        self.contentGuide1Line5Layout.setSpacing(9)
        self.contentGuide1Line5Layout.setObjectName(u"contentGuide1Line5Layout")
        self.contentGuide1Line5Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide1Line5Bullet = QLabel(self.contentGuide1)
        self.contentGuide1Line5Bullet.setObjectName(u"contentGuide1Line5Bullet")
        self.contentGuide1Line5Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide1Line5Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide1Line5Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide1Line5Layout.addWidget(self.contentGuide1Line5Bullet)

        self.contentGuide1Line5Text = QLabel(self.contentGuide1)
        self.contentGuide1Line5Text.setObjectName(u"contentGuide1Line5Text")
        sizePolicy2.setHeightForWidth(self.contentGuide1Line5Text.sizePolicy().hasHeightForWidth())
        self.contentGuide1Line5Text.setSizePolicy(sizePolicy2)
        self.contentGuide1Line5Text.setWordWrap(True)

        self.contentGuide1Line5Layout.addWidget(self.contentGuide1Line5Text)


        self.contentGuide1Layout.addLayout(self.contentGuide1Line5Layout)


        self.btnGuide1GroupLayout.addWidget(self.contentGuide1)


        self.guideCardContent.addLayout(self.btnGuide1GroupLayout)

        self.btnGuide2GroupLayout = QVBoxLayout()
        self.btnGuide2GroupLayout.setSpacing(0)
        self.btnGuide2GroupLayout.setObjectName(u"btnGuide2GroupLayout")
        self.btnGuide2GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGuide2 = QToolButton(self.guideCard)
        self.btnGuide2.setObjectName(u"btnGuide2")
        sizePolicy1.setHeightForWidth(self.btnGuide2.sizePolicy().hasHeightForWidth())
        self.btnGuide2.setSizePolicy(sizePolicy1)
        self.btnGuide2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuide2.setCheckable(True)
        self.btnGuide2.setChecked(False)
        self.btnGuide2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnGuide2GroupLayout.addWidget(self.btnGuide2)

        self.contentGuide2 = QWidget(self.guideCard)
        self.contentGuide2.setObjectName(u"contentGuide2")
        self.contentGuide2Layout = QVBoxLayout(self.contentGuide2)
        self.contentGuide2Layout.setSpacing(7)
        self.contentGuide2Layout.setObjectName(u"contentGuide2Layout")
        self.contentGuide2Layout.setContentsMargins(18, 4, 4, 10)
        self.contentGuide2Line1Layout = QHBoxLayout()
        self.contentGuide2Line1Layout.setSpacing(9)
        self.contentGuide2Line1Layout.setObjectName(u"contentGuide2Line1Layout")
        self.contentGuide2Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide2Line1Bullet = QLabel(self.contentGuide2)
        self.contentGuide2Line1Bullet.setObjectName(u"contentGuide2Line1Bullet")
        self.contentGuide2Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide2Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide2Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide2Line1Layout.addWidget(self.contentGuide2Line1Bullet)

        self.contentGuide2Line1Text = QLabel(self.contentGuide2)
        self.contentGuide2Line1Text.setObjectName(u"contentGuide2Line1Text")
        sizePolicy2.setHeightForWidth(self.contentGuide2Line1Text.sizePolicy().hasHeightForWidth())
        self.contentGuide2Line1Text.setSizePolicy(sizePolicy2)
        self.contentGuide2Line1Text.setWordWrap(True)

        self.contentGuide2Line1Layout.addWidget(self.contentGuide2Line1Text)


        self.contentGuide2Layout.addLayout(self.contentGuide2Line1Layout)

        self.contentGuide2Line2Layout = QHBoxLayout()
        self.contentGuide2Line2Layout.setSpacing(9)
        self.contentGuide2Line2Layout.setObjectName(u"contentGuide2Line2Layout")
        self.contentGuide2Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide2Line2Bullet = QLabel(self.contentGuide2)
        self.contentGuide2Line2Bullet.setObjectName(u"contentGuide2Line2Bullet")
        self.contentGuide2Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide2Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide2Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide2Line2Layout.addWidget(self.contentGuide2Line2Bullet)

        self.contentGuide2Line2Text = QLabel(self.contentGuide2)
        self.contentGuide2Line2Text.setObjectName(u"contentGuide2Line2Text")
        sizePolicy2.setHeightForWidth(self.contentGuide2Line2Text.sizePolicy().hasHeightForWidth())
        self.contentGuide2Line2Text.setSizePolicy(sizePolicy2)
        self.contentGuide2Line2Text.setWordWrap(True)

        self.contentGuide2Line2Layout.addWidget(self.contentGuide2Line2Text)


        self.contentGuide2Layout.addLayout(self.contentGuide2Line2Layout)

        self.contentGuide2Line3Layout = QHBoxLayout()
        self.contentGuide2Line3Layout.setSpacing(9)
        self.contentGuide2Line3Layout.setObjectName(u"contentGuide2Line3Layout")
        self.contentGuide2Line3Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide2Line3Bullet = QLabel(self.contentGuide2)
        self.contentGuide2Line3Bullet.setObjectName(u"contentGuide2Line3Bullet")
        self.contentGuide2Line3Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide2Line3Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide2Line3Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide2Line3Layout.addWidget(self.contentGuide2Line3Bullet)

        self.contentGuide2Line3Text = QLabel(self.contentGuide2)
        self.contentGuide2Line3Text.setObjectName(u"contentGuide2Line3Text")
        sizePolicy2.setHeightForWidth(self.contentGuide2Line3Text.sizePolicy().hasHeightForWidth())
        self.contentGuide2Line3Text.setSizePolicy(sizePolicy2)
        self.contentGuide2Line3Text.setWordWrap(True)

        self.contentGuide2Line3Layout.addWidget(self.contentGuide2Line3Text)


        self.contentGuide2Layout.addLayout(self.contentGuide2Line3Layout)

        self.contentGuide2Line4Layout = QHBoxLayout()
        self.contentGuide2Line4Layout.setSpacing(9)
        self.contentGuide2Line4Layout.setObjectName(u"contentGuide2Line4Layout")
        self.contentGuide2Line4Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide2Line4Bullet = QLabel(self.contentGuide2)
        self.contentGuide2Line4Bullet.setObjectName(u"contentGuide2Line4Bullet")
        self.contentGuide2Line4Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide2Line4Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide2Line4Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide2Line4Layout.addWidget(self.contentGuide2Line4Bullet)

        self.contentGuide2Line4Text = QLabel(self.contentGuide2)
        self.contentGuide2Line4Text.setObjectName(u"contentGuide2Line4Text")
        sizePolicy2.setHeightForWidth(self.contentGuide2Line4Text.sizePolicy().hasHeightForWidth())
        self.contentGuide2Line4Text.setSizePolicy(sizePolicy2)
        self.contentGuide2Line4Text.setWordWrap(True)

        self.contentGuide2Line4Layout.addWidget(self.contentGuide2Line4Text)


        self.contentGuide2Layout.addLayout(self.contentGuide2Line4Layout)

        self.contentGuide2Line5Layout = QHBoxLayout()
        self.contentGuide2Line5Layout.setSpacing(9)
        self.contentGuide2Line5Layout.setObjectName(u"contentGuide2Line5Layout")
        self.contentGuide2Line5Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide2Line5Bullet = QLabel(self.contentGuide2)
        self.contentGuide2Line5Bullet.setObjectName(u"contentGuide2Line5Bullet")
        self.contentGuide2Line5Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide2Line5Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide2Line5Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide2Line5Layout.addWidget(self.contentGuide2Line5Bullet)

        self.contentGuide2Line5Text = QLabel(self.contentGuide2)
        self.contentGuide2Line5Text.setObjectName(u"contentGuide2Line5Text")
        sizePolicy2.setHeightForWidth(self.contentGuide2Line5Text.sizePolicy().hasHeightForWidth())
        self.contentGuide2Line5Text.setSizePolicy(sizePolicy2)
        self.contentGuide2Line5Text.setWordWrap(True)

        self.contentGuide2Line5Layout.addWidget(self.contentGuide2Line5Text)


        self.contentGuide2Layout.addLayout(self.contentGuide2Line5Layout)

        self.contentGuide2Line6Layout = QHBoxLayout()
        self.contentGuide2Line6Layout.setSpacing(9)
        self.contentGuide2Line6Layout.setObjectName(u"contentGuide2Line6Layout")
        self.contentGuide2Line6Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide2Line6Bullet = QLabel(self.contentGuide2)
        self.contentGuide2Line6Bullet.setObjectName(u"contentGuide2Line6Bullet")
        self.contentGuide2Line6Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide2Line6Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide2Line6Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide2Line6Layout.addWidget(self.contentGuide2Line6Bullet)

        self.contentGuide2Line6Text = QLabel(self.contentGuide2)
        self.contentGuide2Line6Text.setObjectName(u"contentGuide2Line6Text")
        sizePolicy2.setHeightForWidth(self.contentGuide2Line6Text.sizePolicy().hasHeightForWidth())
        self.contentGuide2Line6Text.setSizePolicy(sizePolicy2)
        self.contentGuide2Line6Text.setWordWrap(True)

        self.contentGuide2Line6Layout.addWidget(self.contentGuide2Line6Text)


        self.contentGuide2Layout.addLayout(self.contentGuide2Line6Layout)


        self.btnGuide2GroupLayout.addWidget(self.contentGuide2)


        self.guideCardContent.addLayout(self.btnGuide2GroupLayout)

        self.btnGuide3GroupLayout = QVBoxLayout()
        self.btnGuide3GroupLayout.setSpacing(0)
        self.btnGuide3GroupLayout.setObjectName(u"btnGuide3GroupLayout")
        self.btnGuide3GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGuide3 = QToolButton(self.guideCard)
        self.btnGuide3.setObjectName(u"btnGuide3")
        sizePolicy1.setHeightForWidth(self.btnGuide3.sizePolicy().hasHeightForWidth())
        self.btnGuide3.setSizePolicy(sizePolicy1)
        self.btnGuide3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuide3.setCheckable(True)
        self.btnGuide3.setChecked(False)
        self.btnGuide3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnGuide3GroupLayout.addWidget(self.btnGuide3)

        self.contentGuide3 = QWidget(self.guideCard)
        self.contentGuide3.setObjectName(u"contentGuide3")
        self.contentGuide3Layout = QVBoxLayout(self.contentGuide3)
        self.contentGuide3Layout.setSpacing(7)
        self.contentGuide3Layout.setObjectName(u"contentGuide3Layout")
        self.contentGuide3Layout.setContentsMargins(18, 4, 4, 10)
        self.contentGuide3Line1Layout = QHBoxLayout()
        self.contentGuide3Line1Layout.setSpacing(9)
        self.contentGuide3Line1Layout.setObjectName(u"contentGuide3Line1Layout")
        self.contentGuide3Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide3Line1Bullet = QLabel(self.contentGuide3)
        self.contentGuide3Line1Bullet.setObjectName(u"contentGuide3Line1Bullet")
        self.contentGuide3Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide3Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide3Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide3Line1Layout.addWidget(self.contentGuide3Line1Bullet)

        self.contentGuide3Line1Text = QLabel(self.contentGuide3)
        self.contentGuide3Line1Text.setObjectName(u"contentGuide3Line1Text")
        sizePolicy2.setHeightForWidth(self.contentGuide3Line1Text.sizePolicy().hasHeightForWidth())
        self.contentGuide3Line1Text.setSizePolicy(sizePolicy2)
        self.contentGuide3Line1Text.setWordWrap(True)

        self.contentGuide3Line1Layout.addWidget(self.contentGuide3Line1Text)


        self.contentGuide3Layout.addLayout(self.contentGuide3Line1Layout)

        self.contentGuide3Line2Layout = QHBoxLayout()
        self.contentGuide3Line2Layout.setSpacing(9)
        self.contentGuide3Line2Layout.setObjectName(u"contentGuide3Line2Layout")
        self.contentGuide3Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide3Line2Bullet = QLabel(self.contentGuide3)
        self.contentGuide3Line2Bullet.setObjectName(u"contentGuide3Line2Bullet")
        self.contentGuide3Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide3Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide3Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide3Line2Layout.addWidget(self.contentGuide3Line2Bullet)

        self.contentGuide3Line2Text = QLabel(self.contentGuide3)
        self.contentGuide3Line2Text.setObjectName(u"contentGuide3Line2Text")
        sizePolicy2.setHeightForWidth(self.contentGuide3Line2Text.sizePolicy().hasHeightForWidth())
        self.contentGuide3Line2Text.setSizePolicy(sizePolicy2)
        self.contentGuide3Line2Text.setWordWrap(True)

        self.contentGuide3Line2Layout.addWidget(self.contentGuide3Line2Text)


        self.contentGuide3Layout.addLayout(self.contentGuide3Line2Layout)

        self.contentGuide3Line3Layout = QHBoxLayout()
        self.contentGuide3Line3Layout.setSpacing(9)
        self.contentGuide3Line3Layout.setObjectName(u"contentGuide3Line3Layout")
        self.contentGuide3Line3Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide3Line3Bullet = QLabel(self.contentGuide3)
        self.contentGuide3Line3Bullet.setObjectName(u"contentGuide3Line3Bullet")
        self.contentGuide3Line3Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide3Line3Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide3Line3Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide3Line3Layout.addWidget(self.contentGuide3Line3Bullet)

        self.contentGuide3Line3Text = QLabel(self.contentGuide3)
        self.contentGuide3Line3Text.setObjectName(u"contentGuide3Line3Text")
        sizePolicy2.setHeightForWidth(self.contentGuide3Line3Text.sizePolicy().hasHeightForWidth())
        self.contentGuide3Line3Text.setSizePolicy(sizePolicy2)
        self.contentGuide3Line3Text.setWordWrap(True)

        self.contentGuide3Line3Layout.addWidget(self.contentGuide3Line3Text)


        self.contentGuide3Layout.addLayout(self.contentGuide3Line3Layout)

        self.contentGuide3Line4Layout = QHBoxLayout()
        self.contentGuide3Line4Layout.setSpacing(9)
        self.contentGuide3Line4Layout.setObjectName(u"contentGuide3Line4Layout")
        self.contentGuide3Line4Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide3Line4Bullet = QLabel(self.contentGuide3)
        self.contentGuide3Line4Bullet.setObjectName(u"contentGuide3Line4Bullet")
        self.contentGuide3Line4Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide3Line4Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide3Line4Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide3Line4Layout.addWidget(self.contentGuide3Line4Bullet)

        self.contentGuide3Line4Text = QLabel(self.contentGuide3)
        self.contentGuide3Line4Text.setObjectName(u"contentGuide3Line4Text")
        sizePolicy2.setHeightForWidth(self.contentGuide3Line4Text.sizePolicy().hasHeightForWidth())
        self.contentGuide3Line4Text.setSizePolicy(sizePolicy2)
        self.contentGuide3Line4Text.setWordWrap(True)

        self.contentGuide3Line4Layout.addWidget(self.contentGuide3Line4Text)


        self.contentGuide3Layout.addLayout(self.contentGuide3Line4Layout)

        self.contentGuide3Line5Layout = QHBoxLayout()
        self.contentGuide3Line5Layout.setSpacing(9)
        self.contentGuide3Line5Layout.setObjectName(u"contentGuide3Line5Layout")
        self.contentGuide3Line5Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide3Line5Bullet = QLabel(self.contentGuide3)
        self.contentGuide3Line5Bullet.setObjectName(u"contentGuide3Line5Bullet")
        self.contentGuide3Line5Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide3Line5Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide3Line5Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide3Line5Layout.addWidget(self.contentGuide3Line5Bullet)

        self.contentGuide3Line5Text = QLabel(self.contentGuide3)
        self.contentGuide3Line5Text.setObjectName(u"contentGuide3Line5Text")
        sizePolicy2.setHeightForWidth(self.contentGuide3Line5Text.sizePolicy().hasHeightForWidth())
        self.contentGuide3Line5Text.setSizePolicy(sizePolicy2)
        self.contentGuide3Line5Text.setWordWrap(True)

        self.contentGuide3Line5Layout.addWidget(self.contentGuide3Line5Text)


        self.contentGuide3Layout.addLayout(self.contentGuide3Line5Layout)

        self.contentGuide3Line6Layout = QHBoxLayout()
        self.contentGuide3Line6Layout.setSpacing(9)
        self.contentGuide3Line6Layout.setObjectName(u"contentGuide3Line6Layout")
        self.contentGuide3Line6Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide3Line6Bullet = QLabel(self.contentGuide3)
        self.contentGuide3Line6Bullet.setObjectName(u"contentGuide3Line6Bullet")
        self.contentGuide3Line6Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide3Line6Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide3Line6Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide3Line6Layout.addWidget(self.contentGuide3Line6Bullet)

        self.contentGuide3Line6Text = QLabel(self.contentGuide3)
        self.contentGuide3Line6Text.setObjectName(u"contentGuide3Line6Text")
        sizePolicy2.setHeightForWidth(self.contentGuide3Line6Text.sizePolicy().hasHeightForWidth())
        self.contentGuide3Line6Text.setSizePolicy(sizePolicy2)
        self.contentGuide3Line6Text.setWordWrap(True)

        self.contentGuide3Line6Layout.addWidget(self.contentGuide3Line6Text)


        self.contentGuide3Layout.addLayout(self.contentGuide3Line6Layout)


        self.btnGuide3GroupLayout.addWidget(self.contentGuide3)


        self.guideCardContent.addLayout(self.btnGuide3GroupLayout)

        self.btnGuide4GroupLayout = QVBoxLayout()
        self.btnGuide4GroupLayout.setSpacing(0)
        self.btnGuide4GroupLayout.setObjectName(u"btnGuide4GroupLayout")
        self.btnGuide4GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGuide4 = QToolButton(self.guideCard)
        self.btnGuide4.setObjectName(u"btnGuide4")
        sizePolicy1.setHeightForWidth(self.btnGuide4.sizePolicy().hasHeightForWidth())
        self.btnGuide4.setSizePolicy(sizePolicy1)
        self.btnGuide4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuide4.setCheckable(True)
        self.btnGuide4.setChecked(False)
        self.btnGuide4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnGuide4GroupLayout.addWidget(self.btnGuide4)

        self.contentGuide4 = QWidget(self.guideCard)
        self.contentGuide4.setObjectName(u"contentGuide4")
        self.contentGuide4Layout = QVBoxLayout(self.contentGuide4)
        self.contentGuide4Layout.setSpacing(7)
        self.contentGuide4Layout.setObjectName(u"contentGuide4Layout")
        self.contentGuide4Layout.setContentsMargins(18, 4, 4, 10)
        self.contentGuide4Line1Layout = QHBoxLayout()
        self.contentGuide4Line1Layout.setSpacing(9)
        self.contentGuide4Line1Layout.setObjectName(u"contentGuide4Line1Layout")
        self.contentGuide4Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide4Line1Bullet = QLabel(self.contentGuide4)
        self.contentGuide4Line1Bullet.setObjectName(u"contentGuide4Line1Bullet")
        self.contentGuide4Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide4Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide4Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide4Line1Layout.addWidget(self.contentGuide4Line1Bullet)

        self.contentGuide4Line1Text = QLabel(self.contentGuide4)
        self.contentGuide4Line1Text.setObjectName(u"contentGuide4Line1Text")
        sizePolicy2.setHeightForWidth(self.contentGuide4Line1Text.sizePolicy().hasHeightForWidth())
        self.contentGuide4Line1Text.setSizePolicy(sizePolicy2)
        self.contentGuide4Line1Text.setWordWrap(True)

        self.contentGuide4Line1Layout.addWidget(self.contentGuide4Line1Text)


        self.contentGuide4Layout.addLayout(self.contentGuide4Line1Layout)

        self.contentGuide4Line2Layout = QHBoxLayout()
        self.contentGuide4Line2Layout.setSpacing(9)
        self.contentGuide4Line2Layout.setObjectName(u"contentGuide4Line2Layout")
        self.contentGuide4Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide4Line2Bullet = QLabel(self.contentGuide4)
        self.contentGuide4Line2Bullet.setObjectName(u"contentGuide4Line2Bullet")
        self.contentGuide4Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide4Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide4Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide4Line2Layout.addWidget(self.contentGuide4Line2Bullet)

        self.contentGuide4Line2Text = QLabel(self.contentGuide4)
        self.contentGuide4Line2Text.setObjectName(u"contentGuide4Line2Text")
        sizePolicy2.setHeightForWidth(self.contentGuide4Line2Text.sizePolicy().hasHeightForWidth())
        self.contentGuide4Line2Text.setSizePolicy(sizePolicy2)
        self.contentGuide4Line2Text.setWordWrap(True)

        self.contentGuide4Line2Layout.addWidget(self.contentGuide4Line2Text)


        self.contentGuide4Layout.addLayout(self.contentGuide4Line2Layout)

        self.contentGuide4Line3Layout = QHBoxLayout()
        self.contentGuide4Line3Layout.setSpacing(9)
        self.contentGuide4Line3Layout.setObjectName(u"contentGuide4Line3Layout")
        self.contentGuide4Line3Layout.setContentsMargins(0, 0, 0, 0)
        self.contentGuide4Line3Bullet = QLabel(self.contentGuide4)
        self.contentGuide4Line3Bullet.setObjectName(u"contentGuide4Line3Bullet")
        self.contentGuide4Line3Bullet.setMinimumSize(QSize(8, 0))
        self.contentGuide4Line3Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentGuide4Line3Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentGuide4Line3Layout.addWidget(self.contentGuide4Line3Bullet)

        self.contentGuide4Line3Text = QLabel(self.contentGuide4)
        self.contentGuide4Line3Text.setObjectName(u"contentGuide4Line3Text")
        sizePolicy2.setHeightForWidth(self.contentGuide4Line3Text.sizePolicy().hasHeightForWidth())
        self.contentGuide4Line3Text.setSizePolicy(sizePolicy2)
        self.contentGuide4Line3Text.setWordWrap(True)

        self.contentGuide4Line3Layout.addWidget(self.contentGuide4Line3Text)


        self.contentGuide4Layout.addLayout(self.contentGuide4Line3Layout)


        self.btnGuide4GroupLayout.addWidget(self.contentGuide4)


        self.guideCardContent.addLayout(self.btnGuide4GroupLayout)


        self.guideCardLayout.addLayout(self.guideCardContent)


        self.leftColumnLayout.addWidget(self.guideCard)

        self.issuesCard = QFrame(self.leftColumn)
        self.issuesCard.setObjectName(u"issuesCard")
        self.issuesCard.setFrameShape(QFrame.Shape.NoFrame)
        self.issuesCardLayout = QVBoxLayout(self.issuesCard)
        self.issuesCardLayout.setSpacing(12)
        self.issuesCardLayout.setObjectName(u"issuesCardLayout")
        self.issuesCardLayout.setContentsMargins(18, 16, 18, 16)
        self.issuesCardTitleLayout = QHBoxLayout()
        self.issuesCardTitleLayout.setSpacing(10)
        self.issuesCardTitleLayout.setObjectName(u"issuesCardTitleLayout")
        self.issuesCardTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.issuesCardIcon = QLabel(self.issuesCard)
        self.issuesCardIcon.setObjectName(u"issuesCardIcon")
        self.issuesCardIcon.setMinimumSize(QSize(30, 30))
        self.issuesCardIcon.setMaximumSize(QSize(30, 30))
        self.issuesCardIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.issuesCardTitleLayout.addWidget(self.issuesCardIcon)

        self.issuesCardTitle = QLabel(self.issuesCard)
        self.issuesCardTitle.setObjectName(u"issuesCardTitle")

        self.issuesCardTitleLayout.addWidget(self.issuesCardTitle)

        self.issuesCardTitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.issuesCardTitleLayout.addItem(self.issuesCardTitleSpacer)


        self.issuesCardLayout.addLayout(self.issuesCardTitleLayout)

        self.issuesCardDivider = QFrame(self.issuesCard)
        self.issuesCardDivider.setObjectName(u"issuesCardDivider")
        self.issuesCardDivider.setFrameShape(QFrame.Shape.NoFrame)

        self.issuesCardLayout.addWidget(self.issuesCardDivider)

        self.issuesCardContent = QVBoxLayout()
        self.issuesCardContent.setSpacing(2)
        self.issuesCardContent.setObjectName(u"issuesCardContent")
        self.issuesCardContent.setContentsMargins(0, 0, 0, 0)
        self.btnIssue1GroupLayout = QVBoxLayout()
        self.btnIssue1GroupLayout.setSpacing(0)
        self.btnIssue1GroupLayout.setObjectName(u"btnIssue1GroupLayout")
        self.btnIssue1GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnIssue1 = QToolButton(self.issuesCard)
        self.btnIssue1.setObjectName(u"btnIssue1")
        sizePolicy1.setHeightForWidth(self.btnIssue1.sizePolicy().hasHeightForWidth())
        self.btnIssue1.setSizePolicy(sizePolicy1)
        self.btnIssue1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnIssue1.setCheckable(True)
        self.btnIssue1.setChecked(False)
        self.btnIssue1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnIssue1GroupLayout.addWidget(self.btnIssue1)

        self.contentIssue1 = QWidget(self.issuesCard)
        self.contentIssue1.setObjectName(u"contentIssue1")
        self.contentIssue1Layout = QVBoxLayout(self.contentIssue1)
        self.contentIssue1Layout.setSpacing(7)
        self.contentIssue1Layout.setObjectName(u"contentIssue1Layout")
        self.contentIssue1Layout.setContentsMargins(18, 4, 4, 10)
        self.contentIssue1Line1Layout = QHBoxLayout()
        self.contentIssue1Line1Layout.setSpacing(9)
        self.contentIssue1Line1Layout.setObjectName(u"contentIssue1Line1Layout")
        self.contentIssue1Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue1Line1Bullet = QLabel(self.contentIssue1)
        self.contentIssue1Line1Bullet.setObjectName(u"contentIssue1Line1Bullet")
        self.contentIssue1Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue1Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue1Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue1Line1Layout.addWidget(self.contentIssue1Line1Bullet)

        self.contentIssue1Line1Text = QLabel(self.contentIssue1)
        self.contentIssue1Line1Text.setObjectName(u"contentIssue1Line1Text")
        sizePolicy2.setHeightForWidth(self.contentIssue1Line1Text.sizePolicy().hasHeightForWidth())
        self.contentIssue1Line1Text.setSizePolicy(sizePolicy2)
        self.contentIssue1Line1Text.setWordWrap(True)

        self.contentIssue1Line1Layout.addWidget(self.contentIssue1Line1Text)


        self.contentIssue1Layout.addLayout(self.contentIssue1Line1Layout)

        self.contentIssue1Line2Layout = QHBoxLayout()
        self.contentIssue1Line2Layout.setSpacing(9)
        self.contentIssue1Line2Layout.setObjectName(u"contentIssue1Line2Layout")
        self.contentIssue1Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue1Line2Bullet = QLabel(self.contentIssue1)
        self.contentIssue1Line2Bullet.setObjectName(u"contentIssue1Line2Bullet")
        self.contentIssue1Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue1Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue1Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue1Line2Layout.addWidget(self.contentIssue1Line2Bullet)

        self.contentIssue1Line2Text = QLabel(self.contentIssue1)
        self.contentIssue1Line2Text.setObjectName(u"contentIssue1Line2Text")
        sizePolicy2.setHeightForWidth(self.contentIssue1Line2Text.sizePolicy().hasHeightForWidth())
        self.contentIssue1Line2Text.setSizePolicy(sizePolicy2)
        self.contentIssue1Line2Text.setWordWrap(True)

        self.contentIssue1Line2Layout.addWidget(self.contentIssue1Line2Text)


        self.contentIssue1Layout.addLayout(self.contentIssue1Line2Layout)

        self.contentIssue1Line3Layout = QHBoxLayout()
        self.contentIssue1Line3Layout.setSpacing(9)
        self.contentIssue1Line3Layout.setObjectName(u"contentIssue1Line3Layout")
        self.contentIssue1Line3Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue1Line3Bullet = QLabel(self.contentIssue1)
        self.contentIssue1Line3Bullet.setObjectName(u"contentIssue1Line3Bullet")
        self.contentIssue1Line3Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue1Line3Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue1Line3Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue1Line3Layout.addWidget(self.contentIssue1Line3Bullet)

        self.contentIssue1Line3Text = QLabel(self.contentIssue1)
        self.contentIssue1Line3Text.setObjectName(u"contentIssue1Line3Text")
        sizePolicy2.setHeightForWidth(self.contentIssue1Line3Text.sizePolicy().hasHeightForWidth())
        self.contentIssue1Line3Text.setSizePolicy(sizePolicy2)
        self.contentIssue1Line3Text.setWordWrap(True)

        self.contentIssue1Line3Layout.addWidget(self.contentIssue1Line3Text)


        self.contentIssue1Layout.addLayout(self.contentIssue1Line3Layout)


        self.btnIssue1GroupLayout.addWidget(self.contentIssue1)


        self.issuesCardContent.addLayout(self.btnIssue1GroupLayout)

        self.btnIssue2GroupLayout = QVBoxLayout()
        self.btnIssue2GroupLayout.setSpacing(0)
        self.btnIssue2GroupLayout.setObjectName(u"btnIssue2GroupLayout")
        self.btnIssue2GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnIssue2 = QToolButton(self.issuesCard)
        self.btnIssue2.setObjectName(u"btnIssue2")
        sizePolicy1.setHeightForWidth(self.btnIssue2.sizePolicy().hasHeightForWidth())
        self.btnIssue2.setSizePolicy(sizePolicy1)
        self.btnIssue2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnIssue2.setCheckable(True)
        self.btnIssue2.setChecked(False)
        self.btnIssue2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnIssue2GroupLayout.addWidget(self.btnIssue2)

        self.contentIssue2 = QWidget(self.issuesCard)
        self.contentIssue2.setObjectName(u"contentIssue2")
        self.contentIssue2Layout = QVBoxLayout(self.contentIssue2)
        self.contentIssue2Layout.setSpacing(7)
        self.contentIssue2Layout.setObjectName(u"contentIssue2Layout")
        self.contentIssue2Layout.setContentsMargins(18, 4, 4, 10)
        self.contentIssue2Line1Layout = QHBoxLayout()
        self.contentIssue2Line1Layout.setSpacing(9)
        self.contentIssue2Line1Layout.setObjectName(u"contentIssue2Line1Layout")
        self.contentIssue2Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue2Line1Bullet = QLabel(self.contentIssue2)
        self.contentIssue2Line1Bullet.setObjectName(u"contentIssue2Line1Bullet")
        self.contentIssue2Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue2Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue2Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue2Line1Layout.addWidget(self.contentIssue2Line1Bullet)

        self.contentIssue2Line1Text = QLabel(self.contentIssue2)
        self.contentIssue2Line1Text.setObjectName(u"contentIssue2Line1Text")
        sizePolicy2.setHeightForWidth(self.contentIssue2Line1Text.sizePolicy().hasHeightForWidth())
        self.contentIssue2Line1Text.setSizePolicy(sizePolicy2)
        self.contentIssue2Line1Text.setWordWrap(True)

        self.contentIssue2Line1Layout.addWidget(self.contentIssue2Line1Text)


        self.contentIssue2Layout.addLayout(self.contentIssue2Line1Layout)

        self.contentIssue2Line2Layout = QHBoxLayout()
        self.contentIssue2Line2Layout.setSpacing(9)
        self.contentIssue2Line2Layout.setObjectName(u"contentIssue2Line2Layout")
        self.contentIssue2Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue2Line2Bullet = QLabel(self.contentIssue2)
        self.contentIssue2Line2Bullet.setObjectName(u"contentIssue2Line2Bullet")
        self.contentIssue2Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue2Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue2Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue2Line2Layout.addWidget(self.contentIssue2Line2Bullet)

        self.contentIssue2Line2Text = QLabel(self.contentIssue2)
        self.contentIssue2Line2Text.setObjectName(u"contentIssue2Line2Text")
        sizePolicy2.setHeightForWidth(self.contentIssue2Line2Text.sizePolicy().hasHeightForWidth())
        self.contentIssue2Line2Text.setSizePolicy(sizePolicy2)
        self.contentIssue2Line2Text.setWordWrap(True)

        self.contentIssue2Line2Layout.addWidget(self.contentIssue2Line2Text)


        self.contentIssue2Layout.addLayout(self.contentIssue2Line2Layout)

        self.contentIssue2Line3Layout = QHBoxLayout()
        self.contentIssue2Line3Layout.setSpacing(9)
        self.contentIssue2Line3Layout.setObjectName(u"contentIssue2Line3Layout")
        self.contentIssue2Line3Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue2Line3Bullet = QLabel(self.contentIssue2)
        self.contentIssue2Line3Bullet.setObjectName(u"contentIssue2Line3Bullet")
        self.contentIssue2Line3Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue2Line3Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue2Line3Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue2Line3Layout.addWidget(self.contentIssue2Line3Bullet)

        self.contentIssue2Line3Text = QLabel(self.contentIssue2)
        self.contentIssue2Line3Text.setObjectName(u"contentIssue2Line3Text")
        sizePolicy2.setHeightForWidth(self.contentIssue2Line3Text.sizePolicy().hasHeightForWidth())
        self.contentIssue2Line3Text.setSizePolicy(sizePolicy2)
        self.contentIssue2Line3Text.setWordWrap(True)

        self.contentIssue2Line3Layout.addWidget(self.contentIssue2Line3Text)


        self.contentIssue2Layout.addLayout(self.contentIssue2Line3Layout)


        self.btnIssue2GroupLayout.addWidget(self.contentIssue2)


        self.issuesCardContent.addLayout(self.btnIssue2GroupLayout)

        self.btnIssue3GroupLayout = QVBoxLayout()
        self.btnIssue3GroupLayout.setSpacing(0)
        self.btnIssue3GroupLayout.setObjectName(u"btnIssue3GroupLayout")
        self.btnIssue3GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnIssue3 = QToolButton(self.issuesCard)
        self.btnIssue3.setObjectName(u"btnIssue3")
        sizePolicy1.setHeightForWidth(self.btnIssue3.sizePolicy().hasHeightForWidth())
        self.btnIssue3.setSizePolicy(sizePolicy1)
        self.btnIssue3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnIssue3.setCheckable(True)
        self.btnIssue3.setChecked(False)
        self.btnIssue3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnIssue3GroupLayout.addWidget(self.btnIssue3)

        self.contentIssue3 = QWidget(self.issuesCard)
        self.contentIssue3.setObjectName(u"contentIssue3")
        self.contentIssue3Layout = QVBoxLayout(self.contentIssue3)
        self.contentIssue3Layout.setSpacing(7)
        self.contentIssue3Layout.setObjectName(u"contentIssue3Layout")
        self.contentIssue3Layout.setContentsMargins(18, 4, 4, 10)
        self.contentIssue3Line1Layout = QHBoxLayout()
        self.contentIssue3Line1Layout.setSpacing(9)
        self.contentIssue3Line1Layout.setObjectName(u"contentIssue3Line1Layout")
        self.contentIssue3Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue3Line1Bullet = QLabel(self.contentIssue3)
        self.contentIssue3Line1Bullet.setObjectName(u"contentIssue3Line1Bullet")
        self.contentIssue3Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue3Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue3Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue3Line1Layout.addWidget(self.contentIssue3Line1Bullet)

        self.contentIssue3Line1Text = QLabel(self.contentIssue3)
        self.contentIssue3Line1Text.setObjectName(u"contentIssue3Line1Text")
        sizePolicy2.setHeightForWidth(self.contentIssue3Line1Text.sizePolicy().hasHeightForWidth())
        self.contentIssue3Line1Text.setSizePolicy(sizePolicy2)
        self.contentIssue3Line1Text.setWordWrap(True)

        self.contentIssue3Line1Layout.addWidget(self.contentIssue3Line1Text)


        self.contentIssue3Layout.addLayout(self.contentIssue3Line1Layout)

        self.contentIssue3Line2Layout = QHBoxLayout()
        self.contentIssue3Line2Layout.setSpacing(9)
        self.contentIssue3Line2Layout.setObjectName(u"contentIssue3Line2Layout")
        self.contentIssue3Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue3Line2Bullet = QLabel(self.contentIssue3)
        self.contentIssue3Line2Bullet.setObjectName(u"contentIssue3Line2Bullet")
        self.contentIssue3Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue3Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue3Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue3Line2Layout.addWidget(self.contentIssue3Line2Bullet)

        self.contentIssue3Line2Text = QLabel(self.contentIssue3)
        self.contentIssue3Line2Text.setObjectName(u"contentIssue3Line2Text")
        sizePolicy2.setHeightForWidth(self.contentIssue3Line2Text.sizePolicy().hasHeightForWidth())
        self.contentIssue3Line2Text.setSizePolicy(sizePolicy2)
        self.contentIssue3Line2Text.setWordWrap(True)

        self.contentIssue3Line2Layout.addWidget(self.contentIssue3Line2Text)


        self.contentIssue3Layout.addLayout(self.contentIssue3Line2Layout)


        self.btnIssue3GroupLayout.addWidget(self.contentIssue3)


        self.issuesCardContent.addLayout(self.btnIssue3GroupLayout)

        self.btnIssue4GroupLayout = QVBoxLayout()
        self.btnIssue4GroupLayout.setSpacing(0)
        self.btnIssue4GroupLayout.setObjectName(u"btnIssue4GroupLayout")
        self.btnIssue4GroupLayout.setContentsMargins(0, 0, 0, 0)
        self.btnIssue4 = QToolButton(self.issuesCard)
        self.btnIssue4.setObjectName(u"btnIssue4")
        sizePolicy1.setHeightForWidth(self.btnIssue4.sizePolicy().hasHeightForWidth())
        self.btnIssue4.setSizePolicy(sizePolicy1)
        self.btnIssue4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnIssue4.setCheckable(True)
        self.btnIssue4.setChecked(False)
        self.btnIssue4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.btnIssue4GroupLayout.addWidget(self.btnIssue4)

        self.contentIssue4 = QWidget(self.issuesCard)
        self.contentIssue4.setObjectName(u"contentIssue4")
        self.contentIssue4Layout = QVBoxLayout(self.contentIssue4)
        self.contentIssue4Layout.setSpacing(7)
        self.contentIssue4Layout.setObjectName(u"contentIssue4Layout")
        self.contentIssue4Layout.setContentsMargins(18, 4, 4, 10)
        self.contentIssue4Line1Layout = QHBoxLayout()
        self.contentIssue4Line1Layout.setSpacing(9)
        self.contentIssue4Line1Layout.setObjectName(u"contentIssue4Line1Layout")
        self.contentIssue4Line1Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue4Line1Bullet = QLabel(self.contentIssue4)
        self.contentIssue4Line1Bullet.setObjectName(u"contentIssue4Line1Bullet")
        self.contentIssue4Line1Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue4Line1Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue4Line1Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue4Line1Layout.addWidget(self.contentIssue4Line1Bullet)

        self.contentIssue4Line1Text = QLabel(self.contentIssue4)
        self.contentIssue4Line1Text.setObjectName(u"contentIssue4Line1Text")
        sizePolicy2.setHeightForWidth(self.contentIssue4Line1Text.sizePolicy().hasHeightForWidth())
        self.contentIssue4Line1Text.setSizePolicy(sizePolicy2)
        self.contentIssue4Line1Text.setWordWrap(True)

        self.contentIssue4Line1Layout.addWidget(self.contentIssue4Line1Text)


        self.contentIssue4Layout.addLayout(self.contentIssue4Line1Layout)

        self.contentIssue4Line2Layout = QHBoxLayout()
        self.contentIssue4Line2Layout.setSpacing(9)
        self.contentIssue4Line2Layout.setObjectName(u"contentIssue4Line2Layout")
        self.contentIssue4Line2Layout.setContentsMargins(0, 0, 0, 0)
        self.contentIssue4Line2Bullet = QLabel(self.contentIssue4)
        self.contentIssue4Line2Bullet.setObjectName(u"contentIssue4Line2Bullet")
        self.contentIssue4Line2Bullet.setMinimumSize(QSize(8, 0))
        self.contentIssue4Line2Bullet.setMaximumSize(QSize(8, 16777215))
        self.contentIssue4Line2Bullet.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.contentIssue4Line2Layout.addWidget(self.contentIssue4Line2Bullet)

        self.contentIssue4Line2Text = QLabel(self.contentIssue4)
        self.contentIssue4Line2Text.setObjectName(u"contentIssue4Line2Text")
        sizePolicy2.setHeightForWidth(self.contentIssue4Line2Text.sizePolicy().hasHeightForWidth())
        self.contentIssue4Line2Text.setSizePolicy(sizePolicy2)
        self.contentIssue4Line2Text.setWordWrap(True)

        self.contentIssue4Line2Layout.addWidget(self.contentIssue4Line2Text)


        self.contentIssue4Layout.addLayout(self.contentIssue4Line2Layout)


        self.btnIssue4GroupLayout.addWidget(self.contentIssue4)


        self.issuesCardContent.addLayout(self.btnIssue4GroupLayout)


        self.issuesCardLayout.addLayout(self.issuesCardContent)


        self.leftColumnLayout.addWidget(self.issuesCard)

        self.leftColumnSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftColumnLayout.addItem(self.leftColumnSpacer)


        self.bodyLayout.addWidget(self.leftColumn)

        self.rightColumn = QWidget(self.scrollAreaWidgetContents)
        self.rightColumn.setObjectName(u"rightColumn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rightColumn.sizePolicy().hasHeightForWidth())
        self.rightColumn.setSizePolicy(sizePolicy3)
        self.rightColumn.setMinimumSize(QSize(300, 0))
        self.rightColumnLayout = QVBoxLayout(self.rightColumn)
        self.rightColumnLayout.setSpacing(16)
        self.rightColumnLayout.setObjectName(u"rightColumnLayout")
        self.rightColumnLayout.setContentsMargins(0, 0, 0, 0)
        self.shortcutsCard = QFrame(self.rightColumn)
        self.shortcutsCard.setObjectName(u"shortcutsCard")
        self.shortcutsCard.setFrameShape(QFrame.Shape.NoFrame)
        self.shortcutsCardLayout = QVBoxLayout(self.shortcutsCard)
        self.shortcutsCardLayout.setSpacing(12)
        self.shortcutsCardLayout.setObjectName(u"shortcutsCardLayout")
        self.shortcutsCardLayout.setContentsMargins(18, 16, 18, 16)
        self.shortcutsCardTitleLayout = QHBoxLayout()
        self.shortcutsCardTitleLayout.setSpacing(10)
        self.shortcutsCardTitleLayout.setObjectName(u"shortcutsCardTitleLayout")
        self.shortcutsCardTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.shortcutsCardIcon = QLabel(self.shortcutsCard)
        self.shortcutsCardIcon.setObjectName(u"shortcutsCardIcon")
        self.shortcutsCardIcon.setMinimumSize(QSize(30, 30))
        self.shortcutsCardIcon.setMaximumSize(QSize(30, 30))
        self.shortcutsCardIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.shortcutsCardTitleLayout.addWidget(self.shortcutsCardIcon)

        self.shortcutsCardTitle = QLabel(self.shortcutsCard)
        self.shortcutsCardTitle.setObjectName(u"shortcutsCardTitle")

        self.shortcutsCardTitleLayout.addWidget(self.shortcutsCardTitle)

        self.shortcutsCardHint = QLabel(self.shortcutsCard)
        self.shortcutsCardHint.setObjectName(u"shortcutsCardHint")

        self.shortcutsCardTitleLayout.addWidget(self.shortcutsCardHint)

        self.shortcutsCardTitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.shortcutsCardTitleLayout.addItem(self.shortcutsCardTitleSpacer)


        self.shortcutsCardLayout.addLayout(self.shortcutsCardTitleLayout)

        self.shortcutsCardDivider = QFrame(self.shortcutsCard)
        self.shortcutsCardDivider.setObjectName(u"shortcutsCardDivider")
        self.shortcutsCardDivider.setFrameShape(QFrame.Shape.NoFrame)

        self.shortcutsCardLayout.addWidget(self.shortcutsCardDivider)

        self.shortcutsCardContent = QVBoxLayout()
        self.shortcutsCardContent.setSpacing(9)
        self.shortcutsCardContent.setObjectName(u"shortcutsCardContent")
        self.shortcutsCardContent.setContentsMargins(0, 0, 0, 0)
        self.shortcutRow1Layout = QHBoxLayout()
        self.shortcutRow1Layout.setSpacing(10)
        self.shortcutRow1Layout.setObjectName(u"shortcutRow1Layout")
        self.shortcutRow1Layout.setContentsMargins(0, 0, 0, 0)
        self.keyShortcut1 = QLabel(self.shortcutsCard)
        self.keyShortcut1.setObjectName(u"keyShortcut1")
        self.keyShortcut1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.shortcutRow1Layout.addWidget(self.keyShortcut1)

        self.descShortcut1 = QLabel(self.shortcutsCard)
        self.descShortcut1.setObjectName(u"descShortcut1")
        self.descShortcut1.setWordWrap(True)

        self.shortcutRow1Layout.addWidget(self.descShortcut1)

        self.shortcutRow1Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.shortcutRow1Layout.addItem(self.shortcutRow1Spacer)


        self.shortcutsCardContent.addLayout(self.shortcutRow1Layout)

        self.shortcutRow2Layout = QHBoxLayout()
        self.shortcutRow2Layout.setSpacing(10)
        self.shortcutRow2Layout.setObjectName(u"shortcutRow2Layout")
        self.shortcutRow2Layout.setContentsMargins(0, 0, 0, 0)
        self.keyShortcut2 = QLabel(self.shortcutsCard)
        self.keyShortcut2.setObjectName(u"keyShortcut2")
        self.keyShortcut2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.shortcutRow2Layout.addWidget(self.keyShortcut2)

        self.descShortcut2 = QLabel(self.shortcutsCard)
        self.descShortcut2.setObjectName(u"descShortcut2")
        self.descShortcut2.setWordWrap(True)

        self.shortcutRow2Layout.addWidget(self.descShortcut2)

        self.shortcutRow2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.shortcutRow2Layout.addItem(self.shortcutRow2Spacer)


        self.shortcutsCardContent.addLayout(self.shortcutRow2Layout)

        self.shortcutRow3Layout = QHBoxLayout()
        self.shortcutRow3Layout.setSpacing(10)
        self.shortcutRow3Layout.setObjectName(u"shortcutRow3Layout")
        self.shortcutRow3Layout.setContentsMargins(0, 0, 0, 0)
        self.keyShortcut3 = QLabel(self.shortcutsCard)
        self.keyShortcut3.setObjectName(u"keyShortcut3")
        self.keyShortcut3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.shortcutRow3Layout.addWidget(self.keyShortcut3)

        self.descShortcut3 = QLabel(self.shortcutsCard)
        self.descShortcut3.setObjectName(u"descShortcut3")
        self.descShortcut3.setWordWrap(True)

        self.shortcutRow3Layout.addWidget(self.descShortcut3)

        self.shortcutRow3Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.shortcutRow3Layout.addItem(self.shortcutRow3Spacer)


        self.shortcutsCardContent.addLayout(self.shortcutRow3Layout)

        self.shortcutRow4Layout = QHBoxLayout()
        self.shortcutRow4Layout.setSpacing(10)
        self.shortcutRow4Layout.setObjectName(u"shortcutRow4Layout")
        self.shortcutRow4Layout.setContentsMargins(0, 0, 0, 0)
        self.keyShortcut4 = QLabel(self.shortcutsCard)
        self.keyShortcut4.setObjectName(u"keyShortcut4")
        self.keyShortcut4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.shortcutRow4Layout.addWidget(self.keyShortcut4)

        self.descShortcut4 = QLabel(self.shortcutsCard)
        self.descShortcut4.setObjectName(u"descShortcut4")
        self.descShortcut4.setWordWrap(True)

        self.shortcutRow4Layout.addWidget(self.descShortcut4)

        self.shortcutRow4Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.shortcutRow4Layout.addItem(self.shortcutRow4Spacer)


        self.shortcutsCardContent.addLayout(self.shortcutRow4Layout)


        self.shortcutsCardLayout.addLayout(self.shortcutsCardContent)


        self.rightColumnLayout.addWidget(self.shortcutsCard)

        self.systemCard = QFrame(self.rightColumn)
        self.systemCard.setObjectName(u"systemCard")
        self.systemCard.setFrameShape(QFrame.Shape.NoFrame)
        self.systemCardLayout = QVBoxLayout(self.systemCard)
        self.systemCardLayout.setSpacing(12)
        self.systemCardLayout.setObjectName(u"systemCardLayout")
        self.systemCardLayout.setContentsMargins(18, 16, 18, 16)
        self.systemCardTitleLayout = QHBoxLayout()
        self.systemCardTitleLayout.setSpacing(10)
        self.systemCardTitleLayout.setObjectName(u"systemCardTitleLayout")
        self.systemCardTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.systemCardIcon = QLabel(self.systemCard)
        self.systemCardIcon.setObjectName(u"systemCardIcon")
        self.systemCardIcon.setMinimumSize(QSize(30, 30))
        self.systemCardIcon.setMaximumSize(QSize(30, 30))
        self.systemCardIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.systemCardTitleLayout.addWidget(self.systemCardIcon)

        self.systemCardTitle = QLabel(self.systemCard)
        self.systemCardTitle.setObjectName(u"systemCardTitle")

        self.systemCardTitleLayout.addWidget(self.systemCardTitle)

        self.systemCardTitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.systemCardTitleLayout.addItem(self.systemCardTitleSpacer)


        self.systemCardLayout.addLayout(self.systemCardTitleLayout)

        self.systemCardDivider = QFrame(self.systemCard)
        self.systemCardDivider.setObjectName(u"systemCardDivider")
        self.systemCardDivider.setFrameShape(QFrame.Shape.NoFrame)

        self.systemCardLayout.addWidget(self.systemCardDivider)

        self.systemCardContent = QVBoxLayout()
        self.systemCardContent.setSpacing(11)
        self.systemCardContent.setObjectName(u"systemCardContent")
        self.systemCardContent.setContentsMargins(0, 0, 0, 0)
        self.rowVersionLayout = QHBoxLayout()
        self.rowVersionLayout.setSpacing(10)
        self.rowVersionLayout.setObjectName(u"rowVersionLayout")
        self.rowVersionLayout.setContentsMargins(0, 0, 0, 0)
        self.keyVersion = QLabel(self.systemCard)
        self.keyVersion.setObjectName(u"keyVersion")

        self.rowVersionLayout.addWidget(self.keyVersion)

        self.rowVersionSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowVersionLayout.addItem(self.rowVersionSpacer)

        self.valueVersion = QLabel(self.systemCard)
        self.valueVersion.setObjectName(u"valueVersion")
        self.valueVersion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.rowVersionLayout.addWidget(self.valueVersion)


        self.systemCardContent.addLayout(self.rowVersionLayout)

        self.rowDatabaseLayout = QHBoxLayout()
        self.rowDatabaseLayout.setSpacing(10)
        self.rowDatabaseLayout.setObjectName(u"rowDatabaseLayout")
        self.rowDatabaseLayout.setContentsMargins(0, 0, 0, 0)
        self.keyDatabase = QLabel(self.systemCard)
        self.keyDatabase.setObjectName(u"keyDatabase")

        self.rowDatabaseLayout.addWidget(self.keyDatabase)

        self.rowDatabaseSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowDatabaseLayout.addItem(self.rowDatabaseSpacer)

        self.valueDatabase = QLabel(self.systemCard)
        self.valueDatabase.setObjectName(u"valueDatabase")
        self.valueDatabase.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.rowDatabaseLayout.addWidget(self.valueDatabase)


        self.systemCardContent.addLayout(self.rowDatabaseLayout)

        self.rowServerLayout = QHBoxLayout()
        self.rowServerLayout.setSpacing(10)
        self.rowServerLayout.setObjectName(u"rowServerLayout")
        self.rowServerLayout.setContentsMargins(0, 0, 0, 0)
        self.keyServer = QLabel(self.systemCard)
        self.keyServer.setObjectName(u"keyServer")

        self.rowServerLayout.addWidget(self.keyServer)

        self.rowServerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowServerLayout.addItem(self.rowServerSpacer)

        self.valueServer = QLabel(self.systemCard)
        self.valueServer.setObjectName(u"valueServer")
        self.valueServer.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.rowServerLayout.addWidget(self.valueServer)


        self.systemCardContent.addLayout(self.rowServerLayout)

        self.rowCurrentUserLayout = QHBoxLayout()
        self.rowCurrentUserLayout.setSpacing(10)
        self.rowCurrentUserLayout.setObjectName(u"rowCurrentUserLayout")
        self.rowCurrentUserLayout.setContentsMargins(0, 0, 0, 0)
        self.keyCurrentUser = QLabel(self.systemCard)
        self.keyCurrentUser.setObjectName(u"keyCurrentUser")

        self.rowCurrentUserLayout.addWidget(self.keyCurrentUser)

        self.rowCurrentUserSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowCurrentUserLayout.addItem(self.rowCurrentUserSpacer)

        self.valueCurrentUser = QLabel(self.systemCard)
        self.valueCurrentUser.setObjectName(u"valueCurrentUser")
        self.valueCurrentUser.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.rowCurrentUserLayout.addWidget(self.valueCurrentUser)


        self.systemCardContent.addLayout(self.rowCurrentUserLayout)

        self.rowRoleLayout = QHBoxLayout()
        self.rowRoleLayout.setSpacing(10)
        self.rowRoleLayout.setObjectName(u"rowRoleLayout")
        self.rowRoleLayout.setContentsMargins(0, 0, 0, 0)
        self.keyRole = QLabel(self.systemCard)
        self.keyRole.setObjectName(u"keyRole")

        self.rowRoleLayout.addWidget(self.keyRole)

        self.rowRoleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowRoleLayout.addItem(self.rowRoleSpacer)

        self.valueRole = QLabel(self.systemCard)
        self.valueRole.setObjectName(u"valueRole")
        self.valueRole.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.rowRoleLayout.addWidget(self.valueRole)


        self.systemCardContent.addLayout(self.rowRoleLayout)


        self.systemCardLayout.addLayout(self.systemCardContent)


        self.rightColumnLayout.addWidget(self.systemCard)

        self.rightColumnSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightColumnLayout.addItem(self.rightColumnSpacer)


        self.bodyLayout.addWidget(self.rightColumn)


        self.contentLayout.addLayout(self.bodyLayout)

        self.teamCard = QFrame(self.scrollAreaWidgetContents)
        self.teamCard.setObjectName(u"teamCard")
        self.teamCard.setFrameShape(QFrame.Shape.NoFrame)
        self.teamCardLayout = QVBoxLayout(self.teamCard)
        self.teamCardLayout.setSpacing(12)
        self.teamCardLayout.setObjectName(u"teamCardLayout")
        self.teamCardLayout.setContentsMargins(18, 16, 18, 16)
        self.teamCardTitleLayout = QHBoxLayout()
        self.teamCardTitleLayout.setSpacing(10)
        self.teamCardTitleLayout.setObjectName(u"teamCardTitleLayout")
        self.teamCardTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.teamCardIcon = QLabel(self.teamCard)
        self.teamCardIcon.setObjectName(u"teamCardIcon")
        self.teamCardIcon.setMinimumSize(QSize(30, 30))
        self.teamCardIcon.setMaximumSize(QSize(30, 30))
        self.teamCardIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.teamCardTitleLayout.addWidget(self.teamCardIcon)

        self.teamCardTitle = QLabel(self.teamCard)
        self.teamCardTitle.setObjectName(u"teamCardTitle")

        self.teamCardTitleLayout.addWidget(self.teamCardTitle)

        self.teamCardHint = QLabel(self.teamCard)
        self.teamCardHint.setObjectName(u"teamCardHint")

        self.teamCardTitleLayout.addWidget(self.teamCardHint)

        self.teamCardTitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.teamCardTitleLayout.addItem(self.teamCardTitleSpacer)


        self.teamCardLayout.addLayout(self.teamCardTitleLayout)

        self.teamCardDivider = QFrame(self.teamCard)
        self.teamCardDivider.setObjectName(u"teamCardDivider")
        self.teamCardDivider.setFrameShape(QFrame.Shape.NoFrame)

        self.teamCardLayout.addWidget(self.teamCardDivider)

        self.teamCardContent = QVBoxLayout()
        self.teamCardContent.setSpacing(0)
        self.teamCardContent.setObjectName(u"teamCardContent")
        self.teamCardContent.setContentsMargins(0, 0, 0, 0)
        self.memberRow1 = QFrame(self.teamCard)
        self.memberRow1.setObjectName(u"memberRow1")
        self.memberRow1.setFrameShape(QFrame.Shape.NoFrame)
        self.memberRow1Layout = QHBoxLayout(self.memberRow1)
        self.memberRow1Layout.setSpacing(14)
        self.memberRow1Layout.setObjectName(u"memberRow1Layout")
        self.memberRow1Layout.setContentsMargins(6, 10, 6, 10)
        self.avatarMember1 = QToolButton(self.memberRow1)
        self.avatarMember1.setObjectName(u"avatarMember1")
        self.avatarMember1.setMinimumSize(QSize(40, 40))
        self.avatarMember1.setMaximumSize(QSize(40, 40))
        self.avatarMember1.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.memberRow1Layout.addWidget(self.avatarMember1)

        self.nameColumnMember1 = QWidget(self.memberRow1)
        self.nameColumnMember1.setObjectName(u"nameColumnMember1")
        self.nameColumnMember1.setMinimumSize(QSize(210, 0))
        self.nameColumnMember1.setMaximumSize(QSize(210, 16777215))
        self.nameColumnMember1Layout = QVBoxLayout(self.nameColumnMember1)
        self.nameColumnMember1Layout.setSpacing(3)
        self.nameColumnMember1Layout.setObjectName(u"nameColumnMember1Layout")
        self.nameColumnMember1Layout.setContentsMargins(0, 0, 0, 0)
        self.nameMember1 = QLabel(self.nameColumnMember1)
        self.nameMember1.setObjectName(u"nameMember1")

        self.nameColumnMember1Layout.addWidget(self.nameMember1)

        self.roleMember1Layout = QHBoxLayout()
        self.roleMember1Layout.setSpacing(0)
        self.roleMember1Layout.setObjectName(u"roleMember1Layout")
        self.roleMember1Layout.setContentsMargins(0, 0, 0, 0)
        self.roleMember1 = QLabel(self.nameColumnMember1)
        self.roleMember1.setObjectName(u"roleMember1")

        self.roleMember1Layout.addWidget(self.roleMember1)

        self.roleMember1Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.roleMember1Layout.addItem(self.roleMember1Spacer)


        self.nameColumnMember1Layout.addLayout(self.roleMember1Layout)


        self.memberRow1Layout.addWidget(self.nameColumnMember1)

        self.descMember1 = QLabel(self.memberRow1)
        self.descMember1.setObjectName(u"descMember1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.descMember1.sizePolicy().hasHeightForWidth())
        self.descMember1.setSizePolicy(sizePolicy4)
        self.descMember1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.descMember1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.descMember1.setWordWrap(True)

        self.memberRow1Layout.addWidget(self.descMember1)

        self.btnGithub1 = QPushButton(self.memberRow1)
        self.btnGithub1.setObjectName(u"btnGithub1")
        self.btnGithub1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow1Layout.addWidget(self.btnGithub1)

        self.btnLinkedin1 = QPushButton(self.memberRow1)
        self.btnLinkedin1.setObjectName(u"btnLinkedin1")
        self.btnLinkedin1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow1Layout.addWidget(self.btnLinkedin1)

        self.btnEmail1 = QPushButton(self.memberRow1)
        self.btnEmail1.setObjectName(u"btnEmail1")
        self.btnEmail1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow1Layout.addWidget(self.btnEmail1)


        self.teamCardContent.addWidget(self.memberRow1)

        self.teamDivider1 = QFrame(self.teamCard)
        self.teamDivider1.setObjectName(u"teamDivider1")
        self.teamDivider1.setFrameShape(QFrame.Shape.NoFrame)

        self.teamCardContent.addWidget(self.teamDivider1)

        self.memberRow2 = QFrame(self.teamCard)
        self.memberRow2.setObjectName(u"memberRow2")
        self.memberRow2.setFrameShape(QFrame.Shape.NoFrame)
        self.memberRow2Layout = QHBoxLayout(self.memberRow2)
        self.memberRow2Layout.setSpacing(14)
        self.memberRow2Layout.setObjectName(u"memberRow2Layout")
        self.memberRow2Layout.setContentsMargins(6, 10, 6, 10)
        self.avatarMember2 = QToolButton(self.memberRow2)
        self.avatarMember2.setObjectName(u"avatarMember2")
        self.avatarMember2.setMinimumSize(QSize(40, 40))
        self.avatarMember2.setMaximumSize(QSize(40, 40))
        self.avatarMember2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.memberRow2Layout.addWidget(self.avatarMember2)

        self.nameColumnMember2 = QWidget(self.memberRow2)
        self.nameColumnMember2.setObjectName(u"nameColumnMember2")
        self.nameColumnMember2.setMinimumSize(QSize(210, 0))
        self.nameColumnMember2.setMaximumSize(QSize(210, 16777215))
        self.nameColumnMember2Layout = QVBoxLayout(self.nameColumnMember2)
        self.nameColumnMember2Layout.setSpacing(3)
        self.nameColumnMember2Layout.setObjectName(u"nameColumnMember2Layout")
        self.nameColumnMember2Layout.setContentsMargins(0, 0, 0, 0)
        self.nameMember2 = QLabel(self.nameColumnMember2)
        self.nameMember2.setObjectName(u"nameMember2")

        self.nameColumnMember2Layout.addWidget(self.nameMember2)

        self.roleMember2Layout = QHBoxLayout()
        self.roleMember2Layout.setSpacing(0)
        self.roleMember2Layout.setObjectName(u"roleMember2Layout")
        self.roleMember2Layout.setContentsMargins(0, 0, 0, 0)
        self.roleMember2 = QLabel(self.nameColumnMember2)
        self.roleMember2.setObjectName(u"roleMember2")

        self.roleMember2Layout.addWidget(self.roleMember2)

        self.roleMember2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.roleMember2Layout.addItem(self.roleMember2Spacer)


        self.nameColumnMember2Layout.addLayout(self.roleMember2Layout)


        self.memberRow2Layout.addWidget(self.nameColumnMember2)

        self.descMember2 = QLabel(self.memberRow2)
        self.descMember2.setObjectName(u"descMember2")
        sizePolicy4.setHeightForWidth(self.descMember2.sizePolicy().hasHeightForWidth())
        self.descMember2.setSizePolicy(sizePolicy4)
        self.descMember2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.descMember2.setWordWrap(True)

        self.memberRow2Layout.addWidget(self.descMember2)

        self.btnGithub2 = QPushButton(self.memberRow2)
        self.btnGithub2.setObjectName(u"btnGithub2")
        self.btnGithub2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow2Layout.addWidget(self.btnGithub2)

        self.btnLinkedin2 = QPushButton(self.memberRow2)
        self.btnLinkedin2.setObjectName(u"btnLinkedin2")
        self.btnLinkedin2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow2Layout.addWidget(self.btnLinkedin2)

        self.btnEmail2 = QPushButton(self.memberRow2)
        self.btnEmail2.setObjectName(u"btnEmail2")
        self.btnEmail2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow2Layout.addWidget(self.btnEmail2)


        self.teamCardContent.addWidget(self.memberRow2)

        self.teamDivider2 = QFrame(self.teamCard)
        self.teamDivider2.setObjectName(u"teamDivider2")
        self.teamDivider2.setFrameShape(QFrame.Shape.NoFrame)

        self.teamCardContent.addWidget(self.teamDivider2)

        self.memberRow3 = QFrame(self.teamCard)
        self.memberRow3.setObjectName(u"memberRow3")
        self.memberRow3.setFrameShape(QFrame.Shape.NoFrame)
        self.memberRow3Layout = QHBoxLayout(self.memberRow3)
        self.memberRow3Layout.setSpacing(14)
        self.memberRow3Layout.setObjectName(u"memberRow3Layout")
        self.memberRow3Layout.setContentsMargins(6, 10, 6, 10)
        self.avatarMember3 = QToolButton(self.memberRow3)
        self.avatarMember3.setObjectName(u"avatarMember3")
        self.avatarMember3.setMinimumSize(QSize(40, 40))
        self.avatarMember3.setMaximumSize(QSize(40, 40))
        self.avatarMember3.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.memberRow3Layout.addWidget(self.avatarMember3)

        self.nameColumnMember3 = QWidget(self.memberRow3)
        self.nameColumnMember3.setObjectName(u"nameColumnMember3")
        self.nameColumnMember3.setMinimumSize(QSize(210, 0))
        self.nameColumnMember3.setMaximumSize(QSize(210, 16777215))
        self.nameColumnMember3Layout = QVBoxLayout(self.nameColumnMember3)
        self.nameColumnMember3Layout.setSpacing(3)
        self.nameColumnMember3Layout.setObjectName(u"nameColumnMember3Layout")
        self.nameColumnMember3Layout.setContentsMargins(0, 0, 0, 0)
        self.nameMember3 = QLabel(self.nameColumnMember3)
        self.nameMember3.setObjectName(u"nameMember3")

        self.nameColumnMember3Layout.addWidget(self.nameMember3)

        self.roleMember3Layout = QHBoxLayout()
        self.roleMember3Layout.setSpacing(0)
        self.roleMember3Layout.setObjectName(u"roleMember3Layout")
        self.roleMember3Layout.setContentsMargins(0, 0, 0, 0)
        self.roleMember3 = QLabel(self.nameColumnMember3)
        self.roleMember3.setObjectName(u"roleMember3")

        self.roleMember3Layout.addWidget(self.roleMember3)

        self.roleMember3Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.roleMember3Layout.addItem(self.roleMember3Spacer)


        self.nameColumnMember3Layout.addLayout(self.roleMember3Layout)


        self.memberRow3Layout.addWidget(self.nameColumnMember3)

        self.descMember3 = QLabel(self.memberRow3)
        self.descMember3.setObjectName(u"descMember3")
        sizePolicy4.setHeightForWidth(self.descMember3.sizePolicy().hasHeightForWidth())
        self.descMember3.setSizePolicy(sizePolicy4)
        self.descMember3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.descMember3.setWordWrap(True)

        self.memberRow3Layout.addWidget(self.descMember3)

        self.btnGithub3 = QPushButton(self.memberRow3)
        self.btnGithub3.setObjectName(u"btnGithub3")
        self.btnGithub3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow3Layout.addWidget(self.btnGithub3)

        self.btnLinkedin3 = QPushButton(self.memberRow3)
        self.btnLinkedin3.setObjectName(u"btnLinkedin3")
        self.btnLinkedin3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow3Layout.addWidget(self.btnLinkedin3)

        self.btnEmail3 = QPushButton(self.memberRow3)
        self.btnEmail3.setObjectName(u"btnEmail3")
        self.btnEmail3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow3Layout.addWidget(self.btnEmail3)


        self.teamCardContent.addWidget(self.memberRow3)

        self.teamDivider3 = QFrame(self.teamCard)
        self.teamDivider3.setObjectName(u"teamDivider3")
        self.teamDivider3.setFrameShape(QFrame.Shape.NoFrame)

        self.teamCardContent.addWidget(self.teamDivider3)

        self.memberRow4 = QFrame(self.teamCard)
        self.memberRow4.setObjectName(u"memberRow4")
        self.memberRow4.setFrameShape(QFrame.Shape.NoFrame)
        self.memberRow4Layout = QHBoxLayout(self.memberRow4)
        self.memberRow4Layout.setSpacing(14)
        self.memberRow4Layout.setObjectName(u"memberRow4Layout")
        self.memberRow4Layout.setContentsMargins(6, 10, 6, 10)
        self.avatarMember4 = QToolButton(self.memberRow4)
        self.avatarMember4.setObjectName(u"avatarMember4")
        self.avatarMember4.setMinimumSize(QSize(40, 40))
        self.avatarMember4.setMaximumSize(QSize(40, 40))
        self.avatarMember4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.memberRow4Layout.addWidget(self.avatarMember4)

        self.nameColumnMember4 = QWidget(self.memberRow4)
        self.nameColumnMember4.setObjectName(u"nameColumnMember4")
        self.nameColumnMember4.setMinimumSize(QSize(210, 0))
        self.nameColumnMember4.setMaximumSize(QSize(210, 16777215))
        self.nameColumnMember4Layout = QVBoxLayout(self.nameColumnMember4)
        self.nameColumnMember4Layout.setSpacing(3)
        self.nameColumnMember4Layout.setObjectName(u"nameColumnMember4Layout")
        self.nameColumnMember4Layout.setContentsMargins(0, 0, 0, 0)
        self.nameMember4 = QLabel(self.nameColumnMember4)
        self.nameMember4.setObjectName(u"nameMember4")

        self.nameColumnMember4Layout.addWidget(self.nameMember4)

        self.roleMember4Layout = QHBoxLayout()
        self.roleMember4Layout.setSpacing(0)
        self.roleMember4Layout.setObjectName(u"roleMember4Layout")
        self.roleMember4Layout.setContentsMargins(0, 0, 0, 0)
        self.roleMember4 = QLabel(self.nameColumnMember4)
        self.roleMember4.setObjectName(u"roleMember4")

        self.roleMember4Layout.addWidget(self.roleMember4)

        self.roleMember4Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.roleMember4Layout.addItem(self.roleMember4Spacer)


        self.nameColumnMember4Layout.addLayout(self.roleMember4Layout)


        self.memberRow4Layout.addWidget(self.nameColumnMember4)

        self.descMember4 = QLabel(self.memberRow4)
        self.descMember4.setObjectName(u"descMember4")
        sizePolicy4.setHeightForWidth(self.descMember4.sizePolicy().hasHeightForWidth())
        self.descMember4.setSizePolicy(sizePolicy4)
        self.descMember4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.descMember4.setWordWrap(True)

        self.memberRow4Layout.addWidget(self.descMember4)

        self.btnGithub4 = QPushButton(self.memberRow4)
        self.btnGithub4.setObjectName(u"btnGithub4")
        self.btnGithub4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow4Layout.addWidget(self.btnGithub4)

        self.btnLinkedin4 = QPushButton(self.memberRow4)
        self.btnLinkedin4.setObjectName(u"btnLinkedin4")
        self.btnLinkedin4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow4Layout.addWidget(self.btnLinkedin4)

        self.btnEmail4 = QPushButton(self.memberRow4)
        self.btnEmail4.setObjectName(u"btnEmail4")
        self.btnEmail4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow4Layout.addWidget(self.btnEmail4)


        self.teamCardContent.addWidget(self.memberRow4)

        self.teamDivider4 = QFrame(self.teamCard)
        self.teamDivider4.setObjectName(u"teamDivider4")
        self.teamDivider4.setFrameShape(QFrame.Shape.NoFrame)

        self.teamCardContent.addWidget(self.teamDivider4)

        self.memberRow5 = QFrame(self.teamCard)
        self.memberRow5.setObjectName(u"memberRow5")
        self.memberRow5.setFrameShape(QFrame.Shape.NoFrame)
        self.memberRow5Layout = QHBoxLayout(self.memberRow5)
        self.memberRow5Layout.setSpacing(14)
        self.memberRow5Layout.setObjectName(u"memberRow5Layout")
        self.memberRow5Layout.setContentsMargins(6, 10, 6, 10)
        self.avatarMember5 = QToolButton(self.memberRow5)
        self.avatarMember5.setObjectName(u"avatarMember5")
        self.avatarMember5.setMinimumSize(QSize(40, 40))
        self.avatarMember5.setMaximumSize(QSize(40, 40))
        self.avatarMember5.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.memberRow5Layout.addWidget(self.avatarMember5)

        self.nameColumnMember5 = QWidget(self.memberRow5)
        self.nameColumnMember5.setObjectName(u"nameColumnMember5")
        self.nameColumnMember5.setMinimumSize(QSize(210, 0))
        self.nameColumnMember5.setMaximumSize(QSize(210, 16777215))
        self.nameColumnMember5Layout = QVBoxLayout(self.nameColumnMember5)
        self.nameColumnMember5Layout.setSpacing(3)
        self.nameColumnMember5Layout.setObjectName(u"nameColumnMember5Layout")
        self.nameColumnMember5Layout.setContentsMargins(0, 0, 0, 0)
        self.nameMember5 = QLabel(self.nameColumnMember5)
        self.nameMember5.setObjectName(u"nameMember5")

        self.nameColumnMember5Layout.addWidget(self.nameMember5)

        self.roleMember5Layout = QHBoxLayout()
        self.roleMember5Layout.setSpacing(0)
        self.roleMember5Layout.setObjectName(u"roleMember5Layout")
        self.roleMember5Layout.setContentsMargins(0, 0, 0, 0)
        self.roleMember5 = QLabel(self.nameColumnMember5)
        self.roleMember5.setObjectName(u"roleMember5")

        self.roleMember5Layout.addWidget(self.roleMember5)

        self.roleMember5Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.roleMember5Layout.addItem(self.roleMember5Spacer)


        self.nameColumnMember5Layout.addLayout(self.roleMember5Layout)


        self.memberRow5Layout.addWidget(self.nameColumnMember5)

        self.descMember5 = QLabel(self.memberRow5)
        self.descMember5.setObjectName(u"descMember5")
        sizePolicy4.setHeightForWidth(self.descMember5.sizePolicy().hasHeightForWidth())
        self.descMember5.setSizePolicy(sizePolicy4)
        self.descMember5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.descMember5.setWordWrap(True)

        self.memberRow5Layout.addWidget(self.descMember5)

        self.btnGithub5 = QPushButton(self.memberRow5)
        self.btnGithub5.setObjectName(u"btnGithub5")
        self.btnGithub5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow5Layout.addWidget(self.btnGithub5)

        self.btnLinkedin5 = QPushButton(self.memberRow5)
        self.btnLinkedin5.setObjectName(u"btnLinkedin5")
        self.btnLinkedin5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow5Layout.addWidget(self.btnLinkedin5)

        self.btnEmail5 = QPushButton(self.memberRow5)
        self.btnEmail5.setObjectName(u"btnEmail5")
        self.btnEmail5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.memberRow5Layout.addWidget(self.btnEmail5)


        self.teamCardContent.addWidget(self.memberRow5)

        self.teamSupportDivider = QFrame(self.teamCard)
        self.teamSupportDivider.setObjectName(u"teamSupportDivider")
        self.teamSupportDivider.setFrameShape(QFrame.Shape.NoFrame)

        self.teamCardContent.addWidget(self.teamSupportDivider)

        self.teamSupportLayout = QHBoxLayout()
        self.teamSupportLayout.setSpacing(14)
        self.teamSupportLayout.setObjectName(u"teamSupportLayout")
        self.teamSupportLayout.setContentsMargins(6, 14, 6, 2)
        self.supportText = QLabel(self.teamCard)
        self.supportText.setObjectName(u"supportText")
        sizePolicy4.setHeightForWidth(self.supportText.sizePolicy().hasHeightForWidth())
        self.supportText.setSizePolicy(sizePolicy4)
        self.supportText.setWordWrap(True)

        self.teamSupportLayout.addWidget(self.supportText)

        self.btnSupportEmail = QPushButton(self.teamCard)
        self.btnSupportEmail.setObjectName(u"btnSupportEmail")
        self.btnSupportEmail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.teamSupportLayout.addWidget(self.btnSupportEmail)


        self.teamCardContent.addLayout(self.teamSupportLayout)


        self.teamCardLayout.addLayout(self.teamCardContent)


        self.contentLayout.addWidget(self.teamCard)

        self.contentBottomSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.contentLayout.addItem(self.contentBottomSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.mainLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Trung t\u00e2m h\u1ed7 tr\u1ee3", None))
        self.lblTitle.setText(QCoreApplication.translate("Form", u"Trung t\u00e2m h\u1ed7 tr\u1ee3", None))
        self.lblSubTitle.setText(QCoreApplication.translate("Form", u"H\u01b0\u1edbng d\u1eabn s\u1eed d\u1ee5ng, ph\u00edm t\u1eaft v\u00e0 th\u00f4ng tin h\u1ec7 th\u1ed1ng", None))
        self.guideCard.setProperty(u"class", QCoreApplication.translate("Form", u"card", None))
        self.guideCardIcon.setText("")
        self.guideCardIcon.setProperty(u"class", QCoreApplication.translate("Form", u"cardIcon", None))
        self.guideCardIcon.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.book-open", None))
        self.guideCardIcon.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.guideCardTitle.setText(QCoreApplication.translate("Form", u"H\u01b0\u1edbng d\u1eabn nhanh", None))
        self.guideCardTitle.setProperty(u"class", QCoreApplication.translate("Form", u"cardTitle", None))
        self.guideCardHint.setText(QCoreApplication.translate("Form", u"B\u1ea5m v\u00e0o t\u1eebng m\u1ee5c \u0111\u1ec3 xem chi ti\u1ebft", None))
        self.guideCardHint.setProperty(u"class", QCoreApplication.translate("Form", u"cardHint", None))
        self.guideCardDivider.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.btnGuide1.setText(QCoreApplication.translate("Form", u"\u0110\u0103ng nh\u1eadp v\u00e0 kh\u00f4i ph\u1ee5c m\u1eadt kh\u1ea9u", None))
        self.btnGuide1.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentGuide1Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide1Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide1Line1Text.setText(QCoreApplication.translate("Form", u"\u0110\u0103ng nh\u1eadp b\u1eb1ng t\u00ean t\u00e0i kho\u1ea3n v\u00e0 m\u1eadt kh\u1ea9u do qu\u1ea3n tr\u1ecb vi\u00ean c\u1ea5p.", None))
        self.contentGuide1Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide1Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide1Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide1Line2Text.setText(QCoreApplication.translate("Form", u"Qu\u00ean m\u1eadt kh\u1ea9u: b\u1ea5m \"Qu\u00ean m\u1eadt kh\u1ea9u\" \u1edf m\u00e0n h\u00ecnh \u0111\u0103ng nh\u1eadp, nh\u1eadp email \u0111\u00e3 \u0111\u0103ng k\u00fd, h\u1ec7 th\u1ed1ng g\u1eedi m\u00e3 x\u00e1c th\u1ef1c 6 ch\u1eef s\u1ed1 v\u00e0o h\u1ed9p th\u01b0.", None))
        self.contentGuide1Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide1Line3Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide1Line3Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide1Line3Text.setText(QCoreApplication.translate("Form", u"M\u00e3 x\u00e1c th\u1ef1c c\u00f3 h\u1ea1n 5 ph\u00fat v\u00e0 cho t\u1ed1i \u0111a 5 l\u1ea7n nh\u1eadp sai. Hai l\u1ea7n g\u1eedi m\u00e3 ph\u1ea3i c\u00e1ch nhau 60 gi\u00e2y.", None))
        self.contentGuide1Line3Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide1Line4Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide1Line4Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide1Line4Text.setText(QCoreApplication.translate("Form", u"Sau khi x\u00e1c th\u1ef1c \u0111\u00fang, b\u1ea1n c\u00f3 10 ph\u00fat \u0111\u1ec3 \u0111\u1eb7t m\u1eadt kh\u1ea9u m\u1edbi. M\u1eadt kh\u1ea9u t\u1ed1i thi\u1ec3u 8 k\u00fd t\u1ef1.", None))
        self.contentGuide1Line4Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide1Line5Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide1Line5Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide1Line5Text.setText(QCoreApplication.translate("Form", u"T\u00e0i kho\u1ea3n \u0111\u00e3 b\u1ecb kh\u00f3a s\u1ebd kh\u00f4ng \u0111\u0103ng nh\u1eadp \u0111\u01b0\u1ee3c, k\u1ec3 c\u1ea3 khi nh\u1eadp \u0111\u00fang m\u1eadt kh\u1ea9u.", None))
        self.contentGuide1Line5Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.btnGuide2.setText(QCoreApplication.translate("Form", u"M\u00e0n h\u00ecnh T\u1ed5ng quan", None))
        self.btnGuide2.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentGuide2Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide2Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide2Line1Text.setText(QCoreApplication.translate("Form", u"B\u1ed1n th\u1ebb tr\u00ean c\u00f9ng: doanh thu h\u00f4m nay, s\u1ed1 h\u00f3a \u0111\u01a1n, c\u1ea3nh b\u00e1o s\u1eafp h\u1ebft h\u00e0ng v\u00e0 kh\u00e1ch h\u00e0ng m\u1edbi.", None))
        self.contentGuide2Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide2Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide2Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide2Line2Text.setText(QCoreApplication.translate("Form", u"K\u00fd hi\u1ec7u \u25b2 \u25bc d\u01b0\u1edbi m\u1ed7i th\u1ebb l\u00e0 m\u1ee9c t\u0103ng gi\u1ea3m so v\u1edbi c\u00f9ng ch\u1ec9 s\u1ed1 c\u1ee7a ng\u00e0y h\u00f4m qua.", None))
        self.contentGuide2Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide2Line3Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide2Line3Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide2Line3Text.setText(QCoreApplication.translate("Form", u"Bi\u1ec3u \u0111\u1ed3 c\u1ed9t th\u1ec3 hi\u1ec7n doanh thu c\u1ee7a b\u1ed1n tu\u1ea7n trong th\u00e1ng hi\u1ec7n t\u1ea1i.", None))
        self.contentGuide2Line3Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide2Line4Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide2Line4Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide2Line4Text.setText(QCoreApplication.translate("Form", u"B\u1ea3ng \"Giao d\u1ecbch g\u1ea7n \u0111\u00e2y\" li\u1ec7t k\u00ea c\u00e1c h\u00f3a \u0111\u01a1n m\u1edbi nh\u1ea5t, cu\u1ed9n xu\u1ed1ng \u0111\u1ec3 xem h\u1ebft.", None))
        self.contentGuide2Line4Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide2Line5Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide2Line5Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide2Line5Text.setText(QCoreApplication.translate("Form", u"B\u1ed1n \u00f4 thao t\u00e1c nhanh m\u1edf th\u1eb3ng sang nghi\u1ec7p v\u1ee5 t\u01b0\u01a1ng \u1ee9ng.", None))
        self.contentGuide2Line5Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide2Line6Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide2Line6Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide2Line6Text.setText(QCoreApplication.translate("Form", u"B\u1ea5m \"T\u1ea3i l\u1ea1i d\u1eef li\u1ec7u\" \u0111\u1ec3 l\u1ea5y l\u1ea1i s\u1ed1 li\u1ec7u m\u1edbi nh\u1ea5t t\u1eeb c\u01a1 s\u1edf d\u1eef li\u1ec7u.", None))
        self.contentGuide2Line6Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.btnGuide3.setText(QCoreApplication.translate("Form", u"B\u00e1n h\u00e0ng t\u1ea1i qu\u1ea7y", None))
        self.btnGuide3.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentGuide3Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide3Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide3Line1Text.setText(QCoreApplication.translate("Form", u"T\u00ecm h\u00e0ng b\u1eb1ng \u00f4 t\u00ecm ki\u1ebfm, ho\u1eb7c l\u1ecdc nhanh theo nh\u00f3m h\u00e0ng \u1edf d\u00e3y n\u00fat ph\u00eda tr\u00ean.", None))
        self.contentGuide3Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide3Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide3Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide3Line2Text.setText(QCoreApplication.translate("Form", u"B\u1ea5m v\u00e0o m\u1ed9t s\u1ea3n ph\u1ea9m \u0111\u1ec3 th\u00eam v\u00e0o gi\u1ecf. Trong gi\u1ecf, d\u00f9ng n\u00fat + v\u00e0 \u2212 \u0111\u1ec3 \u0111\u1ed5i s\u1ed1 l\u01b0\u1ee3ng.", None))
        self.contentGuide3Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide3Line3Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide3Line3Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide3Line3Text.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn kh\u00e1ch h\u00e0ng \u0111\u1ec3 \u00e1p d\u1ee5ng \u01b0u \u0111\u00e3i theo h\u1ea1ng th\u00e0nh vi\u00ean. B\u1ecf tr\u1ed1ng ngh\u0129a l\u00e0 kh\u00e1ch l\u1ebb.", None))
        self.contentGuide3Line3Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide3Line4Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide3Line4Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide3Line4Text.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn h\u00ecnh th\u1ee9c thanh to\u00e1n: Ti\u1ec1n m\u1eb7t, Th\u1ebb ho\u1eb7c Chuy\u1ec3n kho\u1ea3n.", None))
        self.contentGuide3Line4Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide3Line5Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide3Line5Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide3Line5Text.setText(QCoreApplication.translate("Form", u"B\u1ea5m \"Thanh to\u00e1n\" \u0111\u1ec3 ch\u1ed1t h\u00f3a \u0111\u01a1n. H\u1ec7 th\u1ed1ng ghi h\u00f3a \u0111\u01a1n v\u00e0 tr\u1eeb t\u1ed3n kho t\u01b0\u01a1ng \u1ee9ng.", None))
        self.contentGuide3Line5Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide3Line6Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide3Line6Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide3Line6Text.setText(QCoreApplication.translate("Form", u"S\u1ed1 t\u1ed3n hi\u1ec3n th\u1ecb d\u01b0\u1edbi m\u1ed7i s\u1ea3n ph\u1ea9m. Kh\u00f4ng b\u00e1n \u0111\u01b0\u1ee3c qu\u00e1 s\u1ed1 t\u1ed3n \u0111ang c\u00f3.", None))
        self.contentGuide3Line6Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.btnGuide4.setText(QCoreApplication.translate("Form", u"Ph\u00e2n quy\u1ec1n t\u00e0i kho\u1ea3n", None))
        self.btnGuide4.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentGuide4Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide4Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide4Line1Text.setText(QCoreApplication.translate("Form", u"Admin: to\u00e0n quy\u1ec1n tr\u00ean h\u1ec7 th\u1ed1ng, g\u1ed3m c\u1ea3 qu\u1ea3n l\u00fd ng\u01b0\u1eddi d\u00f9ng.", None))
        self.contentGuide4Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide4Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide4Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide4Line2Text.setText(QCoreApplication.translate("Form", u"Manager: c\u00e1c nghi\u1ec7p v\u1ee5 kho, h\u00e0ng h\u00f3a v\u00e0 b\u00e1o c\u00e1o.", None))
        self.contentGuide4Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentGuide4Line3Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentGuide4Line3Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentGuide4Line3Text.setText(QCoreApplication.translate("Form", u"Cashier: ch\u1ec9 d\u00f9ng m\u00e0n h\u00ecnh b\u00e1n h\u00e0ng t\u1ea1i qu\u1ea7y, c\u00e1c m\u1ee5c qu\u1ea3n tr\u1ecb b\u1ecb \u1ea9n \u0111i.", None))
        self.contentGuide4Line3Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.issuesCard.setProperty(u"class", QCoreApplication.translate("Form", u"card", None))
        self.issuesCardIcon.setText("")
        self.issuesCardIcon.setProperty(u"class", QCoreApplication.translate("Form", u"cardIcon", None))
        self.issuesCardIcon.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.tools", None))
        self.issuesCardIcon.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.issuesCardTitle.setText(QCoreApplication.translate("Form", u"S\u1ef1 c\u1ed1 th\u01b0\u1eddng g\u1eb7p", None))
        self.issuesCardTitle.setProperty(u"class", QCoreApplication.translate("Form", u"cardTitle", None))
        self.issuesCardDivider.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.btnIssue1.setText(QCoreApplication.translate("Form", u"Kh\u00f4ng \u0111\u0103ng nh\u1eadp \u0111\u01b0\u1ee3c", None))
        self.btnIssue1.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentIssue1Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue1Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue1Line1Text.setText(QCoreApplication.translate("Form", u"Ki\u1ec3m tra ph\u00edm Caps Lock, m\u1eadt kh\u1ea9u ph\u00e2n bi\u1ec7t ch\u1eef hoa ch\u1eef th\u01b0\u1eddng.", None))
        self.contentIssue1Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentIssue1Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue1Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue1Line2Text.setText(QCoreApplication.translate("Form", u"N\u1ebfu b\u00e1o t\u00e0i kho\u1ea3n \u0111\u00e3 b\u1ecb kh\u00f3a, li\u00ean h\u1ec7 qu\u1ea3n tr\u1ecb vi\u00ean \u0111\u1ec3 m\u1edf l\u1ea1i.", None))
        self.contentIssue1Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentIssue1Line3Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue1Line3Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue1Line3Text.setText(QCoreApplication.translate("Form", u"N\u1ebfu b\u00e1o l\u1ed7i k\u1ebft n\u1ed1i, \u0111\u1ed1i chi\u1ebfu m\u1ee5c Th\u00f4ng tin h\u1ec7 th\u1ed1ng b\u00ean ph\u1ea3i xem \u0111\u00e3 n\u1ed1i \u0111\u00fang m\u00e1y ch\u1ee7 ch\u01b0a.", None))
        self.contentIssue1Line3Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.btnIssue2.setText(QCoreApplication.translate("Form", u"Kh\u00f4ng nh\u1eadn \u0111\u01b0\u1ee3c m\u00e3 x\u00e1c th\u1ef1c", None))
        self.btnIssue2.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentIssue2Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue2Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue2Line1Text.setText(QCoreApplication.translate("Form", u"Xem l\u1ea1i h\u1ed9p th\u01b0 r\u00e1c (Spam), th\u01b0 g\u1eedi t\u1ef1 \u0111\u1ed9ng th\u01b0\u1eddng b\u1ecb l\u1ecdc v\u00e0o \u0111\u00e2y.", None))
        self.contentIssue2Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentIssue2Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue2Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue2Line2Text.setText(QCoreApplication.translate("Form", u"Email nh\u1eadp v\u00e0o ph\u1ea3i tr\u00f9ng v\u1edbi email \u0111\u00e3 \u0111\u0103ng k\u00fd cho t\u00e0i kho\u1ea3n.", None))
        self.contentIssue2Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentIssue2Line3Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue2Line3Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue2Line3Text.setText(QCoreApplication.translate("Form", u"M\u00e3 c\u0169 h\u1ebft h\u1ea1n sau 5 ph\u00fat, h\u00e3y b\u1ea5m g\u1eedi l\u1ea1i v\u00e0 \u0111\u1ee3i t\u1ed1i thi\u1ec3u 60 gi\u00e2y gi\u1eefa hai l\u1ea7n g\u1eedi.", None))
        self.contentIssue2Line3Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.btnIssue3.setText(QCoreApplication.translate("Form", u"T\u1ed5ng quan kh\u00f4ng c\u00f3 s\u1ed1 li\u1ec7u", None))
        self.btnIssue3.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentIssue3Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue3Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue3Line1Text.setText(QCoreApplication.translate("Form", u"N\u1ebfu trong ng\u00e0y ch\u01b0a ph\u00e1t sinh h\u00f3a \u0111\u01a1n n\u00e0o th\u00ec c\u00e1c th\u1ebb hi\u1ec3n th\u1ecb 0, \u0111\u00e2y kh\u00f4ng ph\u1ea3i l\u1ed7i.", None))
        self.contentIssue3Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentIssue3Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue3Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue3Line2Text.setText(QCoreApplication.translate("Form", u"S\u1ed1 li\u1ec7u ch\u1ec9 \u0111\u01b0\u1ee3c l\u1ea5y l\u1ea1i khi m\u1edf m\u00e0n h\u00ecnh ho\u1eb7c khi b\u1ea5m \"T\u1ea3i l\u1ea1i d\u1eef li\u1ec7u\".", None))
        self.contentIssue3Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.btnIssue4.setText(QCoreApplication.translate("Form", u"Kh\u00f4ng thanh to\u00e1n \u0111\u01b0\u1ee3c \u0111\u01a1n", None))
        self.btnIssue4.setProperty(u"class", QCoreApplication.translate("Form", u"accordion", None))
        self.contentIssue4Line1Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue4Line1Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue4Line1Text.setText(QCoreApplication.translate("Form", u"Gi\u1ecf h\u00e0ng \u0111ang tr\u1ed1ng, c\u1ea7n th\u00eam \u00edt nh\u1ea5t m\u1ed9t s\u1ea3n ph\u1ea9m.", None))
        self.contentIssue4Line1Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.contentIssue4Line2Bullet.setText(QCoreApplication.translate("Form", u"-", None))
        self.contentIssue4Line2Bullet.setProperty(u"class", QCoreApplication.translate("Form", u"bullet", None))
        self.contentIssue4Line2Text.setText(QCoreApplication.translate("Form", u"S\u1ed1 l\u01b0\u1ee3ng \u0111\u1eb7t v\u01b0\u1ee3t qu\u00e1 s\u1ed1 t\u1ed3n kho c\u1ee7a s\u1ea3n ph\u1ea9m.", None))
        self.contentIssue4Line2Text.setProperty(u"class", QCoreApplication.translate("Form", u"accordionLine", None))
        self.shortcutsCard.setProperty(u"class", QCoreApplication.translate("Form", u"card", None))
        self.shortcutsCardIcon.setText("")
        self.shortcutsCardIcon.setProperty(u"class", QCoreApplication.translate("Form", u"cardIcon", None))
        self.shortcutsCardIcon.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.keyboard", None))
        self.shortcutsCardIcon.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.shortcutsCardTitle.setText(QCoreApplication.translate("Form", u"Ph\u00edm t\u1eaft", None))
        self.shortcutsCardTitle.setProperty(u"class", QCoreApplication.translate("Form", u"cardTitle", None))
        self.shortcutsCardHint.setText(QCoreApplication.translate("Form", u"Ch\u1ec9 d\u00f9ng trong m\u00e0n h\u00ecnh b\u00e1n h\u00e0ng", None))
        self.shortcutsCardHint.setProperty(u"class", QCoreApplication.translate("Form", u"cardHint", None))
        self.shortcutsCardDivider.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.keyShortcut1.setText(QCoreApplication.translate("Form", u"F1", None))
        self.keyShortcut1.setProperty(u"class", QCoreApplication.translate("Form", u"keyCap", None))
        self.descShortcut1.setText(QCoreApplication.translate("Form", u"M\u1edf Trung t\u00e2m h\u1ed7 tr\u1ee3", None))
        self.descShortcut1.setProperty(u"class", QCoreApplication.translate("Form", u"keyDesc", None))
        self.keyShortcut2.setText(QCoreApplication.translate("Form", u"F2", None))
        self.keyShortcut2.setProperty(u"class", QCoreApplication.translate("Form", u"keyCap", None))
        self.descShortcut2.setText(QCoreApplication.translate("Form", u"Nh\u1ea3y t\u1edbi \u00f4 t\u00ecm s\u1ea3n ph\u1ea9m", None))
        self.descShortcut2.setProperty(u"class", QCoreApplication.translate("Form", u"keyDesc", None))
        self.keyShortcut3.setText(QCoreApplication.translate("Form", u"F3", None))
        self.keyShortcut3.setProperty(u"class", QCoreApplication.translate("Form", u"keyCap", None))
        self.descShortcut3.setText(QCoreApplication.translate("Form", u"S\u1eeda chi\u1ebft kh\u1ea5u c\u1ee7a \u0111\u01a1n", None))
        self.descShortcut3.setProperty(u"class", QCoreApplication.translate("Form", u"keyDesc", None))
        self.keyShortcut4.setText(QCoreApplication.translate("Form", u"F9", None))
        self.keyShortcut4.setProperty(u"class", QCoreApplication.translate("Form", u"keyCap", None))
        self.descShortcut4.setText(QCoreApplication.translate("Form", u"Thanh to\u00e1n \u0111\u01a1n h\u00e0ng", None))
        self.descShortcut4.setProperty(u"class", QCoreApplication.translate("Form", u"keyDesc", None))
        self.systemCard.setProperty(u"class", QCoreApplication.translate("Form", u"card", None))
        self.systemCardIcon.setText("")
        self.systemCardIcon.setProperty(u"class", QCoreApplication.translate("Form", u"cardIcon", None))
        self.systemCardIcon.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.server", None))
        self.systemCardIcon.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.systemCardTitle.setText(QCoreApplication.translate("Form", u"Th\u00f4ng tin h\u1ec7 th\u1ed1ng", None))
        self.systemCardTitle.setProperty(u"class", QCoreApplication.translate("Form", u"cardTitle", None))
        self.systemCardDivider.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.keyVersion.setText(QCoreApplication.translate("Form", u"Phi\u00ean b\u1ea3n", None))
        self.keyVersion.setProperty(u"class", QCoreApplication.translate("Form", u"infoKey", None))
        self.valueVersion.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.valueVersion.setProperty(u"class", QCoreApplication.translate("Form", u"infoValue", None))
        self.keyDatabase.setText(QCoreApplication.translate("Form", u"C\u01a1 s\u1edf d\u1eef li\u1ec7u", None))
        self.keyDatabase.setProperty(u"class", QCoreApplication.translate("Form", u"infoKey", None))
        self.valueDatabase.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.valueDatabase.setProperty(u"class", QCoreApplication.translate("Form", u"infoValue", None))
        self.keyServer.setText(QCoreApplication.translate("Form", u"M\u00e1y ch\u1ee7", None))
        self.keyServer.setProperty(u"class", QCoreApplication.translate("Form", u"infoKey", None))
        self.valueServer.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.valueServer.setProperty(u"class", QCoreApplication.translate("Form", u"infoValue", None))
        self.keyCurrentUser.setText(QCoreApplication.translate("Form", u"\u0110ang \u0111\u0103ng nh\u1eadp", None))
        self.keyCurrentUser.setProperty(u"class", QCoreApplication.translate("Form", u"infoKey", None))
        self.valueCurrentUser.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.valueCurrentUser.setProperty(u"class", QCoreApplication.translate("Form", u"infoValue", None))
        self.keyRole.setText(QCoreApplication.translate("Form", u"Vai tr\u00f2", None))
        self.keyRole.setProperty(u"class", QCoreApplication.translate("Form", u"infoKey", None))
        self.valueRole.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.valueRole.setProperty(u"class", QCoreApplication.translate("Form", u"infoValue", None))
        self.teamCard.setProperty(u"class", QCoreApplication.translate("Form", u"card", None))
        self.teamCardIcon.setText("")
        self.teamCardIcon.setProperty(u"class", QCoreApplication.translate("Form", u"cardIcon", None))
        self.teamCardIcon.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.users", None))
        self.teamCardIcon.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.teamCardTitle.setText(QCoreApplication.translate("Form", u"\u0110\u1ed9i ng\u0169 ph\u00e1t tri\u1ec3n", None))
        self.teamCardTitle.setProperty(u"class", QCoreApplication.translate("Form", u"cardTitle", None))
        self.teamCardHint.setText(QCoreApplication.translate("Form", u"Li\u00ean h\u1ec7 tr\u1ef1c ti\u1ebfp khi c\u1ea7n h\u1ed7 tr\u1ee3 s\u00e2u h\u01a1n", None))
        self.teamCardHint.setProperty(u"class", QCoreApplication.translate("Form", u"cardHint", None))
        self.teamCardDivider.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.memberRow1.setProperty(u"class", QCoreApplication.translate("Form", u"memberRow", None))
        self.avatarMember1.setText("")
        self.avatarMember1.setProperty(u"class", QCoreApplication.translate("Form", u"avatar", None))
        self.avatarMember1.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.user", None))
        self.avatarMember1.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#94a3b8", None))
        self.nameMember1.setText(QCoreApplication.translate("Form", u"Tr\u1ea7n Th\u00e1i Ki\u1ec7t", None))
        self.nameMember1.setProperty(u"class", QCoreApplication.translate("Form", u"memberName", None))
        self.roleMember1.setText(QCoreApplication.translate("Form", u"Th\u00e0nh vi\u00ean s\u00e1ng l\u1eadp", None))
        self.roleMember1.setProperty(u"class", QCoreApplication.translate("Form", u"memberRole", None))
        self.descMember1.setText(QCoreApplication.translate("Form", u"Contact:", None))
        self.descMember1.setProperty(u"class", QCoreApplication.translate("Form", u"memberDesc", None))
#if QT_CONFIG(tooltip)
        self.btnGithub1.setToolTip(QCoreApplication.translate("Form", u"Xem GitHub", None))
#endif // QT_CONFIG(tooltip)
        self.btnGithub1.setText("")
        self.btnGithub1.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnGithub1.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.github", None))
        self.btnGithub1.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#0f172a", None))
        self.btnGithub1.setProperty(u"url", QCoreApplication.translate("Form", u"https://github.com/Karie206", None))
#if QT_CONFIG(tooltip)
        self.btnLinkedin1.setToolTip(QCoreApplication.translate("Form", u"Xem LinkedIn", None))
#endif // QT_CONFIG(tooltip)
        self.btnLinkedin1.setText("")
        self.btnLinkedin1.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnLinkedin1.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.linkedin", None))
        self.btnLinkedin1.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.btnLinkedin1.setProperty(u"url", QCoreApplication.translate("Form", u"https://linkedin.com/in/tranthaikiet", None))
#if QT_CONFIG(tooltip)
        self.btnEmail1.setToolTip(QCoreApplication.translate("Form", u"G\u1eedi email", None))
#endif // QT_CONFIG(tooltip)
        self.btnEmail1.setText("")
        self.btnEmail1.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnEmail1.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.envelope", None))
        self.btnEmail1.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#64748b", None))
        self.btnEmail1.setProperty(u"email", QCoreApplication.translate("Form", u"thaikiet519@gmail.com", None))
        self.teamDivider1.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.memberRow2.setProperty(u"class", QCoreApplication.translate("Form", u"memberRow", None))
        self.avatarMember2.setText("")
        self.avatarMember2.setProperty(u"class", QCoreApplication.translate("Form", u"avatar", None))
        self.avatarMember2.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.user", None))
        self.avatarMember2.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#94a3b8", None))
        self.nameMember2.setText(QCoreApplication.translate("Form", u"L\u00ea Tr\u1ea7n Khang", None))
        self.nameMember2.setProperty(u"class", QCoreApplication.translate("Form", u"memberName", None))
        self.roleMember2.setText(QCoreApplication.translate("Form", u"Th\u00e0nh vi\u00ean s\u00e1ng l\u1eadp", None))
        self.roleMember2.setProperty(u"class", QCoreApplication.translate("Form", u"memberRole", None))
        self.descMember2.setText(QCoreApplication.translate("Form", u"Contact:", None))
        self.descMember2.setProperty(u"class", QCoreApplication.translate("Form", u"memberDesc", None))
#if QT_CONFIG(tooltip)
        self.btnGithub2.setToolTip(QCoreApplication.translate("Form", u"Xem GitHub", None))
#endif // QT_CONFIG(tooltip)
        self.btnGithub2.setText("")
        self.btnGithub2.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnGithub2.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.github", None))
        self.btnGithub2.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#0f172a", None))
        self.btnGithub2.setProperty(u"url", QCoreApplication.translate("Form", u"https://github.com/letrankhang", None))
#if QT_CONFIG(tooltip)
        self.btnLinkedin2.setToolTip(QCoreApplication.translate("Form", u"Xem LinkedIn", None))
#endif // QT_CONFIG(tooltip)
        self.btnLinkedin2.setText("")
        self.btnLinkedin2.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnLinkedin2.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.linkedin", None))
        self.btnLinkedin2.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.btnLinkedin2.setProperty(u"url", QCoreApplication.translate("Form", u"https://linkedin.com/in/letrankhang", None))
#if QT_CONFIG(tooltip)
        self.btnEmail2.setToolTip(QCoreApplication.translate("Form", u"G\u1eedi email", None))
#endif // QT_CONFIG(tooltip)
        self.btnEmail2.setText("")
        self.btnEmail2.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnEmail2.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.envelope", None))
        self.btnEmail2.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#64748b", None))
        self.btnEmail2.setProperty(u"email", QCoreApplication.translate("Form", u"user2@gmail.com", None))
        self.teamDivider2.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.memberRow3.setProperty(u"class", QCoreApplication.translate("Form", u"memberRow", None))
        self.avatarMember3.setText("")
        self.avatarMember3.setProperty(u"class", QCoreApplication.translate("Form", u"avatar", None))
        self.avatarMember3.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.user", None))
        self.avatarMember3.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#94a3b8", None))
        self.nameMember3.setText(QCoreApplication.translate("Form", u"L\u00ea H\u1ed3ng G\u1ea5m", None))
        self.nameMember3.setProperty(u"class", QCoreApplication.translate("Form", u"memberName", None))
        self.roleMember3.setText(QCoreApplication.translate("Form", u"Th\u00e0nh vi\u00ean s\u00e1ng l\u1eadp", None))
        self.roleMember3.setProperty(u"class", QCoreApplication.translate("Form", u"memberRole", None))
        self.descMember3.setText(QCoreApplication.translate("Form", u"Contact:", None))
        self.descMember3.setProperty(u"class", QCoreApplication.translate("Form", u"memberDesc", None))
#if QT_CONFIG(tooltip)
        self.btnGithub3.setToolTip(QCoreApplication.translate("Form", u"Xem GitHub", None))
#endif // QT_CONFIG(tooltip)
        self.btnGithub3.setText("")
        self.btnGithub3.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnGithub3.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.github", None))
        self.btnGithub3.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#0f172a", None))
        self.btnGithub3.setProperty(u"url", QCoreApplication.translate("Form", u"https://github.com/honggam26", None))
#if QT_CONFIG(tooltip)
        self.btnLinkedin3.setToolTip(QCoreApplication.translate("Form", u"Xem LinkedIn", None))
#endif // QT_CONFIG(tooltip)
        self.btnLinkedin3.setText("")
        self.btnLinkedin3.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnLinkedin3.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.linkedin", None))
        self.btnLinkedin3.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.btnLinkedin3.setProperty(u"url", QCoreApplication.translate("Form", u"https://linkedin.com/in/lehgam", None))
#if QT_CONFIG(tooltip)
        self.btnEmail3.setToolTip(QCoreApplication.translate("Form", u"G\u1eedi email", None))
#endif // QT_CONFIG(tooltip)
        self.btnEmail3.setText("")
        self.btnEmail3.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnEmail3.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.envelope", None))
        self.btnEmail3.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#64748b", None))
        self.btnEmail3.setProperty(u"email", QCoreApplication.translate("Form", u"user3@gmail.com", None))
        self.teamDivider3.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.memberRow4.setProperty(u"class", QCoreApplication.translate("Form", u"memberRow", None))
        self.avatarMember4.setText("")
        self.avatarMember4.setProperty(u"class", QCoreApplication.translate("Form", u"avatar", None))
        self.avatarMember4.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.user", None))
        self.avatarMember4.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#94a3b8", None))
        self.nameMember4.setText(QCoreApplication.translate("Form", u"Phan Tu\u1ea5n Kha", None))
        self.nameMember4.setProperty(u"class", QCoreApplication.translate("Form", u"memberName", None))
        self.roleMember4.setText(QCoreApplication.translate("Form", u"Th\u00e0nh vi\u00ean s\u00e1ng l\u1eadp", None))
        self.roleMember4.setProperty(u"class", QCoreApplication.translate("Form", u"memberRole", None))
        self.descMember4.setText(QCoreApplication.translate("Form", u"Contact:", None))
        self.descMember4.setProperty(u"class", QCoreApplication.translate("Form", u"memberDesc", None))
#if QT_CONFIG(tooltip)
        self.btnGithub4.setToolTip(QCoreApplication.translate("Form", u"Xem GitHub", None))
#endif // QT_CONFIG(tooltip)
        self.btnGithub4.setText("")
        self.btnGithub4.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnGithub4.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.github", None))
        self.btnGithub4.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#0f172a", None))
        self.btnGithub4.setProperty(u"url", QCoreApplication.translate("Form", u"https://github.com/Tuan-Kem", None))
#if QT_CONFIG(tooltip)
        self.btnLinkedin4.setToolTip(QCoreApplication.translate("Form", u"Xem LinkedIn", None))
#endif // QT_CONFIG(tooltip)
        self.btnLinkedin4.setText("")
        self.btnLinkedin4.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnLinkedin4.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.linkedin", None))
        self.btnLinkedin4.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.btnLinkedin4.setProperty(u"url", QCoreApplication.translate("Form", u"https://linkedin.com/in/tuan-kha-love", None))
#if QT_CONFIG(tooltip)
        self.btnEmail4.setToolTip(QCoreApplication.translate("Form", u"G\u1eedi email", None))
#endif // QT_CONFIG(tooltip)
        self.btnEmail4.setText("")
        self.btnEmail4.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnEmail4.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.envelope", None))
        self.btnEmail4.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#64748b", None))
        self.btnEmail4.setProperty(u"email", QCoreApplication.translate("Form", u"user4@gmail.com", None))
        self.teamDivider4.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.memberRow5.setProperty(u"class", QCoreApplication.translate("Form", u"memberRow", None))
        self.avatarMember5.setText("")
        self.avatarMember5.setProperty(u"class", QCoreApplication.translate("Form", u"avatar", None))
        self.avatarMember5.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.user", None))
        self.avatarMember5.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#94a3b8", None))
        self.nameMember5.setText(QCoreApplication.translate("Form", u"\u0110\u1eb7ng Ho\u00e0ng Qu\u1ed1c C\u01b0\u1eddng", None))
        self.nameMember5.setProperty(u"class", QCoreApplication.translate("Form", u"memberName", None))
        self.roleMember5.setText(QCoreApplication.translate("Form", u"Th\u00e0nh vi\u00ean s\u00e1ng l\u1eadp", None))
        self.roleMember5.setProperty(u"class", QCoreApplication.translate("Form", u"memberRole", None))
        self.descMember5.setText(QCoreApplication.translate("Form", u"Contact:", None))
        self.descMember5.setProperty(u"class", QCoreApplication.translate("Form", u"memberDesc", None))
#if QT_CONFIG(tooltip)
        self.btnGithub5.setToolTip(QCoreApplication.translate("Form", u"Xem GitHub", None))
#endif // QT_CONFIG(tooltip)
        self.btnGithub5.setText("")
        self.btnGithub5.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnGithub5.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.github", None))
        self.btnGithub5.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#0f172a", None))
        self.btnGithub5.setProperty(u"url", QCoreApplication.translate("Form", u"https://github.com/dc1458", None))
#if QT_CONFIG(tooltip)
        self.btnLinkedin5.setToolTip(QCoreApplication.translate("Form", u"Xem LinkedIn", None))
#endif // QT_CONFIG(tooltip)
        self.btnLinkedin5.setText("")
        self.btnLinkedin5.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnLinkedin5.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5b.linkedin", None))
        self.btnLinkedin5.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#2563eb", None))
        self.btnLinkedin5.setProperty(u"url", QCoreApplication.translate("Form", u"https://linkedin.com/in/dcisme", None))
#if QT_CONFIG(tooltip)
        self.btnEmail5.setToolTip(QCoreApplication.translate("Form", u"G\u1eedi email", None))
#endif // QT_CONFIG(tooltip)
        self.btnEmail5.setText("")
        self.btnEmail5.setProperty(u"class", QCoreApplication.translate("Form", u"socialButton", None))
        self.btnEmail5.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.envelope", None))
        self.btnEmail5.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#64748b", None))
        self.btnEmail5.setProperty(u"email", QCoreApplication.translate("Form", u"user5@gmail.com", None))
        self.teamSupportDivider.setProperty(u"class", QCoreApplication.translate("Form", u"divider", None))
        self.supportText.setText(QCoreApplication.translate("Form", u"Kh\u00f4ng t\u00ecm th\u1ea5y c\u00e2u tr\u1ea3 l\u1eddi trong h\u01b0\u1edbng d\u1eabn? G\u1eedi email cho nh\u00f3m ph\u00e1t tri\u1ec3n, ch\u00fang t\u00f4i s\u1ebd ph\u1ea3n h\u1ed3i s\u1edbm nh\u1ea5t.", None))
        self.supportText.setProperty(u"class", QCoreApplication.translate("Form", u"supportText", None))
        self.btnSupportEmail.setText(QCoreApplication.translate("Form", u"G\u1eedi email h\u1ed7 tr\u1ee3", None))
        self.btnSupportEmail.setProperty(u"class", QCoreApplication.translate("Form", u"primaryButton", None))
        self.btnSupportEmail.setProperty(u"iconName", QCoreApplication.translate("Form", u"fa5s.paper-plane", None))
        self.btnSupportEmail.setProperty(u"iconColor", QCoreApplication.translate("Form", u"#ffffff", None))
        self.btnSupportEmail.setProperty(u"email", QCoreApplication.translate("Form", u"thaikiet519@gmail.com", None))
    # retranslateUi

