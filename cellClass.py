from windowClasses import *

class Cell:
    def __init__(self, x1, x2, y1, y2, win=None, leftWall = True, rightWall = True, topWall = True, bottomWall = True):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win
        self.leftWall = leftWall
        self.rightWall = rightWall
        self.bottomWall = bottomWall
        self.topWall = topWall

    def draw(self, x1, y1, x2, y2):
        topLeft = Point(x1, y1)
        
