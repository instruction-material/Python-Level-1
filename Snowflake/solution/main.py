import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = random.randint(0, 255)
drawing_turtle.color(red_value, green_value, blue_value)
drawing_turtle.pensize(5)
drawing_turtle.pendown()

for i in range(6):
    drawing_turtle.goto(0, 0)

    for i in range(10):
        # draw part of the branch
        drawing_turtle.forward(10)

        # draw a little side branch
        drawing_turtle.right(45)
        drawing_turtle.forward(20)
        drawing_turtle.backward(20)

        # draw the symmetrical little side branch
        drawing_turtle.left(90)
        drawing_turtle.forward(20)
        drawing_turtle.backward(20)

        # reset positioning
        drawing_turtle.right(45)

    # turn to start drawing the next branch
    drawing_turtle.right(60)
