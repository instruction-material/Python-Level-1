import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

pen.color("steelblue")


def draw_flake(x, y, arms, length, twig):
    for arm in range(arms):
        pen.penup()
        pen.goto(x, y)
        pen.setheading(360 * arm / arms)
        pen.pendown()
        for step in range(5):
            pen.forward(length / 5)
            pen.right(45)
            pen.forward(twig)
            pen.forward(-twig)
            pen.left(90)
            pen.forward(twig)
            pen.forward(-twig)
            pen.right(45)


for y in (-54, 54):
    for x in (-100, 0, 100):
        arms = random.randint(5, 7)
        length = random.randint(20, 38)
        twig = random.randint(4, 7)
        draw_flake(x, y, 6, 24, 5)  # TODO: Pass the three sampled values.

screen.update()
print("Winter Wonderland workspace ready")
turtle.done()
