from random import randint
import turtle


drawing_turtle = turtle.Turtle()
drawing_turtle.speed(0)
drawing_turtle.penup()
numbers = []


def write_row(values, y):
    drawing_turtle.goto(-100, y)
    for value in values:
        drawing_turtle.write(value)
        drawing_turtle.forward(20)


# TODO: Append fifteen random integers from 0 to 10 to numbers.
# TODO: Build a second list with ten added to each original value.
# TODO: Build a third list by multiplying each second-row value by ten.
# Call write_row for the three rows at y = 0, -30, and -60.

print("Numbers:", numbers)
turtle.done()
