from math import radians, sin

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

def ring_color(index):
    if index % 2 == 0:
        return "crimson"
    return "white"


def draw_target(rings):
    for ring in range(rings):
        radius = 70 * (rings - ring) / rings
        pen.penup()
        pen.goto(0, -radius)
        pen.setheading(5)
        pen.color(ring_color(ring))
        pen.pendown()
        pen.begin_fill()
        for edge in range(36):
            pen.forward(2 * radius * sin(radians(5)))
            pen.left(10)
        pen.end_fill()


draw_target(5)

screen.update()
print("Bullseye with Nested Loops reference ready")
turtle.done()
