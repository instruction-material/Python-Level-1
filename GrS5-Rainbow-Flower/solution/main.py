import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)

for petal in range(6):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(60 * petal)
    pen.pendown()

    red = random.randint(60, 200)
    green = random.randint(20, 120)
    blue = 0
    angle = 0
    for step in range(40):
        pen.color(red, green, blue)
        pen.forward(10)
        pen.right(angle)
        angle += 1
        blue += 5

screen.update()
print("Rainbow Flower reference ready")
turtle.done()
