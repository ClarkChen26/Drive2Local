import filetype
# API Access Module
# filter information
# txt, pdf, doc, docx, xls, ppt, pptx
def filter(true):
	filetypelist = ['txt', 'pdf', 'doc', 'docx', 'xls', 'ppt', 'pptx']
	filtering_list = []
	while(True):
		filetype = input('Please input a FileType or Stop: ')
		if filetype.capitalize() == 'Stop':
			return filtering_list
		if filetype.lower() in filetypelist:
			filtering_list.append(filetype.lower())
		else:
			print('Wrong FileType! ')

# File Handling Module
def filehandling(file_address):
	if file_address is not str:
		print('Address not a string!')
		return
	res = filetype.guess(file_address)
	if res is None:
		print('Cannot guess file type!')
		return
	return res

# where to write them
file_dir = input("please put a directory that you want to store the backup")
# how often to write them
write_time = input("please put a time that you want to back up the file")
# and when to delete them
delete_time = input("please put a time that you want to delete the previous backup file")

if __name__ == '__main__':
	#Config Google Account and password
	Datebase = {} 
	# login credentials 
	USERNAME = input('Please input a google account: ')
	if USERNAME in Datebase:
		PASSWORD = input('Please input password: ')
		if Datebase[USERNAME] == PASSWORD:
			print('Enter Successfully! ')
		else:
			print('The password you entered is wrong, please re-enter it. ')
	else:
		print('The user name you entered is not correct, please re-enter it')
