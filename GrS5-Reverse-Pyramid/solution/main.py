###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)
drawing_turtle = turtle.Turtle()
drawing_turtle.penup()
drawing_turtle.speed(10000)

side_length = 500

for i in range(50):
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    drawing_turtle.color(red_value, green_value, blue_value)

    drawing_turtle.goto(0, 200)
    drawing_turtle.setheading(300)
    drawing_turtle.pendown()

    drawing_turtle.begin_fill()
    for j in range(3):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(120)
    drawing_turtle.end_fill()

    side_length = side_length - 10
    drawing_turtle.penup()
