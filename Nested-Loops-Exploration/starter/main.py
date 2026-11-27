import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

side_length = 30
for layer in range(3):
    for side in range(4):
        pen.forward(side_length)
        pen.right(90)
    # TODO: Add 20 to side_length once per square.

screen.update()
print("Nested Loops Exploration workspace ready")
turtle.done()
