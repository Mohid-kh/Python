my_int = int(3.81)             # float converted to int
print(my_int)

my_string = str(2.68)
print(my_string)

my_float = float("2.69")
print(my_float)

list = [2, 4.1, "hello"]
a = list.pop(0)                       # remove list[0] i.e. 2 and store it in a
x = isinstance(list[0], float)        # checks if list[0] is a float (true) or not

if x is True:
    print(list[0])
else:
    print("no floating number found")

list2 = [1 , 2, 3, 4, 3]
list2.remove(3)                       # removes first occurence of the number 3 
print(list2[3])
