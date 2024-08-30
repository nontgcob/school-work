# Vowel or Consonant:
# Write a Python program that takes a single character as input and checks whether it is a vowel or consonant.

# Get a single character from the user
char = input("Enter a single character: ").lower()

# Check if the input is a single character
if len(char) == 1:
    # Check if the character is a letter
    if char.isalpha():
        # Check if the character is a vowel
        if char in 'aeiou':
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    else:
        print("Error: Please enter a letter.")
else:
    print("Error: Please enter a single character.")
