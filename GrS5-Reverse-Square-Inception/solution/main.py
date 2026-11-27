import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)

for quadrant in range(4):
    side_length = 72
    for layer in range(3):
        low = 20 + 60 * layer
        pen.color(random.randint(low, low + 38), random.randint(low, low + 38),
                  random.randint(low, low + 38))
        pen.begin_fill()
        for side in range(4):
            pen.forward(side_length)
            pen.right(90)
        pen.end_fill()
        side_length -= 20
    pen.right(90)

screen.update()
print("Reverse Square Inception reference ready")
turtle.done()
