import turtle
drawing_turtle = turtle.Turtle()

drawing_turtle.pendown()
drawing_turtle.color('blue')
for i in range(4):
  drawing_turtle.forward(100)
  drawing_turtle.right(90)
drawing_turtle.penup()

drawing_turtle.goto(-150,150)
drawing_turtle.pendown()
drawing_turtle.color('red')
for i in range(3):
  drawing_turtle.forward(100)
  drawing_turtle.right(120)
drawing_turtle.penup()

drawing_turtle.goto(-150,-100)
drawing_turtle.pendown()
drawing_turtle.color('green')
for i in range(36):
  drawing_turtle.forward(10)
  drawing_turtle.right(10)