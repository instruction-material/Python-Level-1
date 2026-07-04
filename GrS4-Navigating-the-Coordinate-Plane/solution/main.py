import turtle

graph_drawer = turtle.Turtle()
graph_drawer.speed(0)

graph_drawer.penup()
graph_drawer.goto(-500, 0)
graph_drawer.pendown()
graph_drawer.goto(500, 0)
graph_drawer.penup()
graph_drawer.goto(0, -500)
graph_drawer.pendown()
graph_drawer.goto(0, 500)

graph_drawer.penup()
graph_drawer.goto(50,100)
graph_drawer.write("Quadrant I", font=("Arial", 16, "normal"))
graph_drawer.goto(-150,100)
graph_drawer.write("Quadrant II", font=("Arial", 16, "normal"))
graph_drawer.goto(-150,-100)
graph_drawer.write("Quadrant III", font=("Arial", 16, "normal"))
graph_drawer.goto(50,-100)
graph_drawer.write("Quadrant IV", font=("Arial", 16, "normal"))
graph_drawer.goto(10,-150)
graph_drawer.write("y-axis", font=("Arial", 12, "normal"))
graph_drawer.goto(-120,10)
graph_drawer.write("x-axis", font=("Arial", 12, "normal"))

graph_drawer.ht()

# make a turtle and move it from the origin (where the two lines meet and our turtle starts) to somewhere in Quadrant I using goto()

drawing_turtle = turtle.Turtle()
drawing_turtle.penup()
drawing_turtle.goto(50, 50)

# Next, move your turtle to Qudrant II. Did our X or Y coordinate change into a negative number?

drawing_turtle.goto(-50, 50)

# Now move your turtle to Quadrant III. Again, which of our coordinates changed from a positive to a negative?

drawing_turtle.goto(-50, -50)

# Finally, have your turtle move to Quadrant IV. Which of our coordinates changed its sign this time?

drawing_turtle.goto(50, -50)

# Are positive X coordinates to the left or the right of the y-axis? What about negative coordinates?
#

# Are positive Y coordinates below or above the x-axis? What about negative coordinates?
#

# Tell your turtle to go to (50, 0). What axis is your turtle sitting on after it moves?
#

# Next, tell your turtle to go to (0, 50). What axis is your turtle sitting on after it moves?
#

# Which quadrant will your turtle be in if it goes to the coordinates (-100, -100)?
#

# Which quadrant will your turtle be in if it goes to the coordinates (-200, 50)?
#

# Which quadrant will your turtle be in if it goes to the coordinates (30, 20)?
#

# Which quadrant will your turtle be in if it goes to the coordinates (30, -200)?
#