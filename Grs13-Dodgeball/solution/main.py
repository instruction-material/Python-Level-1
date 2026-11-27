# Original activity: https://app.junilearning.com/juniverse/projects/65e2318a8a9896d5deae7712

import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
arena = 200
lives = 10


def draw_border(color):
    border = turtle.Turtle(visible=False)
    border.color(color)
    border.penup()
    border.goto(-arena, arena)
    border.pendown()
    for side in range(4):
        border.forward(2 * arena)
        border.right(90)


draw_border("black")
player = turtle.Turtle("turtle")
player.penup()
writer = turtle.Turtle(visible=False)
writer.penup()
writer.goto(-arena, arena + 10)

balls = []
for index in range(10):
    ball = turtle.Turtle("circle")
    ball.color("red")
    ball.penup()
    ball.goto(random.randint(-180, 180), random.randint(-180, 180))
    ball.setheading(random.randint(0, 359))
    balls.append(ball)


def reflect_at_walls(actor):
    if actor.xcor() > arena or actor.xcor() < -arena:
        actor.setx(max(-arena, min(arena, actor.xcor())))
        actor.setheading(180 - actor.heading())
    if actor.ycor() > arena or actor.ycor() < -arena:
        actor.sety(max(-arena, min(arena, actor.ycor())))
        actor.setheading(-actor.heading())


def touching(first, second):
    return (
        abs(first.xcor() - second.xcor()) < 10
        and abs(first.ycor() - second.ycor()) < 10
    )


def turn_left():
    player.left(10)


def turn_right():
    player.right(10)


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()


def advance():
    global lives
    player.forward(6)
    reflect_at_walls(player)
    for ball in balls:
        ball.forward(6)
        reflect_at_walls(ball)

    for ball in balls:
        if touching(player, ball):
            lives -= 1
            player.goto(0, 0)
            break

    writer.clear()
    if lives > 0:
        writer.write(f"Lives: {lives}")
        screen.ontimer(advance, 25)
    else:
        writer.write("Game over")
    screen.update()


writer.write(f"Lives: {lives}")
screen.update()
screen.ontimer(advance, 25)
print("Dodgeball running")
turtle.done()
