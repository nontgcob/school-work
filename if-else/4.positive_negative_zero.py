# Positive, Negative, or Zero:
# Create a program that checks if a given number is positive, negative, or zero.

# Get the number from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")
