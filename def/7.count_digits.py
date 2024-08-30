# Count the Number of Digits
# Write a recursive function count_digits(n) that returns the number of digits in a given number n.

def count_digits(n):
    # Base case: if n is less than 10, it has 1 digit
    if n < 10:
        return 1
    
    # Recursive case: divide n by 10 and add 1 to the count
    return 1 + count_digits(n // 10)

# Example usage
def main():
    number = 12345
    result = count_digits(number)
    print(f"The number of digits in {number} is: {result}")

if __name__ == "__main__":
    main()
