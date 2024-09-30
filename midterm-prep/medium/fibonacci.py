# Write a program that prints the first N numbers of the Fibonacci sequence, where N is input by the user.

try:
    num = int(input("Enter a number: "))
    a = 0
    b = 1
    for i in range(num):
        print(a)
        c = a + b
        a = b
        b = c
except ValueError:
    print("Please enter a valid integer.")
