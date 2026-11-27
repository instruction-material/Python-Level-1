import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

screen.colormode(255)
pen.penup()


def move_forward():
    pen.forward(12)
    screen.update()


def move_backward():
    pen.forward(-12)
    screen.update()


def turn_left():
    pen.left(30)
    screen.update()


def turn_right():
    pen.right(30)
    screen.update()


def stamp_dot():
    size = 12  # TODO: Pick a different allowed size on each call.
    pen.color(random.randint(20, 180), random.randint(20, 180), random.randint(20, 180))
    pen.dot(size)
    screen.update()
    print("Dot stamped")


def tap_dot(x, y):
    pen.goto(x, y)
    stamp_dot()


screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(stamp_dot, "space")
screen.onclick(tap_dot)
screen.listen()

screen.update()
print("Polka Dot Game workspace ready")
turtle.done()
