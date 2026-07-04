###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

drawing_turtle = turtle.Turtle()
drawing_turtle.shape("turtle")
drawing_turtle.color("white")
drawing_turtle.goto(0, 0)

screen = turtle.Screen()
screen.bgcolor("black")

# set up target
target = turtle.Turtle()
target.speed(1000)
target.color("aquamarine")
target.shape("circle")
target.penup()
target.goto(random.randint(-200, 200), random.randint(-200, 200))


# set up turn controls for player turtle (left/right)
def turn_left():
    drawing_turtle.left(10)


def turn_right():
    drawing_turtle.right(10)


# set up shoot function, which shoots yellow bullet (pointing in direction of the turtle) and detects if there's a hit
def shoot():
    bullet = turtle.Turtle()
    bullet.penup()
    bullet.color("yellow")
    bullet.speed(1000)
    bullet.setheading(drawing_turtle.heading())

    for i in range(300):
        bullet.forward(10)
        if (
            bullet.xcor() > target.xcor() - 10
            and bullet.xcor() < target.xcor() + 10
            and bullet.ycor() > target.ycor() - 10
            and bullet.ycor() < target.ycor() + 10
        ):
            bullet.ht()
            target.goto(random.randint(-200, 200), random.randint(-200, 200))


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(shoot, "space")
screen.listen()
