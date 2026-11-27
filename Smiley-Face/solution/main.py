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


screen.bgcolor("lightsteelblue")
disk(0, 0, 100, "gold")
for x in (-35, 21):
    rectangle(x, 18, 14, 26, "black")

place(-31, -17, -53)
pen.color("black")
pen.pensize(4)
pen.circle(39, 106)

screen.update()
print("Smiley Face reference ready")
turtle.done()
