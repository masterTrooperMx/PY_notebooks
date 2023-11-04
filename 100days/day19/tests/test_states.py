# according to https://realpython.com/python-application-layouts/
import sys
# adding path
sys.path.insert(0, '/Users/jescruz/dev/PY/PY_notebooks/100days/day19')
from ttt_race.helpers import screen, timmy_the_turtle, ttt_setup
# setting up everything
ttt_setup()

# closing  eveything
timmy_the_turtle.penup()
screen.exitonclick()