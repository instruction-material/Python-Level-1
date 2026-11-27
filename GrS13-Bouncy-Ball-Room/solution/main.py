import random
import turtle


limit = 200
step_size = 10
screen = turtle.Screen()
screen.tracer(0)
border = turtle.Turtle(visible=False)
border.penup()
border.goto(-limit, limit)
border.pendown()
for side in range(4):
    border.forward(2 * limit)
    border.right(90)

balls = []
for index in range(10):
    ball = turtle.Turtle("circle")
    ball.color("red")
    ball.penup()
    ball.goto(random.randint(-180, 180), random.randint(-180, 180))
    ball.setheading(random.randint(0, 359))
    balls.append(ball)


def reflect_at_walls(ball):
    if ball.xcor() > limit:
        ball.setx(limit)
        ball.setheading(180 - ball.heading())
    elif ball.xcor() < -limit:
        ball.setx(-limit)
        ball.setheading(180 - ball.heading())
    if ball.ycor() > limit:
        ball.sety(limit)
        ball.setheading(-ball.heading())
    elif ball.ycor() < -limit:
        ball.sety(-limit)
        ball.setheading(-ball.heading())


def advance():
    for ball in balls:
        ball.forward(step_size)
        reflect_at_walls(ball)
    screen.update()
    screen.ontimer(advance, 25)


advance()
print("Ball room running")
turtle.done()
