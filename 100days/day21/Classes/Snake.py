from turtle import Screen, Turtle
import time
# constants for heading
UP    =  90
DOWN  = 270
RIGHT = 0
LEFT  = 180
# constants of distance
NEAR  = 18
COLLIDE = 1
# world constants
WORLD_WITH   = 600
WORLD_HEIGHT = 600
WORLD_XPOS = WORLD_WITH/2
WORLD_XNEG = -WORLD_XPOS
WORLD_YPOS = WORLD_HEIGHT/2
WORLD_YNEG = -WORLD_YPOS
class Snake:
    def __init__(self) -> None:
        self.screen = Screen()
        self.arr_turtles = []
        self.keep_running = True

    def setupScreen(self):
        self.screen.setup(width=WORLD_WITH, height=WORLD_HEIGHT)
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
        self.tail = self.arr_turtles[-1] # last of it

    def turnUp(self):
        self.head.setheading(UP)

    def turnDown(self):
        self.head.setheading(DOWN)

    def turnLeft(self):
        self.head.setheading(LEFT)

    def turnRight(self):
        self.head.setheading(RIGHT)

    def growSnake(self):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        l_timmy = self.tail
        timmy.goto(l_timmy.position())
        self.arr_turtles.append(timmy)
        self.tail = self.arr_turtles[-1] # last of them
