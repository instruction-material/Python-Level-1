import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)
frame = 0
last_frame = 20


def draw_frame():
    # TODO: Clear the previous circle, lift the pen and reposition it.
    # Use x = -100 + 10 * frame and y = -20. Draw a circle of radius 20.
    # TODO: Update the screen once after the frame is complete.
    pass


def advance():
    # TODO: Draw the frame. If frame is below last_frame, increment it
    # and schedule advance in 40 milliseconds.
    pass


screen.update()
advance()
print("Animation workspace ready")
turtle.done()
