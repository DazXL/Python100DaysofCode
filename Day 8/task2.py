# Task 2 is creating a Life in weeks calculator function
# It calculates how many weeks you have left to until reach 90 years old

def life_in_weeks(currentAge):
    yearsLeft = 90 - currentAge
    x = yearsLeft * 52
    print(f'You have {x} weeks left.')

age = int(input("What is your current age?"))
life_in_weeks(age)