import turtle
import random

turtle.colormode(255)

# create 10 turtles in a list
turtles = []
for i in range(10):
    drawing_turtle = turtle.Turtle()
    drawing_turtle.shape("turtle")
    turtles.append(drawing_turtle)

# make all 10 turtles move in a random direction
for turtle in turtles:
    turtle.speed(1000)
    turtle.left(random.randint(0, 360))
    turtle.color(
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )
    turtle.forward(200)
