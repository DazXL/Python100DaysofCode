# Task 4 is the Love calculator

def calculate_love_score(name1, name2):
    var1 = "TRUE"
    var2 = "LOVE"
    names = (name1 + name2).upper()
    trueScore = 0
    loveScore = 0
    for letter in names:
        for match in var1:
            if letter == match:
                trueScore += 1
        for match2 in var2:
            if letter == match2:
                loveScore += 1
    trueLoveScore = str(trueScore) + str(loveScore)
    print(trueLoveScore)

print("Lets calculate your Love with The True Love Calculator!")
yours = input("What is your name?: ")
theirs = input("What is their name?: ")

calculate_love_score(yours, theirs)

