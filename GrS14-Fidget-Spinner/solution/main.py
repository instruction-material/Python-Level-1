# Inspired by http://www.grantjenks.com/docs/freegames/index.html#fidget

import turtle

# setup drawing turtle and screen
drawing_turtle = turtle.Turtle()
drawing_turtle.ht()
drawing_turtle.width(20)
drawing_turtle.speed(0)

screen = turtle.Screen()
screen.tracer(0)

# global variable for turn speed
turn_speed = 0


# flick() increases the turn speed
def flick():
    global turn_speed
    turn_speed += 10


# slow() decreases the turn speed
def slow():
    global turn_speed
    if turn_speed > 0:
        turn_speed -= 10


# setup key listeners
screen.onkey(flick, "space")
screen.onkey(slow, "Down")
screen.listen()

# setup turnSpeed writer
writer = turtle.Turtle()
writer.ht()
writer.penup()
writer.goto(200, 200)

# main loop
while True:
    # clear our previous drawings
    drawing_turtle.clear()

    # get the angle that we will have to change by and rotate
    angle = turn_speed / 10
    drawing_turtle.right(angle)

    # draw the red circle side
    drawing_turtle.color("black")
    drawing_turtle.forward(100)
    drawing_turtle.color("red")
    drawing_turtle.begin_fill()
    drawing_turtle.left(90)
    for i in range(36):
        drawing_turtle.forward(8)
        drawing_turtle.right(10)
    drawing_turtle.right(90)
    drawing_turtle.end_fill()
    drawing_turtle.color("black")
    drawing_turtle.backward(100)
    drawing_turtle.right(120)

    # draw the green circle side
    drawing_turtle.color("black")
    drawing_turtle.forward(100)
    drawing_turtle.color("green")
    drawing_turtle.begin_fill()
    drawing_turtle.left(90)
    for i in range(36):
        drawing_turtle.forward(8)
        drawing_turtle.right(10)
    drawing_turtle.right(90)
    drawing_turtle.end_fill()
    drawing_turtle.color("black")
    drawing_turtle.backward(100)
    drawing_turtle.right(120)

    # draw the blue circle side
    drawing_turtle.color("black")
    drawing_turtle.forward(100)
    drawing_turtle.color("blue")
    drawing_turtle.begin_fill()
    drawing_turtle.left(90)
    for i in range(36):
        drawing_turtle.forward(8)
        drawing_turtle.right(10)
    drawing_turtle.right(90)
    drawing_turtle.end_fill()
    drawing_turtle.color("black")
    drawing_turtle.backward(100)
    drawing_turtle.right(120)

    # write turnSpeed
    writer.clear()
    writer.write("Turn Speed: " + str(turn_speed))

    screen.update()
