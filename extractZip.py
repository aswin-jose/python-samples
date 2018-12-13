# script to input a directory and extract all the zip files in that folder in that folder itself.

from zipfile import ZipFile 
import os

directory = input("Enter Directory : ")
for root, dirs, files in os.walk(directory):  
    for filename in files:
        filepath = os.path.join(root, filename)
        with ZipFile(filepath, 'r') as zip: 

            # extracting all the files 
            print(f'Extracting {filename} now...') 
            zip.extractall(root) 
            print('Done!')  


