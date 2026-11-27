import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)
blue = 20
for group in range(24):
    pen.color(220 - 6 * group, 50 + 7 * group, blue)
    for length in (18, 34, 50, 66):
        for edge in range(4):
            pen.forward(length)
            pen.right(90)
    pen.right(15)
    # TODO: Advance blue by 23 and wrap when it would exceed 255.

screen.update()
print("Rainbow Square Inception workspace ready")
turtle.done()
