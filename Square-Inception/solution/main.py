import turtle
import random

turtle.colormode(255)

juni = turtle.Turtle()

for i in range(4):
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    juni.color(red_value, green_value, blue_value)

    side_length = 30

    for i in range(3):
        for i in range(4):
            juni.forward(side_length)
            juni.right(90)

        side_length += 20

    juni.right(90)
