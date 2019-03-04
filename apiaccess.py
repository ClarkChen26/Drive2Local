from __future__ import print_function

import io
from apiclient import errors
from apiclient import http
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

def getDrive():
	# Define the permission scope
	SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
	# Define the local credential store
	store = file.Storage('storage.json')
	# Get credentials from the local store
	creds = store.get()
	# If the credentials are invalid, get new credentials from the user
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
	    creds = tools.run_flow(flow, store)

	# Get the Google Drive of the credentialed user
	DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

	return DRIVE

def listFiles(DRIVE):
	# Gets the entire list of files in the DRIVE and stores them in a list variable
	files = DRIVE.files().list().execute().get('files', [])

	# Iterate through the list of files and print the names, mimetypes, and ids
	for f in files:
	    print(f['name'], f['mimeType'], f['id'])

def downloadFile(DRIVE, fileid, mimetype, filename):
	# Store the fileid in a variable
	file_id = fileid
	# Store the exported file within a variable for later use
	request = DRIVE.files().export_media(fileId=file_id, mimeType=mimetype)
	# Open a stream up to write bytes to a filename in current working directory
	fh = io.FileIO(filename, 'wb')
	# Connect the bytes of exported file to a FileIO stream
	downloader = http.MediaIoBaseDownload(fh, request)
	# Boolean to mark when done
	done = False
	# While not done, download chunks of bytes through stream until done and print progress
	while done is False:
	    status, done = downloader.next_chunk()
	    print ("Download %d%%." % int(status.progress() * 100))

if __name__ == '__main__':
	# Setup the users Google Drive and save the instance
	DRIVE = getDrive()
	# Download the file from the drive as a word document
	downloadFile(DRIVE, "1D6tgGZjmhjtgO2dVxw3IlLXgU4JlQsJuluokfs-DYpg", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "test.docx")
