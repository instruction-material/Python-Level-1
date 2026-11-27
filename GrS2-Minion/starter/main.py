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


def disk(x, y, radius, color):
    place(x, y - radius)
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def rectangle(x, y, width, height, color):
    place(x, y)
    pen.color(color)
    pen.begin_fill()
    for pair in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()


screen.bgcolor("lavender")
rectangle(-84, -69, 168, 132, "steelblue")
rectangle(-6, 63, 12, 27, "darkslategray")
disk(0, 94, 10, "tomato")
for x in (-45, 21):
    # TODO: Draw a light of the same size at both x positions.
    pass
for x in (-43, -21, 1, 23):
    # TODO: Repeat the slot at each of the four x positions.
    pass

screen.update()
print("Robot Portrait workspace ready")
turtle.done()
