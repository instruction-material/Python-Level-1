from math import cos, radians, sin

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)


def point(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.dot(size, color)


def label(x, y, text):
    pen.penup()
    pen.goto(x, y)
    pen.color("midnightblue")
    pen.write(text, align="center", font=("Arial", 12, "normal"))

angle = 0
speed = 0
timer_pending = False


def render():
    pen.clear()
    point(0, 0, 26, "midnightblue")
    for offset, color in [(0, "darkcyan"), (120, "tomato"), (240, "goldenrod")]:
        radians_here = radians(angle + offset)
        x, y = cos(radians_here) * 39, sin(radians_here) * 39
        point(x / 2, y / 2, 18, "slateblue")
        point(x, y, 28, color)
    label(0, 75, "Speed: " + str(speed))
    screen.update()


def schedule():
    global timer_pending
    if speed > 0 and not timer_pending:
        timer_pending = True
        screen.ontimer(tick, 110)


def tick():
    global angle, speed, timer_pending
    timer_pending = False
    angle = (angle + speed) % 360
    # TODO: Reduce speed by one, without going below zero.
    render()
    schedule()


def adjust(change):
    global speed
    speed = min(24, max(0, speed + change))
    print("Spinner speed:", speed)
    render()
    schedule()


render()
screen.onkey(lambda: adjust(8), "space")
screen.onkey(lambda: adjust(-4), "Down")
screen.onclick(lambda x, y: adjust(-4 if x < 0 else 8))
screen.listen()

print("Fidget Spinner workspace ready")
turtle.done()
