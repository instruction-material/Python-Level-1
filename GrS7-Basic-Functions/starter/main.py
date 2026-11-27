import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

screen.colormode(255)
pen.pensize(4)


def random_spot():
    pen.penup()
    pen.goto(random.randint(-95, 95), random.randint(-55, 55))
    pen.pendown()


def random_color():
    pen.color(random.randint(20, 180), random.randint(20, 180), random.randint(20, 180))


def reset():
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    pen.color("black")
    pen.pendown()


def all_random():
    random_spot()
    # TODO: Call random_color here so every new position gets a color.


reset()
for stroke in range(5):
    all_random()
    pen.forward(24)

screen.update()
print("Basic Functions workspace ready")
turtle.done()
