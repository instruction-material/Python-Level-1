import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)


def place(x, y, heading=0):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()


def polygon(sides, length, turn):
    for step in range(sides):
        pen.forward(length)
        pen.left(turn)


screen.colormode(255)
sky = (random.randint(175, 255), random.randint(175, 255), random.randint(175, 255))
screen.bgcolor(*sky)
side_length = random.randint(45, 100)

for heading, color in [(-30, "teal"), (150, "darkviolet")]:
    place(0, 0, heading)
    pen.color(color)
    pen.begin_fill()
    polygon(3, side_length, 120)
    pen.end_fill()

screen.update()
print("Random Bowtie reference ready")
turtle.done()
