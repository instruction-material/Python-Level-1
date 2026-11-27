import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

rows = 5
columns = 8
spacing = 25
dot_size = 8
start_x, start_y = -88, 50
pen.penup()
pen.color("darkcyan")

for row in range(rows):
    y = start_y  # TODO: Move down by one spacing for each row.
    for column in range(columns):
        x = start_x + column * spacing
        pen.goto(x, y)
        pen.dot(dot_size)

screen.update()
print("Dot Grid workspace ready")
turtle.done()
