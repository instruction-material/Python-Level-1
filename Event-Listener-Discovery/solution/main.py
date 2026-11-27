import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

pen.color("steelblue")


def draw_square():
    for side in range(4):
        pen.forward(34)
        pen.right(90)
    screen.update()
    print("Square drawn")


def click_square(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    draw_square()


screen.onkey(draw_square, "s")
screen.onclick(click_square)
screen.listen()

screen.update()
print("Event Listener Discovery reference ready")
turtle.done()
