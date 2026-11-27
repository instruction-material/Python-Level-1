import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
lion = turtle.Turtle()
lion.speed(0)


def draw_shape_at(x, y, sides, size):
    lion.penup()
    lion.goto(x, y)
    lion.setheading(0)
    lion.pendown()
    # TODO: Repeat one move and one exterior turn for each side.
    screen.update()


def range_color(number):
    # TODO: Return red for 0–20, yellow for 21–40, and green for 41–60.
    return "red"


for index in range(5):
    draw_shape_at(-160 + index * 62, 80, 4, 28)
for index in range(3):
    x = random.randint(-165 + index * 118, -130 + index * 118)
    lion.color(range_color(random.randint(0, 60)))
    draw_shape_at(x, 5, 3, 32)

def count_passes():
    turns = 0
    while True:
        turns += 1
        if turns == 1:  # TODO: Stop on the fifth pass.
            break
    return turns


turns = count_passes()

swimmers = []
for index in range(3):
    swimmer = turtle.Turtle("turtle")
    swimmer.penup()
    swimmer.goto(-125 + index * 90, -90)
    swimmers.append(swimmer)
for swimmer in swimmers:
    # TODO: Move this swimmer back 30 steps.
    pass

screen.update()
print("Check-In 3 workspace ready")
turtle.done()
