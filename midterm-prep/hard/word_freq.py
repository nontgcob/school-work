# Write a program that takes a sentence as input and returns a dictionary with the frequency of each word in the sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print(type(words))
print(words)
dictionary = {}
for word in words:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
print(dictionary)
# Output:
# Enter a sentence: hello world hello
# {'hello': 2, 'world': 1}
