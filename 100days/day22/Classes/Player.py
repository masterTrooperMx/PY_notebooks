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
        # don't leave world!
        delta_up = self.pos() + (0, 1.5*Pong.DELTA)
        if delta_up[1] <= Pong.WORLD_YPOS-45: 
            self.goto(delta_up)
        else:
            pass
            #print(self.pos()) do some noise!
        
    def turnDown(self):
        # don't leave world!
        delta_down = self.pos() + (0, -1.5*Pong.DELTA)
        if delta_down[1] >= Pong.WORLD_YNEG+45:
            self.goto(delta_down)
        else:
            pass
            #print(self.pos()) do some noise!!