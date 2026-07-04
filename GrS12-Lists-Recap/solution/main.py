###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

turtle.colormode(255)


# Explain what a list is:
#

# Make an empty list named turtles

turtles = []

# Add 3 turtles to turtles

for i in range(3):
    drawing_turtle = turtle.Turtle()
    turtles.append(drawing_turtle)

# Loop through turtles and have each turtle move 50 pixels forward

for turt in turtles:
    turt.forward(50)

# Edit your loop so that the turtles turn a random amount of degrees before going forward

for turt in turtles:
    turt.right(random.randint(1, 360))
    turt.forward(50)

# Explain why lists are useful:
#
