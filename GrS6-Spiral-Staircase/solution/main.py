import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)

screen = turtle.Screen()
screen.bgcolor("black")

red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = 0
length = 20
for i in range(40):
    drawing_turtle.color(red_value, green_value, blue_value)

    drawing_turtle.begin_fill()
    for i in range(4):
        drawing_turtle.forward(length)
        drawing_turtle.right(90)
    drawing_turtle.end_fill()

    blue_value += 5
    length += 5
    drawing_turtle.right(10)
