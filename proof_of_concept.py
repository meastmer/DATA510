import json
import os
from re import template

# 
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

# some JSON:
templateJson =  '{ "park":{ "name": "Magic Kindom","rides" : { "name" : "Dummy Ride", "waitTimes" : { "time" : "900", "waitTime" : 20, "temp" : 75}}}}'
loadedJson = json.loads(templateJson)

# Initialize Directory
os.chdir("/")
# Load File List

print(os.listdir())
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".pdf"):
        file_path = f"{path}\{file}"
        print(file_path)
  
        # call read text file function
        read_text_file(file_path)

# Iterate through each file from the file list
# Iterate through file contents
# Load file contents into template JSON file

# Determine oldest and most recent dates
# Call open weather API and build value table for temperatures

# Iterate through templateJson and insert temps into wait time array
