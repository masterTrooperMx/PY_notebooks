# different shapes
from turtle import Turtle, Screen
# import random
from random import randint

screen = Screen()
xmax = 400
ymax = 300
long = 10
screen.screensize(xmax, ymax)
screen.setworldcoordinates(0, 0, xmax-1, ymax-1)
timmy_the_turtle = Turtle()

screen.colormode(255)
timmy_the_turtle.shape("classic")
timmy_the_turtle.color("red")
timmy_the_turtle.home()
# random color
#timmy_the_turtle.goto(-100,0)
timmy_the_turtle.pen(pensize=10)
timmy_the_turtle.speed('fastest')

# https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
for _ in range(round(xmax/long)*27):
    if(timmy_the_turtle.xcor() > xmax):
        timmy_the_turtle.goto([0.0, timmy_the_turtle.ycor()+long])
    timmy_the_turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(1)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(long)
    #print(timmy_the_turtle.pos())
    
timmy_the_turtle.penup()
screen.exitonclick()