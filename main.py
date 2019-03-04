import APIAccess
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

# Probably needs some work.
def isFilteredExtension(file):
	'''
	Checks whether or not the file extension is in the filtered list.
	'''

	try:
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

if __name__ == '__main__':
	# Setup the users Google Drive and save the instance
	DRIVE = APIAccess.getDrive()
	# Get a listing of all files the user has access to
	files = APIAccess.getFiles(DRIVE)

	for f in files:
		# FILTERING
		if owner_filter:
			if not isOwned(f):
				continue
		if not trash_filter:
			if isTrashed(f):
				continue
#		if filetype_filter:
#			if not isFilteredExtension(f):
#				continue

		# DOWNLOADING
		if isGoogleFile(f):
			export_mime = APIAccess.MIME_EXPORT[f['mimeType']]
			APIAccess.exportFile(DRIVE, f['id'], export_mime, f['name']+APIAccess.MIME_EXTENSIONS[export_mime])
#       for f in files:
#               # Handle native Google Drive files
#               if f['mimeType'] in MIME_EXPORT:
#                       mimeType = MIME_EXPORT[f['mimeType']]
#                       extension = MIME_EXTENSIONS[mimeType]
#                       name = f['name']+extension
#                       #exportFile(DRIVE, f['id'], mimeType, name)
#                       print(name, mimeType)
#               # Handle files uploaded to Google Drive (non-native)
#               else:
#                       #downloadFile(DRIVE, f['id'], name)
#                       print(name, f['mimeType'])
