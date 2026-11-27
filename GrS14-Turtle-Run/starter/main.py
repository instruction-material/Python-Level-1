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

lanes = (-64, 0, 64)
sequence = [(1, "gem"), (0, "block"), (2, "gem"), (1, "block"), (0, "gem")]
player_lane = 1
step = 0
y = 66
score = 0
running = False
message = "Press Space or tap to start"
fall_speed = 8


def render():
    pen.clear()
    for x in lanes:
        for mark in range(-80, 81, 20):
            point(x, mark, 3, "lightsteelblue")
    point(lanes[player_lane], -62, 20, "darkcyan")
    if running:
        lane, kind = sequence[step]
        point(lanes[lane], y, 15, "goldenrod" if kind == "gem" else "firebrick")
    label(0, 86, "Gems: " + str(score))
    label(0, -95, message)
    screen.update()


def move(change):
    global player_lane
    if running:
        player_lane = min(2, max(0, player_lane + change))
        render()


def resolve(lane, kind):
    global score
    if lane == player_lane:
        if kind == "block":
            return "A blocker ended the run"
        score += 0  # TODO: Count the collected gem exactly once.
        if score == 3:
            return "Three gems collected"
    return ""


def tick():
    global y, step, message, running
    y -= fall_speed
    if y <= -62:
        message = resolve(*sequence[step])
        step += 1
        y = 66
        if message or step == len(sequence):
            running = False
            message = message or "Run ended. Try a new route."
            print(message, "Gems:", score)
    render()
    if running:
        screen.ontimer(tick, 75)


def start():
    global player_lane, step, y, score, running, message
    if running:
        return
    player_lane, step, y, score = 1, 0, 66, 0
    running, message = True, "Left and Right change lanes"
    print("Turtle run started")
    render()
    screen.ontimer(tick, 75)


def tap(x, y):
    if running:
        move(-1 if x < 0 else 1)
    else:
        start()


render()
screen.onkey(lambda: move(-1), "Left")
screen.onkey(lambda: move(1), "Right")
screen.onkey(start, "space")
screen.onclick(tap)
screen.listen()

print("Turtle Run workspace ready")
turtle.done()
