import turtle
turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.color('white')
drawing_turtle.speed(100)

s = turtle.Screen()
s.bgcolor('black')

n = 50

for i in range(300):
  drawing_turtle.forward(n)
  drawing_turtle.right(91)
  n = n + 1