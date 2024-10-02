# Write a Python program to print all prime numbers less than N (user input) using loops and if-else.

# Get user input
N = int(input("Enter a number N: "))

print(f"Prime numbers less than {N}:")

for num in range(2, N):
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num, end=" ")

print()