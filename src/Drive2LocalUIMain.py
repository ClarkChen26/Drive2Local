#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Drive2LocalUISetting import Ui_Setting
import Drive2Local

class Ui_Main(object):
    def openSetting(self):
        # link to Uisetting
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Setting()
        self.ui.setupUi(self.window)
        self.window.show()

    def StartMainFunction(self):
        # run main program
        Drive2Local.main()
        
    def setupUi(self, Main):
        # initial the value for canvas
        Main.setObjectName("Main")
        Main.resize(610, 383)

        # back button
        self.Backup_Button = QtWidgets.QPushButton(Main)
        self.Backup_Button.setGeometry(QtCore.QRect(240, 190, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Backup_Button.setFont(font)
        self.Backup_Button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Backup_Button.setObjectName("Backup_Button")
        self.Backup_Button.clicked.connect(self.StartMainFunction)

        # setting button
        self.Setting_Button = QtWidgets.QPushButton(Main)
        self.Setting_Button.setGeometry(QtCore.QRect(240, 250, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Setting_Button.setFont(font)
        self.Setting_Button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Setting_Button.setObjectName("Setting_Button")
        self.Setting_Button.clicked.connect(self.openSetting)

        # label for drive2local
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(190, 40, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(41)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Setting_Button.raise_()
        self.Backup_Button.raise_()
        self.label.raise_()

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Dialog"))
        self.Backup_Button.setText(_translate("Main", "Backup"))
        self.Setting_Button.setText(_translate("Main", "Settings"))
        self.label.setText(_translate("Main", "Drive2Local"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

