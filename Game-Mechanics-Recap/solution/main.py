import turtle

# A while True loop repeats until an explicit break condition is reached.
screen = turtle.Screen()
drawing_turtle = turtle.Turtle()

# Move forward by 1 pixel exactly 100 times, then stop.
counter = 0
while True:
    drawing_turtle.forward(1)
    counter += 1
    if counter >= 100:
        break

# Start a separate upward walk. Stop only after y is above 50.
drawing_turtle.penup()
drawing_turtle.goto(0, 0)
drawing_turtle.setheading(90)
drawing_turtle.pendown()

while True:
    drawing_turtle.forward(1)
    if drawing_turtle.ycor() > 50:
        break

# Start a separate leftward walk. Either limit can stop this loop.
drawing_turtle.penup()
drawing_turtle.goto(0, 0)
drawing_turtle.setheading(180)
drawing_turtle.pendown()

while True:
    drawing_turtle.forward(1)
    if drawing_turtle.ycor() > 50 or drawing_turtle.xcor() < -100:
        break

# At y == 50 or x == -100 the strict comparisons are still false.
# The next one-pixel step crosses the corresponding limit.
screen.mainloop()
