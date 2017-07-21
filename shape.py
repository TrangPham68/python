import turtle
from turtle import*
import math


#Name your turtle
simba = Turtle()

numberofside = input("how many sides do you want?")
color = ["red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink", "red", "blue", "black", "yellow", "green", "pink"]
i=0

#Set up your screen and starting position
setup(1000,800)
x_pos = 0
y_pos = 0
simba.setposition(x_pos, y_pos)
side = 50
#code
for i in range(500):
    simba.forward(side)
    simba.left(360/int(numberofside))
    i+=1
    simba.pencolor(color[i])
    side = side + 5

#close window on click
exitonclick()









