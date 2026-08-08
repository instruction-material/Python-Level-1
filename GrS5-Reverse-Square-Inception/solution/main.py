import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10)

for i in range(4):
    length = 80

    for j in range(3):
        length -= 20

        red_value = random.randint(0, 255)
        green_value = random.randint(0, 255)
        blue_value = random.randint(0, 255)
        drawing_turtle.color(red_value, green_value, blue_value)

        drawing_turtle.begin_fill()
        for k in range(4):
            drawing_turtle.forward(length)
            drawing_turtle.right(90)
        drawing_turtle.end_fill()

    drawing_turtle.right(90)
