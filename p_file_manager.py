import os

def create_file():
	pass

def create_directory():
	pass
	
def remove_directory():
	folders = [item for item in os.listdir() if os.path.isdir(item)]
	print('\n Choose a directory from below to delete...')
	for ind, fol in enumerate(folders):
		print(f'{ind+1}. {fol}')
	choice = int(input('\nEnter you option: '))
	if len(os.listdir(folders[choice-1])) != 0:
		import shutil
		shutil.rmtree(folders[choice-1])
	else: 
		os.rmdir(folders[choice-1])
	print(f'{folders[choice-1]} directory is deleted...')
	
def show_curr_dir():
	curr_path = os.getcwd()
	print(f'\nCurrent directory name: {os.path.basename(curr_path)}')
	print(f'Current directory path: {os.path.dirname(curr_path)}')

def list_directory():
	files = [item for item in os.listdir() if os.path.isfile(item)]
	folders = [item for item in os.listdir() if os.path.isdir(item)]
	if len(folders) == 0:
		print('\nThere are no folders in the current directory.')
	else:
		print('\nAll Folders...')
		for ind, fol in enumerate(folders):
			print(f'{ind+1}. {fol}')
	if len(files) == 0:
		print('\nThere are no files in the current directory.')
	else:
		print('\nAll Files...')
		for ind, fil in enumerate(files):
			print(f'{ind+1}. {fil}')

def remove_file():
	files = [item for item in os.listdir() if os.path.isfile(item)]
	print('\n Choose a file from below...')
	for ind, fil in enumerate(files):
		print(f'{ind+1}. {fil}')
	choice = int(input('\nEnter you option: '))
	os.remove(files[choice-1])
	print(f'{files[choice-1]} is deleted...')

def list_directory_files():
	print('\nAll Files...')
	ind = 1
	for item in os.listdir():
		if os.path.isfile(item):
			print(f'{ind}. {item}')
			ind += 1

def list_directory_folders():
	print('\nAll Folders...')
	ind = 1
	for item in os.listdir():
		if os.path.isdir(item):
			print(f'{ind}. {item}')
			ind += 1

def show_menu():
	menu_items = ['Create a new directory', 'Remove a directory', 'Create a file', 'Delete a file', 'List Folders and Files', 'List all folders', 'List all files', 'Show curent directory details']
	while True:
		print('\n **** OPTIONS ****')
		for ind in range(len(menu_items)):
			print(f'{ind+1}. {menu_items[ind]}')
		print('0. Exit')
		choice = int(input('\nEnter you option: '))
		if choice == 0:
			exit(1)
			# return 
		elif choice == 1:
			create_directory()
		elif choice == 2:
			remove_directory()
		elif choice == 3:
			create_file()
		elif choice == 4:
			# done
			remove_file()
		elif choice == 5:
			# done
			list_directory()
		elif choice == 6:
			# done
			list_directory_folders()
		elif choice == 7:
			# done
			list_directory_files()
		elif choice == 8:
			# done
			show_curr_dir()

os.chdir('C:\\Users\\rajap\\Desktop\\Eduyear\\Python Programming - 11 Feb\\testing folder')


show_menu()