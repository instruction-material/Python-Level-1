import turtle
import random
turtle.colormode(255)

drawing_turtle = turtle.Turtle()
l = []

for i in range(15):
  l.append(random.randint(0,10))

drawing_turtle.penup()
drawing_turtle.goto(-100, 0)

for num in l:
  drawing_turtle.write(num)
  drawing_turtle.forward(20)

drawing_turtle.goto(-100, -30)

for num in l:
  drawing_turtle.write(num + 10)
  drawing_turtle.forward(20)

drawing_turtle.goto(-100, -60)

for num in l:
  drawing_turtle.write((num+10)*10)
  drawing_turtle.forward(20)

'''
If your student is comfortable with lists, you can introduce them to indexing
then they can use this technique to actually change the values inside the list

Discuss with the student when they want to change the values in the list, and when they want to keep them stagnant
'''