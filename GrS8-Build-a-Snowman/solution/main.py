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
disk(0, 58, 19)

pen.penup()
pen.color("midnightblue")
for x in (-6, 6):
    pen.goto(x, 62)
    pen.dot(5)
pen.goto(0, 52)
pen.color("darkorange")
pen.dot(7)

screen.update()
print("Build a Snowman reference ready")
turtle.done()
