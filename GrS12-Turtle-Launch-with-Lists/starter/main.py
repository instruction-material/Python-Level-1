import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

pen.penup()
pen.goto(70, -67)
pen.setheading(90)
pen.color("lightsteelblue")
pen.pensize(4)
pen.pendown()
pen.forward(136)
pen.penup()
pen.goto(100, -67)
pen.pendown()
pen.forward(136)
pen.penup()
pen.goto(60, 76)
pen.write("Landing zone")

fleet = []
for lane in range(4):
    pilot = turtle.Turtle(visible=False)
    pilot.speed(0)
    pilot.penup()
    pilot.goto(-120, 45 - 30 * lane)
    fleet.append(pilot)


def launch(pilot, distance):
    endpoint = -120 + distance
    if endpoint < 70:
        outcome, color = "undershoot", "darkorange"
    elif endpoint <= 100:
        outcome, color = "landed", "seagreen"
    else:
        outcome, color = "overshoot", "firebrick"
    pilot.color(color)
    pilot.pendown()
    pilot.goto(endpoint, pilot.ycor())
    pilot.penup()
    pilot.dot(10)
    return outcome


outcomes = []
for pilot in fleet[:1]:  # TODO: Visit every turtle in the list.
    outcomes.append(launch(pilot, random.randint(160, 245)))

print("Launched:", len(outcomes), outcomes)

screen.update()
print("Turtle Launch with Lists workspace ready")
turtle.done()
