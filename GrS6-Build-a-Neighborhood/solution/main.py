import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

pen.hideturtle()

def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()


def draw_house(x, y):
    move_to(x, y)
    pen.color("slateblue")
    pen.begin_fill()
    for side in range(4):
        pen.forward(32)
        pen.left(90)
    pen.end_fill()
    move_to(x, y + 32)
    pen.color("tomato")
    pen.begin_fill()
    for side in range(3):
        pen.forward(32)
        pen.left(120)
    pen.end_fill()


draw_house(-85, -35)
draw_house(-16, -35)
draw_house(53, -35)

screen.update()
print("Build a Neighborhood reference ready")
turtle.done()
