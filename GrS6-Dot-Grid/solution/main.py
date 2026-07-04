import turtle
turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(50)
drawing_turtle.penup()

distance = 25
num_rows = 5
num_cols = 8

for i in range(num_rows):
  for j in range(num_cols):
    drawing_turtle.dot()
    drawing_turtle.forward(distance)
  drawing_turtle.backward(distance * num_cols)
  drawing_turtle.right(90)
  drawing_turtle.forward(distance)
  drawing_turtle.left(90)
drawing_turtle.ht()

