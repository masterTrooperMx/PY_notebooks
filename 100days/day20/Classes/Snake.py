from turtle import Screen, Turtle
import time

class Snake:
    def __init__(self) -> None:
        self.screen = Screen()
        self.arr_turtles = []
        self.keep_running = True

    def setupScreen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)

    # create snake body
    def createSnakeBody(self):
        for i in range(3):
            timmy = Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.forward(20*i)
            self.arr_turtles.append(timmy)
        self.head = self.arr_turtles[0] # first turtle

    def turnUp(self):
        self.head.setheading(90)

    def turnDown(self):
        self.head.setheading(270)

    def turnLeft(self):
        self.head.setheading(180)

    def turnRight(self):
        self.head.setheading(0)

