from Classes.config import Pong
from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

    def __str__(self) -> str:
        return super().__str__() + str(f"{Pong.WORLD_WIDTH}")