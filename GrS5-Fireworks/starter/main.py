import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)


screen.bgcolor("midnightblue")
screen.colormode(255)
length = 8
number_of_rays = 72
turn = 5

for ray in range(number_of_rays):
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    pen.color(red, green, blue)
    pen.pendown()
    pen.forward(length)
    pen.penup()
    pen.goto(0, 0)
    pen.right(turn)
    # TODO: Increase length by 1 for the next ray.

screen.update()
print("Fireworks workspace ready")
turtle.done()
