from sys import argv
from csv import reader, DictReader

sequences = {}

# input validation
if len(argv) != 3: # check if the user input is correct
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1) # error code 1

# get maximum number of STR sequence
# (a function that, given both a DNA sequence and an STR as inputs
# , returns the maximum number of times that the STR repeats)


def getMax(dna, STR):
    i = 0
    j = len(STR)
    maximum = 0
    for x in range(len(dna)):
        if dna[i:j] == STR:
            temp = 0
            while dna[i:j] == STR:
                temp += 1
                i += len(STR)
                j += len(STR)
                if temp > maximum:
                    maximum = temp
        else:
            i += 1
            j += 1
    return maximum


# open CSV file and read its contents into memory
with open(argv[1], "r") as peopleCsvFile:
    peopleReader = reader(peopleCsvFile)
    for row in peopleReader:
        header = row
        header.pop(0) # remove the first element
        for item in header:
            sequences[item] = 0 # initialize the dictionary with 0
        break

# open the DNA sequence and read its contents into memory
with open(argv[2], "r") as dnaFile:
    dna = dnaFile.read()

# give sequence keys value from max function
for key in sequences:
    ans = getMax(dna, key)
    sequences[key] = ans

# print person if found
with open(argv[1], "r") as peopleCsvFile:
    people = DictReader(peopleCsvFile)
    for person in people:
        match = 0
        for key in sequences:
            if int(person[key]) == sequences[key]:
                match += 1
        if match == len(sequences):
            print("match:", match)
            print("sequences:", sequences)
            print("person:", person)
            print(person["name"])
            exit(0)

    print("No match")