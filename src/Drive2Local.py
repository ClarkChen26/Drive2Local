#!/usr/bin/env python3
import os

import Drive2LocalAPIAccess, Drive2LocalHandleLocal, Drive2LocalLogging
from Drive2LocalConfig import *



def isOwned(file):
	'''
	Returns a boolean representing whether a file is owned by the user.
	'''

	return file['owners'][0]['me']


def isTrashed(file):
	'''
	Returns a boolean representing whether a file has been trashed.
	'''

	return file['trashed']


def isFilteredExtension(file, config):
	'''
	Checks whether or not the file extension is in the filtered list.
	'''

	try:
		if isGoogleFile(file):
			mimeType = Drive2LocalAPIAccess.MIME_EXPORT[file['mimeType']]
			exten = Drive2LocalAPIAccess.MIME_EXTENSIONS[mimeType]
		else:
			exten = file['fileExtension']
	except:
		return False

	return exten in config[1]
	#filetypes


def isGoogleFile(file):
	'''
	Checks whether or not the file is a native Google file (as opposed
	one updloaded to Google Drive)
	'''

	return file['mimeType'] in Drive2LocalAPIAccess.MIME_EXPORT


def main():
	# Setup logger
	config_list = config_setup()


	Drive_logger = Drive2LocalLogging.setupLogger(config_list)

	Drive_logger.info("Backup Initiating")

	os.system("open " + config_list[9] + "backup.log")
	
	# Setup the users Google Drive and save the instance
	DRIVE = Drive2LocalAPIAccess.getDrive()
	# Get a listing of all files the user has access to
	files = Drive2LocalAPIAccess.getFiles(DRIVE, Drive_logger)

	path = Drive2LocalHandleLocal.buildDir(config_list[8])


	# Download loop
	for f in files:
		# FILTERING
		if config_list[2]:
			if not isOwned(f):
				continue
		if not config_list[3]:
			if isTrashed(f):
				continue
		if config_list[0]:
			if not isFilteredExtension(f, config_list):
				continue

		# DOWNLOADING
		try:
			if isGoogleFile(f):
				if Drive2LocalHandleLocal.writeGoogleFile(DRIVE, path, f, Drive_logger) == 1:
					break
			else:
				if Drive2LocalHandleLocal.writeFile(DRIVE, path, f, Drive_logger) == 1:
					break
		except KeyboardInterrupt:
			break

	# Compress the newly created backup
	Drive2LocalHandleLocal.compressDir(path)

	if config_list[10]:
		# rotation_on
		Drive2LocalHandleLocal.rotateBackups(Drive_logger, config_list[8], config_list[11])

	Drive_logger.info("Backup Complete")

if __name__ == '__main__':
	main()
