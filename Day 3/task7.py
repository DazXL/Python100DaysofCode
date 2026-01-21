# Task 7 is the Treasure Island Project
# ascii art from https://ascii.co.uk/art/treasure
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

event1 = input(f"You're at a cross road. Where do you want to go?\n     Type \"left\" or \"right\": ").lower()

if event1 == "left":
    event2 = input(f"You've arrived at a lake. There is an island in the middle of the lake.\n"
                   f"      Type \"wait\" to wait for the boat. Or type \"swim\" to swim across: ").lower()
    if event2 == "wait":
        event3 = input(f"You arrive at the island unharmed. There is a house with 3 doors.\n"
                       f"One \"red\", one \"yellow\" and one \"blue\". Which color do you choose?: ").lower()
        if event3 == "red":
            print("The room engulfs into flames and you die. Game Over.")
        elif event3 == "yellow":
            print("You found the One Piece! Congratulations! You Win!")
        elif event3 == "blue":
            print("You enter a room full of snakes. You die. Game Over.")
    elif event2 == "swim":
        print("You get attacked by an angry goose. Game Over")
    else:
        print("That's not an option. Game Over")
elif event1 == "right":
    print("You fell into a hole. Game Over.")
else:
    print("That's not an option. Game Over.")