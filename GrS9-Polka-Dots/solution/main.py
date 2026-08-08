import turtle
import random

turtle.colormode(255)

# Set up the turtle screen
screen = turtle.Screen()

# Create a turtle for drawing
artist = turtle.Turtle()
artist.speed(0)  # Adjust the drawing speed


def draw_circle():
    # Draw a colorful circle
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)

    artist.color(red_value, green_value, blue_value)

    circle_size = random.randint(1, 10)

    artist.begin_fill()
    for i in range(36):
        artist.forward(circle_size)
        artist.right(10)
    artist.end_fill()


# Function to handle mouse clicks
def move(x, y):
    artist.penup()  # Lift the pen to move to the clicked position
    artist.goto(x, y)
    artist.pendown()  # Lower the pen to start drawing

    draw_circle()


# Set up the event listener
screen.onclick(move)

# Keep the window open
turtle.done()
