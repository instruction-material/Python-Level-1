import turtle

drawing_turtle = turtle.Turtle()
drawing_turtle.pensize(10)
drawing_turtle.speed(10)

# rectangle for body
drawing_turtle.color("yellow")
drawing_turtle.penup()
drawing_turtle.goto(-150, 0)
drawing_turtle.pendown()
drawing_turtle.begin_fill()
for i in range(2):
    drawing_turtle.forward(300)
    drawing_turtle.right(90)
    drawing_turtle.forward(60)
    drawing_turtle.right(90)
drawing_turtle.end_fill()

# trapezoid for windows and roof
drawing_turtle.penup()
drawing_turtle.goto(-70, 0)
drawing_turtle.pendown()
drawing_turtle.setheading(45)
drawing_turtle.forward(80)
drawing_turtle.right(45)
drawing_turtle.forward(80)
drawing_turtle.right(45)
drawing_turtle.forward(80)

# line to seperate windows
drawing_turtle.setheading(90)
drawing_turtle.penup()
drawing_turtle.goto(50, 10)
drawing_turtle.pendown()
drawing_turtle.forward(40)

# tires
drawing_turtle.penup()
drawing_turtle.goto(-80, -60)
drawing_turtle.pendown()
drawing_turtle.color("black")
drawing_turtle.begin_fill()
for i in range(36):
    drawing_turtle.forward(3)
    drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(60, -60)
drawing_turtle.pendown()
drawing_turtle.begin_fill()
for i in range(36):
    drawing_turtle.forward(3)
    drawing_turtle.right(10)
drawing_turtle.end_fill()

drawing_turtle.ht()
