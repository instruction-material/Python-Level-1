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
# TODO: Draw ten sides of length 20 and turn 36 degrees per side.

place(83, 20)
pen.color("turquoise")
pen.begin_fill()
# TODO: Draw five equal strokes with 144-degree turns.
pen.end_fill()

screen.update()
print("More Shapes workspace ready")
turtle.done()
