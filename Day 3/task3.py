#Task 3 is about Nesting and Elif

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Checking if they can ride the rollercoaster and their age to find out how much they need to pay.
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12: # Nested if statement
        print("Please pay $5")
    elif age <= 18: # Use of Else If, a second condition is compared after the first one being False
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")