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
    # TODO: Add the roof above the 32-pixel body.


draw_house(-85, -35)
# TODO: Call the same function at (-16, -35) and (53, -35).

screen.update()
print("Build a Neighborhood workspace ready")
turtle.done()
