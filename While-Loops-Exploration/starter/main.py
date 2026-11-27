import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)


guide = turtle.Turtle(visible=False)
guide.speed(0)
guide.penup()
guide.goto(0, -86)
guide.pendown()
guide.setheading(90)
guide.forward(172)

guide.penup()
guide.goto(24, 62)
guide.setheading(0)
guide.color("firebrick")
guide.begin_fill()
guide.pendown()
for edge in range(8):
    guide.forward(22)
    guide.right(45)
guide.end_fill()
guide.penup()
guide.goto(35, 34)
guide.color("white")
guide.write("STOP", align="center", font=("Arial", 11, "bold"))

pen.penup()
pen.goto(-150, 0)
pen.shape("turtle")
pen.color("forestgreen")


def move_to_line(step):
    if step <= 0:
        raise ValueError("Step must be positive.")
    pen.setheading(0)
    moves = 0
    # TODO: Replace False with the condition that the turtle is left of x = 0.
    while False:
        pen.forward(min(step, -pen.xcor()))
        moves += 1
    return moves


moves = move_to_line(5)
print("Moves:", moves, "Final x:", round(pen.xcor()))

screen.update()
print("While Loops Exploration workspace ready")
turtle.done()
