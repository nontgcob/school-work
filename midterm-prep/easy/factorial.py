# Write a program to calculate the factorial of a given number using a for loop.
try:
    num = int(input("Enter a number: "))
    result = 1
    while True:
        if num != 0:
            result = result * num
            num = num - 1
        else:
            break

    print(result)
except:
    print("Invalid input")
    pass
