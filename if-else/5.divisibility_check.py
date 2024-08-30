# Divisibility Check:
# Write a program that takes two integers as input and checks whether the first number is divisible by the second.

# Get two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Check if the first number is divisible by the second
if num2 != 0:
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}.")
    else:
        print(f"{num1} is not divisible by {num2}.")
else:
    print("Error: Cannot divide by zero.")
