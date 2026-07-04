import turtle

drawing_turtle = turtle.Turtle()
screen = turtle.Screen()

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


# create functions for keyboard events
def turn_left():
    drawing_turtle.left(10)


def turn_right():
    drawing_turtle.right(10)


# bind keyboard events to screen
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()

# write score
score = 0
score_turtle = turtle.Turtle()
score_turtle.speed(1000)
score_turtle.penup()
score_turtle.goto(-200, 210)
score_turtle.write("Score: " + str(score))

# main loop - turtle continuously moves and checks if out of bounds
drawing_turtle.color("black")
drawing_turtle.goto(0, 0)
drawing_turtle.pendown()
while True:
    drawing_turtle.forward(5)

    # check if turtle is out of bounds
    if (
        drawing_turtle.xcor() > 200
        or drawing_turtle.xcor() < -200
        or drawing_turtle.ycor() > 200
        or drawing_turtle.ycor() < -200
    ):
        drawing_turtle.write("Out of bounds!")
        break
    else:
        # update score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: " + str(score))

"""
alternative while loop solution, for advanced students:

while not (t.xcor() > 200 or t.xcor() < -200 or t.ycor() > 200 or t.ycor() < -200):
  t.forward(5)
  score += 1
  scoreTurtle.clear()
  scoreTurtle.write("Score: " + str(score))
"""
