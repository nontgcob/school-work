# Generate a List of Squares
# Create a Python program that generates a list of squares of numbers from 1 to 20 using a for loop.

# Initialize an empty list to store the squares
squares = []

# Generate squares of numbers from 1 to 20 using a for loop
for num in range(1, 21):
    squares.append(num ** 2)

# Print the list of squares
print("List of squares from 1 to 20:")
print(squares)
