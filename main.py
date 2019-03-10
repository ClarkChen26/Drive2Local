import APIAccess
import HandleLocal
from config import *

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
			mimeType = APIAccess.MIME_EXPORT[file['mimeType']]
			exten = APIAccess.MIME_EXTENSIONS[mimeType]
		else:
			exten = f['fileExtension']
	except:
		return False

	return exten in filetypes

def isGoogleFile(file):
	'''
	Checks whether or not the file is a native Google file (as opposed
	one updloaded to Google Drive)
	'''

	return file['mimeType'] in APIAccess.MIME_EXPORT
def main():
	# Setup the users Google Drive and save the instance
	DRIVE = APIAccess.getDrive()
	# Get a listing of all files the user has access to
	files = APIAccess.getFiles(DRIVE)

	path = HandleLocal.buildDir()

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
			HandleLocal.writeGoogleFile(DRIVE, path, f)
		else:
			HandleLocal.writeFile(DRIVE, path, f)

	# Compress the newly created backup
	HandleLocal.compressDir(path)

	if rotation_on:
		HandleLocal.rotateBackups()
if __name__ == '__main__':
	main()
