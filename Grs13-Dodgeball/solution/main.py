# Try this project in the Juniverse! https://app.junilearning.com/juniverse/projects/65e2318a8a9896d5deae7712

import turtle
import random

# create screen object
screen = turtle.Screen()
# disable screen updates
screen.tracer(0)

# draw the boundary box
box_drawer = turtle.Turtle()
box_drawer.speed(10)
box_drawer.penup()
box_drawer.goto(-200, 200)
box_drawer.pendown()
for i in range(4):
  box_drawer.forward(400)
  box_drawer.right(90)
box_drawer.ht()

balls = []
for i in range(10):
  drawing_turtle = turtle.Turtle()
  drawing_turtle.penup()
  drawing_turtle.speed(1000)
  drawing_turtle.color("red")
  drawing_turtle.shape("circle")
  drawing_turtle.goto(random.randint(-200,200), random.randint(-200,200))
  drawing_turtle.right(random.randint(0,360))
  balls.append(drawing_turtle)

# add a player
player = turtle.Turtle()
player.shape("turtle")
player.penup()

# start with 10 lives
lives = 10
# display lives
lives_writer = turtle.Turtle()
lives_writer.penup()
lives_writer.goto(-200,210)
lives_writer.write("Lives: " + str(lives))

def check_collision(ball):
  if ball.xcor() > 200 or ball.xcor() < -200:
    ball.right(180)
  elif ball.ycor() > 200 or ball.ycor() < -200:
    ball.right(180)

# motion commands for player
def left():
  player.left(10)

def right():
  player.right(10)

screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

while lives > 0:
  player.forward(10)
  check_collision(player)
  for ball in balls:
    check_collision(ball)
    # check for collision between player and ball
    if abs(ball.xcor() - player.xcor()) < 10 and abs(ball.ycor() - player.ycor()) < 10:
      lives -= 1
      lives_writer.clear()
      lives_writer.write("Lives: " + str(lives))
      player.goto(random.randint(-200,200), random.randint(-200,200))
    ball.forward(10)
    screen.update()

# after the player loses all lives, display game over
lives_writer.goto(0,0)
lives_writer.write("GAME OVER!")
screen.update()

# for repl.it projects only: keep the window open
turtle.mainloop()
