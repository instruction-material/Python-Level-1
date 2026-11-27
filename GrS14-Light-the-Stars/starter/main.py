import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
screen.colormode(255)
arena = 190
frames_left = 1650
last_status = None
screen.bgcolor(195, 20, 50)
player = turtle.Turtle("turtle")
player.color("white")
player.penup()
status = turtle.Turtle(visible=False)
status.color("white")
status.penup()
status.goto(-arena, arena + 10)

unlit = []
for index in range(10):
    star = turtle.Turtle("circle")
    star.color("white")
    star.penup()
    star.goto(random.randint(-175, 175), random.randint(-175, 175))
    unlit.append(star)


def show_status(message):
    global last_status
    if message != last_status:
        status.clear()
        status.write(message)
        last_status = message


def reflect_at_walls(actor):
    if actor.xcor() > arena or actor.xcor() < -arena:
        actor.setx(max(-arena, min(arena, actor.xcor())))
        actor.setheading(180 - actor.heading())
    if actor.ycor() > arena or actor.ycor() < -arena:
        actor.sety(max(-arena, min(arena, actor.ycor())))
        actor.setheading(-actor.heading())


def touching(first, second):
    # TODO: Compare both absolute coordinate differences to the hitbox limit.
    return False


def turn_left():
    player.left(10)


def turn_right():
    player.right(10)


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")


def advance():
    global frames_left
    player.forward(2)
    reflect_at_walls(player)
    # TODO: Loop over a copy of unlit, color each touched star yellow,
    # and remove it from unlit so one star can only count once.

    frames_left -= 1
    red = 30 + frames_left // 10
    screen.bgcolor(red, 20, 50)
    if not unlit:
        show_status("All stars lit!")
    elif frames_left == 0:
        show_status("Time is up!")
    else:
        show_status(f"Stars lit: {10 - len(unlit)} / 10")
        screen.ontimer(advance, 20)
    screen.update()


advance()
print("Light the Stars workspace ready")
screen.listen()
turtle.done()
