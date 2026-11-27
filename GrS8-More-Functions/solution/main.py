import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

def place(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pendown()


def draw_square(length):
    for edge in range(4):
        pen.forward(length)
        pen.left(90)


def draw_triangle(length):
    for edge in range(3):
        pen.forward(length)
        pen.left(120)


for x, size in [(-98, 18), (-29, 30), (40, 42)]:
    place(x, -62, "teal")
    draw_square(size)
    place(x, 12, "coral")
    draw_triangle(size)

screen.update()
print("More Functions reference ready")
turtle.done()
