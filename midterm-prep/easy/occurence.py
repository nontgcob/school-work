# Write a Python program to count how many times a given element appears in a list.
def count_element(list, element):
    count = 0
    for i in list:
        if i == element:
            count = count + 1
    return count

# Test cases
print(count_element([1, 2, 3, 4, 5, 2, 2], 2)) # 3