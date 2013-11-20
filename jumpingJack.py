#jumpingJack.py
#Scott Ziegler
#this will make a stick man
from graphics import *

win = GraphWin("Jack",500,500)
win.setCoords(0,0,100,100)
center = Point(50,75)
circ = Circle(center, 10)
circ.draw(win)
line = Line(Point(50,65),Point(50,30))
##left leg
line2=Line(Point(50,30),Point(35,15))
##right leg    
line3=Line(Point(50,30),Point(65,15))
##right arm
line4=Line(Point(50,55),Point(65,35))
##left arm
line5=Line(Point(50,55),Point(35,35))
##drawing
line2.draw(win)
line.draw(win)
line3.draw(win)
line4.draw(win)
line5.draw(win)
##Buttons
startButton = Rectangle(Point(13,90), Point(22,80))
startButton.draw(win)
stopButton = Rectangle(Point(30,90), Point(39,80))
stopButton.draw(win)
start = Text(Point(17, 85), "Start")
start.draw(win)
stop = Text(Point(35, 85), "Stop")
stop.draw(win)
quitButton = Rectangle(Point(75,90), Point(84,80))
quitButton.draw(win)
quit = Text(Point(80, 85), "Quit")
quit.draw(win)

def start():
    while True:
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        if x >= 13 and x <= 22 and y >= 80 and y <= 90: # Check to see if start clicked
            return True
while start()==True:
    for i in range():
        line.move(0,-20)
        line2.move(0,-20)
        line3.move(0,-20)
        line4.move(0,-20)
        line5.move(0,-20)
        circ.move(0,20)
        line.move(0,20)
        line2.move(0,20)
        line3.move(0,20)
        line4.move(0,20)
        line5.move(0,20)

    break


# Check for stop will updating something on screen
def stop():
    while True:
        p = win.checkMouse()
        if p != None:
            x = p.getX()
            y = p.getY()
            if x >= 30 and x <= 39 and y >= 80 and y <= 90: # Check to see if start clicked
                break
while stop()==True:
    line.move(0,20)
    line2.move(0,20)
    line3.move(0,20)
    line4.move(0,20)
    line5.move(0,20)
    circ.move(0,-20)
    line.move(0,-20)
    line2.move(0,-20)
    line3.move(0,-20)
    line4.move(0,-20)
    line5.move(0,-20)
while True:
    p = win.checkMouse()
    if p != None:
        x = p.getX()
        y = p.getY()
        if x >= 75 and x <= 84 and y >= 80 and y <= 90: # Check to see if start clicked
            win.close()
            break






####moves Jack
##    win.getMouse()
##    line.move(0,-50)
##    line2.move(0,-50)
##    line3.move(0,-50)
##    line4.move(0,-50)
##    line5.move(0,-50)
##    circ.move(0,50)
##    line.move(0,50)
##    line2.move(0,50)
##    line3.move(0,50)
##    line4.move(0,50)
##    line5.move(0,50)
##
##
####closes window
##    win.getMouse()
##    win.close()

