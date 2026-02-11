# Task 1 is about how to use the turtle module
# access: https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(25)


screen = Screen()
screen.exitonclick()