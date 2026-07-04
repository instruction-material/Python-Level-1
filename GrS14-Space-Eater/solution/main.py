###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

# draw the boundary box
box_drawer = turtle.Turtle()
box_drawer.speed(10)
box_drawer.color("red")
box_drawer.penup()
box_drawer.goto(-200, 200)
box_drawer.pendown()
for i in range(4):
    box_drawer.forward(400)
    box_drawer.right(90)
box_drawer.penup()

# create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()

# write score
score = 0
score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.color("white")
score_turtle.goto(-200, 210)
score_turtle.write("Score: 0")

# create targets
targets = []
for i in range(10):
    targets.append(turtle.Turtle())
    targets[i].color("red")
    targets[i].shape("circle")
    targets[i].penup()
    targets[i].speed(0)
    targets[i].setposition(random.randint(-190, 190), random.randint(-190, 190))
    targets[i].right(random.randint(0, 360))


# create functions for keyboard events
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


# bind keyboard events to screen
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()

# main loop for game
while True:
    player.forward(10)

    # check for collisions with boundary
    if player.xcor() > 190 or player.xcor() < -190:
        player.right(180)
    elif player.ycor() > 190 or player.ycor() < -190:
        player.right(180)

    for target in targets:
        target.forward(1)

        # check for collisions with boundary
        if target.xcor() > 190 or target.xcor() < -190:
            target.right(180)
        elif target.ycor() > 190 or target.ycor() < -190:
            target.right(180)

        # check for player/target collisions
        if (
            abs(player.xcor() - target.xcor()) < 10
            and abs(player.ycor() - target.ycor()) < 10
        ):
            target.goto(random.randint(-200, 200), random.randint(-200, 200))
            target.right(random.randint(0, 360))
            score += 1
            score_turtle.clear()
            score_turtle.write("Score: " + str(score))
