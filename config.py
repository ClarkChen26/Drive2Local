import filetype
# API Access Module

# filter information
def filter(true):
	filetype = {}
	while(true):
		if confirm = True:
			return filetype

# File Handling Module
# txt, pdf, doc, docx, xls, ppt, pptx
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
	USERNAME = input("please input a google account: ")
	if USERNAME in NameDatebase:
		PASSWORD = input("please input password: ")
		if Datebase[USERNAME] == PASSWORD:
			print('Enter Successfully! ')
		else:
			print('The password you entered is wrong, please re-enter it. ')
	else:
		print('The user name you entered is not correct, please re-enter it')
