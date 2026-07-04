###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# This code is needed at the beginning of every project:

import turtle

drawing_turtle = turtle.Turtle()

# This is how I write a loop that draws a square:

for i in range(4):
    drawing_turtle.forward(50)
    drawing_turtle.right(90)

# Explain how the computer knows how many times to repeat the loop:
#

# Here I added code that will move the turtle to a new spot:

drawing_turtle.penup()
drawing_turtle.goto(100, 100)
drawing_turtle.pendown()

# This is how I write a loop that draws a circle:

for i in range(36):
    drawing_turtle.forward(3)
    drawing_turtle.right(10)


# Explain how the above code works:
#
# Explain how I could draw  a half circle:
#

# Here I added code that will move the turtle to a new spot:

drawing_turtle.penup()
drawing_turtle.goto(-100, -100)
drawing_turtle.pendown()

# This is how I write a loop that draws a rectangle:

for i in range(2):
    drawing_turtle.forward(100)
    drawing_turtle.right(90)
    drawing_turtle.forward(30)
    drawing_turtle.right(90)
