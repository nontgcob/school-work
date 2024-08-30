# Factorial Calculation
# Write a Python program that calculates the factorial of a given number using a for loop.

def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Example usage
number = 5
result = calculate_factorial(number)
if result is None:
    print(f"Factorial is not defined for {number}")
else:
    print(f"The factorial of {number} is: {result}")
