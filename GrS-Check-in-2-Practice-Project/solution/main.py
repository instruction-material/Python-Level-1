###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

ball = turtle.Turtle()
ball.penup()
ball.goto(random.randint(-300, 300), random.randint(-300, 300))
ball.shape("circle")
ball.color("red")

drawing_turtle = turtle.Turtle()
drawing_turtle.penup()
drawing_turtle.goto(0, 0)
drawing_turtle.shape("turtle")
drawing_turtle.color("blue")


def aim():
    drawing_turtle.pendown()
    drawing_turtle.forward(300)


screen = turtle.Screen()
screen.onkey(aim, "space")
screen.listen()

while True:
    # only spins when the turtle hasn't moved
    if drawing_turtle.xcor() == 0 and drawing_turtle.ycor() == 0:
        drawing_turtle.left(10)
    else:
        break
