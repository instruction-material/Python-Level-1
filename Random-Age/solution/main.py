import random

import turtle


screen = turtle.Screen()
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)

def age_group(age):
    if age < 2:
        return "Hatchling"
    elif age < 5:
        return "Young hatchling"
    elif age < 12:
        return "Young turtle"
    elif age < 18:
        return "Teen turtle"
    elif age < 50:
        return "Adult turtle"
    else:
        return "50 and older"


age = random.randint(0, 80)
group = age_group(age)
pen.penup()
pen.goto(-100, 22)
pen.color("darkgreen")
pen.write("Age " + str(age) + ": " + group, font=("Arial", 17, "normal"))
pen.goto(0, -16)
pen.dot(23)
print("Age", age, group)

screen.update()
print("Random Age reference ready")
turtle.done()
