import requests as rq

url = "https://www.google.com"
my_file = "my_file.txt"

response = rq.get(url)

if response.status_code == 200:
    with open("my_file.txt", "w") as my_file:
        my_file.write(response.text)                # write URL data to text file
if not my_file:
    print("no data found")
else:
        print("data written on new file successfully.")
