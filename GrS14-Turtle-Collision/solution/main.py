import turtle


screen = turtle.Screen()
screen.tracer(0)
player = turtle.Turtle("turtle")
other = turtle.Turtle("turtle")
other.color("blue")
player.penup()
other.penup()
player.goto(-20, 0)
other.goto(20, 0)
other.setheading(180)
message = turtle.Turtle(visible=False)
message.penup()
message.goto(-80, 40)
touching_before = False
frames_left = 40


def touching(ax, ay, bx, by):
    return abs(ax - bx) < 10 and abs(ay - by) < 10


def advance():
    global touching_before, frames_left
    if frames_left == 0:
        return
    player.forward(1)
    other.forward(1)
    contact = touching(player.xcor(), player.ycor(), other.xcor(), other.ycor())
    if contact and not touching_before:
        message.clear()
        message.write("Collision!")
    touching_before = contact
    frames_left -= 1
    screen.update()
    if frames_left > 0:
        screen.ontimer(advance, 25)


screen.onkey(lambda: player.left(10), "Left")
screen.onkey(lambda: player.right(10), "Right")
screen.onkey(lambda: other.left(10), "a")
screen.onkey(lambda: other.right(10), "d")
screen.listen()
advance()
print("Collision run started")
turtle.done()
