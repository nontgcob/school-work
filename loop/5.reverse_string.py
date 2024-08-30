# Reverse a String
# Write a Python program that reverses a given string using a for loop.

def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
original_string = "Hello, World!"
reversed_result = reverse_string(original_string)
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_result}")
