###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)


def draw_snowflake(num_branches, branch_length, side_branch_length):
    drawing_turtle = turtle.Turtle()
    drawing_turtle.speed(10000)
    drawing_turtle.penup()

    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    drawing_turtle.color(red_value, green_value, blue_value)

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    for i in range(num_branches):
        drawing_turtle.goto(x, y)
        drawing_turtle.pendown()

        for i in range(10):
            # draw part of the branch
            drawing_turtle.forward(branch_length / 10)

            # draw a little side branch
            drawing_turtle.right(45)
            drawing_turtle.forward(side_branch_length)
            drawing_turtle.backward(side_branch_length)

            # draw the symmetrical little side branch
            drawing_turtle.left(90)
            drawing_turtle.forward(side_branch_length)
            drawing_turtle.backward(side_branch_length)

            # reset positioning
            drawing_turtle.right(45)

        # turn to start drawing the next branch
        drawing_turtle.right(360 / num_branches)

    drawing_turtle.penup()


for i in range(10):
    num_branches = random.randint(5, 20)
    branch_length = random.randint(20, 80)
    side_branch_length = random.randint(5, 20)
    draw_snowflake(num_branches, branch_length, side_branch_length)
