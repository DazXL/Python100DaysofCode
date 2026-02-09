""" Constructing Objects and accessing their attributes and methods """

import turtle #import the turtle module

charlin = turtle.Turtle() #create an object from the module

print(charlin)

#calling methods of an object
charlin.shape("turtle")
charlin.forward(100) #giving values to attributes of the method


my_screen = turtle.Screen() #screen object
print(my_screen.canvheight) #shows screen height(attribute) in pixels
my_screen.exitonclick() #leaves the screen up unless you click




