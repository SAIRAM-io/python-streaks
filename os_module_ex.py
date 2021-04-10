# A directory or folder is a collection of files and subdirectories. 
# Python has the os module that provides us with many useful methods to work with directories (and files as well).
import os
# To get current working directory
print(os.getcwd())

# To change directory -- (we need to use \\)
os.chdir('C:\\Users\\rajap\\Desktop\\Eduyear')
print(os.getcwd())

# To get list of files and directories
print(os.listdir())
os.listdir('C:\\Users\\rajap\\Desktop')

# Make a new directory
os.mkdir('testing_directory')
print(os.listdir())

# Rename a directory or file
os.rename('testing_directory','new_testing_directory')
print(os.listdir())

# Remove an empty directory
os.rmdir('new_testing_directory')

# Remove a file
os.remove('file_name.txt')

# Remove a non-empty directory
# rmdir() will throw an error. Instead we use shutil.rmtree().
os.rmdir('C:\\Users\\rajap\\Desktop\\Eduyear\\test')		# throw an error

import shutil
shutil.rmtree('C:\\Users\\rajap\\Desktop\\Eduyear\\test')
os.listdir()

# To recursively get the file and sub-directories to directory
for (dirpath, dirnames, filenames) in os.walk('C:\\Users\\rajap\\Desktop\\Eduyear'):
    print(dirpath)
    print(dirnames)
    print(filenames)
    print()