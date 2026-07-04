###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

# to make the starting direction for each petal easier to implement, we create a variable degreesToTurn that goes 0, 60, 120, 180 etc. thus, after we goto(0,0), we always point toward the right and then turn by this amount
degrees_to_turn = 0

for i in range(6):
    drawing_turtle.penup()
    drawing_turtle.goto(0, 0)
    drawing_turtle.setheading(0)
    drawing_turtle.right(degrees_to_turn)
    drawing_turtle.pendown()

    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = 0

    angle = 0

    for j in range(40):
        drawing_turtle.color(red_value, green_value, blue_value)
        drawing_turtle.forward(10)
        drawing_turtle.right(angle)

        angle = angle + 1
        blue_value = blue_value + 5

    degrees_to_turn += 60
