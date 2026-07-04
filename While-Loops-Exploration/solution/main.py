import turtle

drawing_turtle = turtle.Turtle()
sign_drawer = turtle.Turtle()

# Go to the starting position
sign_drawer.penup()
sign_drawer.goto(50, 50)
sign_drawer.pendown()

# Draw a stop sign
sign_drawer.color("red")
sign_drawer.begin_fill()
for i in range(8):
    sign_drawer.forward(50)
    sign_drawer.right(360 / 8)
sign_drawer.end_fill()

# Draw text on sign, then hide the turtle
sign_drawer.penup()
sign_drawer.color("white")
sign_drawer.goto(75, -20)
sign_drawer.pendown()
sign_drawer.write("STOP", align="center", font=("Arial", 16, "normal"))
sign_drawer.ht()

# Configure the main turtle
drawing_turtle.goto(-200, 0)
drawing_turtle.color("green")
drawing_turtle.shape("turtle")
drawing_turtle.pendown()

# Program the turtle to move forward as long as the x coordinate is less than 0
while drawing_turtle.xcor() < 0:
    # Print the x coordinate of the turtle
    drawing_turtle.clear()
    drawing_turtle.write(drawing_turtle.xcor(), font=("Arial", 16, "normal"))
    drawing_turtle.forward(1)

# Keep the window open: note this line is only needed when running projects in repl.it
turtle.mainloop()
