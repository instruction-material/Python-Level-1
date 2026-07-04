import turtle

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(10000)

side_length = 10

drawing_turtle.penup()
drawing_turtle.goto(0, 200)
drawing_turtle.pendown()
drawing_turtle.setheading(300)

for i in range(50):
    for j in range(3):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(120)

    side_length = side_length + 10
