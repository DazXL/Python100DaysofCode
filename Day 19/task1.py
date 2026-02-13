# Task 1 is about higher order function
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(100)



screen.listen() # this function let the application detect actions in it like click or key presses
screen.onkey(move_forwards, "space") #The .onkey() function is a function that uses another function as parameter
screen.exitonclick()
