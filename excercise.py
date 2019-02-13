# Define a function that accepts a percentage as an argument and returns a letter grade (A+, A, A-, B+, etc) for that percentage.
#
# Prompt your user to enter a percentage and display a message showing them the equivalent letter grade.

def letter_grade(grade_percentage):
    if grade_percentage >= 90:
        print("You got an A+!")
    elif grade_percentage >= 80:
        print("You got an A!")
    elif grade_percentage >= 70:
        print("You got a B!")
    elif grade_percentage >= 60:
        print("You got a C!")
    elif grade_percentage >= 50:
        print("You got a D!")
    elif grade_percentage < 50:
        print("You got an F")


print("Enter your the percentage you got on the test")
grade_percentage = int(input())
