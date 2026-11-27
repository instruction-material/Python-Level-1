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
    for side in range(sides):
        lion.forward(size)
        lion.left(360 / sides)
    screen.update()


def range_color(number):
    if number <= 20:
        return "red"
    elif number <= 40:
        return "yellow"
    return "green"


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
        if turns == 5:
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
    swimmer.backward(30)

screen.update()
print("Check-In 3:", turns, len(swimmers), range_color(20), range_color(21), range_color(41))
turtle.done()
