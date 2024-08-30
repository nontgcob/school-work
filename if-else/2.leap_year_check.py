# Leap Year Checker:
# Create a program that takes a year as input and checks whether it is a leap year.

# Get the year from the user
year = int(input("Enter a year: "))
# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")