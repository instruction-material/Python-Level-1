import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)
turn = 70
step_length = 16
pairs = 30


def draw_zigzag(pair_count):
    pen.setheading(turn)
    for pair in range(1):  # TODO: Repeat pair_count times once a pair works.
        pen.forward(step_length)
        # TODO: Draw the return stroke and restore the original heading.


def connect_square(side_length):
    pen.setheading(0)
    # TODO: Extend the zigzag with one closed shape at the same endpoint.
    pass


pen.penup()
pen.goto(-180, 0)
pen.pendown()
draw_zigzag(pairs)
connect_square(36)
screen.update()
print("Zigzag workspace ready")
turtle.done()
