import turtle


limit = 200
step_size = 5
score = 0
screen = turtle.Screen()
player = turtle.Turtle("turtle")
player.speed(0)

border = turtle.Turtle(visible=False)
border.speed(0)
border.color("red")
border.penup()
border.goto(-limit, limit)
border.pendown()
for side in range(4):
    border.forward(2 * limit)
    border.right(90)

label = turtle.Turtle(visible=False)
label.penup()
label.goto(-limit, limit + 10)
label.write("Score: 0")


def turn_left():
    player.left(10)


def turn_right():
    player.right(10)


def outside(x, y):
    # TODO: Return true if either coordinate crosses its bounds.
    return False


def advance():
    # TODO: Move once, then check the new coordinates before scoring.
    # TODO: If outside, announce the ending and stop scheduling frames.
    # TODO: Otherwise update the score and schedule advance in 20 ms.
    pass


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()
advance()
print("Boundary workspace ready")
turtle.done()
