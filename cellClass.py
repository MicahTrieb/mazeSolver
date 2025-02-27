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

    def draw(self, x1, y1, x2, y2, canvas, color):
        topLeft = Point(x1, y1)
        topRight = Point(x2, y1)
        bottomLeft = Point(x1, y2)
        bottomRight = Point(x2,y2)
        if self.leftWall:
            line = Line(topLeft, bottomLeft)
            line.draw(canvas, color)
        if self.rightWall:
            line = Line(topRight, bottomRight)
            line.draw(canvas, color)
        if self.bottomWall:
            line = Line(bottomLeft, bottomRight)
            line.draw(canvas, color)
        if self.topWall:
            line = Line(topLeft, topRight)
            line.draw(canvas, color)
        
