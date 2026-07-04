###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)


def draw_shape(side_length, num_sides):
    for i in range(num_sides):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(360 / num_sides)


red_value = 0
green_value = random.randint(0, 255)
blue_value = random.randint(0, 255)
drawing_turtle.color(red_value, green_value, blue_value)

side_length = random.randint(10, 30)
num_sides = random.randint(2, 12)

for i in range(100):
    draw_shape(side_length, num_sides)
    drawing_turtle.right(10)
    side_length += 1
    red_value += 1
    drawing_turtle.color(red_value, green_value, blue_value)
