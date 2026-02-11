# Task 3 is making the Turtle to draw a dashed line
from turtle import Turtle, Screen

tim = Turtle()
test = True
test2 = False

# this will cause an infinite loop, but I don't care
while test:
    tim.forward(10)
    tim.pu()
    test2 = True
    while test2:
        tim.forward(10)
        tim.pd()
        test2 = False




screen = Screen()
screen.exitonclick()
