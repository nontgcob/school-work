# Triangle Type:
# Write a program that takes three sides of a triangle as input and determines if it is an equilateral, isosceles, or scalene triangle.

# Get the three sides of the triangle from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the input values can form a valid triangle
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    # Determine the type of triangle
    if side1 == side2 == side3:
        print("This is an equilateral triangle.")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("This is an isosceles triangle.")
    else:
        print("This is a scalene triangle.")
else:
    print("These side lengths cannot form a valid triangle.")
