###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(5)

screen = turtle.Screen()
screen.bgcolor("black")

drawing_turtle.pendown()
drawing_turtle.color("magenta")
drawing_turtle.begin_fill()
for i in range(6):
    drawing_turtle.forward(100)
    drawing_turtle.right(60)
drawing_turtle.end_fill()
drawing_turtle.penup()

drawing_turtle.goto(100, 200)
drawing_turtle.pendown()
drawing_turtle.color("purple")
drawing_turtle.begin_fill()
for i in range(10):
    drawing_turtle.forward(30)
    drawing_turtle.right(36)
drawing_turtle.end_fill()
drawing_turtle.penup()

# star will not appear filled in repl.it however should be filled in on the student's web portal
drawing_turtle.goto(-150, 150)
drawing_turtle.pendown()
drawing_turtle.color("teal")
drawing_turtle.begin_fill()
for i in range(5):
    drawing_turtle.forward(50)
    drawing_turtle.right(144)
drawing_turtle.end_fill()
