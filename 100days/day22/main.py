from Classes.Score import *
from Classes.Player import *

# setup world and screen
scoreboard = Scoreboard()

player1 = Player(Pong.WORLD_XNEG+20, 10)
player2 = Player(Pong.WORLD_XPOS-30, -10)

# closing  eveything
screen.exitonclick()