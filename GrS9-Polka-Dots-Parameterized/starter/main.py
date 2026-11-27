import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

def draw_dot(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.dot(size)


def place_dot(x, y):
    size = 10  # TODO: Grow the dot with horizontal distance from the center.
    color = "orchid" if x < 0 else "teal"
    draw_dot(x, y, size, color)
    screen.update()
    print("Dot diameter:", size)


screen.onclick(place_dot)
screen.listen()

screen.update()
print("Polka Dots workspace ready")
turtle.done()
