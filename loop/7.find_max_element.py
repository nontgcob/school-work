# Find the Maximum Element
# Write a Python program that finds the maximum element in a list of integers using a for loop.

# Initialize a list of integers
numbers = [23, 45, 12, 67, 89, 34, 56, 78, 90, 11]

# Initialize the maximum value with the first element of the list
max_element = numbers[0]

# Find the maximum element using a for loop
for num in numbers:
    if num > max_element:
        max_element = num

# Print the result
print("The list of numbers is:", numbers)
print("The maximum element in the list is:", max_element)
