import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
screen.colormode(255)
whale = turtle.Turtle()
whale.speed(0)


def move_to(x, y):
    whale.penup()
    whale.goto(x, y)
    whale.setheading(0)
    whale.pendown()


def polygon(sides, side_length, turn):
    # TODO: Repeat one forward movement and one turn for each side.
    pass


def surprise_shape(number):
    # TODO: Return the name, side count and turn for all three ranges.
    return "square", 4, 90


def position_color(x, y):
    # TODO: Test the green rule first, then quadrant III; use black otherwise.
    return "black"


move_to(-150, 120)
whale.color("red")
polygon(4, 50, 90)
move_to(-50, 120)
whale.begin_fill()
polygon(4, 50, 90)
whale.end_fill()

move_to(-160, 40)
for step in range(20):
    whale.forward(2)
move_to(-140, -70)
polygon(12, 10, 30)
move_to(-50, -70)
polygon(12, 6, 30)
move_to(30, -70)
polygon(36, 3, 10)

size = random.randint(42, 90)
rgb = (100, 75, 160)  # TODO: Generate three independent values from 0 to 255.
whale.color(*rgb)
number = random.randint(0, 10)
name, sides, turn = surprise_shape(number)
move_to(115, 110)
polygon(sides, size // 2, turn)

move_to(80, -80)
for x, y in [(-50, -50), (101, 0), (0, -100)]:
    whale.color(position_color(x, y))
    whale.forward(15)

screen.update()
print("Check-In 1 workspace ready")
turtle.done()
