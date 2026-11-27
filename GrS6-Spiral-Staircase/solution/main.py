import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

screen.colormode(255)
length = 12
for layer in range(24):
    pen.color(60, 70 + layer * 5, 185)
    for edge in range(4):
        pen.forward(length)
        pen.right(90)
    pen.right(15)
    length += 3

screen.update()
print("Spiral Staircase reference ready")
turtle.done()
