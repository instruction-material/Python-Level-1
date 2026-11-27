import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

pen.hideturtle()


def move_fruit(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pendown()


def orange():
    move_fruit(-65, -20, "darkorange")
    pen.dot(36)
    screen.update()
    print("Orange drawn")


def starfruit():
    move_fruit(-19, -13, "goldenrod")
    pen.begin_fill()
    for edge in range(5):
        pen.forward(38)
        pen.right(144)
    pen.end_fill()
    screen.update()
    print("Starfruit drawn")


def cherry():
    move_fruit(66, -20, "crimson")
    pen.dot(26)
    move_fruit(66, -8, "forestgreen")
    pen.left(70)
    pen.forward(16)
    screen.update()
    print("Cherry drawn")


def tap_fruit(x, y):
    if x < -25:
        orange()
    elif x > 25:
        cherry()
    else:
        starfruit()


screen.onkey(orange, "1")
screen.onkey(starfruit, "2")
# TODO: Connect number 3 to the cherry drawing function.
screen.onclick(tap_fruit)
screen.listen()

screen.update()
print("Fruit Stand workspace ready")
turtle.done()
