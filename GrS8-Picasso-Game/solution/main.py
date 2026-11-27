import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

pen.hideturtle()
part = 0


def move_pen(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pendown()


def reveal_base():
    global part
    if part == 0:
        move_pen(-24, -45, "sienna")
        for edge in range(2):
            pen.forward(48)
            pen.left(90)
            pen.forward(20)
            pen.left(90)
        part = 1
        screen.update()
        print("Base revealed")


def reveal_stem():
    global part
    if part == 1:
        move_pen(0, -25, "forestgreen")
        pen.left(90)
        pen.forward(47)
        part = 2
        screen.update()
        print("Stem revealed")


def reveal_petals():
    global part
    if part == 2:
        for x, y in [(-12, 28), (0, 41), (12, 28), (0, 18)]:
            move_pen(x, y, "orchid")
            pen.dot(18)
        part = 3
        screen.update()
        print("Petals revealed")


def reset_scene():
    global part
    pen.clear()
    part = 0
    screen.update()
    print("Scene reset")


def tap_scene(x, y):
    if y < -70:
        reset_scene()
    elif part == 0:
        reveal_base()
    elif part == 1:
        reveal_stem()
    elif part == 2:
        reveal_petals()


screen.onkey(reveal_base, "1")
screen.onkey(reveal_stem, "2")
screen.onkey(reveal_petals, "3")
screen.onkey(reset_scene, "r")
screen.onclick(tap_scene)
screen.listen()

screen.update()
print("Interactive Drawing reference ready")
turtle.done()
