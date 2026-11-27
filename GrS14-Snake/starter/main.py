import random

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

trail = [(0, 0), (-1, 0), (-2, 0)]
food = (1, 0)
direction = (1, 0)
pending_direction = direction
running = False
score = 0
message = "Tap or press Space to start"


def render():
    pen.clear()
    for x in range(-7, 8):
        for y in (-4, 4):
            point(19 * x, 19 * y, 4, "lightsteelblue")
    for x, y in trail:
        point(19 * x, 19 * y, 15, "darkcyan")
    point(19 * food[0], 19 * food[1], 13, "goldenrod")
    label(0, 84, "Lights: " + str(score) + " / 5")
    label(0, -98, message)
    screen.update()


def choose_food():
    cells = [(x, y) for y in range(-3, 4) for x in range(-6, 7) if (x, y) not in trail]
    return random.choice(cells)


def queue_turn(turn):
    opposite = (-direction[0], -direction[1])
    global pending_direction
    if running and pending_direction == direction and turn != opposite:
        pending_direction = turn


def advance():
    global direction, score, food
    direction = pending_direction
    x = trail[0][0] + direction[0]
    y = trail[0][1] + direction[1]
    head = (x, y)
    if abs(x) > 7 or abs(y) > 4:
        return "Trail reached the edge"
    collecting = head == food
    occupied = trail if collecting else trail[:-1]
    if head in occupied:
        return "Trail folded onto itself"
    trail.insert(0, head)
    if collecting:
        score += 1
        food = choose_food()
        print("Lights collected:", score)
        if score == 5:
            return "All five lights collected"
    else:
        pass  # TODO: Remove the last position on a move without food.
    return ""


def tick():
    global message, running
    message = advance()
    if message:
        running = False
        print(message)
    render()
    if running:
        screen.ontimer(tick, 235)


def start():
    global food, direction, pending_direction, running, score, message
    if running:
        return
    trail[:] = [(0, 0), (-1, 0), (-2, 0)]
    food, score = (1, 0), 0
    direction = pending_direction = (1, 0)
    running, message = True, ""
    print("Trail started")
    render()
    screen.ontimer(tick, 235)


def tap(x, y):
    if not running:
        start()
    elif abs(x) > abs(y):
        queue_turn((1 if x > 0 else -1, 0))
    else:
        queue_turn((0, 1 if y > 0 else -1))


render()
screen.onkey(lambda: queue_turn((0, 1)), "Up")
screen.onkey(lambda: queue_turn((0, -1)), "Down")
screen.onkey(lambda: queue_turn((-1, 0)), "Left")
screen.onkey(lambda: queue_turn((1, 0)), "Right")
screen.onkey(start, "space")
screen.onclick(tap)
screen.listen()

print("Trail Collector workspace ready")
turtle.done()
