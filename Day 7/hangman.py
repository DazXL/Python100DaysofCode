#This is the Hangman Game Challenge
#Using everything learned so far to create a hangman game

import random
from hangman_words import word_list
from hangman_arts import logo, stages

print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
lives = 6
correct_letters = []

while not game_over:
    print(f"You have {lives} lives left")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed this letter ({guess})")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(stages[lives])
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word, you lose a life")

    if "_" not in display:
        game_over = True
        print("You guessed correctly! You win!")

    if lives == 0:
        game_over = True

        print(f"The correct word is {chosen_word}. You lose!")