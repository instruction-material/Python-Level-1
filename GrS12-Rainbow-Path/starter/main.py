import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

colors = ["crimson", "darkorange", "goldenrod", "seagreen", "teal", "royalblue", "purple"]
pen.penup()
pen.goto(-100, -22)
pen.pensize(5)
pen.pendown()

for color in colors[:1]:  # TODO: Visit every color in the palette.
    pen.color(color)
    pen.setheading(random.randint(-20, 20))
    pen.forward(24)

print("Palette:", colors)

screen.update()
print("Rainbow Path workspace ready")
turtle.done()
