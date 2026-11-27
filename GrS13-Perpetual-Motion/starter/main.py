import turtle


screen = turtle.Screen()
player = turtle.Turtle("turtle")
player.penup()
player.speed(0)
running = True


def turn_left():
    player.left(5)


def turn_right():
    player.right(5)


def stop():
    global running
    running = False


def advance():
    if not running:
        return
    # TODO: Move the player forward one step.
    # TODO: Schedule advance to run again in 20 milliseconds.
    pass


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(stop, "space")
screen.listen()
advance()
print("Motion workspace ready")
turtle.done()
