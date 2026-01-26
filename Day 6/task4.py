#Task 4 is the While Loops
# Finish the Reeborg's Hurdle Race 2 using While loops

# access: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Defines the Turn Right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Defines the Jump function so the robot can pass over the obstacle
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Call the functions using While loop
while not at_goal():
    jump()