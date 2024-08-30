# Reverse a String
# Write a recursive function reverse_string(s) that takes a string s and returns the string in reverse.

def reverse_string(s):
    # Base case: if the string is empty or has only one character, return it
    if len(s) <= 1:
        return s
    
    # Recursive case: return the last character + reverse of the rest of the string
    return s[-1] + reverse_string(s[:-1])

# Example usage
def main():
    input_string = "Hello, World!"
    result = reverse_string(input_string)
    print(f"The reverse of '{input_string}' is: '{result}'")

if __name__ == "__main__":
    main()
