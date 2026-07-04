import turtle

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(1000)

drawing_turtle.color("yellow")
drawing_turtle.penup()
drawing_turtle.goto(-100,-100)
drawing_turtle.pendown()

drawing_turtle.begin_fill()
drawing_turtle.forward(200)
drawing_turtle.left(90)
drawing_turtle.forward(200)

for i in range(18):
  drawing_turtle.forward(18)
  drawing_turtle.left(10)

drawing_turtle.forward(220)
drawing_turtle.left(90)
drawing_turtle.end_fill()

drawing_turtle.color("black")
drawing_turtle.penup()
drawing_turtle.goto(-105, 115)
drawing_turtle.pendown()

drawing_turtle.begin_fill()
for i in range(2):
  drawing_turtle.forward(205)
  drawing_turtle.right(90)
  drawing_turtle.forward(20)
  drawing_turtle.right(90)
drawing_turtle.end_fill()

drawing_turtle.color("silver")
drawing_turtle.penup()
drawing_turtle.goto(-60, 110)
drawing_turtle.pendown()

drawing_turtle.right(90)
drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(10)
  drawing_turtle.left(10)
drawing_turtle.end_fill()

drawing_turtle.color("white")
drawing_turtle.penup()
drawing_turtle.goto(-38,110)
drawing_turtle.pendown()

drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(6)
  drawing_turtle.left(10)
drawing_turtle.end_fill()

drawing_turtle.color("brown")
drawing_turtle.penup()
drawing_turtle.goto(-15,110)
drawing_turtle.pendown()

drawing_turtle.begin_fill()
for i in range(36):
  drawing_turtle.forward(2)
  drawing_turtle.left(10)
drawing_turtle.end_fill()

drawing_turtle.left(90)
drawing_turtle.penup()
drawing_turtle.goto(-105,-30)
drawing_turtle.pendown()

drawing_turtle.begin_fill()
drawing_turtle.color("blue")
drawing_turtle.forward(30)
drawing_turtle.right(90)
drawing_turtle.forward(50)
drawing_turtle.left(90)
drawing_turtle.forward(150)
drawing_turtle.left(90)
drawing_turtle.forward(50)
drawing_turtle.right(90)
drawing_turtle.forward(25)
drawing_turtle.right(90)
drawing_turtle.forward(70)
drawing_turtle.right(90)
drawing_turtle.forward(207)
drawing_turtle.right(90)
drawing_turtle.forward(70)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(-30,0)
drawing_turtle.pendown()

drawing_turtle.color("black")
drawing_turtle.right(90)
for i in range(18):
  drawing_turtle.forward(6)
  drawing_turtle.left(3)

drawing_turtle.penup()
drawing_turtle.goto(0,210)

drawing_turtle.setheading(0)
drawing_turtle.pendown()

for i in range(3):
  drawing_turtle.left(45)
  drawing_turtle.forward(70)
  drawing_turtle.backward(70)