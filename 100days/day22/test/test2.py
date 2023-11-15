from turtle import Screen, Turtle

screen = Screen()
# turtle shape
Rectangle = ((-40,10),(40,10),(40,-10),(-40,-10))
# register shape
screen.register_shape('rectangle', Rectangle)
# constants are in main
WORLD_WIDTH  = 800
WOLRD_HEIGHT = 600
WORLD_XPOS   = WORLD_WIDTH/2
WORLD_XNEG   = -WORLD_XPOS
WORLD_YPOS   = WOLRD_HEIGHT/2
WORLD_YNEG   = -WORLD_YPOS
# setup
screen.setup(width=WORLD_WIDTH, height=WOLRD_HEIGHT)
screen.bgcolor("black")
screen.title("PONG Game")

# create player
class Player(Turtle):
    def __init__(self, x, y, shape: str = "rectangle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.goto(x=x, y=y)
        self.showturtle()
        self.color("white")

player1 = Player(WORLD_XNEG+20, 10)
player2 = Player(WORLD_XPOS-30, -10)

# closing  eveything
screen.exitonclick()