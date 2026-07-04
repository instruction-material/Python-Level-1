###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle

drawing_turtle = turtle.Turtle()

# Why would you use a while True loop?


# Write a while True loop which causes a turtle to go forward by 1px 100 times and then breaks.

counter = 0
while True:
    drawing_turtle.forward(1)
    if counter >= 100:
        break

# Change your while True loop to break instead when the turtle's y-coordinate is above 50.

while True:
    drawing_turtle.forward(1)
    if drawing_turtle.ycor() > 50:
        break

# Change your while True loop to break as well if the turtle is more than 100px to the left side of the screen.

while True:
    drawing_turtle.forward(1)
    if drawing_turtle.ycor() > 50 or drawing_turtle.xcor() < 100:
        break

# Explain how the above code works:
#
# Explain how we use an or if statement to end a while True loop at an appropriate time
#
