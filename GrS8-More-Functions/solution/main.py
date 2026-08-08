import turtle

drawing_turtle = turtle.Turtle()
drawing_turtle.speed(0)


def draw_square(side_length):
    drawing_turtle.pendown()
    for i in range(4):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(90)
    drawing_turtle.penup()


def draw_triangle(side_length):
    drawing_turtle.pendown()
    for i in range(3):
        drawing_turtle.forward(side_length)
        drawing_turtle.right(120)
    drawing_turtle.penup()


draw_square(100)
draw_triangle(200)

# How would we make the turtle draw ten different squares, starting from a side length of 20 and going up by 5 each time?

side_length = 20
for i in range(10):
    draw_square(side_length)
    side_length += 5
