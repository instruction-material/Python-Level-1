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
    # TODO: Hold the center inside each wall it crossed.
    # TODO: Reflect the horizontal or vertical part of its direction.
    pass


def advance():
    # TODO: For each ball, move once and reflect at any crossed wall.
    # Refresh the whole scene once and schedule the next frame in 25 ms.
    pass


screen.update()
advance()
print("Ball room workspace ready")
turtle.done()
