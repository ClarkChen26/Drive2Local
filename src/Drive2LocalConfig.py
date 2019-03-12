import os
#------------------------------ 
# FILTERS
#------------------------------ 
#
if os.path.exists("/tmp/temp_config.txt"):
	file = open("/tmp/temp_config.txt", "r")
	l = file.read().split()
else:
	l = [False, [], True, False, False, 1, 0, 0, "", "", False, 7]
#
# Whether to filter items based on filetype
global filetype_filter
filetype_filter = l[0]
#def set_filetype_filter(arg):
#	filetype_filter = arg
#
# Which filetypes to backup
global filetypes
filetypes = l[1]
#def set_filetypes(arg):
#	filetypes.append(arg)
#
# Whether or not backups are limited to files owned by the user
global owner_filter
owner_filter = l[2]
#def set_owner_filter(arg):
#	owner_filter = arg
#
# Whether or not to backup files that have been trashed
global trash_filter
trash_filter = l[3]
#def set_trash_filter(arg):
#	trash_filter = arg
#
#------------------------------ 
# LOCAL FILE SETTINGS
#------------------------------ 
#
# Whether or not to automatically create backups
global automatic_backup
automatic_backup = l[4]
#def set_automatic_backup(arg):
#	automatic_backup = arg
#
# How often automatic backups should be created (in days)
global backup_frequency
backup_frequency = l[5]
#def set_backup_frequency(arg):
#	backup_frequency = arg
#
# What time the backups should run
global backup_hour
backup_hour = l[6]
global backup_minute
backup_minute = l[7]
#def set_time(hour, minute):
#	backup_hour = hour
#	backup_minute = minute
#
# Path to a directory for backups to be stored in
global backup_root
backup_root = l[8]
#def set_backup_root(arg):
#	backup_root = arg
#
# Path to the logfile
global log_root
log_root = l[9]
#def set_log_root(arg):
#	log_root = arg
#
# Whether or not to automatically delete backups
global rotation_on
rotation_on = l[10]
#def set_rotation_on(arg):
#	rotation_on = arg
#
# The number of backups to maintain
global rotation_num
rotation_num = l[1]
#def set_rotation_num(arg):
#	rotation_num = arg
