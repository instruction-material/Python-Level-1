import turtle

juni = turtle.Turtle()

side_length = 30

for i in range(3):
  for j in range(4):
    juni.forward(side_length)
    juni.right(90)

  side_length += 20
