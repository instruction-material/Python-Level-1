###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

for i in range(100):
    drawing_turtle.pendown()
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    drawing_turtle.color(red_value, green_value, blue_value)

    drawing_turtle.begin_fill()
    for i in range(6):
        drawing_turtle.right(60)
        drawing_turtle.forward(50)
    drawing_turtle.end_fill()

    drawing_turtle.penup()
    drawing_turtle.right(10)
