''' Task 3 is about Dictionary Comprehension '''
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Generating a dictionary from the list of students and giving it random scores
students_scores = {student:random.randint(1,100) for student in names}

print(students_scores)

#creating a new dictionary from the student_scores where only the ones with scores higher than 60 are added

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(passed_students)