import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)

for quadrant in range(4):
    pen.color(random.randint(25, 180), random.randint(25, 180), random.randint(25, 180))
    side_length = 30
    for layer in range(3):
        for side in range(4):
            pen.forward(side_length)
            pen.right(90)
        side_length += 20
    pen.right(90)

screen.update()
print("Square Inception reference ready")
turtle.done()
