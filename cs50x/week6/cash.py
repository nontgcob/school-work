# from cs50 import get_float

# ask for an input
while True:
    # d = get_float("Change owed($): ")
    d = float(input("Change owed($): "))
    if d > -1: # check if the input is positive
        break # if positive, then break out of the loop

# convert dollars to cents
c = round(d * 100)
print(f"Equal to: {c} cents")

# calculate number of coins
coin = 0
while c > 24:
    c -= 25
    coin += 1
while c > 9 and c < 25:
    c -= 10
    coin += 1
while c > 4 and c < 10:
    c -= 5
    coin += 1
while c > 0 and c < 5:
    c -= 1
    coin += 1

# output the report
print(f"{coin} coins")