import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

def dimensions(x, y):
    width = min(105, max(12, abs(round(x))))
    height = min(72, max(12, abs(round(y))))
    return width, height


def draw_rectangle(width, height):
    pen.penup()
    pen.goto(-width / 2, -height / 2)
    pen.setheading(0)
    pen.color("teal" if width >= height else "darkorange")
    pen.pendown()
    for pair in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)


def on_click(x, y):
    width, height = dimensions(x, y)
    draw_rectangle(width, height)
    screen.update()
    print("Rectangle:", width, "by", height)


screen.onclick(on_click)
screen.listen()

screen.update()
print("Click and Draw Rectangles reference ready")
turtle.done()
