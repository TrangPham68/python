from turtle import *
import math

# Name your Turtle.
simba = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
simba.setposition(x_pos, y_pos)
side = 200
numberofside = input("how many sides?")


### Write your code below:
for x in range(100):
    simba.pencolor("blue")
    simba.forward(side)
    simba.left(360/int(numberofside))
    side = side-5

# Close window on click.
exitonclick()
