# Task 4 is about Multiple Ifs
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 #total price to be paid

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Ticket price is $5.")
        bill = 5
    elif age <= 18:
        print("Ticket price is $7.")
        bill = 7
    else:
        print("Ticket price is $12.")
        bill = 12

    photo = input("Do you want to have a photon taken? Type y for Yes and n for No: ")
    if photo == "y": #a second if statement will happen regardless of the result of the code above
        bill += 3

    print(f"Your final bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")