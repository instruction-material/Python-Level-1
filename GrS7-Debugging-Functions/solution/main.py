###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import turtle

drawing_turtle = turtle.Turtle()
turtle.colormode(255)


# This function draws a circle with size "circleSize"
def draw_snowball(circle_size):
    drawing_turtle.color("black")
    drawing_turtle.setheading(0)
    for i in range(36):
        drawing_turtle.forward(circle_size)
        drawing_turtle.right(10)


# This function draws a hat, where the middle of the bottom of the hat is at coordinates (x, y)
def draw_hat(x, y):
    drawing_turtle.color("black")
    drawing_turtle.penup()
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()
    drawing_turtle.setheading(0)
    drawing_turtle.forward(30)
    drawing_turtle.left(180)
    drawing_turtle.forward(60)
    drawing_turtle.penup()
    drawing_turtle.begin_fill()
    drawing_turtle.goto(x + 20, y)
    drawing_turtle.pendown()
    drawing_turtle.right(90)
    drawing_turtle.forward(20)
    drawing_turtle.left(90)
    drawing_turtle.forward(40)
    drawing_turtle.left(90)
    drawing_turtle.forward(20)
    drawing_turtle.left(90)
    drawing_turtle.forward(40)
    drawing_turtle.end_fill()


# This function draws a nose, with size "noseSize" at coordinates (x, y)
def draw_carrot_nose(x, y, size):
    drawing_turtle.setheading(0)
    drawing_turtle.penup()
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()
    drawing_turtle.color("orange")
    drawing_turtle.begin_fill()
    for i in range(36):
        drawing_turtle.forward(size)
        drawing_turtle.left(10)
    drawing_turtle.end_fill()


# This function draws an eye, with size "eyeSize" at coordinates (x, y)
def draw_charcoal_eye(x, y, size):
    drawing_turtle.setheading(0)
    drawing_turtle.penup()
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()
    drawing_turtle.color("black")
    drawing_turtle.begin_fill()
    for i in range(36):
        drawing_turtle.forward(size)
        drawing_turtle.left(10)
    drawing_turtle.end_fill()


def draw_left_broomstick_arm(x, y, arm_length):
    drawing_turtle.penup()
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()
    drawing_turtle.color("brown")
    drawing_turtle.setheading(145)
    drawing_turtle.forward(arm_length)
    # Draw fingers
    drawing_turtle.right(40)
    for i in range(20):
        drawing_turtle.forward(15)
        drawing_turtle.backward(15)
        drawing_turtle.left(4)


def draw_right_broomstick_arm(x, y, arm_length):
    drawing_turtle.penup()
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()
    drawing_turtle.color("brown")
    drawing_turtle.setheading(35)
    drawing_turtle.forward(arm_length)
    # Draw fingers
    drawing_turtle.right(40)
    for i in range(20):
        drawing_turtle.forward(15)
        drawing_turtle.backward(15)
        drawing_turtle.left(4)


# Draw the whole snowman!

# Draw his three snowballs: size 8 at (0,100), size 10 at (0,10), and size 12 at (0,-105)
drawing_turtle.penup()
drawing_turtle.goto(0, 100)
drawing_turtle.pendown()
draw_snowball(8)

drawing_turtle.penup()
drawing_turtle.goto(0, 10)
drawing_turtle.pendown()
draw_snowball(10)

drawing_turtle.penup()
drawing_turtle.goto(0, -105)
drawing_turtle.pendown()
draw_snowball(12)

# Draw nose of size 1 at (0,50)
draw_carrot_nose(0, 50, 1)

# Draw eyes of size 0.75 at (-15,65) and (15,65)
draw_charcoal_eye(-15, 65, 0.75)
draw_charcoal_eye(15, 65, 0.75)

# Draw hat at (0,100)
draw_hat(0, 100)

# Draw arms of size 100 at (-25,-25) and (25,-25)
draw_left_broomstick_arm(-25, -25, 100)
draw_right_broomstick_arm(25, -25, 100)
