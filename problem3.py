# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.?

import os

# Specify the directory path
directory_path = '.'

# Get the list of all files and directories in the specified directory
contents = os.listdir('/js dom')

# Print the contents
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)
