# Sum of Digits
# Write a recursive function sum_of_digits(n) that returns the sum of the digits of a given number n.

def sum_of_digits(n):
    # Base case: if n is a single digit, return n
    if n < 10:
        return n
    
    # Recursive case: sum of the last digit and sum of digits of the remaining number
    return (n % 10) + sum_of_digits(n // 10)

# Example usage
def main():
    number = 12345
    result = sum_of_digits(number)
    print(f"The sum of digits of {number} is: {result}")

if __name__ == "__main__":
    main()
