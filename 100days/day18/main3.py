# dash line
from turtle import Turtle, Screen

screen = Screen()
timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.pencolor("purple")
timmy_the_turtle.pendown()

for _ in range(10):
    timmy_the_turtle.forward(30)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(20)
    timmy_the_turtle.pendown()

timmy_the_turtle.penup()
screen.exitonclick()