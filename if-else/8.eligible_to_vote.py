# Eligibility to Vote:
# Create a program that takes a person's age as input and checks if they are eligible to vote (18 years or older).

# Get the person's age from the user
try:
    age = int(input("Enter your age: "))

    # Check if the person is eligible to vote
    if age >= 18:
        print("You are eligible to vote.")
    elif age < 0:
        print("Error: Age cannot be negative.")
    else:
        print("You are not eligible to vote yet.")
except ValueError:
    print("Error: Please enter a valid integer for age.")
