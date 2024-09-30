# Write a function to check whether a given number is prime or not using a loop and if-else.

def is_prime(num):
    # Check if the number is less than or equal to 1
    if num <= 1:
        return False
    
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        # If the number is divisible by any integer in this range, it's not prime
        if num % i == 0:
            return False
    
    # If no divisors were found, the number is prime
    return True

# Test cases
print(is_prime(7)) # True