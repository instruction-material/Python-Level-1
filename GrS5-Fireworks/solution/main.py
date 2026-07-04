import turtle
import random
turtle.colormode(255)
drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

line_length = 1

for i in range(360):
  # set random color
  red_value = random.randint(0,255)
  green_value = random.randint(0,255)
  blue_value = random.randint(0,255)
  drawing_turtle.color(red_value,green_value,blue_value)

  # draw line
  drawing_turtle.goto(0,0)
  drawing_turtle.forward(line_length)
  drawing_turtle.right(5)

  # increase length of line
  line_length = line_length + 1