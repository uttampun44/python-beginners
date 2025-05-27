import os

directoryPath = "/projects"

contents = os.listdir(directoryPath)

# loop through the files in the directory
for file in contents:
    print(file)