import turtle
import random

drawing_turtle = turtle.Turtle()
turtle.colormode(255)
drawing_turtle.right(45)
drawing_turtle.speed(5)


screen = turtle.Screen()

def change_color():
  drawing_turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def draw_diamond():
  side_length = 20
  for i in range(3):
    change_color()
    drawing_turtle.begin_fill()
    for i in range(4):
      drawing_turtle.forward(side_length)
      drawing_turtle.right(90)
    drawing_turtle.end_fill()

def change_location():
  drawing_turtle.penup()
  drawing_turtle.goto(random.randint(-200,200),random.randint(-200,200))
  drawing_turtle.pendown()

def draw_circle():
  side_length = 3
  for i in range(3):
    change_color()
    drawing_turtle.begin_fill()
    for i in range(36):
      drawing_turtle.forward(side_length)
      drawing_turtle.right(10)
    drawing_turtle.end_fill()

def draw_pyramid():
  side_length = 30
  for i in range(3):
    change_color()
    drawing_turtle.begin_fill()
    for i in range(3):
      drawing_turtle.forward(side_length)
      drawing_turtle.right(120)
    drawing_turtle.end_fill()

screen.onkey(draw_diamond, "d")
screen.onkey(draw_circle, "c")
screen.onkey(draw_pyramid, "p")
screen.onkey(change_location, "space")
screen.listen()