from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkOrange1")

#for i in range(4):
#    timmy.forward(100)
#    timmy.right(90)

#for i in range(8):
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(5)
#    timmy.pendown()

colors = ["red","brown","blue","green","aquamarine","blueviolet","blue4","black",
          "darkgreen","deeppink","darkslateblue","darkolivegreen","deepskyblue"]



timmy.speed(10)
shapes = 3
while shapes < 11:
    timmy.pencolor(random.choice(colors))
    for side in range(shapes):
        timmy.forward(100)
        timmy.right(360/shapes)
    shapes += 1










screen = Screen()
screen.exitonclick()
