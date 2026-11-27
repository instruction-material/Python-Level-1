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


rectangle(-110, -38, 220, 48, "gold")
rectangle(-58, 10, 116, 51, "gold")
for x in (-47, 5):
    rectangle(x, 21, 42, 29, "lightsteelblue")
for x in (-65, 65):
    disk(x, -36, 21, "black")
    disk(x, -36, 7, "lightgray")
rectangle(-18, 61, 36, 13, "black")

screen.update()
print("Taxi reference ready")
turtle.done()
