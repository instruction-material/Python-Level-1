import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)

for x, y in [(-98, -55), (0, -55), (98, -55), (-98, 55), (0, 55), (98, 55)]:
    pen.penup()
    pen.goto(x + random.randint(-8, 8), y + random.randint(-8, 8))
    pen.setheading(0)
    pen.color(random.randint(25, 180), random.randint(25, 180), random.randint(25, 180))
    pen.pendown()
    length = random.randint(2, 6)
    for step in range(32):
        pen.forward(length)
        pen.left(123)
        length += 1

screen.update()
print("Spirals reference ready")
turtle.done()
