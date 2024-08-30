# Check if a String is a Palindrome
# Write a recursive function is_palindrome(s) that checks if a given string s is a palindrome.

def is_palindrome(s):
    # Base case: if the string has 0 or 1 character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Compare the first and last characters
    if s[0].lower() != s[-1].lower():
        return False
    
    # Recursive case: check if the substring without the first and last characters is a palindrome
    return is_palindrome(s[1:-1])

# Example usage
def main():
    test_strings = ["racecar", "Hello", "A man a plan a canal Panama", "python"]
    
    for string in test_strings:
        if is_palindrome(string):
            print(f"'{string}' is a palindrome.")
        else:
            print(f"'{string}' is not a palindrome.")

if __name__ == "__main__":
    main()
