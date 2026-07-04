###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)
drawing_turtle = turtle.Turtle()
drawing_turtle.penup()

# set random color
red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = random.randint(0, 255)
drawing_turtle.color(red_value, green_value, blue_value)

# set random side length
side_length = random.randint(0, 200)

# set random starting position
x = random.randint(-300, 300)
y = random.randint(-300, 300)
drawing_turtle.goto(x, y)

# draw square
drawing_turtle.pendown()
drawing_turtle.begin_fill()
for i in range(4):
    drawing_turtle.forward(side_length)
    drawing_turtle.right(90)
drawing_turtle.end_fill()

drawing_turtle.penup()
