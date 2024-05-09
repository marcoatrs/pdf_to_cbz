# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Pdf2Cbz(object):
    def setupUi(self, Pdf2Cbz):
        if not Pdf2Cbz.objectName():
            Pdf2Cbz.setObjectName(u"Pdf2Cbz")
        Pdf2Cbz.resize(1019, 555)
        self.centralwidget = QWidget(Pdf2Cbz)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_conversion = QTableWidget(self.frame)
        if (self.table_conversion.columnCount() < 3):
            self.table_conversion.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_conversion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_conversion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_conversion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_conversion.setObjectName(u"table_conversion")
        self.table_conversion.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_conversion.horizontalHeader().setMinimumSectionSize(50)
        self.table_conversion.horizontalHeader().setDefaultSectionSize(300)
        self.table_conversion.horizontalHeader().setStretchLastSection(False)
        self.table_conversion.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.table_conversion, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_add_file = QPushButton(self.frame)
        self.pb_add_file.setObjectName(u"pb_add_file")
        self.pb_add_file.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pb_add_file)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pb_create = QPushButton(self.frame)
        self.pb_create.setObjectName(u"pb_create")
        self.pb_create.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pb_create)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.gridLayout_3.setRowStretch(1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Pdf2Cbz.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pdf2Cbz)

        QMetaObject.connectSlotsByName(Pdf2Cbz)
    # setupUi

    def retranslateUi(self, Pdf2Cbz):
        Pdf2Cbz.setWindowTitle(QCoreApplication.translate("Pdf2Cbz", u"Pdf 2 Cbz", None))
        ___qtablewidgetitem = self.table_conversion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Pdf2Cbz", u"Title", None));
        ___qtablewidgetitem1 = self.table_conversion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Pdf2Cbz", u"Conversion status", None));
        ___qtablewidgetitem2 = self.table_conversion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Pdf2Cbz", u"Open in folder", None));
        self.pb_add_file.setText(QCoreApplication.translate("Pdf2Cbz", u"+ Add Files", None))
        self.pb_create.setText(QCoreApplication.translate("Pdf2Cbz", u"Create cbz", None))
    # retranslateUi

