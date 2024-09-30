# Given a list of numbers, reverse the order of the list using a loop and without using built-in methods.

a = [1, 2, 3, 4, 5]
b = []
# print("line 5")
for i in range(-1, -(len(a)+1), -1):
    # print(i)
    # print(a[i])
    b.append(a[i])

print(b)