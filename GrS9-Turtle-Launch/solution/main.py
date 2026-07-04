import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

# draw Earth
earth = turtle.Turtle()
earth.speed(10000)
earth.penup()
earth.goto(-200, 0)
earth.color("deep sky blue")
earth.pendown()
earth.begin_fill()
for i in range(36):
    earth.forward(10)
    earth.right(10)
earth.end_fill()
earth.ht()

# draw moon
moon = turtle.Turtle()
moon.speed(10000)
moon.penup()
moon.goto(200, -25)
moon.color("light slate gray")
moon.pendown()
moon.begin_fill()
for i in range(36):
    moon.forward(5)
    moon.right(10)
moon.end_fill()
moon.ht()


def launch():
    drawing_turtle = turtle.Turtle()
    drawing_turtle.color("red")
    drawing_turtle.shape("turtle")
    drawing_turtle.speed(10000)
    drawing_turtle.penup()
    drawing_turtle.goto(-200, -50)
    drawing_turtle.speed(10)
    travel_dist = random.randint(200, 500)
    drawing_turtle.forward(travel_dist)
    if travel_dist > 400:
        drawing_turtle.color("white")


screen.onkey(launch, "space")
screen.listen()
