# Task 2 is a challenge using For Loop to explain certain python functions

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
totalExamScore = sum(student_scores)
print(totalExamScore)

# The sum() function could be explained using a for loop

scoreSum = 0
for score in student_scores:
    scoreSum += score
print(scoreSum) # Should be equal to sum(student_scores)

#How does the max() function work using for?

scoreList = [8, 65, 89, 86, 55, 91, 64, 89]
scoreMax = max(scoreList)
print(scoreMax)

# Using the For Loop:

maxScore = 0
for value in scoreList:
    if value > maxScore:
        maxScore = value

print(maxScore) # Should be equal to max(scoreList).
