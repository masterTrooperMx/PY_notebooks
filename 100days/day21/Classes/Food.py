from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
    
    def moveFood(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)