# Sum of Natural Numbers
# Write a recursive function sum_of_natural_numbers(n) that returns the sum of the first n natural numbers.

def sum_of_natural_numbers(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    
    # Recursive case: sum of n and sum of first (n-1) natural numbers
    return n + sum_of_natural_numbers(n - 1)

# Example usage
def main():
    n = 5
    result = sum_of_natural_numbers(n)
    print(f"The sum of the first {n} natural numbers is: {result}")

if __name__ == "__main__":
    main()
