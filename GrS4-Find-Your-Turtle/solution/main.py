import turtle
import random

drawing_turtle = turtle.Turtle()

drawing_turtle.penup()
drawing_turtle.goto(random.randint(-200,200), random.randint(-200,200))
drawing_turtle.pendown()

if drawing_turtle.xcor() >= 0 and drawing_turtle.ycor() >= 0:
  drawing_turtle.color("blue")
if drawing_turtle.xcor() <= 0 and drawing_turtle.ycor() >= 0:
  drawing_turtle.color("yellow")
if drawing_turtle.xcor() >= 0 and drawing_turtle.ycor() <= 0:
  drawing_turtle.color("orange")
if drawing_turtle.xcor() <= 0 and drawing_turtle.ycor() <= 0:
  drawing_turtle.color("green")

if drawing_turtle.xcor() >= 0 or drawing_turtle.ycor() >= 0:
  for i in range(4):
    drawing_turtle.forward(20)
    drawing_turtle.right(90)
if drawing_turtle.xcor() >= 0 and drawing_turtle.ycor() <= 0:
  for i in range(36):
    drawing_turtle.forward(2)
    drawing_turtle.right(10)