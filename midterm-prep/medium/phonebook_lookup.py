# Create a dictionary that stores names as keys and phone numbers as values. Write a program that searches for a phone number by name.

phonebook = {
    "John": "123-456-7890",
    "Jane": "987-654-3210",
    "Jim": "555-555-5555"
}
name = input("Enter a name: ")
if name in phonebook:
    print(phonebook[name])
else:
    print("Name not found")
#midterm-prep/easy/sum_of_squares.py