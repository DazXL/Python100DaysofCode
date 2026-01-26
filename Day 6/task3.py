# Reeborg's Hurdle Race Challenge

# Access in: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Move the robot using the functions available and define your own functions to move Reeborg to the Flag

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


# Call the functions using a For loop
for step in range(6):
    jump()