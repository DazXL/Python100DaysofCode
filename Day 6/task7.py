#Task 7 is the challenge of Reeborg's Maze

# access: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# solution to reeborg stop running in circles
while front_is_clear():
    move()


# I will return to this code during day 15 of the challenge
while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()
    if right_is_clear():
        turn_right()
