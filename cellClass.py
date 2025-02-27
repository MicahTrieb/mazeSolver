from windowClasses import Point, Window, Line

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

    def draw_move(self, to_cell, undo=False):
        if undo:
            middleX = (abs(self.x1 - self.x2)) / 2
            middleY = (abs(self.y1 - self.y2)) / 2
            middleX2 = (abs(to_cell.x1 - to_cell.x2)) / 2
            middleY2 = (abs(to_cell.y1 - to_cell.y2)) / 2
            firstPoint, secondPoint = Point(middleX, middleY), Point(middleX2, middleY2)
            line = Line(firstPoint, secondPoint)
            line.draw(self.win._canvas, "red")
        else:
            middleX = (abs(self.x1 + self.x2)) / 2
            middleY = (abs(self.y1 + self.y2)) / 2
            middleX2 = (abs(to_cell.x1 + to_cell.x2)) / 2
            middleY2 = (abs(to_cell.y1 + to_cell.y2)) / 2
            firstPoint, secondPoint = Point(middleX, middleY), Point(middleX2, middleY2)
            line = Line(firstPoint, secondPoint)
            line.draw(self.win._canvas, "gray")
        
