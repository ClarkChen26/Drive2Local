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

if __name__ == '__main__':
	# Setup the users Google Drive and save the instance
	DRIVE = APIAccess.getDrive()
	# Get a listing of all files the user has access to
	files = APIAccess.getFiles(DRIVE)

	for f in files:
		if owner_filter:
			if not isOwned(f):
				continue
		if trash_filter:
			if isTrashed(f):
				continue
		if filetype_filter:
			if not isFilteredExtension(f):
				continue
		try:
			print(f['name'], f['fullFileExtension'])
		except:
			continue
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
