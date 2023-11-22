from Classes.config import *
from turtle import Turtle
import random
import time

# create ball
class Ball(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.angle = -1
        (self.t_x, self.t_y) = self.pos()
        self.t_x = Pong.DELTA
        self.t_y = Pong.DELTA
        
    def inWorldY(self):
        if self.ycor() < Pong.WORLD_INNYP and self.ycor() > Pong.WORLD_INNYN:
            return True
        else:
            return False
        
    def inWorldX(self):
        if self.xcor() < Pong.WORLD_INNXP and self.xcor() > Pong.WORLD_INNXN:
            return True
        else:
            return False

    def setupBall(self):
        if self.angle < 0:
            self.angle = random.randint(0, 89) # where to go
            self.setheading(self.angle)
        else:
            # bounce, complementary angle
            #self.angle = -1 * self.angle
            self.t_y = -1 * Pong.DELTA
    
    def move(self):
        (new_x, new_y) = self.pos()
        time.sleep(0.1)
        if self.inWorldY():
            #self.goto(self.t_x + new_x, self.t_y + new_y)
            new_x += self.t_x
            new_y += self.t_y
        else:
            #self.t_y = -1 * Pong.DELTA
            print("bounce Y!")
            self.t_y *= -1
            new_x += self.t_x
            new_y += self.t_y
        self.goto(self.t_x + new_x, self.t_y + new_y)

