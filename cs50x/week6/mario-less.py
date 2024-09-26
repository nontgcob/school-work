# from cs50 import get_int

# get an integer from the user
# height = get_int("Height: ")
height = int(input("Height: "))

# validate the input
if height > 8 or height < 1:
    while height > 8 or height < 1:
        # height = get_int("Height: ")
        height = int(input("Height: "))

for count in range(height):
    count += 1
    print(" " * (height - count), end="")
    print("#" * count)