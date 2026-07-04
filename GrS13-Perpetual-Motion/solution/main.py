import turtle

drawing_turtle = turtle.Turtle()
screen = turtle.Screen()

drawing_turtle.shape("turtle")
drawing_turtle.penup()

def turn_left():
  drawing_turtle.left(5)

def turn_right():
  drawing_turtle.right(5)

screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()

while True:
  drawing_turtle.forward(1)