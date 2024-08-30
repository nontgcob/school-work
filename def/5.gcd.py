# Greatest Common Divisor (GCD)
# Write a recursive function gcd(a, b) that returns the greatest common divisor of two numbers a and b.

def gcd(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: call gcd with b and the remainder of a divided by b
    return gcd(b, a % b)

# Example usage
def main():
    a = 48
    b = 18
    result = gcd(a, b)
    print(f"The greatest common divisor of {a} and {b} is: {result}")

if __name__ == "__main__":
    main()
