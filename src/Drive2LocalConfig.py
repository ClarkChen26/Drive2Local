#------------------------------ 
# FILTERS
#------------------------------ 
#
# Whether to filter items based on filetype
global filetype_filter = True
def set_filetype_filter(arg):
	filetype_filter = arg
#
# Which filetypes to backup
global filetypes = []
def set_filetypes(arg):
	filetypes = arg
#
# Whether or not backups are limited to files owned by the user
global owner_filter = True
def set_owner_filter(arg):
	owner_filter = arg
#
# Whether or not to backup files that have been trashed
global trash_filter = False
def set_trash_filter(arg):
	trash_filter = arg
#
#------------------------------ 
# LOCAL FILE SETTINGS
#------------------------------ 
#
# Whether or not to automatically create backups
global automatic_backup = False
def set_automatic_backup(arg):
	automatic_backup = arg
#
# How often automatic backups should be created (in days)
global backup_frequency = 1
def set_backup_frequency(arg):
	backup_frequency = arg
#
# What time the backups should run
global backup_hour = 0
global backup_minute = 0
def set_time(hour, minute):
	backup_hour = hour
	backup_minute = minute
#
# Path to a directory for backups to be stored in
global backup_root = "/path/to/backup/root/"
def set_backup_root(arg):
	backup_root = arg
#
# Path to the logfile
global log_root = "/path/to/logroot/"
def set_log_root(arg):
	log_root = arg
#
# Whether or not to automatically delete backups
global rotation_on = False
def set_rotation_on(arg):
	rotation_on = arg
#
# The number of backups to maintain
global rotation_num = 7
def set_rotation_num(arg):
	rotation_num = arg
