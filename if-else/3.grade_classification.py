# Grade Classification:
# Write a Python program that takes a student's score as input and classifies the grade according to the following:

# 90 and above: A
# 80 to 89: B
# 70 to 79: C
# 60 to 69: D
# Below 60: F

try:
    score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"The student's grade is: {grade}")
    else:
        print("Error: Score must be between 0 and 100.")
except ValueError:
    print("Error: Please enter a valid numeric score.")
