import turtle
drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)
drawing_turtle.right(5)

y = 100
circle_step = 20

for i in range(5):
  drawing_turtle.penup()
  drawing_turtle.goto(0,y)
  drawing_turtle.pendown()

  # decide which color
  if (i % 2 == 0):
    drawing_turtle.color('red')
  else:
    drawing_turtle.color('white')

  # draw circle
  drawing_turtle.begin_fill()
  for i in range(36):
    drawing_turtle.forward(circle_step)
    drawing_turtle.right(10)
  drawing_turtle.end_fill()

  # decrease y and circleStep
  y -= 23
  circle_step -= 4