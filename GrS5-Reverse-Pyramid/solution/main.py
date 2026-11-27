import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)
pen.penup()
pen.goto(0, 65)
pen.setheading(300)
pen.pendown()

side_length = 150
for layer in range(10):
    pen.color(random.randint(25, 200), random.randint(25, 200), random.randint(25, 200))
    pen.begin_fill()
    for side in range(3):
        pen.forward(side_length)
        pen.right(120)
    pen.end_fill()
    side_length -= 15

screen.update()
print("Reverse Pyramid reference ready")
turtle.done()
