#Task 5 is a little project for a Tip Calculator

#Presentation and variables to be used
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#Mathematical operations learned
billPlusTip = bill * (1 + tip / 100)
billPerPerson = billPlusTip / people
finalAmount = round(billPerPerson, 2)

#End Result
print(f"Each person should pay ${finalAmount}")

