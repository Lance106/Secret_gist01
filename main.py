Route001import numpy as np
from utils import routeGame, userInputRoute, getStartingCoordinates
import sys
import os.path

game = 1 # Used to determine to carry on game or not
gridSizeX = 12
gridSizeY = 12
file = 1

while(game):
    
    route = userInputRoute() # Call this function to gather data from the user

    while(file):
        if os.path.exists(route):
            route = open(route, 'r') # Open file as read only 'r'
            file = 0
        else:
            if route == "STOP":
                sys.exit("Game Stopped")
            route = input("File Not Found. Enter Route Instructions File again \n")
            file = 1
    
    Lines = route.readlines()

    xStart, yStart = getStartingCoordinates(Lines)
    xBoundary = gridSizeX
    yBoundary = gridSizeY

    arr = np.zeros((yBoundary, xBoundary), dtype=int) # Make a new Array of zeros
    
    routeGame(Lines, xBoundary, yBoundary, arr)
    file = 1
