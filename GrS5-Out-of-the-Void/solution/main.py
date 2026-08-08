import turtle

turtle.colormode(255)

drawing_turtle = turtle.Turtle()
drawing_turtle.color("white")
drawing_turtle.speed(100)
drawing_turtle.setheading(300)
drawing_turtle.penup()
drawing_turtle.goto(-10, 200)
drawing_turtle.pendown()

s = turtle.Screen()
s.bgcolor("black")

n = 300

for i in range(200):
    drawing_turtle.forward(n)
    drawing_turtle.right(119)
    n = n - 3

drawing_turtle.ht()
