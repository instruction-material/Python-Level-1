import turtle
import random

# draw starting lines
lane_drawer = turtle.Turtle()
lane_drawer.right(90)
lane_drawer.speed(1000)
for i in range(15):
  lane_drawer.penup()
  lane_drawer.goto(-200+20*i, 100)
  lane_drawer.write(i)
  lane_drawer.pendown()
  lane_drawer.forward(100)
# draw finish line
lane_drawer.penup()
lane_drawer.goto(-200+20*(i+1), 100)
lane_drawer.write("Finish")
lane_drawer.pendown()
lane_drawer.forward(100)
lane_drawer.ht()

# set up the race turtles
race_turtle_one = turtle.Turtle()
race_turtle_one.penup()
race_turtle_one.color("red")
race_turtle_one.shape("turtle")
race_turtle_one.goto(-200, 80)
race_turtle_one.pendown()

race_turtle_two = turtle.Turtle()
race_turtle_two.penup()
race_turtle_two.color("blue")
race_turtle_two.shape("turtle")
race_turtle_two.goto(-200, 50)
race_turtle_two.pendown()

race_turtle_three = turtle.Turtle()
race_turtle_three.penup()
race_turtle_three.color("orange")
race_turtle_three.shape("turtle")
race_turtle_three.goto(-200, 20)
race_turtle_three.pendown()

# race the turtles until at least one of them reaches the finish line at x = 100
while race_turtle_one.xcor() < 100 and race_turtle_two.xcor() < 100 and race_turtle_three.xcor() < 100:
  race_turtle_one.forward(random.randint(1,5))
  race_turtle_two.forward(random.randint(1,5))
  race_turtle_three.forward(random.randint(1,5))

# check who won or tied
if race_turtle_one.xcor() > race_turtle_two.xcor() and race_turtle_one.xcor() > race_turtle_three.xcor():
  race_turtle_one.write("I win!", font=("Arial", 16, "normal"))
if race_turtle_two.xcor() > race_turtle_one.xcor() and race_turtle_two.xcor() > race_turtle_three.xcor():
  race_turtle_two.write("I win!", font=("Arial", 16, "normal"))
if race_turtle_three.xcor() > race_turtle_one.xcor() and race_turtle_three.xcor() > race_turtle_two.xcor():
  race_turtle_three.write("I win!", font=("Arial", 16, "normal"))
if race_turtle_one.xcor() == race_turtle_two.xcor() and race_turtle_two.xcor() == race_turtle_three.xcor():
  race_turtle_one.write("Tie!", font=("Arial", 16, "normal"))
  race_turtle_two.write("Tie!", font=("Arial", 16, "normal"))
  race_turtle_three.write("Tie!", font=("Arial", 16, "normal"))
if race_turtle_one.xcor() == race_turtle_two.xcor():
  race_turtle_one.write("Tie!", font=("Arial", 16, "normal"))
  race_turtle_two.write("Tie!", font=("Arial", 16, "normal"))
if race_turtle_one.xcor() == race_turtle_three.xcor():
  race_turtle_one.write("Tie!", font=("Arial", 16, "normal"))
  race_turtle_three.write("Tie!", font=("Arial", 16, "normal"))
if race_turtle_two.xcor() == race_turtle_three.xcor():
  race_turtle_two.write("Tie!", font=("Arial", 16, "normal"))
  race_turtle_three.write("Tie!", font=("Arial", 16, "normal"))

# Keep the window open (this is only needed if running in replit)
turtle.mainloop()