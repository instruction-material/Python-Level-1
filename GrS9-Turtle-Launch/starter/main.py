import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

pen.color("steelblue")
pen.penup()
pen.goto(70, -28)
pen.pendown()
pen.pensize(6)
pen.forward(30)
pen.penup()
pen.goto(65, -52)
pen.write("Landing zone")
pen.pensize(2)
marker = turtle.Turtle(visible=False)
marker.speed(0)
marker.penup()


def classify(endpoint):
    if endpoint < 70:
        return "undershoot", "darkorange"
    elif endpoint < 100:  # TODO: Include the last landing coordinate.
        return "landed", "seagreen"
    else:
        return "overshoot", "firebrick"


def launch(distance):
    endpoint = -120 + distance
    outcome, color = classify(endpoint)
    marker.clear()
    marker.color(color)
    marker.goto(-120, -15)
    marker.pendown()
    marker.goto(endpoint, -15)
    marker.penup()
    marker.dot(12)
    marker.goto(-115, 12)
    marker.write(outcome)
    screen.update()
    print("End x:", endpoint, outcome)


def random_launch(x=None, y=None):
    launch(random.randint(160, 245))


launch(205)
screen.onkey(random_launch, "space")
screen.onclick(random_launch)
screen.listen()

screen.update()
print("Turtle Launch workspace ready")
turtle.done()
