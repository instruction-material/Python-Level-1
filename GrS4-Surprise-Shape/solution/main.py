import turtle
import random

turtle.colormode(255)
drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)

red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = random.randint(0, 255)
drawing_turtle.color(red_value, green_value, blue_value)

num = random.randint(0, 3)

drawing_turtle.begin_fill()
if num == 0:
    for i in range(4):
        drawing_turtle.forward(100)
        drawing_turtle.right(90)
elif num == 1:
    for i in range(3):
        drawing_turtle.forward(100)
        drawing_turtle.right(120)
elif num == 2:
    for i in range(6):
        drawing_turtle.forward(100)
        drawing_turtle.right(60)
else:
    for i in range(36):
        drawing_turtle.forward(5)
        drawing_turtle.right(10)
drawing_turtle.end_fill()
