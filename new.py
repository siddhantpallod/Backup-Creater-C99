import os
import shutil

source = input("Enter Source Folder Name: ")
destination = input("Enter Destination Folder Name: ")

source = source + '/'
destination = destination + '/'

listOfFiles = os.listdir(source)

for files in listOfFiles:
    shutil.copy((source + files), destination)
