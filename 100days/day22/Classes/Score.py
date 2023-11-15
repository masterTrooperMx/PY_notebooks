from Classes.config import *
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        # setup
        screen.setup(width=Pong.WORLD_WIDTH, height=Pong.WOLRD_HEIGHT)
        screen.bgcolor("black")
        screen.title("PONG Game")
        # create screen
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto([0,Pong.WORLD_YPOS])
        self.pensize(5)
        self.right(90)
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)

    def setupScore(self):
        pass