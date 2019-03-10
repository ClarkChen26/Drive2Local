# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Setting.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_Setting(object):
    def open_dir(self):
        # select an exiting directory from local drive
        filepath = QFileDialog.getExistingDirectory(None, "select Directory")
        print(filepath)
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(566, 382)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(Setting)
        self.buttonBox_2.setGeometry(QtCore.QRect(200, 300, 171, 41))
        self.buttonBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.label = QtWidgets.QLabel(Setting)
        self.label.setGeometry(QtCore.QRect(50, 240, 151, 21))
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.label_BackupDir = QtWidgets.QLabel(Setting)
        self.label_BackupDir.setGeometry(QtCore.QRect(40, 20, 120, 20))
        self.label_BackupDir.setAutoFillBackground(False)
        self.label_BackupDir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_BackupDir.setObjectName("label_BackupDir")
        self.pushButton_3 = QtWidgets.QPushButton(Setting)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 340, 113, 32))
        self.pushButton_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(Setting)
        self.checkBox.setGeometry(QtCore.QRect(200, 170, 141, 21))
        self.checkBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox.setObjectName("checkBox")
        self.Button_BackupDir = QtWidgets.QPushButton(Setting)
        self.Button_BackupDir.setGeometry(QtCore.QRect(150, 20, 120, 31))
        self.Button_BackupDir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Button_BackupDir.setObjectName("Button_BackupDir")
        self.Button_BackupDir.clicked.connect(self.open_dir)
        self.check_Trash = QtWidgets.QCheckBox(Setting)
        self.check_Trash.setGeometry(QtCore.QRect(310, 90, 151, 21))
        self.check_Trash.setObjectName("check_Trash")
        self.timeEdit = QtWidgets.QTimeEdit(Setting)
        self.timeEdit.setGeometry(QtCore.QRect(200, 240, 118, 24))
        self.timeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit.setObjectName("timeEdit")
        self.spinBox = QtWidgets.QSpinBox(Setting)
        self.spinBox.setGeometry(QtCore.QRect(170, 200, 48, 21))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Setting)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 121, 21))
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Setting)
        self.label_5.setGeometry(QtCore.QRect(220, 200, 61, 21))
        self.label_5.setObjectName("label_5")
        self.label_LogDir = QtWidgets.QLabel(Setting)
        self.label_LogDir.setGeometry(QtCore.QRect(280, 20, 120, 20))
        self.label_LogDir.setAutoFillBackground(False)
        self.label_LogDir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_LogDir.setObjectName("label_LogDir")
        self.Button_LogDir = QtWidgets.QPushButton(Setting)
        self.Button_LogDir.setGeometry(QtCore.QRect(420, 20, 113, 32))
        self.Button_LogDir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Button_LogDir.setObjectName("Button_LogDir")
        self.Button_LogDir.clicked.connect(self.open_dir)
        self.check_Only = QtWidgets.QCheckBox(Setting)
        self.check_Only.setGeometry(QtCore.QRect(310, 60, 191, 21))
        self.check_Only.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.check_Only.setObjectName("check_Only")
        self.label_7 = QtWidgets.QLabel(Setting)
        self.label_7.setGeometry(QtCore.QRect(50, 280, 221, 21))
        self.label_7.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_7.setObjectName("label_7")
        self.spinBox_2 = QtWidgets.QSpinBox(Setting)
        self.spinBox_2.setGeometry(QtCore.QRect(270, 280, 48, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(Setting)
        self.checkBox_4.setGeometry(QtCore.QRect(330, 280, 181, 21))
        self.checkBox_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox_4.setObjectName("checkBox_4")
        self.check_ft1 = QtWidgets.QCheckBox(Setting)
        self.check_ft1.setGeometry(QtCore.QRect(40, 90, 51, 20))
        self.check_ft1.setObjectName("check_ft1")
        self.check_ft2 = QtWidgets.QCheckBox(Setting)
        self.check_ft2.setGeometry(QtCore.QRect(90, 90, 51, 20))
        self.check_ft2.setObjectName("check_ft2")
        self.checkBox_7 = QtWidgets.QCheckBox(Setting)
        self.checkBox_7.setGeometry(QtCore.QRect(40, 110, 87, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Setting)
        self.checkBox_8.setGeometry(QtCore.QRect(90, 110, 87, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Setting)
        self.checkBox_9.setGeometry(QtCore.QRect(150, 90, 87, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Setting)
        self.checkBox_10.setGeometry(QtCore.QRect(200, 90, 87, 20))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(Setting)
        self.checkBox_11.setGeometry(QtCore.QRect(150, 110, 111, 20))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(Setting)
        self.checkBox_12.setGeometry(QtCore.QRect(200, 110, 81, 21))
        self.checkBox_12.setObjectName("checkBox_12")
        self.line = QtWidgets.QFrame(Setting)
        self.line.setGeometry(QtCore.QRect(40, 150, 511, 16))
        self.line.setStyleSheet("")
        self.line.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.check_Based = QtWidgets.QCheckBox(Setting)
        self.check_Based.setGeometry(QtCore.QRect(40, 60, 221, 21))
        self.check_Based.setObjectName("check_Based")
        self.line_2 = QtWidgets.QFrame(Setting)
        self.line_2.setGeometry(QtCore.QRect(270, 60, 20, 81))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Dialog"))
        self.label.setText(_translate("Setting", "Automatic Backup Time "))
        self.label_BackupDir.setText(_translate("Setting", "Backup Directory"))
        self.pushButton_3.setText(_translate("Setting", "Back to Menu"))
        self.checkBox.setText(_translate("Setting", "Automatic Backup"))
        self.Button_BackupDir.setText(_translate("Setting", "Select"))
        self.check_Trash.setText(_translate("Setting", "Backup Trash Folder"))
        self.label_2.setText(_translate("Setting", "Backup Frequency"))
        self.label_5.setText(_translate("Setting", "Day"))
        self.label_LogDir.setText(_translate("Setting", "Backup Log Directory"))
        self.Button_LogDir.setText(_translate("Setting", "Select"))
        self.check_Only.setText(_translate("Setting", "Only Backup Files You Own"))
        self.label_7.setText(_translate("Setting", "The Number of Backups to Maintain"))
        self.checkBox_4.setText(_translate("Setting", "Automatic Delete Backup"))
        self.check_ft1.setText(_translate("Setting", "txt"))
        self.check_ft2.setText(_translate("Setting", "pdf"))
        self.checkBox_7.setText(_translate("Setting", "doc"))
        self.checkBox_8.setText(_translate("Setting", "docx"))
        self.checkBox_9.setText(_translate("Setting", "xls"))
        self.checkBox_10.setText(_translate("Setting", "xlsx"))
        self.checkBox_11.setText(_translate("Setting", "ppt"))
        self.checkBox_12.setText(_translate("Setting", "pptx"))
        self.check_Based.setText(_translate("Setting", "Backup Items Based on File Type "))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Setting = QtWidgets.QWidget()
    ui = Ui_Setting()
    ui.setupUi(Setting)
    Setting.show()
    sys.exit(app.exec_())
