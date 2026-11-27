import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

screen.bgcolor("black")
pen.color("white")


pen.penup()
pen.goto(20, 100)
pen.setheading(300)
pen.pendown()


def inward_spiral(length, shrink, turn):
    if shrink <= 0:
        raise ValueError("Shrink must be positive.")
    count = 0
    while length > 0:
        pen.forward(length)
        pen.right(turn)
        length -= 1  # TODO: Use the supplied shrink amount for each step.
        count += 1
    return count, length


steps, final_length = inward_spiral(160, 3, 119)
print("Steps:", steps, "Final length:", final_length)

screen.update()
print("Out of the Void workspace ready")
turtle.done()
