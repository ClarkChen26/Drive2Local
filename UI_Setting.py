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
    # initial global value for text browser display
    global backup_dir, log_dir
    backup_dir = "Choose the Directory to Store Backups"
    log_dir = "Choose the Directory to Store Backup Logs"
    def open_backup_dir(self):
        # choose an existing directory from users local drive as the dirctory to store the backups
        backup_dir = QFileDialog.getExistingDirectory(None, "select directory")
        self.textBrowser_backup.setText(backup_dir)
    def open_log_dir(self):
        # choose an existing directory from users local drive as the dirctory to store the backup logs
        log_dir = QFileDialog.getExistingDirectory(None, "select directory")
        self.textBrowser_log.setText(log_dir)
    def setupUi(self, Setting):
        # canvas size
        Setting.setObjectName("Setting")
        Setting.resize(580, 430)
        # backup time label
        self.label_backup_time = QtWidgets.QLabel(Setting)
        self.label_backup_time.setGeometry(QtCore.QRect(50, 270, 151, 21))
        self.label_backup_time.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_backup_time.setObjectName("label_backup_time")

        # backup dirctory label
        self.label_backup_dir = QtWidgets.QLabel(Setting)
        self.label_backup_dir.setGeometry(QtCore.QRect(40, 10, 120, 20))
        self.label_backup_dir.setAutoFillBackground(False)
        self.label_backup_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_backup_dir.setObjectName("label_backup_dir")

        # button back to menu
        self.pushButton_back_to_menu = QtWidgets.QPushButton(Setting)
        self.pushButton_back_to_menu.setGeometry(QtCore.QRect(220, 390, 113, 32))
        self.pushButton_back_to_menu.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_back_to_menu.setObjectName("pushButton_back_to_menu")

        # checkbox auto backup
        self.checkBox_auto_backup = QtWidgets.QCheckBox(Setting)
        self.checkBox_auto_backup.setGeometry(QtCore.QRect(210, 200, 141, 21))
        self.checkBox_auto_backup.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox_auto_backup.setObjectName("checkBox_auto_backup")

        # button select the backup directory
        self.Button_backup_dir = QtWidgets.QPushButton(Setting)
        self.Button_backup_dir.setGeometry(QtCore.QRect(150, 10, 120, 31))
        self.Button_backup_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Button_backup_dir.setObjectName("Button_backup_dir")

        # checkbox back up trash folder
        self.checkBox_trash = QtWidgets.QCheckBox(Setting)
        self.checkBox_trash.setGeometry(QtCore.QRect(310, 140, 151, 21))
        self.checkBox_trash.setObjectName("checkBox_trash")

        # time for auto back up
        self.timeEdit = QtWidgets.QTimeEdit(Setting)
        self.timeEdit.setGeometry(QtCore.QRect(200, 270, 118, 24))
        self.timeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit.setObjectName("timeEdit")

        # spinbox back up frequency
        self.spinBox_frequency = QtWidgets.QSpinBox(Setting)
        self.spinBox_frequency.setGeometry(QtCore.QRect(170, 230, 48, 21))
        self.spinBox_frequency.setObjectName("spinBox_frequency")

        # label back up frequency
        self.label_backup_frequency = QtWidgets.QLabel(Setting)
        self.label_backup_frequency.setGeometry(QtCore.QRect(50, 230, 121, 21))
        self.label_backup_frequency.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_backup_frequency.setObjectName("label_backup_frequency")

        # label back up frequency days
        self.label_frequency_day = QtWidgets.QLabel(Setting)
        self.label_frequency_day.setGeometry(QtCore.QRect(220, 230, 61, 21))
        self.label_frequency_day.setObjectName("label_frequency_day")

        # label back up log directory
        self.label_log_dir = QtWidgets.QLabel(Setting)
        self.label_log_dir.setGeometry(QtCore.QRect(290, 10, 120, 20))
        self.label_log_dir.setAutoFillBackground(False)
        self.label_log_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_log_dir.setObjectName("label_log_dir")

        # button select the backup log directory
        self.Button_log_dir = QtWidgets.QPushButton(Setting)
        self.Button_log_dir.setGeometry(QtCore.QRect(430, 10, 113, 32))
        self.Button_log_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Button_log_dir.setObjectName("Button_log_dir")

        # checkbox only back up your own file
        self.checkBox_own_fIle = QtWidgets.QCheckBox(Setting)
        self.checkBox_own_fIle.setGeometry(QtCore.QRect(310, 100, 191, 21))
        self.checkBox_own_fIle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox_own_fIle.setObjectName("checkBox_own_fIle")

        # label the number of backups to maintain
        self.label_backup_numbers = QtWidgets.QLabel(Setting)
        self.label_backup_numbers.setGeometry(QtCore.QRect(50, 310, 221, 21))
        self.label_backup_numbers.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_backup_numbers.setObjectName("label_backup_numbers")

        # spinbox backup numbers
        self.spinBox_backup_numbers = QtWidgets.QSpinBox(Setting)
        self.spinBox_backup_numbers.setGeometry(QtCore.QRect(270, 310, 48, 21))
        self.spinBox_backup_numbers.setObjectName("spinBox_backup_numbers")
        self.checkBox_auto_delete = QtWidgets.QCheckBox(Setting)
        self.checkBox_auto_delete.setGeometry(QtCore.QRect(330, 310, 181, 21))
        self.checkBox_auto_delete.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox_auto_delete.setObjectName("checkBox_auto_delete")
        self.check_txt = QtWidgets.QCheckBox(Setting)
        self.check_txt.setGeometry(QtCore.QRect(40, 120, 51, 20))
        self.check_txt.setObjectName("check_txt")
        self.check_pdf = QtWidgets.QCheckBox(Setting)
        self.check_pdf.setGeometry(QtCore.QRect(90, 120, 51, 20))
        self.check_pdf.setObjectName("check_pdf")
        self.checkBox_doc = QtWidgets.QCheckBox(Setting)
        self.checkBox_doc.setGeometry(QtCore.QRect(40, 140, 51, 20))
        self.checkBox_doc.setObjectName("checkBox_doc")
        self.checkBox_docx = QtWidgets.QCheckBox(Setting)
        self.checkBox_docx.setGeometry(QtCore.QRect(90, 140, 61, 20))
        self.checkBox_docx.setObjectName("checkBox_docx")
        self.checkBox_xls = QtWidgets.QCheckBox(Setting)
        self.checkBox_xls.setGeometry(QtCore.QRect(150, 120, 41, 20))
        self.checkBox_xls.setObjectName("checkBox_xls")
        self.checkBox_xlsx = QtWidgets.QCheckBox(Setting)
        self.checkBox_xlsx.setGeometry(QtCore.QRect(200, 120, 51, 20))
        self.checkBox_xlsx.setObjectName("checkBox_xlsx")
        self.checkBox_ppt = QtWidgets.QCheckBox(Setting)
        self.checkBox_ppt.setGeometry(QtCore.QRect(150, 140, 51, 20))
        self.checkBox_ppt.setObjectName("checkBox_ppt")
        self.checkBox_pptx = QtWidgets.QCheckBox(Setting)
        self.checkBox_pptx.setGeometry(QtCore.QRect(200, 140, 51, 21))
        self.checkBox_pptx.setObjectName("checkBox_pptx")
        self.Horizontal_line = QtWidgets.QFrame(Setting)
        self.Horizontal_line.setGeometry(QtCore.QRect(40, 180, 511, 16))
        self.Horizontal_line.setStyleSheet("")
        self.Horizontal_line.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_line.setObjectName("Horizontal_line")
        self.checkBox_file_type = QtWidgets.QCheckBox(Setting)
        self.checkBox_file_type.setGeometry(QtCore.QRect(40, 90, 221, 21))
        self.checkBox_file_type.setObjectName("checkBox_file_type")
        self.Vertical_line = QtWidgets.QFrame(Setting)
        self.Vertical_line.setGeometry(QtCore.QRect(270, 90, 20, 81))
        self.Vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.Vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Vertical_line.setObjectName("Vertical_line")
        self.textBrowser_backup = QtWidgets.QTextBrowser(Setting)
        self.textBrowser_backup.setGeometry(QtCore.QRect(40, 40, 221, 41))
        self.textBrowser_backup.setObjectName("textBrowser_backup")
        self.textBrowser_log = QtWidgets.QTextBrowser(Setting)
        self.textBrowser_log.setGeometry(QtCore.QRect(290, 40, 221, 41))
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.pushButton_apply = QtWidgets.QPushButton(Setting)
        self.pushButton_apply.setGeometry(QtCore.QRect(140, 360, 111, 32))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.pushButton_cancel = QtWidgets.QPushButton(Setting)
        self.pushButton_cancel.setGeometry(QtCore.QRect(310, 360, 111, 32))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.Horizontal_line_2 = QtWidgets.QFrame(Setting)
        self.Horizontal_line_2.setGeometry(QtCore.QRect(40, 340, 511, 16))
        self.Horizontal_line_2.setStyleSheet("")
        self.Horizontal_line_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Horizontal_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizontal_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizontal_line_2.setObjectName("Horizontal_line_2")

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Dialog"))
        self.label_backup_time.setText(_translate("Setting", "Automatic Backup Time "))
        self.label_backup_dir.setText(_translate("Setting", "Backup Directory"))
        self.pushButton_back_to_menu.setText(_translate("Setting", "Back to Menu"))
        self.checkBox_auto_backup.setText(_translate("Setting", "Automatic Backup"))
        self.Button_backup_dir.setText(_translate("Setting", "Select"))
        self.checkBox_trash.setText(_translate("Setting", "Backup Trash Folder"))
        self.label_backup_frequency.setText(_translate("Setting", "Backup Frequency"))
        self.label_frequency_day.setText(_translate("Setting", "Day"))
        self.label_log_dir.setText(_translate("Setting", "Backup Log Directory"))
        self.Button_log_dir.setText(_translate("Setting", "Select"))
        self.checkBox_own_fIle.setText(_translate("Setting", "Only Backup Files You Own"))
        self.label_backup_numbers.setText(_translate("Setting", "The Number of Backups to Maintain"))
        self.checkBox_auto_delete.setText(_translate("Setting", "Automatic Delete Backup"))
        self.check_txt.setText(_translate("Setting", "txt"))
        self.check_pdf.setText(_translate("Setting", "pdf"))
        self.checkBox_doc.setText(_translate("Setting", "doc"))
        self.checkBox_docx.setText(_translate("Setting", "docx"))
        self.checkBox_xls.setText(_translate("Setting", "xls"))
        self.checkBox_xlsx.setText(_translate("Setting", "xlsx"))
        self.checkBox_ppt.setText(_translate("Setting", "ppt"))
        self.checkBox_pptx.setText(_translate("Setting", "pptx"))
        self.checkBox_file_type.setText(_translate("Setting", "Backup Items Based on File Type "))
        self.pushButton_apply.setText(_translate("Setting", "Apply"))
        self.pushButton_cancel.setText(_translate("Setting", "Cancel"))
        self.textBrowser_backup.setText(_translate("Setting", backup_dir))
        self.textBrowser_log.setText(_translate("Setting", log_dir))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Setting = QtWidgets.QWidget()
    ui = Ui_Setting()
    ui.setupUi(Setting)
    Setting.show()
    sys.exit(app.exec_())
