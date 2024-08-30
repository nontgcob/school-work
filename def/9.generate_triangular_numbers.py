# Generate Triangular Numbers
# Write a recursive function triangular_number(n) that returns the nth triangular number.

def triangular_number(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    
    # Recursive case: nth triangular number is n plus (n-1)th triangular number
    return n + triangular_number(n - 1)

def main():
    n = 5  # Example: Calculate the 5th triangular number
    result = triangular_number(n)
    print(f"The {n}th triangular number is: {result}")

if __name__ == "__main__":
    main()
