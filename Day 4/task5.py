#Task 5 is The Rock Paper Scissors game
import random #importing random
import sys #using a sys module function stops the program if an invalid input is used


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

joKenPo = [rock, paper, scissors] #storing the ascii art to a list
result = "" #result variable is empty

print("This is the Rock Paper Scissors game!")
playerInput = input("Type 0 for Rock, 1 for Paper and 2 for Scissors!:\n ")
computerChoice = random.choice(["0", "1", "2"])

# game logic
if playerInput.isnumeric() == False or int(playerInput) >= 3:
    print("error 42: invalid input")
    sys.exit() #exit function to stop the program if an invalid input is used
if playerInput == computerChoice:
    result = "That's a draw!"
if playerInput == "0":
    if computerChoice == "1":
        result = "Paper beats Rock! You Lose!"
    elif computerChoice == "2":
        result = "Rock beats Scissors! You Win!"
if playerInput == "1":
    if computerChoice == "0":
        result = "Paper beats Rock! You Win!"
    elif computerChoice == "2":
        result = "Scissors beats Paper! You Lose!"
if playerInput == "2":
    if computerChoice == "0":
        result = "Rock beats Scissors! You Lose!"
    elif computerChoice == "1":
        result = "Scissors beats Paper! You Win!"




print("You chose: ")
print(joKenPo[int(playerInput)])

print("Computer chose: ")
print(joKenPo[int(computerChoice)])

print(result)
