import turtle
drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)

# draw the outer green layer
drawing_turtle.penup()
drawing_turtle.goto(-200,0)
drawing_turtle.pendown()
drawing_turtle.color("green")
drawing_turtle.begin_fill()
drawing_turtle.forward(400)
drawing_turtle.right(90)

for i in range(37):
  drawing_turtle.forward(17.5)
  drawing_turtle.right(5)

drawing_turtle.end_fill()

# draw the inner pink layer
drawing_turtle.penup()
drawing_turtle.right(85)
drawing_turtle.forward(50)
drawing_turtle.pendown()
drawing_turtle.color("pink")
drawing_turtle.begin_fill()
drawing_turtle.forward(300)
drawing_turtle.right(90)

for i in range(37):
  drawing_turtle.forward(13)
  drawing_turtle.right(5)

drawing_turtle.end_fill()

# draw seeds

drawing_turtle.penup()
drawing_turtle.goto(80,-40)
drawing_turtle.pendown()
drawing_turtle.color("black")
drawing_turtle.begin_fill()

for i in range(36):
  drawing_turtle.forward(1)
  drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(-10,-100)
drawing_turtle.pendown()
drawing_turtle.color("black")
drawing_turtle.begin_fill()

for i in range(36):
  drawing_turtle.forward(1)
  drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(-90,-30)
drawing_turtle.pendown()
drawing_turtle.color("black")
drawing_turtle.begin_fill()

for i in range(36):
  drawing_turtle.forward(1)
  drawing_turtle.right(10)
drawing_turtle.end_fill()