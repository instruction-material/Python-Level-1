import turtle

drawing_turtle = turtle.Turtle()
screen = turtle.Screen()

move_speed = 10
turn_speed = 10

def move_forward():
  drawing_turtle.pendown()
  drawing_turtle.forward(move_speed)

def move_backward():
  drawing_turtle.pendown()
  drawing_turtle.backward(move_speed)

def turn_left():
  drawing_turtle.left(turn_speed)

def turn_right():
  drawing_turtle.right(turn_speed)

drawing_turtle.goto(0,0)

# associating event listeners with functions
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()