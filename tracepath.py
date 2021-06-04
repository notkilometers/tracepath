import time
from numpy import random
from bresenham import bresenham
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()

def salt():
    # generate random 3 digit decimal past thousands place
    return (random.randint(999)/100000)

def move(x,y):
    # move mouse to coords
    mouse.position = (x,y)

    # sleep to slightly mimic human movement
    time.sleep(salt()) 

def trace(start,finish):
    # calculate points for path with algo
    path = list(bresenham(start[0],start[1],finish[0],finish[1]))

    # for each point, move to point
    for pos in path:
        move(pos[0],pos[1])
