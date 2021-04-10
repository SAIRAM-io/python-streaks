import os

os.chdir('test folder')
print(os.getcwd())
print(len(os.listdir()))

for file in os.listdir():
    # Split file name and file extension 
    file_name, file_ext = os.path.splitext(file)
    # Split file name
    topic, number = file_name.split('-')
    # Remove whitespaces
    topic, number = topic.strip(), number.strip()
    # define new file name
    new_filename = '{} - {}{}'.format(number, topic, file_ext)
    # rename the file
    os.rename(file, new_filename)
