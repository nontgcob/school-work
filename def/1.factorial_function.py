# Factorial Function
# Write a recursive function factorial(n) that returns the factorial of a given number n.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n = 5  # Example input
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")

if __name__ == "__main__":
    main()
