# Ryan Sprowles
# Nov. 14, 2011
# I certify that this lab is my own work, but I had help from Trevor Welsh
# vigenere.py
# This lab will take an input and do a vigenere cipher

from graphics import *

border1Pt1 = Point(90, 325)
border1Pt2 = Point(175, 375)

border2Pt1 = Point(240, 325)
border2Pt2 = Point(325, 375)

def clickedPt(border, pointClicked):
    print("test2")
    clickedPt = False
    pointClickedX = pointClicked.getX()
    pointClickedY = pointClicked.getY()
    pt1X = border1Pt1.getX()
##    print(pt1X)
    pt1Y = border1Pt1.getY()
    pt2X = border1Pt2.getX()
    pt2Y = border1Pt2.getY()
    pt3X = border2Pt1.getX()
    pt3Y = border2Pt1.getY()
    pt4X = border2Pt2.getX()
    pt4Y = border2Pt2.getY()

##    print("test3")
    if pointClickedX >= pt1X and pointClickedX <= pt2X:
        if pointClickedY >= pt1Y and pointClickedY <= pt2Y:
##            print("Text")
            clickedPt == True
           
    elif pointClickedX >= pt3X and pointClickedX <= pt4X:
        if pointClickedY >= pt3Y and pointClickedY <= pt4Y:
            clickedPt == True
##            print("tests")
           
    else:
        clickedPt == False
##        print("Asadf")
        
        

def main():

    win = GraphWin("virgenere", 400, 600)

    
    encoder = Text(Point(200, 100), "Input the word/phrase you want encoded: ")
    encoder.draw(win)

    inp1 = Entry(Point(200, 125), 30)
    inp1.setText(" ")
    inp1.draw(win)

    key = Text(Point(200, 250), "Input the key you want to use: ")
    key.draw(win)

    inp2 = Entry(Point(200, 275), 30)
    inp2.setText(" ")
    inp2.draw(win)

    buttonEncode = Text(Point(125, 350), "Encode")
    buttonEncode.draw(win)
    
##    border1Pt1 = Point(90, 325)
##    border1Pt2 = Point(175, 375)
    border1 = Rectangle(border1Pt1, border1Pt2)
    border1.draw(win)

    buttonDecode = Text(Point(275, 350), "Decode")
    buttonDecode.draw(win)
##    border2Pt1 = Point(240, 325)
##    border2Pt2 = Point(325, 375)
    border2 = Rectangle(Point(240, 325), Point(325, 375))
    border2.draw(win)

    phrase = inp1.getText()
    newPhrase = inp2.getText()

    phraseUpper = phrase.upper()
    encodePhrase = phrase.replace(" ", "")

    pointClicked = win.getMouse()
    print(pointClicked.getX())
    print(pointClicked.getY())
    
    codeList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codeList = codeList * 2

##    print("test1")

    if clickedPt(border1, pointClicked) == True:
        print("test5")
        for i in range(len(phrase)):
            letter = phrse[i]
            letterVal = ord(letter)- (ord("A"))
            phraseLet = newPhrase[i]
            phraseLetVal = ord(phraseLet) - (ord("A"))
            newLetter = letterVal + phraseLetVal
            letterPos = codeList[newLetter]
            newMessage += letterPos
            message = Text(Point(250, 500), newMessage)
            message.draw(win)
            
    elif clickedPt(border2, pointClicked) == True:
        print("Test 2")

        for i in range(len(phrase)):
            letter = phrse[i]
            letterVal = ord(letter)+ (ord("A"))
            phraseLetDecode = newPhrase[i]
            phraseLetValDecode = ord(phraseLet) + (ord("A"))
            newLetter = letterValDecode + phraseLetValDecode
            letterPos = codeList[newLetter]
            newMessage += letterPos
            message = Text(Point(250, 500), newMessage)
            message.draw(win)
    else:
        text2 = Text(Point(250, 500), "Error, you did not click one of the buttons")

    win.getMouse()
    buttonDecode.undraw()
    buttonEncode.undraw()
    border1.undraw()
    border2.undraw()

    win.getMouse()
    win.close()

main()
