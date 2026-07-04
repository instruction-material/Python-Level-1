###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(100000)

red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = 0

for i in range(36):
    blue_value += 20
    drawing_turtle.color(red_value, green_value, blue_value)
    length = 20

    for j in range(15):
        length += 10

        for j in range(4):
            drawing_turtle.forward(length)
            drawing_turtle.right(90)

    drawing_turtle.right(10)
