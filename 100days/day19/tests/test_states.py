# according to https://realpython.com/python-application-layouts/
import sys
# adding path
sys.path.insert(0, '/Users/jescruz/dev/PY/PY_notebooks/100days/day19')
from ttt_race.helpers import screen, l_turtles, ttt_setup, ttt_loadlist, ttt_align_players
# setting up everything
ttt_setup()
ttt_loadlist()

""" x = -300
y = 90
for timmy in l_turtles:
    timmy.penup()
    timmy.goto(x, y)
    y += 30 """
ttt_align_players()

#print(l_turtles)

# closing  eveything
screen.exitonclick()