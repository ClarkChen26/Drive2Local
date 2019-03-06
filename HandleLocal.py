import APIAccess
from config import *
import sys
import os
import datetime
import shutil
import re
from crontab import CronTab

def buildDir():
    '''
    Builds a directory under the backup root named using the current
    year, month, day, hour, minute, and second.
    '''

    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = backup_root+now
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def writeFile(DRIVE, path, f):
    '''
    Calls the APIAccess module to download a file object, then writes it
    to the path and filename given.
    '''

    try:
        print("Downloading", f['name'])
        APIAccess.downloadFile(DRIVE, f['id'], path+"/"+f['name'])
    except:
        err = sys.exc_info()[0]
        print("Error: Could not download file ", f['name'], f['id'], err)

def writeGoogleFile(DRIVE, path, f):
    '''
    Calls the APIAccess module to download a file object, then writes it
    to the path and filename given.

    This function is used specifically for native Google files.
    '''

    export_mime = APIAccess.MIME_EXPORT[f['mimeType']]
    # Skip folders
    if not export_mime == "application/vnd.google-apps.folder":
        try:
            print("Downloading", f['name'])
            APIAccess.exportFile(DRIVE, f['id'], export_mime, path+"/"+f['name'] + "." + APIAccess.MIME_EXTENSIONS[export_mime])
        except:
            err = sys.exc_info()[0]
            print("Error: Could not download file ", f['name'], f['id'], err)

def compressDir(path):
    '''
    Compresses a target directory to a zipfile.
    '''

    # Creates a new zipfile containing the backup located at path
    shutil.make_archive(path, "zip", path)
    # Deletes the unzipped folder
    shutil.rmtree(path)

def rotateBackups():
    '''
    Deletes old backups until there are less than the
    number specified by rotate_num in the config file.
    '''

    count = 0
    r = re.compile(".*\.zip")
    try:
        backups = os.listdir(backup_root)
        backups.sort()
        for file in reversed(backups):
            if r.match(file):
                count += 1
                if count > rotation_num:
                    os.remove(backup_root+"/"+file)
    except TypeError:
        print("No backups found.")

def scheduleBackups():
    '''
    Creates a crontab to run the main file
    '''
    
    crontab = CronTab(user=True)
    job = crontab.new(command="/path/to/main/file")
    job.day.every(backup_frequency)
