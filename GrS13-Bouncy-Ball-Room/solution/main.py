###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle
import random

# draw the boundary box
box_drawer = turtle.Turtle()
box_drawer.speed(10)
box_drawer.penup()
box_drawer.goto(-200, 200)
box_drawer.pendown()
for i in range(4):
    box_drawer.forward(400)
    box_drawer.right(90)
box_drawer.ht()

balls = []
for i in range(10):
    drawing_turtle = turtle.Turtle()
    drawing_turtle.penup()
    drawing_turtle.speed(1000)
    drawing_turtle.color("red")
    drawing_turtle.shape("circle")
    drawing_turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
    drawing_turtle.right(random.randint(0, 360))
    balls.append(drawing_turtle)


def check_collision(ball):
    if ball.xcor() > 200 or ball.xcor() < -200:
        ball.right(180)
    elif ball.ycor() > 200 or ball.ycor() < -200:
        ball.right(180)


while True:
    for ball in balls:
        check_collision(ball)
        ball.forward(10)
