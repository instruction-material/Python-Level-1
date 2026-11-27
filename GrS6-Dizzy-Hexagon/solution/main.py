import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)
for index in range(100):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(index * 12)
    pen.forward(index / 4)
    pen.color(random.randint(20, 160), random.randint(20, 140), random.randint(80, 210))
    pen.pendown()
    length = 18 + index // 4
    for side in range(6):
        pen.forward(length)
        pen.right(60)

screen.update()
print("Dizzy Hexagon reference ready")
turtle.done()
