import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.pensize(5)


def random_spot():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    drawing_turtle.penup()
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()


def random_color():
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    drawing_turtle.color(red_value, green_value, blue_value)


def reset():
    drawing_turtle.penup()
    drawing_turtle.goto(0, 0)
    drawing_turtle.pendown()
    drawing_turtle.color("black")
    drawing_turtle.setheading(0)
    drawing_turtle.clear()
    drawing_turtle.speed(6)


def all_random():
    random_spot()
    random_color()


random_color()
random_spot()
drawing_turtle.right(90)
drawing_turtle.forward(100)
reset()
