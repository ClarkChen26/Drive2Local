import Drive2LocalAPIAccess
from Drive2LocalConfig import *
import sys
import os
import datetime
import shutil
import re
from crontab import CronTab
import Drive2LocalLogging


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
        Drive2LocalLogging.infoLog("Downloading, " + f['name'])
        Drive2LocalAPIAccess.downloadFile(DRIVE, f['id'], path+"/"+f['name'])
        Drive2LocalLogging.infoLog("Download complete, " + f['name'] + "\n")
    except:
        err = sys.exc_info()[0]
        Drive2LocalLogging.errorLog("Error: Could not download file " + f['name'] + str(err) + "\n")


def writeGoogleFile(DRIVE, path, f):
    '''
    Calls the APIAccess module to download a file object, then writes it
    to the path and filename given.

    This function is used specifically for native Google files.
    '''

    export_mime = Drive2LocalAPIAccess.MIME_EXPORT[f['mimeType']]
    # Skip folders
    if not export_mime == "application/vnd.google-apps.folder":
        try:
            Drive2LocalLogging.infoLog("Downloading, " + f['name'])
            Drive2LocalAPIAccess.exportFile(DRIVE, f['id'], export_mime, path+"/"+f['name'] + "." + APIAccess.MIME_EXTENSIONS[export_mime])
            Drive2LocalLogging.infoLog("Download complete, " + f['name'] + "\n")
        except:
            err = sys.exc_info()[0]
            Drive2LocalLogging.errorLog("Error: Could not download file " + f['name'] + str(err) + "\n")


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
        Drive2LocalLogging.errorLog("No backups found.\n")


def scheduleBackups():
    '''
    Creates a crontab to run the main file
    '''

    crontab = CronTab()
    job = crontab.new(command="/path/to/main/file")
    job.hour.on(backup_hour)
    job.minute.on(backup_minute)
    job.day.every(backup_frequency)
    crontab.write_to_user(user=True)
