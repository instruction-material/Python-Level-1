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
sky = (228, 228, 228)  # TODO: Generate three independent channels from 175 to 255.
screen.bgcolor(*sky)
side_length = 60  # TODO: Use one random length for both halves.

for heading, color in [(-30, "teal")]:  # TODO: Add a second triangle rotated by 180 degrees.
    place(0, 0, heading)
    pen.color(color)
    pen.begin_fill()
    polygon(3, side_length, 120)
    pen.end_fill()

screen.update()
print("Random Bowtie workspace ready")
turtle.done()
