import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

pen.color("midnightblue")
pen.pensize(3)
distance = 14
angle = 30


def move_forward():
    pen.forward(distance)
    screen.update()
    print("Forward")


def move_backward():
    pen.forward(-distance)
    screen.update()
    print("Backward")


def turn_left():
    pen.left(angle)
    screen.update()
    print("Left")


def turn_right():
    pen.right(angle)
    screen.update()
    print("Right")


def tap_direction(x, y):
    if abs(x) > abs(y):
        if x > 0:
            turn_right()
        else:
            turn_left()
    elif y > 0:
        move_forward()
    else:
        move_backward()


screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
# TODO: Connect the remaining arrow key to its callback.
screen.onclick(tap_direction)
screen.listen()

screen.update()
print("Etch A Sketch workspace ready")
turtle.done()
