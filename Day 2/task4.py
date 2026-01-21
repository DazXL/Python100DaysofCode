#Task 4 is about Number Manipulation
bmi = 84 / 1.65 ** 2
print(bmi) #gives a float number.

print(int(bmi)) #gives an integer number flooring it.

print(round(bmi)) #rounds the number.

print(round(bmi, 2)) #the second argument "2" of the function, gives a float number with 2 digits after the dot.

#Assignment Operators

score = 0
print(score)
score += 5 #allows to increment 5 to the variable instead of needing to type score = score + 5
print(score)

score -= 2 # subtracts
score *= 4 # multiplies
score /= 2 # divide

#f-Strings

print(f"your score is: {score}") #the f in front of the string allows to add a variable inside the brackets

isWinning = True
print(f"Are you winning? {isWinning}")
