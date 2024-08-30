# Print Even Numbers
# Create a Python program that prints all the even numbers between 1 and 100 using a for loop.

# Initialize an empty list to store even numbers
even_numbers = []

# Use a for loop to iterate through numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is even
    if num % 2 == 0:
        even_numbers.append(num)

# Print the list of even numbers
print("Even numbers between 1 and 100:")
print(even_numbers)
