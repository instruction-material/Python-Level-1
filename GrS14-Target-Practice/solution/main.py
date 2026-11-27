from math import cos, hypot, radians, sin

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

direction = 0
distance = 0
running = False
cursor = (0, 0)
beacon = (92, 0)
radius = 12
message = "Tap to turn or start"


def reaches_beacon(x, y):
    gap = hypot(x - beacon[0], y - beacon[1])
    return gap <= radius


def render():
    pen.clear()
    point(*beacon, radius * 2, "lightseagreen")
    point(0, 0, 8, "lightsteelblue")
    point(cos(radians(direction)) * 25, sin(radians(direction)) * 25, 7, "goldenrod")
    point(*cursor, 14, "purple")
    label(0, 70, "Heading: " + str(direction))
    label(0, -89, message)
    screen.update()


def turn(change):
    global direction
    if not running:
        direction = (direction + change) % 360
        render()


def tick():
    global distance, cursor, message, running
    distance += 8
    angle = radians(direction)
    cursor = (cos(angle) * distance, sin(angle) * distance)
    if reaches_beacon(*cursor):
        running, message = False, "Beacon reached"
    elif distance >= 120:
        running, message = False, "Beacon missed"
    render()
    if running:
        screen.ontimer(tick, 55)
    else:
        print(message)


def start():
    global cursor, distance, running, message
    if running:
        return
    cursor, distance = (0, 0), 0
    running, message = True, "Moving"
    print("Beacon hop started")
    render()
    screen.ontimer(tick, 55)


def tap(x, y):
    if x < -40:
        turn(15)
    elif x > 40:
        turn(-15)
    else:
        start()


render()
screen.onkey(lambda: turn(15), "Left")
screen.onkey(lambda: turn(-15), "Right")
screen.onkey(start, "space")
screen.onclick(tap)
screen.listen()

print("Beacon Hop reference ready")
turtle.done()
