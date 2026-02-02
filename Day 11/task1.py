import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# cards list correspond to the value of the cards, Ace is 11 and J Q K are 10 each
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]


def play_again():
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer == "y":
        game()
    else:
        print("good bye!")

def game():
    # Game variables
    keep_playing = False
    dealer_turn = False
    player_hand = []
    dealer_hand = []
    more_cards = ""

    # Pulling players cards
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    player_score = sum(player_hand)

    # Pulling dealers cards
    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    dealer_score = sum(dealer_hand)

    print(logo + "\n")

    # If the player pulls two aces(11) he chooses what score he will have.
    if player_score == 22:
        print("Two Aces!")
        two_aces = input("which score you want to keep? type '1' for score of '2' or 2 for score of 12: ")
        if two_aces == "1":
            player_hand = [1, 1]
            player_score = sum(player_hand)
        elif two_aces == "2":
            player_hand = [11, 1]
            player_score = sum(player_hand)

    #randomizes the computer choice when it gets two aces.
    if dealer_score == 22:
        choice_of_hand = [[11,1], [1,1], [1,11]]
        dealer_hand = random.choice(choice_of_hand)
        dealer_score = sum(dealer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    # If the player scores a natural blackjack
    if player_score == 21:
        print("That's a blackjack! You win!")
        answer = input("Do you want to play again? (y/n): ").lower()
        if answer == "y":
            game()
        else:
            return
    elif dealer_score == 21:
        print("The dealer got a blackjack! You lose!")
    else:
        more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if more_cards == "y":
        keep_playing = True
    else:
        dealer_turn = True

    #Player's Turn
    while keep_playing and player_score < 21:
        player_hand.append(random.choice(cards))
        player_score = sum(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")

        if player_score > 21:
            keep_playing = False
        else:
            print(f"Dealer's first card: {dealer_hand[0]}")
            more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if more_cards == "n":
                print("Let's see those results:")
                keep_playing = False
                dealer_turn = True
    # end of the Loop

    # Dealer's turn
    while dealer_turn:
        if dealer_score > player_score:
            dealer_turn = False

        if dealer_score < 17:
            print(f"Current Dealer's hand: {dealer_hand}, total score of {dealer_score}")
            print("Dealer starts pulling cards...")
            dealer_hand.append(random.choice(cards))
            dealer_score = sum(dealer_hand)
            print(f"Current Dealer's Hand is {dealer_hand}, with a total score of {dealer_score}")

            if dealer_score > player_score:
                print(f"Dealer will not pull more cards...")
                dealer_turn = False

        else:
            print(f"Dealer will not pull more cards...")
            dealer_turn = False
    #end of the loop

    # Check the Score

    if player_score == 21:
        if dealer_score == 21:
            print(f"Player's hand is {player_hand}, with a total score of {player_score}")
            print(f"Dealer's hand is {dealer_hand}, with a total score of {dealer_score}")
            print("Draw! Thank you for playing")
            play_again()
        else:
            print(f"Player's hand is {player_hand}, with a total score of {player_score}")
            print(f"Dealer's hand is {dealer_hand}, with a total score of {dealer_score}")
            print("You Win!")
            play_again()


    elif player_score == dealer_score:
        print(f"Player's hand is {player_hand}, with a total score of {player_score}")
        print(f"Dealer's hand is {dealer_hand}, with a total score of {dealer_score}")
        print("Draw! Thank you for playing")

        play_again()

    elif player_score > 21:
        print("You score above 21!")
        print(f"Player's hand is {player_hand}, with a total score of {player_score}")
        print(f"Dealer's hand is {dealer_hand}, with a total score of {dealer_score}")
        print("You Lose!")

        play_again()

    elif dealer_score > 21:
        print(f"Player's hand is {player_hand}, with a total score of {player_score}")
        print(f"Dealer's hand is {dealer_hand}, with a total score of {dealer_score}")
        print("You Win!")
        play_again()

    elif player_score > dealer_score:
        print(f"Player's hand is {player_hand}, with a total score of {player_score}")
        print(f"Dealer's hand is {dealer_hand}, with a total score of {dealer_score}")
        print("You Win!")

        play_again()

    else:
        print(f"Player's hand is {player_hand}, with a total score of {player_score}")
        print(f"Dealer's hand is {dealer_hand}, with a total score of {dealer_score}")
        print("You Lose!")
        play_again()

game()

