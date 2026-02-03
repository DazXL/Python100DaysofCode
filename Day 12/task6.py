# Task 6 is the Guess The Number project
import random

logo = r"""
   _____                  _______ _          _   _                 _               
  / ____|                |__   __| |        | \ | |               | |              
 | |  __ _   _  ___  ___ ___| |  | |__   ___|  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| |  | '_ \ / _ \ . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ |  | | | |  __/ |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/_|  |_| |_|\___|_| \_|\__,_|_| |_| |_|_.__/ \___|_|   

                                                                                   """

game_over = r"""
   _____                       ____                 
  / ____|                     / __ \                
 | |  __  __ _ _ __ ___   ___| |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|\____/  \_/ \___|_|   

                                                    """

you_win = r"""
 __     __          __          ___         _ _ _ 
 \ \   / /          \ \        / (_)       | | | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __   | | | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \  | | | |
    | | (_) | |_| |    \  /\  /  | | | | | |_|_|_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_| (_|_|_)

                                                  """

# Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against user input, returns number of turns remaining"""

    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1

    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1

    else:
        print(f"You guessed the number!! {actual_answer}!!")
        print(you_win)
        return

def difficulty():
    """Select difficulty level"""
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS

    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("this is not a difficulty")
        return 1


def game():
    """game logic"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    # print(number) #reveals the number for cheating

    turns = difficulty() # calls difficult function

    # main game loop
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns) # calls function to check the answer

        if turns == 0: # as turns reaches 0 is game over
            print("You've run out of guesses, you lose.")
            print(game_over)
            return
        elif guess != number: # if guessed wrong
            print("Guess again.")


game() # Starts the game