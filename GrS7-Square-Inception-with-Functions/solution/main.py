import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)


def draw_square(length, red, green, blue):
    pen.color(red, green, blue)
    for edge in range(4):
        pen.forward(length)
        pen.right(90)


for group in range(4):
    for length in (18, 34, 50):
        draw_square(length, 45 + 40 * group, 80, 175)
    pen.right(90)

screen.update()
print("Square Inception with Functions reference ready")
turtle.done()
