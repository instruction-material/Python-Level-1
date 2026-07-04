import turtle
import random
turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

# define a function that draws a shape with a random number of sides
def draw_random_shape():
  num_sides = random.randint(3, 9)
  drawing_turtle.begin_fill()
  turn_angle = 360.0 / num_sides
  # you can also use a random side length for more randomness!
  side_length = 15
  for i in range(num_sides):
    drawing_turtle.forward(side_length)
    drawing_turtle.right(turn_angle)
  drawing_turtle.end_fill()

# call your function a random number of times, programming the turtle to go to a new random location and turn a new random color each time
num_shapes = random.randint(10,50)

for i in range(num_shapes):
  # Go to random position
  drawing_turtle.penup()
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)
  drawing_turtle.goto(x, y)
  drawing_turtle.pendown()

  # Make the turtle turn a random color
  red_value = random.randint(0,255)
  green_value = random.randint(0,255)
  blue_value = random.randint(0,255)
  drawing_turtle.color(red_value, green_value, blue_value)

  draw_random_shape()


