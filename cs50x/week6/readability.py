# from cs50 import get_string

# get input from the user
# s = get_string("Text: ")
s = str(input("Text: "))

# calculate the number of CHARACTERS
letter = 0
for a in range(len(s)):
    if s[a] != " " and s[a] != "." and s[a] != "!" and s[a] != "?" and s[a] != "'" and s[a] != ",":
        letter += 1
print(f"Number of character: {letter}")

# calculate number of WORDS
word = 1
for c in range(len(s)):
    if s[c] == " ":
        word += 1
print(f"Number of word: {word}")

# calculate number of SENTENCES
sen = 0
for e in range(len(s)):
    if s[e] == "." or s[e] == "!" or s[e] == "?":
        sen += 1
print(f"Number of sentence: {sen}")

# grade calculation
L = (letter * 100.0) / word # L is the average number of letters per 100 words in the text
S = (sen * 100.0) / word    # S is the average number of sentences per 100 words in the text

print(f"We have {L} characters / 100 words.")
print(f"We have {S} sentences / 100 words.")

# real calculating
index = 0.0
index = 0.0588 * L - 0.296 * S - 15.8 # calculation formula for the Coleman-Liau index

# reporting grade
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {int(round(index))}")