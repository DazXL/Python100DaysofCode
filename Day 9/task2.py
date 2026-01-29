# Task 2 is about manipulating dictionaries
# Creating a grading program for students where it evaluates their scores and assort grades

# Dictionary with students names as key and their scores as values
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


# Every score is given a certain grade
student_grades = {}
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"

# Printing the results
for key in student_grades:
    print(key + " " + student_grades[key])