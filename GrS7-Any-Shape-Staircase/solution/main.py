import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

def draw_shape(length, sides):
    turn = 360 / sides
    for edge in range(sides):
        pen.forward(length)
        pen.left(turn)


for step, sides in enumerate((3, 4, 5, 6)):
    pen.penup()
    pen.goto(-104 + 58 * step, -55 + 23 * step)
    pen.setheading(0)
    pen.color("darkslateblue")
    pen.pendown()
    draw_shape(23, sides)

screen.update()
print("Any Shape Staircase reference ready")
turtle.done()
