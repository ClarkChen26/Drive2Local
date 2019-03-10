#------------------------------ 
# FILTERS
#------------------------------ 
#
# Whether to filter items based on filetype
global filetype_filter
def set_filetype_filter(arg):
	filetype_filter = arg
#filetype_filter = True
#
# Which filetypes to backup
global filetypes
filetypes = []
def set_filetypes(arg):
	filetypes = arg
#filetypes = ["txt", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]
#
# Whether or not backups are limited to files owned by the user
global owner_filter
def set_owner_filter(arg):
	owner_filter = arg
#owner_filter = True
#
# Whether or not to backup files that have been trashed
global trash_filter
def set_trash_filter(arg):
	trash_filter = arg
#trash_filter = False
#
#------------------------------ 
# LOCAL FILE SETTINGS
#------------------------------ 
#
# Whether or not to automatically create backups
global automatic_backup
def set_automatic_backup(arg):
	automatic_backup = arg
#automatic_backup = False
#
# How often automatic backups should be created (in days)
global backup_frequency
def set_backup_frequency(arg):
	backup_frequency = arg
#backup_frequency = 1
#
# What time the backups should run
global backup_hour
global backup_minute
def set_time(hour, minute):
	backup_hour = hour
	backup_minute = minute
#backup_hour = 0
#backup_minute = 0
#
# Path to a directory for backups to be stored in
global backup_root
backup_root = "/Users/kaijingzhang/Drive2Local_Backups/"
def set_backup_root(arg):
	backup_root = arg
#
# Path to the logfile
global log_root
log_root = "/Users/kaijingzhang/Drive2Local_logs/drive2local.log"
def set_log_root(arg):
	log_root = arg
#
# Whether or not to automatically delete backups
global rotation_on
def set_rotation_on(arg):
	rotation_on = arg
#rotation_on = False
#
# The number of backups to maintain
global rotation_num
def set_rotation_num(arg):
	rotation_num = arg
#rotation_num = 7
#
#------------------------------ 
# GUI SETTINGS
#------------------------------ 
#
# Not yet implemented
#
