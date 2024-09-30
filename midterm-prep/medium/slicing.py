l = [1,3,5,6,7]
print(l[2:])        # output: [5, 6, 7]
print(l[:-2])       # output: [1, 3, 5]

print(l[-1:1])      # output: []
print(l[-1:0:-1])   # output: [7, 6, 5, 3]
print(l[-1::-1])    # output: [7, 6, 5, 3, 1]
print(l[::-1])      # output: [7, 6, 5, 3, 1]
