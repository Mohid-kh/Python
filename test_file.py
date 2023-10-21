## Creating a new file and writing/reading data

import os

f = open("new_file", "w")  # Creates a new file and sets it in write mode (overwriting any existing file)

for i in range(10):                      # i = 0 till i = 9
    data=f.write("hello there\n\n")      # Writing data to txt file
    if i==5:
        break

f = open("new_file", "a")                # append (write at end of text file)
data =f.write("end of text")

f = open("new_file", "r")                # read mode

tmp = f.read()
data = f.close()                         #close file

file_size = os.path.getsize("new_file")  # size of text file

if file_size == 0:                       # if no data found
    print("no data found")
else:
    print("data found")
    print("data is: ", tmp)
