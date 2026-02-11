# Task 4 is drawing several polygonal shapes on the screen with turtle

import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255) #to be able to use rgb colors

#random color function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# function to draw polygons
def draw_shape():
    sides = 3
    while sides < 11:
        tim.color(random_color())
        for i in range(sides):
            tim.forward(100)
            tim.right(360 / sides)
        sides += 1


draw_shape()

screen = Screen()
screen.exitonclick()