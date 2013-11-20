#prog lab6_3.py
#Scott Ziegler
import math
from graphics import *
def main():
    win =GraphWin("circle",400,400)
    width=win.getWidth()
    height=win.getHeight()

    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move circle")
    instructions.draw(win)
    
    p1=win.getMouse()
    p2=win.getMouse()
    x=p1.getX()
    y=p1.getY()
    xx=p2.getX()
    yy=p2.getY()
    r=math.sqrt((xx-x)**2+(yy-y)**2)
    shape= Circle(Point(x, y), r)
    shape.draw(win)
    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

main()    
