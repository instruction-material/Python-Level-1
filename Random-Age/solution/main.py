import turtle
import random

drawing_turtle = turtle.Turtle()
drawing_turtle.shape("turtle")
drawing_turtle.goto(0, 0)
drawing_turtle.left(90)

writer = turtle.Turtle()
writer.ht()
writer.penup()
writer.goto(25, 0)

age = random.randint(0, 80)

if age < 2:
    writer.write("I'm a baby turtle!")
elif age < 5:
    writer.write("I'm a toddler turtle!")
elif age < 12:
    writer.write("I'm a kiddie turtle!")
elif age < 18:
    writer.write("I'm a teen turtle!")
elif age < 50:
    writer.write("I'm an adult turtle!")
else:
    writer.write("I'm an old turtle!")
