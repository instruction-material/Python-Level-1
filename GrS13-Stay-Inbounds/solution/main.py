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
    return x < -limit or x > limit or y < -limit or y > limit


def advance():
    global score
    player.forward(step_size)
    if outside(player.xcor(), player.ycor()):
        player.write("Out of bounds!")
        return
    score += 1
    label.clear()
    label.write("Score: " + str(score))
    screen.ontimer(advance, 20)


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()
advance()
print("Boundary running")
turtle.done()
