# Linear Search algorithm (finding the target element in an array)
# Time complexity: O(n)
arr = [10, 23, 45, 70, 11, 15]
target = 70

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print(f"Element not found")