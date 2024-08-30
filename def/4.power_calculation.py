# Power Calculation
# Write a recursive function power(base, exponent) that returns the value of base raised to the power of exponent.

def power(base, exponent):
    # Base case: if exponent is 0, return 1
    if exponent == 0:
        return 1
    
    # Recursive case: multiply base with power of (base, exponent-1)
    return base * power(base, exponent - 1)

# Example usage
def main():
    base = 2
    exponent = 5
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")

if __name__ == "__main__":
    main()
