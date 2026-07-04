###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random
import time
import turtle

# ------------------------------------------------------------
# Function definitions
# ------------------------------------------------------------


def is_inside_bounds(x, y):
    inside_x = -BOUNDARY <= x <= BOUNDARY
    inside_y = -BOUNDARY <= y <= BOUNDARY
    return inside_x and inside_y


def update_score():
    score_turtle.clear()
    score_turtle.write("Score: " + str(score), font=("Arial", 16, "normal"))


def draw_border():
    border_turtle.penup()
    border_turtle.goto(-BOUNDARY, -BOUNDARY)
    border_turtle.pendown()

    for side in range(4):
        border_turtle.forward(BOUNDARY * 2)
        border_turtle.left(90)


def move_player(dx, dy):
    next_x = player.xcor() + dx
    next_y = player.ycor() + dy

    if is_inside_bounds(next_x, next_y):
        player.goto(next_x, next_y)


def move_up():
    move_player(0, PLAYER_STEP)


def move_down():
    move_player(0, -PLAYER_STEP)


def move_left():
    move_player(-PLAYER_STEP, 0)


def move_right():
    move_player(PLAYER_STEP, 0)


def make_enemy(x, y, dx, dy, color):
    enemy = turtle.Turtle()
    enemy.shape("triangle")
    enemy.color(color)
    enemy.penup()
    enemy.goto(x, y)
    enemy.dx = dx
    enemy.dy = dy
    enemies.append(enemy)


def move_enemies():
    for enemy in enemies:
        next_x = enemy.xcor() + enemy.dx
        next_y = enemy.ycor() + enemy.dy

        if not is_inside_bounds(next_x, enemy.ycor()):
            enemy.dx *= -1
            next_x = enemy.xcor() + enemy.dx

        if not is_inside_bounds(enemy.xcor(), next_y):
            enemy.dy *= -1
            next_y = enemy.ycor() + enemy.dy

        enemy.goto(next_x, next_y)


def check_enemy_collisions():
    global score

    for enemy in enemies:
        close_x = abs(player.xcor() - enemy.xcor()) < HIT_DISTANCE
        close_y = abs(player.ycor() - enemy.ycor()) < HIT_DISTANCE

        if close_x and close_y:
            score += 1
            update_score()
            enemy.goto(random.randint(-120, 120), random.randint(-120, 120))


# ------------------------------------------------------------
# Variables and turtle attributes
# ------------------------------------------------------------

BOUNDARY = 160
PLAYER_STEP = 15
HIT_DISTANCE = 20
score = 0
enemies = []

screen = turtle.Screen()
screen.setup(420, 420)
screen.tracer(0)

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-180, 175)

border_turtle = turtle.Turtle()
border_turtle.hideturtle()
border_turtle.speed(0)


# ------------------------------------------------------------
# One-time setup logic
# ------------------------------------------------------------

draw_border()
update_score()

make_enemy(-100, -70, 2, 3, "red")
make_enemy(80, 40, -3, 2, "purple")
make_enemy(20, 120, 2, -2, "orange")

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")


# ------------------------------------------------------------
# Continuous game logic
# ------------------------------------------------------------

while True:
    move_enemies()
    check_enemy_collisions()
    screen.update()
    time.sleep(0.03)
