# different shapes
from turtle import *
# import random
import random

screen = Screen()
players = 8
l_colors = ["brown", "black", "red", "blue", "orange", "pink", "cyan", "magenta", "purple", "yellow", "green", "olive"]
# create a random list of turtles
l_turtles = []

def ttt_loadlist():
    for _ in range(players):
        timmy = Turtle()
        timmy.shape("turtle")
        timmy.color(random.choice(l_colors))
        l_turtles.append(timmy)

def ttt_setup():
    screen.colormode(255)

def ttt_align_players():
    x = -300
    y = 90
    for timmy in l_turtles:
        timmy.penup()
        timmy.goto(x, y)
        y += 30