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

paddles = [0, 0]
scores = [0, 0]
ball = [0, 0]
velocity = [7, 3]
running = False
wall = 77
goal = 5


def set_paddle(side, y):
    paddles[side] = min(54, max(-54, y))
    render()


def render():
    pen.clear()
    for y in range(-60, 61, 15):
        point(0, y, 3, "lightsteelblue")
    for side, x in enumerate((-112, 112)):
        for offset in (-18, -9, 0, 9, 18):
            point(x, paddles[side] + offset, 13, "steelblue" if side == 0 else "darkorange")
    point(*ball, 12, "purple")
    label(0, 81, str(scores[0]) + "   Rally   " + str(scores[1]))
    if not running:
        label(0, -93, "Tap center or press Space")
    screen.update()


def advance():
    old_x = ball[0]
    ball[0] += velocity[0]
    ball[1] += velocity[1]
    if ball[1] > wall or ball[1] < -wall:
        limit = wall if ball[1] > wall else -wall
        ball[1] = 2 * limit - ball[1]
        velocity[1] = -velocity[1]
    for side, x in enumerate((-112, 112)):
        crossing = old_x > x >= ball[0] if side == 0 else old_x < x <= ball[0]
        if crossing and abs(ball[1] - paddles[side]) <= 25:
            ball[0] = 2 * x - ball[0]
            velocity[0] = -velocity[0]
    if abs(ball[0]) > 145:
        winner = int(ball[0] < 0)
        scores[winner] += 0  # TODO: Award one point to the player who did not miss.
        ball[:] = [0, 0]
        velocity[:] = [7 if winner == 0 else -7, 3]
        return winner


def tick():
    global running
    winner = advance()
    if winner is not None:
        print("Rally score:", scores[0], scores[1])
        if scores[winner] == goal:
            running = False
            print("Match finished")
    render()
    if running:
        screen.ontimer(tick, 65)


def start():
    global running
    if running:
        return
    paddles[:] = [0, 0]
    scores[:] = [0, 0]
    ball[:] = [0, 0]
    velocity[:] = [7, 3]
    running = True
    render()
    print("Rally started")
    screen.ontimer(tick, 65)


def tap(x, y):
    if not running:
        start()
    elif x < -25:
        set_paddle(0, y)
    elif x > 25:
        set_paddle(1, y)


render()
screen.onkey(lambda: set_paddle(0, paddles[0] + 15), "w")
screen.onkey(lambda: set_paddle(0, paddles[0] - 15), "s")
screen.onkey(lambda: set_paddle(1, paddles[1] + 15), "Up")
screen.onkey(lambda: set_paddle(1, paddles[1] - 15), "Down")
screen.onkey(start, "space")
screen.onclick(tap)
screen.listen()

print("Paddle Rally workspace ready")
turtle.done()
