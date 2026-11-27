import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

pen.color("steelblue")
pen.pensize(2)


def draw_arm(step, twig):
    for level in range(6):
        pen.forward(step)
        pen.right(45)
        pen.forward(twig)
        pen.forward(-twig)
        pen.left(90)
        pen.forward(twig)
        pen.forward(-twig)
        pen.right(45)


for arm in range(6):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(60 * arm)
    pen.pendown()
    draw_arm(9, 10)

screen.update()
print("Snowflake reference ready")
turtle.done()
