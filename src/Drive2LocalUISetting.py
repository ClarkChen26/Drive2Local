# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Setting.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
#import Drive2LocalConfig as config

class Ui_Setting(object):
	# initial global value for text browser display
	#global backup_dir, log_dir
	def __init__(self):
		self.backup_dir = "Choose the Directory to Store Backups"
		self.log_dir = "Choose the Directory to Store Backup Logs"
		self.message = ""
	
	def open_backup_dir(self):
		# choose an existing directory from users local drive as the dirctory to store the backups
		self.backup_dir = QFileDialog.getExistingDirectory(None, "select directory")
		self.textBrowser_backup.setText(self.backup_dir)
		
	def open_log_dir(self):
		# choose an existing directory from users local drive as the dirctory to store the backup logs
		self.log_dir = QFileDialog.getExistingDirectory(None, "select directory")
		self.textBrowser_log.setText(self.log_dir)
		
	def setupUi(self, Setting):
		# canvas size
		Setting.setObjectName("Setting")
		Setting.resize(580, 430)

		# ################
		# #	Labels	#
		# ################
		# label backup time

		self.label_backup_time = QtWidgets.QLabel(Setting)
		self.label_backup_time.setGeometry(QtCore.QRect(50, 270, 151, 21))
		self.label_backup_time.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.label_backup_time.setObjectName("label_backup_time")
		# label backup dirctory 
		self.label_backup_dir = QtWidgets.QLabel(Setting)
		self.label_backup_dir.setGeometry(QtCore.QRect(40, 10, 120, 20))
		self.label_backup_dir.setAutoFillBackground(False)
		self.label_backup_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.label_backup_dir.setObjectName("label_backup_dir")
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
		self.label_log_dir.setGeometry(QtCore.QRect(290, 10, 130, 20))
		self.label_log_dir.setAutoFillBackground(False)
		self.label_log_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.label_log_dir.setObjectName("label_log_dir")
		# label the number of backups to maintain
		self.label_backup_numbers = QtWidgets.QLabel(Setting)
		self.label_backup_numbers.setGeometry(QtCore.QRect(50, 310, 221, 21))
		self.label_backup_numbers.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.label_backup_numbers.setObjectName("label_backup_numbers")

		# lable the change save message
		self.label_commit_message = QtWidgets.QLabel(Setting)
		self.label_commit_message.setGeometry(QtCore.QRect(190, 390, 191, 20))
		self.label_commit_message.setObjectName("label_commit_message")

		# #################
		# #	Buttons	#
		# #################
		# button select the backup directory
		self.Button_backup_dir = QtWidgets.QPushButton(Setting)
		self.Button_backup_dir.setGeometry(QtCore.QRect(150, 10, 120, 31))
		self.Button_backup_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.Button_backup_dir.setObjectName("Button_backup_dir")
		# call open_backup_dir function to update the value of backup_dir
		self.Button_backup_dir.clicked.connect(self.open_backup_dir)
		# button select the backup log directory
		self.Button_log_dir = QtWidgets.QPushButton(Setting)
		self.Button_log_dir.setGeometry(QtCore.QRect(430, 10, 113, 32))
		self.Button_log_dir.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.Button_log_dir.setObjectName("Button_log_dir")
		# call open_log_dir function to update the value of log_dir
		self.Button_log_dir.clicked.connect(self.open_log_dir)
		# button apply
		self.pushButton_apply = QtWidgets.QPushButton(Setting)
		self.pushButton_apply.setObjectName("pushButton_apply")
		self.pushButton_apply.setGeometry(QtCore.QRect(230, 360, 111, 32))


		# ###################
		# #	CheckBoxs	#
		# ###################
		# checkbox backup items based on file type
		self.checkBox_file_type = QtWidgets.QCheckBox(Setting)
		self.checkBox_file_type.setGeometry(QtCore.QRect(40, 90, 221, 21))
		self.checkBox_file_type.setObjectName("checkBox_file_type")
		# checkbox back up trash folder
		self.checkBox_trash = QtWidgets.QCheckBox(Setting)
		self.checkBox_trash.setGeometry(QtCore.QRect(310, 140, 151, 21))
		self.checkBox_trash.setObjectName("checkBox_trash")
		# checkbox auto backup
		self.checkBox_auto_backup = QtWidgets.QCheckBox(Setting)
		self.checkBox_auto_backup.setGeometry(QtCore.QRect(210, 200, 141, 21))
		self.checkBox_auto_backup.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.checkBox_auto_backup.setObjectName("checkBox_auto_backup")
		# checkbox only back up your own file
		self.checkBox_own_file = QtWidgets.QCheckBox(Setting)
		self.checkBox_own_file.setGeometry(QtCore.QRect(310, 100, 191, 21))
		self.checkBox_own_file.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.checkBox_own_file.setObjectName("checkBox_own_fIle")
		# checkbox auto delete backups
		self.checkBox_auto_delete = QtWidgets.QCheckBox(Setting)
		self.checkBox_auto_delete.setGeometry(QtCore.QRect(330, 310, 181, 21))
		self.checkBox_auto_delete.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.checkBox_auto_delete.setObjectName("checkBox_auto_delete")
		# check box txt
		self.checkBox_txt = QtWidgets.QCheckBox(Setting)
		self.checkBox_txt.setGeometry(QtCore.QRect(40, 120, 51, 20))
		self.checkBox_txt.setObjectName("check_txt")
		# check box pdf
		self.checkBox_pdf = QtWidgets.QCheckBox(Setting)
		self.checkBox_pdf.setGeometry(QtCore.QRect(90, 120, 51, 20))
		self.checkBox_pdf.setObjectName("check_pdf")
		# check box doc
		self.checkBox_doc = QtWidgets.QCheckBox(Setting)
		self.checkBox_doc.setGeometry(QtCore.QRect(40, 140, 51, 20))
		self.checkBox_doc.setObjectName("checkBox_doc")
		# check box docx
		self.checkBox_docx = QtWidgets.QCheckBox(Setting)
		self.checkBox_docx.setGeometry(QtCore.QRect(90, 140, 61, 20))
		self.checkBox_docx.setObjectName("checkBox_docx")
		# check box xls
		self.checkBox_xls = QtWidgets.QCheckBox(Setting)
		self.checkBox_xls.setGeometry(QtCore.QRect(150, 120, 41, 20))
		self.checkBox_xls.setObjectName("checkBox_xls")
		# check box xlsx
		self.checkBox_xlsx = QtWidgets.QCheckBox(Setting)
		self.checkBox_xlsx.setGeometry(QtCore.QRect(200, 120, 51, 20))
		self.checkBox_xlsx.setObjectName("checkBox_xlsx")
		# check box ppt
		self.checkBox_ppt = QtWidgets.QCheckBox(Setting)
		self.checkBox_ppt.setGeometry(QtCore.QRect(150, 140, 51, 20))
		self.checkBox_ppt.setObjectName("checkBox_ppt")
		# check box pptx
		self.checkBox_pptx = QtWidgets.QCheckBox(Setting)
		self.checkBox_pptx.setGeometry(QtCore.QRect(200, 140, 51, 21))
		self.checkBox_pptx.setObjectName("checkBox_pptx")

		# ##################
		# #	SpinBoxs	#
		# ##################
		# spinbox backup numbers
		self.spinBox_backup_numbers = QtWidgets.QSpinBox(Setting)
		self.spinBox_backup_numbers.setGeometry(QtCore.QRect(270, 310, 48, 21))
		self.spinBox_backup_numbers.setObjectName("spinBox_backup_numbers")
		self.spinBox_backup_numbers.setMinimum(1)
		# spinbox back up frequency
		self.spinBox_frequency = QtWidgets.QSpinBox(Setting)
		self.spinBox_frequency.setGeometry(QtCore.QRect(170, 230, 48, 21))
		self.spinBox_frequency.setObjectName("spinBox_frequency")
		self.spinBox_frequency.setMinimum(1)

		# ###############
		# #	Lines	#
		# ###############
		# horizon line up
		self.Horizontal_line = QtWidgets.QFrame(Setting)
		self.Horizontal_line.setGeometry(QtCore.QRect(40, 180, 511, 16))
		self.Horizontal_line.setStyleSheet("")
		self.Horizontal_line.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.Horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
		self.Horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.Horizontal_line.setObjectName("Horizontal_line")
		# horizon line bottom
		self.Horizontal_line_2 = QtWidgets.QFrame(Setting)
		self.Horizontal_line_2.setGeometry(QtCore.QRect(40, 340, 511, 16))
		self.Horizontal_line_2.setStyleSheet("")
		self.Horizontal_line_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.Horizontal_line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.Horizontal_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.Horizontal_line_2.setObjectName("Horizontal_line_2")
		# vertical line
		self.Vertical_line = QtWidgets.QFrame(Setting)
		self.Vertical_line.setGeometry(QtCore.QRect(270, 90, 20, 81))
		self.Vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
		self.Vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.Vertical_line.setObjectName("Vertical_line")

		# ######################
		# #	TextBrowsers	#
		# ######################
		# text browser display back up directory
		self.textBrowser_backup = QtWidgets.QTextBrowser(Setting)
		self.textBrowser_backup.setGeometry(QtCore.QRect(40, 40, 221, 41))
		self.textBrowser_backup.setObjectName("textBrowser_backup")
		# text browser display log directory
		self.textBrowser_log = QtWidgets.QTextBrowser(Setting)
		self.textBrowser_log.setGeometry(QtCore.QRect(290, 40, 221, 41))
		self.textBrowser_log.setObjectName("textBrowser_log")

		# time for auto back up
		self.timeEdit = QtWidgets.QTimeEdit(Setting)
		self.timeEdit.setGeometry(QtCore.QRect(200, 270, 118, 24))
		self.timeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.timeEdit.setObjectName("timeEdit")
		self.pushButton_apply.clicked.connect(self.accept)


		self.retranslateUi(Setting)
		QtCore.QMetaObject.connectSlotsByName(Setting)

		if os.path.exists("/tmp/temp_config.txt"):
			file = open("/tmp/temp_config.txt", "r")
			l = file.read().splitlines()

			if l[0] == "True":
				self.checkBox_file_type.setChecked(True)

			if "txt" in l[1]:
				self.checkBox_txt.setChecked(True)
			if "pdf" in l[1]:
				self.checkBox_pdf.setChecked(True)
			if "doc" in l[1]:
				self.checkBox_doc.setChecked(True)
			if "docx" in l[1]:
				self.checkBox_docx.setChecked(True)
			if "xls" in l[1]:
				self.checkBox_xls.setChecked(True)
			if "xlsx" in l[1]:
				self.checkBox_xlsx.setChecked(True)
			if "ppt" in l[1]:
				self.checkBox_ppt.setChecked(True)
			if "pptx" in l[1]:
				self.checkBox_pptx.setChecked(True)

			self.spinBox_frequency.setValue(int(l[5]))

			if l[2] == "True":
				self.checkBox_own_file.setChecked(True)

			if l[3] == "True":
				self.checkBox_trash.setChecked(True)

			time = QtCore.QTime(int(l[6]), int(l[7]), 0, 0)
			self.timeEdit.setTime(time)
			self.spinBox_backup_numbers.setValue(int(l[11]))
			self.textBrowser_backup.setText(l[8])
			self.textBrowser_log.setText(l[9])


	def accept(self):

		QtWidgets.qApp.processEvents()
		self.message = "Your settings have been applied!"
		self.label_commit_message.setStyleSheet("background-color:lightgreen")
		self.label_commit_message.setText(self.message)

		QApplication.processEvents()

		file = open("/tmp/temp_config.txt", 'w')
		#Set filetype_filter
		if self.checkBox_file_type.isChecked():
			file.write("True\n")
			#config.set_filetype_filter(True)
			#print(str(config.filetype_filter))
		else:
			file.write("False\n")
			#config.set_filetype_filter(False)
			#print(str(config.filetype_filter))

		#Set filetypes
		filetypes = []
		if self.checkBox_txt.isChecked():
			filetypes.append('txt')
			#config.set_filetypes('txt')
		if self.checkBox_pdf.isChecked():
			filetypes.append('pdf')
			#config.set_filetypes('pdf')
		if self.checkBox_doc.isChecked():
			filetypes.append('doc')
			#config.set_filetypes('doc')
		if self.checkBox_docx.isChecked():
			filetypes.append('docx')
			#config.set_filetypes('docx')
		if self.checkBox_xls.isChecked():
			filetypes.append('xls')
			#config.set_filetypes('xls')
		if self.checkBox_xlsx.isChecked():
			filetypes.append('xlsx')
			#config.set_filetypes('xlsx')
		if self.checkBox_ppt.isChecked():
			filetypes.append('ppt')
			#config.set_filetypes('ppt')
		if self.checkBox_pptx.isChecked():
			filetypes.append('pptx')
			#config.set_filetypes('pptx')
		file.write(str(filetypes)+"\n")

		#Set owner_filter
		if self.checkBox_own_file.isChecked():
			file.write("True\n")
			#config.set_owner_filter(True)
		else:
			file.write("False\n")
			#config.set_owner_filter(False)

		#Set trash_filter
		if self.checkBox_trash.isChecked():
			file.write("True\n")
			#config.set_trash_filter(True)
		else:
			file.write("False\n")
			#config.set_trash_filter(False)

		#Set automatic_backup
		if self.checkBox_auto_backup.isChecked():
			file.write("True\n")
			#config.set_automatic_backup(True)
		else:
			file.write("False\n")
			#config.set_automatic_backup(False)

		#Set backup_frequency
		file.write(str(self.spinBox_frequency.value())+"\n")
		#config.set_backup_frequency(self.spinBox_frequency.value())

		#Set what time the backups should run
		ntime = self.timeEdit.time().toString()
		file.write(ntime[:2] + "\n")
		file.write(ntime[3:5] + "\n")
		#config.set_time(int(ntime[:2]),int(ntime[3:5]))

		#Set backup_root and log_root
		if self.backup_dir != "Choose the Directory to Store Backups":
			file.write(str(self.backup_dir)+'/'+"\n")
			#config.set_backup_root(backup_dir)
			#config.set_log_root(log_dir)
		else:
			file.write("./\n")

		if self.log_dir != "Choose the Directory to Store Backup Logs":
			file.write(str(self.backup_dir)+'/'+"\n")
		else:
			file.write("./\n")

		#Set rotation_on
		if self.checkBox_auto_delete.isChecked():
			file.write("True\n")
			#config.set_rotation_on(True)
		else:
			file.write("False\n")
			#config.set_rotation_on(False)

		#Set rotation_num
		file.write(str(self.spinBox_backup_numbers.value()))
		#config.set_rotation_num(self.spinBox_backup_numbers.value())

		file.close()

	def retranslateUi(self, Setting):
		_translate = QtCore.QCoreApplication.translate
		# initial first value for each part
		Setting.setWindowTitle(_translate("Setting", "Dialog"))
		self.label_backup_time.setText(_translate("Setting", "Automatic Backup Time "))
		self.label_backup_dir.setText(_translate("Setting", "Backup Directory"))
		self.checkBox_auto_backup.setText(_translate("Setting", "Automatic Backup"))
		self.Button_backup_dir.setText(_translate("Setting", "Select"))
		self.checkBox_trash.setText(_translate("Setting", "Backup Trash Folder"))
		self.label_backup_frequency.setText(_translate("Setting", "Backup Frequency"))
		self.label_frequency_day.setText(_translate("Setting", "Day"))
		self.label_log_dir.setText(_translate("Setting", "Backup Log Directory"))
		self.Button_log_dir.setText(_translate("Setting", "Select"))
		self.checkBox_own_file.setText(_translate("Setting", "Only Backup Files You Own"))
		self.label_backup_numbers.setText(_translate("Setting", "The Number of Backups to Maintain"))
		self.checkBox_auto_delete.setText(_translate("Setting", "Automatic Delete Backup"))
		self.checkBox_txt.setText(_translate("Setting", "txt"))
		self.checkBox_pdf.setText(_translate("Setting", "pdf"))
		self.checkBox_doc.setText(_translate("Setting", "doc"))
		self.checkBox_docx.setText(_translate("Setting", "docx"))
		self.checkBox_xls.setText(_translate("Setting", "xls"))
		self.checkBox_xlsx.setText(_translate("Setting", "xlsx"))
		self.checkBox_ppt.setText(_translate("Setting", "ppt"))
		self.checkBox_pptx.setText(_translate("Setting", "pptx"))
		self.checkBox_file_type.setText(_translate("Setting", "Backup Items Based on File Type "))
		self.pushButton_apply.setText(_translate("Setting", "Apply"))
		self.textBrowser_backup.setText(_translate("Setting", self.backup_dir))
		self.textBrowser_log.setText(_translate("Setting", self.log_dir))
		self.label_commit_message.setText(_translate("Setting", self.message))

