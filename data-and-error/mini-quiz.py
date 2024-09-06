# generate a list of numbers from 5 to 15 using the range() function and loop through it
numero_lista = []
for i in range(5, 15+1):
    numero_lista.append(i)

print(numero_lista)

# list_name.append(new_item)

# print the value of pi to two decimal places using formatted strings, provide an example using print(f"...")
pi = 22/7
print(f"{pi:.2f}")

# using formatted strings, print the number 123.456789 rounded to three decimal places
number = 123.456789
print(f"{number:.3f}")

# create a simple function
def hello_world():
    print("Hello, World!")