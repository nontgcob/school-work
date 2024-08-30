# Sum of Digits
# Write a Python program that calculates the sum of digits of a given integer using a for loop.

# Get the integer from the user
number = input("Enter an integer: ")

# Initialize the sum
sum_of_digits = 0

# Calculate the sum of digits using a for loop
for digit in number:
    if digit.isdigit():
        sum_of_digits += int(digit)

# Print the result
print(f"The sum of digits in {number} is: {sum_of_digits}")
