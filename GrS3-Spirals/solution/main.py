import turtle
import random
turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(100)
drawing_turtle.penup()

for i in range(100):

  red_value = random.randint(0,255)
  green_value = random.randint(0,255)
  blue_value = random.randint(0,255)
  drawing_turtle.color(red_value,green_value,blue_value)

  x = random.randint(-200,200)
  y = random.randint(-200,200)
  drawing_turtle.goto(x,y)
  drawing_turtle.pendown()

  side_length = random.randint(25,150)

  for i in range(50):
    drawing_turtle.forward(side_length)
    drawing_turtle.left(123)

  drawing_turtle.penup()