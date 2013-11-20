#winterGreeting.py
#Scott Ziegler
#This program will make a Christmas gift card using the graphics library

from graphics import *
import random
def main():
    
    win=GraphWin("card",500,500)
    win.setCoords(0,0,100,100)
    width = win.getWidth()
    height = win.getHeight()

    #background
    win.setBackground("sky blue")
    horizon = Line(Point(0,30),Point(100,30))
    horizon.draw(win)

    #ground settings
    ground = Rectangle(Point(0,30), Point(101,0))
    ground.setOutline("black")
    ground.setFill("green")
    ground.draw(win)


    #roof settings
    tria1 = Point(20,70)
    tria2 = Point(50,90)
    tria3 = Point(80,70)
    triangle = Polygon(tria1, tria2, tria3)
    triangle.setFill("brown")
    triangle.setOutline("black")
    triangle.draw(win)
    
    #house settings
    house =Rectangle(Point(20,70), Point(80,10))
    house.setOutline("black")
    house.setFill("white")
    house.draw(win)

   # door
    door = Rectangle(Point(40,10), Point(60,40))
    door.setFill("dark red")
    door.draw(win)
    knob=Circle(Point(42,23), 2)
    knob.setFill("yellow")
    knob.draw(win)
    
    #window1
    window1 = Rectangle(Point(28,50), Point(43,65))
    window1.setFill("yellow")
    window1.draw(win)
    pane1=Line(Point(35.5,50),Point(35.5,65))
    pane1.draw(win)
    pane2=Line(Point(28,57.5), Point(43,57.5))
    pane2.draw(win)
    
    
    #window2
    window2=window1.clone()
    window2.move(30,0)
    window2.draw(win)
    pane11=pane1.clone()
    pane22=pane2.clone()
    pane11.move(30,0)
    pane22.move(30,0)
    pane11.draw(win)
    pane22.draw(win)
    
    #snow
    win.getMouse()
    win.setBackground("gray")
    x=random.randint(0,100)
    y=random.randint(0,100)
    x1=random.randint(0,100)
    y1=random.randint(0,100)
    x2=random.randint(0,100)
    y2=random.randint(0,100)
    x3=random.randint(0,100)
    y3=random.randint(0,100)
    x4=random.randint(0,100)
    y4=random.randint(0,100)
    x5=random.randint(0,100)
    y5=random.randint(0,100)
    x6=random.randint(0,100)
    y6=random.randint(0,100)

        
    flake=Point(x,y)
    flake2=Point(x1,y1)
    flake3=Point(x2,y2)
    flake4=Point(x3,y3)
    flake5=Point(x4,y4)
    flake6=Point(x5,y5)
    
    #for i in range(5):
    flake.setFill("white")
    flake2.setFill("white")
    flake3.setFill("white")
    flake4.setFill("white")
    flake5.setFill("white")
    flake6.setFill("white")

    #win.getMouse()
    
    flake2.draw(win)

    
    #win.getMouse()
    flake3.draw(win)

    
    #win.getMouse()
    flake4.draw(win)

    
    #win.getMouse()
    flake5.draw(win)

    
    #win.getMouse()
    flake6.draw(win)


    #win.getMouse()
    flake.draw(win)


    win.getMouse()
    ground.setFill("white")
    triangle.setFill("white")

    #Message settings
    win.getMouse()
    instPt = Point(50, 80)
    instructions = Text(instPt,"Happy Holidays!!!\n Click to quit")
    instructions.draw(win)
    win.getMouse()
    win.close()
main()
