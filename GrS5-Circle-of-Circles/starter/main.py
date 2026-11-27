import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

pen.color("darkcyan")
for ring in range(18):
    for segment in range(36):
        pen.forward(6)
        pen.right(10)
    # TODO: Turn right by one eighteenth of 360 degrees.

screen.update()
print("Circle of Circles workspace ready")
turtle.done()
