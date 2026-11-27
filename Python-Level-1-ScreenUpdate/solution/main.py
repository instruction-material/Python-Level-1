import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)
frame = 0
last_frame = 20


def draw_frame():
    pen.clear()
    pen.penup()
    pen.goto(-100 + 10 * frame, -20)
    pen.pendown()
    pen.circle(20)
    screen.update()


def advance():
    global frame
    draw_frame()
    if frame < last_frame:
        frame += 1
        screen.ontimer(advance, 40)


advance()
print("Animation running")
turtle.done()
