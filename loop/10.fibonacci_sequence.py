# Fibonacci Sequence
# Create a Python program that generates the first 15 numbers of the Fibonacci sequence using a for loop.

# Initialize the first two numbers of the Fibonacci sequence
a, b = 0, 1

# Print the first number
print(a, end=" ")

# Generate and print the next 14 numbers
for _ in range(14):
    print(b, end=" ")
    a, b = b, a + b

# Print a newline at the end for better formatting
print()
