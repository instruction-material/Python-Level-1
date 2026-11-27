import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)


def place(x, y, heading=0):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()


def polygon(sides, length, turn):
    for step in range(sides):
        pen.forward(length)
        pen.left(turn)


screen.colormode(255)
x = -60  # TODO: Choose a random x in the supplied range.
y = -60  # TODO: Choose y independently.
side_length = 40  # TODO: Choose a length from 28 through 80.
red, green, blue = 40, 112, 155  # TODO: Use three independent channel draws.

place(x, y)
pen.color(red, green, blue)
pen.begin_fill()
polygon(4, side_length, 90)
pen.end_fill()

screen.update()
print("Surprise Me Square workspace ready")
turtle.done()
