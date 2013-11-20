from graphics import *
def main():
    win= GraphWin()
    width=win.getWidth()
    height=win.getHeight()

    numClicks=2
    
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to draw square")
    instructions.draw(win)

    

    for i in range (numClicks):
        p1=win.getMouse()
        p2=win.getMouse()
        shape = Rectangle(p1, p2)
        shape.draw(win)
        w=abs(p1.getX()-p1.getY())
        h=abs(p2.getX()-p2.getY())
        perimeter=2*(w+h)
        area=(w)*(h)
        win.getMouse()
        instructions.setText("Perimeter=" + str(perimeter) + "Area=" + str(area))
    win.getMouse()
    win.close()
main()        
