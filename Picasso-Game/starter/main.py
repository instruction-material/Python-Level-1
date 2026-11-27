import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

screen.colormode(255)
pen.hideturtle()


def start_mark():
    pen.penup()
    pen.goto(random.randint(-75, 75), random.randint(-45, 40))
    pen.setheading(0)
    pen.color(random.randint(20, 180), random.randint(20, 180), random.randint(20, 180))
    pen.pendown()


def draw_square():
    start_mark()
    for edge in range(4):
        pen.forward(28)
        pen.right(90)
    screen.update()
    print("Square drawn")


def draw_octagon():
    start_mark()
    for edge in range(8):
        pen.forward(12)
        pen.right(45)
    screen.update()
    print("Octagon drawn")


def draw_burst():
    start_mark()
    x, y = pen.xcor(), pen.ycor()
    for ray in range(12):
        pen.forward(22)
        pen.penup()
        pen.goto(x, y)
        pen.right(30)
        pen.pendown()
    screen.update()
    print("Burst drawn")


def draw_circle():
    start_mark()
    pen.circle(16)
    screen.update()
    print("Circle drawn")


def tap_mark(x, y):
    if y >= 0:
        if x < 0:
            draw_square()
        else:
            draw_octagon()
    elif x < 0:
        draw_burst()
    else:
        draw_circle()


screen.onkey(draw_square, "Up")
screen.onkey(draw_octagon, "Down")
screen.onkey(draw_burst, "Left")
# TODO: Bind the Right arrow to the circle callback.
screen.onclick(tap_mark)
screen.listen()

screen.update()
print("Picasso Game workspace ready")
turtle.done()
