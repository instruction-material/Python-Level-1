# Code I need at the top of every project is:

import turtle

# I create a turtle with this line:

drawing_turtle = turtle.Turtle()

# I move that turtle forward with this command:

drawing_turtle.forward(10)

# I turn the turtle with these commands:

drawing_turtle.right(90)
drawing_turtle.left(90)

# I change the turtles color with this command:

drawing_turtle.color("yellow")

# I move the turtle to a new place without leaving a line with these commands:

drawing_turtle.penup()
drawing_turtle.goto(50, 50)
drawing_turtle.pendown()

# Explain how the above commands work:
#

# I draw a filled in square with these commands:

drawing_turtle.begin_fill()
for i in range(4):
    drawing_turtle.forward(100)
    drawing_turtle.right(90)
drawing_turtle.end_fill()
