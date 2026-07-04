import turtle
drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)

drawing_turtle.penup()
drawing_turtle.goto(0,100)
drawing_turtle.pendown()
drawing_turtle.right(5)        # This allows the target to appear centered

drawing_turtle.color('red')
drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(20)
  drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(0,77)      # Moving down by 23 contributes to making the rings appear more concentric
drawing_turtle.pendown()

drawing_turtle.color('white')
drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(16)
  drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(0,54)
drawing_turtle.pendown()

drawing_turtle.color('red')
drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(12)
  drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(0,31)
drawing_turtle.pendown()

drawing_turtle.color('white')
drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(8)
  drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(0,8)
drawing_turtle.pendown()

drawing_turtle.color('red')
drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(4)
  drawing_turtle.right(10)
drawing_turtle.end_fill()