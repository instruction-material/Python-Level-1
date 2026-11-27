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


length = 70
degrees = 90
number_of_sides = 4

place(-35, -35)
polygon(number_of_sides, length, degrees)

screen.update()
print("Awesome Angles reference ready")
turtle.done()
