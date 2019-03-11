#!/usr/bin/env python3
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


def isFilteredExtension(file):
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

	return exten in filetypes


def isGoogleFile(file):
	'''
	Checks whether or not the file is a native Google file (as opposed
	one updloaded to Google Drive)
	'''

	return file['mimeType'] in Drive2LocalAPIAccess.MIME_EXPORT


def main():
	# Setup logger
	Drive2LocalLogging.setupLogger()
	
	# Setup the users Google Drive and save the instance
	DRIVE = Drive2LocalAPIAccess.getDrive()
	# Get a listing of all files the user has access to
	files = Drive2LocalAPIAccess.getFiles(DRIVE)

	path = Drive2LocalHandleLocal.buildDir()

	# Download loop
	for f in files:
		# FILTERING
		if owner_filter:
			if not isOwned(f):
				continue
		if not trash_filter:
			if isTrashed(f):
				continue
		if filetype_filter:
			if not isFilteredExtension(f):
				continue

		# DOWNLOADING
		if isGoogleFile(f):
			Drive2LocalHandleLocal.writeGoogleFile(DRIVE, path, f)
		else:
			Drive2LocalHandleLocal.writeFile(DRIVE, path, f)

	# Compress the newly created backup
	Drive2LocalHandleLocal.compressDir(path)

	if rotation_on:
		Drive2LocalHandleLocal.rotateBackups()


if __name__ == '__main__':
	main()
