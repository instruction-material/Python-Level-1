###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)

list_of_turtles = []

# Add 25 red turtles to the list
for i in range(25):
    drawing_turtle = turtle.Turtle()
    drawing_turtle.color("red")
    drawing_turtle.speed(10000)
    list_of_turtles.append(drawing_turtle)

# Turn each turtle a random number of degrees
for drawing_turtle in list_of_turtles:
    degrees = random.randint(0, 360)
    drawing_turtle.right(degrees)

# Move each turtle forward a different random amount between 0 and 100 pixels
for turtle in list_of_turtles:
    distance = random.randint(0, 100)
    turtle.forward(distance)

# Make each turtle a different random color
for drawing_turtle in list_of_turtles:
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    drawing_turtle.color(red_value, green_value, blue_value)
