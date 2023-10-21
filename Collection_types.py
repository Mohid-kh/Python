## 4 collection data types in python that can be used as arrays

import os

with open("test_file", "w") as test_file:
    test_file.write("")

if os.path.getsize("test_file") == 0:
    print("no data found")
else:
    print("data is: ")
    with open("test_file", "r") as test_file:
        print(test_file.read())
     

