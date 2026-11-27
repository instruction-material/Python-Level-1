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


screen.bgcolor("black")
place(-154, -50)
pen.color("magenta")
polygon(6, 32, 60)

place(-35, -50)
pen.color("violet")
polygon(10, 20, 36)

place(83, 20)
pen.color("turquoise")
pen.begin_fill()
polygon(5, 84, 144)
pen.end_fill()

screen.update()
print("More Shapes reference ready")
turtle.done()
