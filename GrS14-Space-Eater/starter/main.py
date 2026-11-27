import random
import turtle


arena = 200
winning_score = 10
round_frames = 1600
score = 0
frames_left = round_frames
playing = True
last_status = None

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)


def draw_border(color):
    border = turtle.Turtle(visible=False)
    border.color(color)
    border.penup()
    border.goto(-arena, arena)
    border.pendown()
    for side in range(4):
        border.forward(2 * arena)
        border.right(90)


draw_border("red")
player = turtle.Turtle("turtle")
player.color("deepskyblue")
player.penup()
scoreboard = turtle.Turtle(visible=False)
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(-arena, arena + 10)

targets = []
for index in range(10):
    target = turtle.Turtle("circle")
    target.color("red")
    target.penup()
    targets.append(target)


def place_target(target):
    target.goto(random.randint(-180, 180), random.randint(-180, 180))
    target.setheading(random.randint(0, 359))


def show_status(message):
    global last_status
    if message != last_status:
        scoreboard.clear()
        scoreboard.write(message)
        last_status = message


def reset_round():
    global score, frames_left, playing
    score = 0
    frames_left = round_frames
    playing = True
    player.goto(0, 0)
    player.setheading(0)
    for target in targets:
        place_target(target)
    show_status(f"Score: {score} / {winning_score}")
    screen.update()


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


screen.onkey(reset_round, "r")


def advance():
    global score, frames_left, playing
    if playing:
        player.forward(6)
        reflect_at_walls(player)
        for target in targets:
            target.forward(2)
            reflect_at_walls(target)
            # TODO: On contact, add a point and move the target.
            # Stop scanning targets after reaching winning_score.

        frames_left -= 1
        if score == winning_score:
            playing = False
            show_status("You win! Press R to replay.")
        elif frames_left == 0:
            playing = False
            show_status("Time is up. Press R to replay.")
        else:
            show_status(f"Score: {score} / {winning_score}")
        screen.update()

    # Keep one timer chain. Resetting the round never creates a second timer.
    screen.ontimer(advance, 25)


reset_round()
screen.ontimer(advance, 25)
print("Space Eater workspace ready")
screen.listen()
turtle.done()
