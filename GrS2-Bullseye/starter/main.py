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


rings = [(100, "firebrick"), (80, "white")]
# TODO: Add the last three radii (60, 40, 20) and alternate the colors.
for radius, color in rings:
    disk(0, 0, radius, color)

screen.update()
print("Bullseye workspace ready")
turtle.done()
