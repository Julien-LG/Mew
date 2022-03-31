# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mewqVGNms.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(403, 200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 110, 71, 71))
        self.label.setPixmap(QPixmap(u"../logo.png"))
        self.label.setScaledContents(True)
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(310, 150, 75, 23))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(270, 10, 111, 91))
        self.text_log = QTextEdit(self.centralwidget)
        self.text_log.setObjectName(u"text_log")
        self.text_log.setGeometry(QRect(10, 10, 251, 91))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 150, 61, 21))
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(220, 150, 75, 23))
        self.btn_start.setContextMenuPolicy(Qt.NoContextMenu)
        self.btn_start.setCheckable(False)
        self.btn_start.setAutoDefault(False)
        self.btn_start.setFlat(False)
        self.btn_test = QPushButton(self.centralwidget)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setGeometry(QRect(310, 110, 75, 23))
        self.spinBox_minutes = QSpinBox(self.centralwidget)
        self.spinBox_minutes.setObjectName(u"spinBox_minutes")
        self.spinBox_minutes.setGeometry(QRect(150, 150, 42, 22))
        self.btn_calib = QPushButton(self.centralwidget)
        self.btn_calib.setObjectName(u"btn_calib")
        self.btn_calib.setGeometry(QRect(220, 110, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_start.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nb minutes", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"Test position", None))
        self.btn_calib.setText(QCoreApplication.translate("MainWindow", u"Calibrage", None))
    # retranslateUi

