# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1178, 806)
        MainWindow.setStyleSheet(u"border-color: rgb(0, 85, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.list_table = QTableWidget(self.centralwidget)
        if (self.list_table.columnCount() < 7):
            self.list_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.list_table.setObjectName(u"list_table")
        self.list_table.setGeometry(QRect(70, 110, 1041, 581))
        self.open_btn = QPushButton(self.centralwidget)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setGeometry(QRect(520, 70, 101, 31))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515"])
        self.open_btn.setFont(font)
        self.excel_edit = QLineEdit(self.centralwidget)
        self.excel_edit.setObjectName(u"excel_edit")
        self.excel_edit.setGeometry(QRect(70, 70, 441, 31))
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(70, 710, 1011, 16))
        self.progress_bar.setValue(24)
        self.pdf_btn = QPushButton(self.centralwidget)
        self.pdf_btn.setObjectName(u"pdf_btn")
        self.pdf_btn.setGeometry(QRect(1020, 70, 91, 30))
        self.split_excel_btn = QPushButton(self.centralwidget)
        self.split_excel_btn.setObjectName(u"split_excel_btn")
        self.split_excel_btn.setGeometry(QRect(910, 70, 101, 30))
        self.open_tobe_btn = QPushButton(self.centralwidget)
        self.open_tobe_btn.setObjectName(u"open_tobe_btn")
        self.open_tobe_btn.setGeometry(QRect(630, 70, 101, 31))
        self.cal_price_btn = QPushButton(self.centralwidget)
        self.cal_price_btn.setObjectName(u"cal_price_btn")
        self.cal_price_btn.setGeometry(QRect(790, 70, 111, 31))
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(70, 20, 301, 41))
        font1 = QFont()
        font1.setPointSize(28)
        self.title.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1178, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ud55c\uae00\uc774\ub984", None));
        ___qtablewidgetitem1 = self.list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc601\ubb38\uc774\ub984", None));
        ___qtablewidgetitem2 = self.list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\ubc1c\uc77c", None));
        ___qtablewidgetitem3 = self.list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\ub3c4\ucc29\uc77c", None));
        ___qtablewidgetitem4 = self.list_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubbfc\ub4f1\ub85d\ubc88\ud638", None));
        ___qtablewidgetitem5 = self.list_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\uc5ec\ud589\uc0c1\ud488", None));
        ___qtablewidgetitem6 = self.list_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\ubcf4\ud5d8\ub8cc", None));
        self.open_btn.setText(QCoreApplication.translate("MainWindow", u"\uc6d0\ubcf8 \uc5f4\uae30", None))
        self.pdf_btn.setText(QCoreApplication.translate("MainWindow", u"PDF \uc0dd\uc131", None))
        self.split_excel_btn.setText(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140 \uc0dd\uc131", None))
        self.open_tobe_btn.setText(QCoreApplication.translate("MainWindow", u"\uac00\uacf5 \uc5f4\uae30", None))
        self.cal_price_btn.setText(QCoreApplication.translate("MainWindow", u"\ubcf4\ud5d8\ub8cc \uacc4\uc0b0", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\ud5c8\ub2c8\ubb38\ub9ac\uc870\ud2b8", None))
    # retranslateUi

