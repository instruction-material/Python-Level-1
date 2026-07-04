import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)
screen = turtle.Screen()

# set random background color
red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = random.randint(0, 255)
screen.bgcolor(red_value, green_value, blue_value)

# draw right half of bowtie
drawing_turtle.left(30)
red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = random.randint(0, 255)
drawing_turtle.color(red_value, green_value, blue_value)
drawing_turtle.begin_fill()
for i in range(3):
    drawing_turtle.forward(80)
    drawing_turtle.right(120)
drawing_turtle.end_fill()

# draw left half of bowtie
drawing_turtle.right(180)
red_value = random.randint(0, 255)
green_value = random.randint(0, 255)
blue_value = random.randint(0, 255)
drawing_turtle.color(red_value, green_value, blue_value)
drawing_turtle.begin_fill()
for i in range(3):
    drawing_turtle.forward(80)
    drawing_turtle.right(120)
drawing_turtle.end_fill()
