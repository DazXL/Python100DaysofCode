# task 5 is the random walk using turtle
# https://en.wikipedia.org/wiki/Random_walk

import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]
tim.speed("fastest")
tim.width(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# This will cause an infinite loop, but I don't care
def random_walk():
    while True:
        tim.color(random_color())
        tim.forward(50)
        tim.setheading(random.choice(directions))

random_walk()



screen = Screen()
screen.exitonclick()