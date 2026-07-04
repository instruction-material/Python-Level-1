###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle

drawing_turtle = turtle.Turtle()

colors = []

colors.append("red")
colors.append("yellow")
colors.append("purple")
colors.append("pink")
colors.append("green")

for color in colors:
    drawing_turtle.color(color)
    drawing_turtle.forward(10)

if "purple" in colors:
    drawing_turtle.write("yes")
else:
    drawing_turtle.write("no")
