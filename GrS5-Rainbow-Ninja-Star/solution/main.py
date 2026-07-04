import turtle
import random
turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

red_value = random.randint(0,255)
green_value = random.randint(0,255)
blue_value = 0

for i in range(180):
  drawing_turtle.color(red_value,green_value,blue_value)

  drawing_turtle.forward(100)
  drawing_turtle.right(30)
  drawing_turtle.forward(20)
  drawing_turtle.left(60)
  drawing_turtle.forward(50)
  drawing_turtle.right(30)

  drawing_turtle.penup()
  drawing_turtle.goto(0, 0)
  drawing_turtle.pendown()

  drawing_turtle.right(2)

  blue_value = blue_value+2