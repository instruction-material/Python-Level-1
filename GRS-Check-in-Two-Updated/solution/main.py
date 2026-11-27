import turtle


screen = turtle.Screen()
screen.tracer(0)
zebra = turtle.Turtle()
zebra.speed(0)


def move_to(x, y):
    zebra.penup()
    zebra.goto(x, y)
    zebra.setheading(0)
    zebra.pendown()


def growing_lengths(repeats, maximum):
    lengths = []
    size = 10
    while len(lengths) < repeats:
        lengths.append(size)
        size = min(size + 5, maximum)
    return lengths


def draw_square(size):
    for side in range(4):
        zebra.forward(size)
        zebra.right(90)


def move_forward50():
    zebra.forward(50)
    screen.update()


def draw_triangle():
    for side in range(3):
        zebra.forward(40)
        zebra.left(120)
    screen.update()


move_to(-145, 105)
lengths = growing_lengths(10, 30)
for size in lengths:
    zebra.forward(size)
    zebra.right(45)

move_to(-80, 15)
for size in [10, 20, 30, 40]:
    draw_square(size)
    zebra.left(90)

screen.onkey(move_forward50, "Right")
screen.onkey(draw_triangle, "Up")
screen.onkey(draw_triangle, "a")
screen.update()
print("Check-In 2:", lengths)
screen.listen()
turtle.done()
