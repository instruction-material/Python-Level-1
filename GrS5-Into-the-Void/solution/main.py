import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

screen.bgcolor("black")
pen.color("white")


def expanding_spiral(length, increase, turn, steps):
    for step in range(steps):
        pen.forward(length)
        pen.right(turn)
        length += increase
    return length


after_last = expanding_spiral(30, 1, 91, 120)
print("Next length:", after_last)

screen.update()
print("Into the Void reference ready")
turtle.done()
