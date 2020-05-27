# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoBKInnovation = QtWidgets.QLabel(self.centralwidget)
        self.logoBKInnovation.setGeometry(QtCore.QRect(630, 780, 311, 221))
        self.logoBKInnovation.setText("")
        self.logoBKInnovation.setPixmap(QtGui.QPixmap(":/logoBKInnovation/BK-Innovation-official Logo.png"))
        self.logoBKInnovation.setScaledContents(True)
        self.logoBKInnovation.setObjectName("logoBKInnovation")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(760, 310, 491, 371))
        self.MplWidget.setObjectName("MplWidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(250, 300, 231, 241))
        self.image_label.setObjectName("image_label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 30, 1125, 135))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.logoBK1 = QtWidgets.QLabel(self.widget)
        self.logoBK1.setMaximumSize(QtCore.QSize(100, 100))
        self.logoBK1.setText("")
        self.logoBK1.setPixmap(QtGui.QPixmap(":/logoBK/Logo BK.png"))
        self.logoBK1.setScaledContents(True)
        self.logoBK1.setObjectName("logoBK1")
        self.horizontalLayout_2.addWidget(self.logoBK1)
        self.SystemName = QtWidgets.QLabel(self.widget)
        self.SystemName.setMaximumSize(QtCore.QSize(817, 16777215))
        self.SystemName.setObjectName("SystemName")
        self.horizontalLayout_2.addWidget(self.SystemName)
        self.logoBK2 = QtWidgets.QLabel(self.widget)
        self.logoBK2.setMaximumSize(QtCore.QSize(100, 100))
        self.logoBK2.setText("")
        self.logoBK2.setPixmap(QtGui.QPixmap(":/logoBK/Logo BK.png"))
        self.logoBK2.setScaledContents(True)
        self.logoBK2.setObjectName("logoBK2")
        self.horizontalLayout_2.addWidget(self.logoBK2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.teamName = QtWidgets.QLabel(self.widget)
        self.teamName.setAlignment(QtCore.Qt.AlignCenter)
        self.teamName.setObjectName("teamName")
        self.verticalLayout_2.addWidget(self.teamName)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EVALUATION SYSTEM OF STUDENT\'S CONCENTRATION"))
        self.image_label.setText(_translate("MainWindow", "TextLabel"))
        self.SystemName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">EVALUATION SYSTEM OF STUDENT\'S CONCENTRATION</span></p></body></html>"))
        self.teamName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">TEAM ELECTRIC</span></p></body></html>"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
from mplwidget import MplWidget
import logo_rc
