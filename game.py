# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programme\Schule\4AHITM\SEW\Projects\SimpleGame\game.ui'
#
# Created: Mon Nov 28 15:35:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

"""
@author: TEKIN Abdurrahim Burak
@date: 2016-11-27
-- Simple game with threads! --
"""

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    """
    converting -> game.ui to game.py
    """
    def setupUi(self, MainWindow):
        """
        Gui-configuration game.py
        :param MainWindow:
        :return:
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(210, 40, 581, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_15 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 1, 4, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 4, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 0, 3, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(209, 369, 581, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_16 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout.addWidget(self.pushButton_17)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 101, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 40, 101, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        retranslate game.py
        :param MainWindow:
        :return:
        """
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("MainWindow", "Neues Spiel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Offen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Richtig", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Falsch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Gesamt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Spiel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))

