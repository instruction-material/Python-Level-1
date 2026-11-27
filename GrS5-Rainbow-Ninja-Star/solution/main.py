import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)


screen.colormode(255)
screen.bgcolor("black")
red = random.randint(120, 250)
green = random.randint(80, 215)
blue = 0
arms = 180


def next_channel(current):
    return (current + 2) % 256


for arm in range(arms):
    pen.color(red, green, blue)
    pen.pendown()
    pen.forward(48)
    pen.right(30)
    pen.forward(13)
    pen.left(60)
    pen.forward(24)
    pen.right(30)
    pen.penup()
    pen.goto(0, 0)
    pen.right(2)
    blue = next_channel(blue)

screen.update()
print("Rainbow Ninja Star reference ready")
turtle.done()
