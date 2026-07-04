###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# Explain what a function is:
#
# What are the two parts of a function? What do they each do?
#
# Define a function that draws a square with a side length of 50

import turtle

turtle.colormode(255)
drawing_turtle = turtle.Turtle()


def draw_square():
    for i in range(4):
        drawing_turtle.forward(50)
        drawing_turtle.right(90)


# Call your function

draw_square()

# Call your function 2 more times in different locations

drawing_turtle.penup()
drawing_turtle.goto(-100, 100)
drawing_turtle.pendown()
draw_square()

drawing_turtle.penup()
drawing_turtle.goto(100, -100)
drawing_turtle.pendown()
draw_square()
