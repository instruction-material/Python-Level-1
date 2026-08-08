import turtle

turtle.colormode(255)
drawing_turtle = turtle.Turtle()

# If the variable x starts at 3 and then we do x += 5, what is the value of x now?


# Write a while loop which runs makes a turtle go forward by 1px 10 times.

counter = 0
while counter < 10:
    drawing_turtle.forward(1)
    counter += 1

# Write the same loop using a for loop.

for i in range(10):
    drawing_turtle.forward(1)

# Make two variables, one called lineLength and the other one called degrees. Set lineLength to 10 and degrees to 5. Use a while loop to have the turtle move forward by lineLength and then turn by degrees 10 times, then increment lineLength by 5 and degrees by 1 each time.

line_length = 10
degrees = 5

counter = 0
while counter < 10:
    drawing_turtle.forward(line_length)
    drawing_turtle.right(degrees)
    line_length += 10
    degrees += 5
    counter += 1

# Explain how the above code works:
#
# Explain how we you can figure out what the value of lineLength and degrees will be by the end of the loop.
#
