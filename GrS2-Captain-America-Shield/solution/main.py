import turtle

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(0)
drawing_turtle.color("red")

drawing_turtle.penup()
drawing_turtle.goto(0, 195)
drawing_turtle.pendown()

drawing_turtle.begin_fill()
for i in range(40):
    drawing_turtle.forward(30)
    drawing_turtle.right(9)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(0, 165)
drawing_turtle.pendown()

drawing_turtle.color("light grey")
drawing_turtle.begin_fill()
for i in range(40):
    drawing_turtle.forward(25)
    drawing_turtle.right(9)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(0, 135)
drawing_turtle.pendown()

drawing_turtle.color("red")
drawing_turtle.begin_fill()
for i in range(40):
    drawing_turtle.forward(20)
    drawing_turtle.right(9)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(0, 105)
drawing_turtle.pendown()

drawing_turtle.color("blue")
drawing_turtle.begin_fill()
for i in range(40):
    drawing_turtle.forward(15)
    drawing_turtle.right(9)
drawing_turtle.end_fill()

drawing_turtle.penup()
drawing_turtle.goto(-60, 35)
drawing_turtle.pendown()
drawing_turtle.color("white")

# star will not appear filled in repl.it however should be filled in on the student's web portal
drawing_turtle.begin_fill()
for i in range(5):
    drawing_turtle.forward(140)
    drawing_turtle.right(144)
drawing_turtle.end_fill()
