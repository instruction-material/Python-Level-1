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


writer = turtle.Turtle(visible=False)
writer.penup()
writer.color("black")


def walk_positions(start, step):
    if step <= 0:
        raise ValueError("Step must be positive.")
    positions = []
    x = start
    while x < 0:
        x += min(step, -x)
        positions.append(x)
    return positions


def show_position(x):
    pen.goto(x, 0)
    writer.clear()
    writer.goto(x, -23)
    writer.write(x, align="center", font=("Arial", 11, "normal"))
    screen.update()


positions = walk_positions(-150, 5)


def show_next(index):
    show_position(positions[index])
    if index + 1 < len(positions):
        screen.ontimer(lambda: show_next(index + 1), 45)


show_position(-150)
if positions:
    screen.ontimer(lambda: show_next(0), 45)
print("Moves:", len(positions))

print("While Loops Exploration reference ready")
turtle.done()
