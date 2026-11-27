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
    player.forward(1)
    screen.ontimer(advance, 20)


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(stop, "space")
screen.listen()
advance()
print("Motion running")
turtle.done()
