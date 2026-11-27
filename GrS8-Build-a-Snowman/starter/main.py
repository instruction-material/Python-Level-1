import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.bgcolor("lightsteelblue")


def disk(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.color("white")
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


disk(0, -52, 37)
disk(0, 12, 27)
# TODO: Use disk to draw the head centered at (0, 58).

# Add the eyes and nose once the head is in place.

screen.update()
print("Build a Snowman workspace ready")
turtle.done()
