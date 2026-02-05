#This is the Higher or Lower Project
#Guessing which profile has more followers on instagram

import random
from game_data import data
from art import *

"""--------------Comparing followers function-------------------"""
def compare(player_answer, other_answer):

    if player_answer['follower_count'] > other_answer['follower_count']:
        return False

    elif player_answer['follower_count'] < other_answer['follower_count']:
        return True
    else:
        print("They're the same! How odd!")
        return False

"""------------------Game main logic----------------------"""
def game():
    score = 0
    game_over = False
    choice_b = random.choice(data)
    while not game_over:
        choice_a = choice_b
        choice_b = random.choice(data)

        while choice_a == choice_b:
            choice_b = random.choice(data)

        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"{choice_a['name']}, {choice_a['description']}, from {choice_a['country']}")

        print(vs)

        print(f"{choice_b['name']}, {choice_b['description']}, from {choice_b['country']}")

        """For debugging purposes"""
        #print(choice_a['follower_count'])
        #print(choice_b['follower_count'])
        """----------------------------"""

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        other_answer = ""
        if answer == "a":
            answer = choice_a
            other_answer = choice_b

        elif answer == "b":
            answer = choice_b
            other_answer = choice_a

        else: # for invalid inputs
            print("Please type 'A' or 'B'.")
            game()

        result = compare(answer, other_answer)
        if result:
            print(f"You're wrong! Final score: {score} - Game over... ")
            game_over = True
        else:
            score += 1

game()