import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)


def place(x, y, heading=0):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()


def polygon(sides, length, turn):
    for step in range(sides):
        pen.forward(length)
        pen.left(turn)


def shape_parameters(choice):
    if choice == 0:
        return "square", 4, 45, 90
    elif choice == 1:
        return "triangle", 3, 58, 120
    elif choice == 2:
        return "hexagon", 6, 32, 60
    else:
        return "circle approximation", 36, 5, 10


choice = random.randint(0, 3)
name, sides, length, turn = shape_parameters(choice)
place(-35, -40)
pen.color("teal")
pen.begin_fill()
polygon(sides, length, turn)
pen.end_fill()
print("Selected:", choice, name)

screen.update()
print("Surprise Shape reference ready")
turtle.done()
