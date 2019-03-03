import filetype
# API Access Module

# filter information
# txt, pdf, doc, docx, xls, ppt, pptx
def filter(true):
	filetypelist = {'txt', 'pdf', 'doc', 'docx', 'xls', 'ppt', 'pptx'}
	mylist = {}
	while(True):
		filetype = input('Please input a FileType or Stop: ')
		if  filetype.capitalize() = 'Stop':
			return mylist
		if filetype.lower() in filetypelist:
			mylist.append(filetype.lower())
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
file_dir = ''
# how often to write them
write_time = input()
# and when to delete them
delete_time = ''

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
