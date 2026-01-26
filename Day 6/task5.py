# Task 5 is the Hurdle 3 challenge
# Finish the Reeborg's Hurdle Race 3 using While loops
# access: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Defines the Turn Right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Defines the Jump function so the robot can pass over the obstacle
def jump():
    turn_left() # first move() removed so it doesn't crash to the wall
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Call the functions using while and if statements properly indented
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()