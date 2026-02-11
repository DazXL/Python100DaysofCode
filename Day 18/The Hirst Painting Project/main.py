# about the painting: https://www.myartbroker.com/artist-damien-hirst/articles/damien-hirst-spot-paintings

"""
# this is used to get the color_list

import colorgram #https://pypi.org/project/colorgram.py/

rgb_colors = []
colors = colorgram.extract('image.jpg', 30) #uses the image.jpg file to get 30 color samples from it
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

#importing needed modules
import turtle
import turtle as turtle_module
import random


turtle_module.colormode(255) #needed to use rgb colors
tim = turtle_module.Turtle() #creating object
tim.speed("fastest") #speed of the turtle
tim.penup() #removes the line draw
tim.hideturtle() #removes the arrow

#this color list was extracted from the commented function above, rgb codes close to 255 or white color where removed.
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# setting the start position
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

#number of paint dots
number_of_dots = 100

#loop to draw each dot
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

#screen
screen = turtle.Screen()
screen.exitonclick()