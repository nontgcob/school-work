# Write a program that finds and prints the duplicate elements in a list.

a = [1, 1, 2, 3, 4, 4, 5]
dictionary = {}
final = []

for i in a:
    if i not in dictionary:
        dictionary[i] = 1
    # if i in dictionary: # will fail because logically, that element will be created in the dictionary and it will redundantly add one more count to it so this is logically broken
    else: # that's why we use else here
        dictionary[i] += 1

# print(dictionary)
for key, value in dictionary.items():
    if value > 1:
        # print(key, end=",")
        final.append(key)
# print()

final = str(final)
print("the duplicated elements are: " + final.strip("[").strip("]").strip())