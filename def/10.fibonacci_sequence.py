# Fibonacci Sequence
# Write a recursive function fibonacci(n) that returns the nth Fibonacci number.

def fibonacci(n):
    # Base cases: first two Fibonacci numbers
    if n <= 1:
        return n
    
    # Recursive case: sum of the two preceding numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = 10  # Example: Calculate the 10th Fibonacci number
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()
