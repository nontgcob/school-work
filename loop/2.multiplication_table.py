# Multiplication Table
# Create a Python program that prints the multiplication table for any given number up to 12 using a for loop.

def print_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage
num = int(input("Enter a number to generate its multiplication table: "))
print_multiplication_table(num)
