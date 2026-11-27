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


def needle(direction, color):
    place(0, 14)
    pen.color(color)
    pen.begin_fill()
    pen.goto(61 * direction, 0)
    pen.goto(0, -14)
    pen.goto(0, 14)
    pen.end_fill()


disk(0, 0, 100, "midnightblue")
disk(0, 0, 86, "wheat")
disk(0, 0, 75, "darkslategray")
for direction, color in [(1, "gold"), (-1, "turquoise")]:
    # TODO: Call needle with the direction and color for each half.
    pass
disk(0, 0, 6, "wheat")

screen.update()
print("Compass Badge workspace ready")
turtle.done()
