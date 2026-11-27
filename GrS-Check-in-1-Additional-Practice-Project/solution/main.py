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
    for pair in range(pair_count):
        pen.forward(step_length)
        pen.right(2 * turn)
        pen.forward(step_length)
        pen.left(2 * turn)


def connect_square(side_length):
    pen.setheading(0)
    for side in range(4):
        pen.forward(side_length)
        pen.left(90)


pen.penup()
pen.goto(-180, 0)
pen.pendown()
draw_zigzag(pairs)
connect_square(36)
screen.update()
print("Zigzag pairs:", pairs, "Endpoint:", round(pen.xcor()), round(pen.ycor()))
turtle.done()
