import turtle

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(0)
drawing_turtle.penup()
drawing_turtle.goto(-200, 0)
drawing_turtle.pendown()

drawing_turtle.left(70)
for i in range(30):
  drawing_turtle.forward(20)
  drawing_turtle.right(140)
  drawing_turtle.forward(20)
  drawing_turtle.left(140)

"""
# Bonus extension for advanced students
t.right(70)
for i in range(4):
  t.forward(100)
  t.right(90)

t.penup()
t.goto(-200, 0)
t.pendown()
t.right(60)
for i in range(3):
  t.forward(100)
  t.right(120)
"""