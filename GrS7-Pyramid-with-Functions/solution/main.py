###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)


def draw_triangle(side_length):
    for i in range(3):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(120)


side_length = 10

for i in range(50):
    drawing_turtle.penup()
    drawing_turtle.goto(0, 200)
    drawing_turtle.setheading(300)
    drawing_turtle.pendown()

    draw_triangle(side_length)
    side_length = side_length + 10
