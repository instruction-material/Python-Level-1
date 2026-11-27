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
    # TODO: Both coordinate differences must be strictly below 10.
    return False


def advance():
    # TODO: Move both turtles, then check touching.
    # Announce a new contact once. Clear the flag on separation.
    # Update the scene and schedule one more frame while frames remain.
    pass


screen.onkey(lambda: player.left(10), "Left")
screen.onkey(lambda: player.right(10), "Right")
screen.onkey(lambda: other.left(10), "a")
screen.onkey(lambda: other.right(10), "d")
screen.listen()
screen.update()
advance()
print("Collision workspace ready")
turtle.done()
