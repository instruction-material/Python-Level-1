import turtle
import random
turtle.colormode(255)

juni = turtle.Turtle()
juni.speed(0)
juni.goto(0,0)

screen = turtle.Screen()

def draw_rectangle(x, y):
  red_value = random.randint(0, 255)
  green_value = random.randint(0, 255)
  blue_value = random.randint(0, 255)

  juni.color(red_value, green_value, blue_value)

  for i in range(2):
    juni.forward(x)
    juni.left(90)
    juni.forward(y)
    juni.left(90)


screen.onclick(draw_rectangle)
screen.listen()