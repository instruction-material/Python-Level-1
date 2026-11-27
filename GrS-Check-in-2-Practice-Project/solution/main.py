import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
player = turtle.Turtle("turtle")
player.color("blue")
player.penup()
target = turtle.Turtle("circle")
target.color("red")
target.penup()
writer = turtle.Turtle(visible=False)
writer.penup()
writer.goto(-175, 180)
state = "aiming"
distance_left = 0


def target_hit():
    return player.distance(target) < 16


def reset():
    global state, distance_left
    state = "aiming"
    distance_left = 0
    player.goto(0, 0)
    player.setheading(0)
    target.setheading(random.randint(0, 35) * 10)
    target.goto(0, 0)
    target.forward(random.randint(80, 155))
    writer.clear()
    writer.write("Space to launch. R to reset.")
    screen.update()


def launch():
    global state, distance_left
    if state == "aiming":
        state = "moving"
        distance_left = 180


def finish(message):
    global state
    state = "finished"
    writer.clear()
    writer.write(message + " Press R to replay.")
    print(message)


def advance():
    global distance_left
    if state == "aiming":
        player.left(10)
        screen.update()
    elif state == "moving":
        player.forward(6)
        distance_left -= 6
        if target_hit():
            finish("Hit!")
        elif distance_left == 0:
            finish("Miss.")
        screen.update()
    screen.ontimer(advance, 35)


screen.onkey(launch, "space")
screen.onkey(reset, "r")
reset()
screen.ontimer(advance, 35)
print("Target Check-In running")
screen.listen()
turtle.done()
