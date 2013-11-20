## lab6_1.py
## Moves a square based on user clicks
## Scott Ziegler

from graphics import *

def main():
    #Creates a graphical window
    win = GraphWin()
    width = win.getWidth()
    height = win.getHeight()

    #number of times user can move square
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move square")
    instructions.draw(win)

    #builds a square
    shape =Rectangle(Point(30,30), Point(70,70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #square
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of square

        #move amount is distance from center of square to the
        #point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        s=shape.clone()
        shape.move(dx, dy)
        s.draw(win)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

main()
