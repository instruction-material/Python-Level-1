import turtle

drawing_turtle = turtle.Turtle()
screen = turtle.Screen()

drawing_turtle.speed(1000)
screen.bgcolor("yellow")

drawing_turtle.penup()
drawing_turtle.goto(-100,200)

drawing_turtle.pendown()
for i in range(2):
  drawing_turtle.forward(10)
  drawing_turtle.right(90)
  drawing_turtle.forward(100)
  drawing_turtle.right(90)
drawing_turtle.penup()

drawing_turtle.goto(50,200)
drawing_turtle.pendown()
for i in range(2):
  drawing_turtle.forward(10)
  drawing_turtle.right(90)
  drawing_turtle.forward(100)
  drawing_turtle.right(90)
drawing_turtle.penup()

drawing_turtle.goto(-200,0)
drawing_turtle.pendown()
drawing_turtle.right(90)
for i in range(37):
  drawing_turtle.forward(15)
  drawing_turtle.left(5)