import APIAccess

if __name__ == '__main__':
        # Setup the users Google Drive and save the instance
        DRIVE = APIAccess.getDrive()

        files = APIAccess.getFiles(DRIVE)
        for f in files:
                print(f)
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
