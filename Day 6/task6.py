# Task 6 is the Hurdle 4 challenge
# Finish the Reeborg's Hurdle Race 4 using While loops
# access: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Defines the Turn Right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Defines the Jump function so the robot can pass over the obstacle
#Had to perform a few while loops so the change in wall height could be into account
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

# Call the functions
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()