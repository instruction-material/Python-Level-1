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


def region(x, y):
    if x > 0 and y > 0:
        return "I", "royalblue"
    elif x < 0 and y > 0:
        return "II", "darkgoldenrod"
    elif x < 0 and y < 0:
        return "III", "forestgreen"
    elif x > 0 and y < 0:
        return "IV", "darkorange"
    else:
        return "axis", "black"


def outside_box(x, y):
    return abs(x) > 100 or abs(y) > 100


x = random.randint(-125, 125)
y = random.randint(-125, 125)
place(x, y)
name, color = region(pen.xcor(), pen.ycor())
pen.color(color)
if outside_box(x, y):
    pen.circle(12)
else:
    polygon(4, 20, 90)
print("Point:", x, y, "Region:", name)

screen.update()
print("Find Your Turtle reference ready")
turtle.done()
