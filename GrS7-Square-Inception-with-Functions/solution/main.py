import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10)


def draw_square(side_length, red_value, green_value, blue_value):
    drawing_turtle.color(red_value, green_value, blue_value)

    for i in range(4):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(90)


for i in range(4):
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)

    length = 20

    for j in range(3):
        length += 20
        draw_square(length, red_value, green_value, blue_value)

    drawing_turtle.right(90)
