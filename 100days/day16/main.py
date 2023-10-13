#from turtle import *

#for steps in range(100):
#    for c in ('blue', 'red', 'green'):
#        color(c)
#        forward(steps)
#        right(30)

# way 1 to import classes
#import turtle

#timmy = turtle.Turtle()
# way 2
from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("DarkOrchid")
timmy.forward(100)
print(my_screen.canvheight)
my_screen.exitonclick()