def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Test cases
divide_numbers(10, 2)
divide_numbers("5", "0")
divide_numbers(10, 0)