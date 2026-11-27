import random
import turtle


screen = turtle.Screen()
screen.tracer(0)
screen.colormode(255)
drawing_turtle = turtle.Turtle()
drawing_turtle.speed(0)
drawing_turtle.right(45)


def change_color():
    drawing_turtle.color(
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )


def draw_layers(sides, turn, base_size):
    for layer in range(1, 4):
        change_color()
        drawing_turtle.begin_fill()
        for side in range(sides):
            drawing_turtle.forward(base_size * layer)
            drawing_turtle.right(turn)
        drawing_turtle.end_fill()
    screen.update()


def draw_diamond():
    draw_layers(4, 90, 16)
    print("Keyboard Art: diamond")


def draw_circle():
    # TODO: Use 36 sides and a 10-degree turn to approximate a circle.
    pass


def draw_pyramid():
    # TODO: Use three sides and a 120-degree turn.
    pass


def change_location():
    drawing_turtle.penup()
    # TODO: Choose independent random coordinates between -115 and 115.
    drawing_turtle.pendown()
    screen.update()
    print("Keyboard Art: moved")


screen.onkey(draw_diamond, "d")
screen.onkey(draw_circle, "c")
# TODO: Bind P to the pyramid callback.
screen.onkey(change_location, "space")
screen.update()
print("Keyboard Art workspace ready")
screen.listen()
turtle.done()
