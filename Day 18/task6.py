# Task 6 is creating a spirograph with turtle

import turtle as t
from turtle import Turtle
import random

tim = Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

def draw_spirograph(size):
    for x in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()