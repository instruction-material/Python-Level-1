import turtle
import random

drawing_turtle = turtle.Turtle()
drawing_turtle.right(45)
drawing_turtle.speed(0)

screen = turtle.Screen()

def change_color():
  drawing_turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def draw_diamond():
  side_length = 10
  for i in range(3*4):
    change_color()
    drawing_turtle.forward(side_length)
    drawing_turtle.right(90)
    side_length += 2

def change_location():
  drawing_turtle.penup()
  drawing_turtle.goto(random.randint(-200,200),random.randint(-200,200))
  drawing_turtle.pendown()

def draw_circle():
  side_length = 1
  for i in range(3*36):
    side_length += 1
    change_color()
    drawing_turtle.forward(side_length)
    drawing_turtle.right(10)

def draw_pyramid():
  side_length = 20
  for i in range(3*3):
    side_length += 5
    change_color()
    drawing_turtle.forward(side_length)
    drawing_turtle.right(120)

screen.onkey(draw_diamond, "d")
screen.onkey(draw_circle, "c")
screen.onkey(draw_pyramid, "p")
screen.onkey(change_location, "space")
screen.listen()