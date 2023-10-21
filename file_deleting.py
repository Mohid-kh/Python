import os
if os.path.exists("new_file.txt"):      ## check if path exists
    os.remove("new_file.txt")           #  remove the file
    print("file removed")
else:
    print("File does not exist")
