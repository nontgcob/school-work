# Odd or Even Number:
# Write a Python program that takes an integer as input and checks whether the number is odd or even.

# Get the number from the user
number = int(input("Enter an integer: "))
# Check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")