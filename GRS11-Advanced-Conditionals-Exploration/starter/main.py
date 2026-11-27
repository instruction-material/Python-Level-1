import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

def draw_choice(choice):
    if choice == 0:
        pen.color("navy")
        for edge in range(4):
            pen.forward(29)
            pen.left(90)
        return "square"
    elif choice == 4:  # TODO: Use the choice that belongs to the triangle.
        pen.color("teal")
        for edge in range(3):
            pen.forward(29)
            pen.left(120)
        return "triangle"
    else:
        pen.color("darkorange")
        pen.circle(14)
        return "circle"


for choice in range(4):
    pen.penup()
    pen.goto(-105 + 60 * choice, -18)
    pen.setheading(0)
    pen.pendown()
    print(choice, draw_choice(choice))

screen.update()
print("Advanced Conditionals Exploration workspace ready")
turtle.done()
