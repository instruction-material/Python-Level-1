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


place(-40, -40)
polygon(4, 80, 90)

place(80, -40)
# TODO: Add or call a three-side loop with length 60 and left turns of 120.

place(-100, 40)
# TODO: Draw the circle of radius 30.

screen.update()
print("Basic Shapes workspace ready")
turtle.done()
