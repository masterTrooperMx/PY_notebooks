# according to https://realpython.com/python-application-layouts/
import sys
# adding path
sys.path.insert(0, '/Users/jescruz/dev/PY/PY_notebooks/100days/day19')
from ttt_events.helpers import screen, timmy_the_turtle, ttt_setup

ttt_setup()
# events definitions
def move_forward():
    timmy_the_turtle.forward(10)

# just listen to events
screen.listen()

# events triggers
screen.onkey(fun=move_forward, key="space")

# closing  eveything
timmy_the_turtle.penup()
screen.exitonclick()