import turtle
import random

turtle.colormode(255)

drawing_turtle = turtle.Turtle()

drawing_turtle.shape("turtle")
drawing_turtle.pensize(random.randint(1, 10))

num_steps = 100

# Perform random walk
for _ in range(num_steps):
    # Generate random length and angle
    step_length = random.randint(10, 30)
    turn_angle = random.randint(-180, 180)

    # Generate random colors
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)

    # Set the color of the turtle
    drawing_turtle.color(red_value, green_value, blue_value)

    # Move the turtle
    drawing_turtle.forward(step_length)
    drawing_turtle.left(turn_angle)
