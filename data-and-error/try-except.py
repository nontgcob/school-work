# code for 5 try-except errors

# NameError
try:
    print(x)
except NameError:
    print("x is not defined")

# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# FileNotFoundError
try:
    f = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("File not found")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range")

# KeyError
try:
    my_dict = {"name": "John", "age": 25}
    print(my_dict["city"])
except KeyError:
    print("Key not found")