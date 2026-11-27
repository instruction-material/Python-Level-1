import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)


screen.colormode(255)


def spiral(side, increase, limit):
    counter = 0
    while counter < limit:
        pen.color(random.randint(20, 200), random.randint(20, 200), random.randint(20, 200))
        pen.forward(side)
        pen.right(90)
        side += increase
        counter += 1
    return counter, side


sides_drawn, next_side = spiral(10, 5, 50)
print("Sides:", sides_drawn, "Next length:", next_side)

screen.update()
print("Square Spiral reference ready")
turtle.done()
