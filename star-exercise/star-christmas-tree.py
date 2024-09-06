# generates a christmas tree with stars
layers = 14
for i in range(1, layers+1):
    print(' ' * int((layers+1)*1.02 - i) + '*' * (2 * i - 1)) # use either int() or round() will do
    # print(2 * i - 1)

print()

for j in range(1, layers+1):
    # print(' ' * int((layers+1)*(1.6*1.02) - j) + '* ' * (2 * j - 1))
    print(' ' * int((layers+1)*(1.6) - j) + ' ' * int((layers+1)*(1.2) - j) + '* ' * (2 * j - 1))

print(len("                                                                                                                  "))

for k in range(1, layers+1):
    # print(' ' * round(114 - (k*2)) + '* ' * (2 * k - 1))
    print(' ' * int(114 - (k*2)) + '* ' * (2 * k - 1))