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


def half_disk(radius, color):
    place(-radius, 0, -90)
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius, 180)
    pen.setheading(180)
    pen.forward(2 * radius)
    pen.end_fill()


half_disk(100, "forestgreen")
# TODO: Add the smaller half disk for the fruit.
for x in (-48, -24, 0, 24, 48):
    # TODO: Draw one seed at each x position.
    pass

screen.update()
print("Watermelon Slice workspace ready")
turtle.done()
