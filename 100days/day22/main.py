from Classes.Score import *
from Classes.Player import *

# setup world and screen
scoreboard = Scoreboard()

player1 = Player(Pong.WORLD_XNEG+20, 10)
player2 = Player(Pong.WORLD_XPOS-30, -10)

# just listen to events
screen.listen()

screen.onkey(player1.turnUp, 'w')
screen.onkey(player1.turnDown, 'x')
screen.onkey(player2.turnUp, 'u')
screen.onkey(player2.turnDown, 'm')

# closing  eveything
screen.exitonclick()