import turtle
import random

drawing_turtle = turtle.Turtle()
screen = turtle.Screen()
drawing_turtle.speed(10000)
drawing_turtle.penup()


def rand_color():
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    drawing_turtle.color(red_value, green_value, blue_value)


def rand_spot():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    drawing_turtle.goto(x, y)


def draw_square():
    rand_color()
    rand_spot()

    side_length = random.randint(20, 100)

    drawing_turtle.pendown()
    drawing_turtle.begin_fill()
    for i in range(4):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(90)
    drawing_turtle.end_fill()
    drawing_turtle.penup()


def draw_octagon():
    rand_color()
    rand_spot()

    side_length = random.randint(20, 100)

    drawing_turtle.pendown()
    drawing_turtle.begin_fill()
    for i in range(8):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(315)
    drawing_turtle.end_fill()
    drawing_turtle.penup()


def draw_firework():
    rand_color()

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    for i in range(36):
        drawing_turtle.goto(x, y)
        drawing_turtle.pendown()
        drawing_turtle.forward(20)
        drawing_turtle.right(10)
        drawing_turtle.penup()


def draw_circle():
    rand_color()
    rand_spot()

    side_length = random.randint(5, 20)

    drawing_turtle.pendown()
    drawing_turtle.begin_fill()
    for i in range(36):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(10)
    drawing_turtle.end_fill()
    drawing_turtle.penup()


drawing_turtle.goto(0, 0)

screen.onkey(draw_square, "Up")
screen.onkey(draw_octagon, "Down")
screen.onkey(draw_firework, "Left")
screen.onkey(draw_circle, "Right")
screen.listen()
