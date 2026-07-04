###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
race_turtle_two = turtle.Turtle()
screen = turtle.Screen()


def turn_left1():
    drawing_turtle.left(10)


def turn_right1():
    drawing_turtle.right(10)


def turn_left2():
    race_turtle_two.left(10)


def turn_right2():
    race_turtle_two.right(10)


def check_collision():
    if (
        abs(drawing_turtle.xcor() - race_turtle_two.xcor()) < 10
        and abs(drawing_turtle.ycor() - race_turtle_two.ycor()) < 10
    ):
        drawing_turtle.write("Collision!")
        drawing_turtle.color(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        )
        race_turtle_two.color(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        )


screen.onkey(turn_left1, "Left")
screen.onkey(turn_right1, "Right")
screen.onkey(turn_left2, "a")
screen.onkey(turn_right2, "d")
screen.listen()

# start turtles at a random location
drawing_turtle.penup()
race_turtle_two.penup()
drawing_turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
race_turtle_two.goto(random.randint(-200, 200), random.randint(-200, 200))
drawing_turtle.pendown()
race_turtle_two.pendown()
race_turtle_two.color("blue")

# both turtles continuously move and check for collisions
while True:
    drawing_turtle.forward(1)
    race_turtle_two.forward(1)
    check_collision()
