#Task 4 is the Password Generator Challenge
#There is the Easy Mode and Hard Mode

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#The Easy level will make a password with letters then symbols, then numbers in that order

print("This is the Easy Mode")

passwordList = []

# Randomizes the amount of letters chose by the user
for nrLetters in range(1, nr_letters + 1):
    passwordList.append(random.choice(letters))

# Randomizes the amount of symbols chose by the user
for nrSymbols in range(1, nr_symbols + 1):
    passwordList.append(random.choice(symbols))

# Randomizes the amount of numbers chose by the user
for nrNumbers in range(1, nr_numbers + 1):
    passwordList.append(random.choice(numbers))

finalPassword = "".join(passwordList)
print(finalPassword)

#The Hard level will generate a password with the letters, symbols and numbers in a random order.
print("This is the Hard Mode")
passwordListHard = []

# Randomizes the amount of letters chose by the user
for nrLetters in range(1, nr_letters + 1):
    passwordListHard.append(random.choice(letters))

# Randomizes the amount of symbols chosen by the user
for nrSymbols in range(1, nr_symbols + 1):
    passwordListHard.append(random.choice(symbols))

# Randomizes the amount of numbers chosen by the user
for nrNumbers in range(1, nr_numbers + 1):
    passwordListHard.append(random.choice(numbers))

# Randomizes the list content to generate the final password
passwordRandomize = random.sample(passwordListHard, len(passwordListHard))
finalPassword = "".join(passwordRandomize) # Stringify the randomized password
print(finalPassword)
