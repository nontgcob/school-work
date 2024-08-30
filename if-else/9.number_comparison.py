# Number Comparison:
# Write a program that takes two numbers as input and prints "Greater" if the first number is greater than the second, "Smaller" if it's smaller, or "Equal" if both numbers are the same.

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print("Greater")
elif num1 < num2:
    print("Smaller")
else:
    print("Equal")
