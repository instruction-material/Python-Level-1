###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

side = 10

counter = 0
while counter < 50:
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    drawing_turtle.color(red_value, green_value, blue_value)

    drawing_turtle.forward(side)
    drawing_turtle.right(90)

    side = side + 5
    counter += 1
