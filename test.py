from graphics import *

win = GraphWin("Jump Jack",300,300)
win.setCoords(0,0,100,100)

text = Text(Point(25,90),"Start")
text.draw(win)
text = Text(Point(75,90),"Stop")
text.draw(win)
rect = Rectangle(Point(15,95),Point(35,85))
rect.draw(win)
rect = Rectangle(Point(65,95),Point(85,85))
rect.draw(win)

# Check for start
while True:
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    if x >= 15 and x <= 35 and y >= 85 and y <= 95: # Check to see if start clicked
        break

i = 0
text = Text(Point(50,50),str(i))
text.draw(win)
# Check for stop will updating something on screen
while True:
    p = win.checkMouse()
    if p != None:
        x = p.getX()
        y = p.getY()
        if x >= 65 and x <= 85 and y >= 85 and y <= 95: # Check to see if start clicked
            break
    i = i + 1
    text.setText(str(i))
    
win.getMouse()
win.close()
