from Classes.config import Pong
from turtle import Turtle

class Player(Turtle):
    def __init__(self, x, y, shape: str = "rectangle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        # use new shape
        self.goto(x=x, y=y)
        self.color("white")
        self.penup()

    def __str__(self) -> str:
        return super().__str__() + str(f"{Pong.WORLD_WIDTH}")
    
    def turnUp(self):
        self.goto(self.pos() + (0, Pong.DELTA))
        
    def turnDown(self):
        self.goto(self.pos() + (0, -Pong.DELTA))