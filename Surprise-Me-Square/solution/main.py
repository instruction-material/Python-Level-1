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
x = random.randint(-125, 45)
y = random.randint(-125, 45)
side_length = random.randint(28, 80)
red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

place(x, y)
pen.color(red, green, blue)
pen.begin_fill()
polygon(4, side_length, 90)
pen.end_fill()

screen.update()
print("Surprise Me Square reference ready")
turtle.done()
