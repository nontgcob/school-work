# Count Vowels in a String
# Create a Python program that counts the number of vowels in a given string using a for loop.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Example usage
text = "Hello, how are you today?"
result = count_vowels(text)
print(f"The string '{text}' contains {result} vowels.")
