# Create a program where the user has to guess a random number between 1 and 100, and the program gives hints ("Too high" or "Too low"). Use a loop and try-except for input validation.

import random
random_number = random.randint(0, 100)
# print(random_number)
while True:
    input_num = int(input("input a number: "))
    if input_num > random_number:
        print("too high")
    elif input_num < random_number:
        print("too low")
    # if input_num == random_number:
    else:
        print(random_number, "is the random number")
        print("congrats")
        break