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
	files = DRIVE.files().list().execute().get('files', [])
	for f in files:
	    print(f['name'], f['mimeType'], f['id'])

def downloadFile(DRIVE, fileid, mimetype, filename):
	file_id = fileid
	request = DRIVE.files().export_media(fileId=file_id, mimeType=mimetype)
	fh = io.FileIO(filename, 'wb')
	downloader = http.MediaIoBaseDownload(fh, request)
	done = False
	while done is False:
	    status, done = downloader.next_chunk()
	    print ("Download %d%%." % int(status.progress() * 100))

if __name__ == '__main__':
	DRIVE = getDrive()
	downloadFile(DRIVE, "1D6tgGZjmhjtgO2dVxw3IlLXgU4JlQsJuluokfs-DYpg", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "test.docx")
