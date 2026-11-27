import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

pen.color("darkorange")
pen.penup()
pen.goto(0, 65)
pen.setheading(300)
pen.pendown()

side_length = 15
for layer in range(10):
    for side in range(3):
        pen.forward(side_length)
        pen.right(120)
    side_length += 15

screen.update()
print("Pyramid reference ready")
turtle.done()
