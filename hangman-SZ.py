##hangman-SZ.py
##Scott Ziegler
##This will play hangman

from graphics import *
import random
def main():
    win = GraphWin("Hangman",500,500)
    win.setCoords(0,0,100,100)
    def readfile():
        infile=open("wordlist.txt", 'r')
        text=infile.read()
        lines=text.split("\n")
        l=len(lines)
        x=random.randint(1,l-1)
        word=lines[x]
        return word
    def create_graphics(win):

        Text(Point(30,10),"Guess").draw(win)
        en=Entry(Point(50,10),5)
        en.draw(win)
        
        return en
    def enter_guess(win,en):
        word=readfile()
        empty=[]
        char=len(word)
        print(char)
        for i in range(char):
            empty.append("_ ")
        print(empty)

        incorrect=0
        while incorrect < 7:
            print("".join(empty))
            win.getMouse()
            guess=en.getText()
            if word.find(guess)== -1:
                incorrect= incorrect+1
                print("Incorrect guess. Try Again!!!")
                
                center = Point(50,75)
                circ = Circle(center, 10)
                
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
                if incorrect == 1:
                    circ.draw(win)
                if incorrect == 2:
                    line.draw(win)
                if incorrect == 3:
                    line2.draw(win)
                if incorrect == 4:
                    line3.draw(win)
                if incorrect == 5:
                    line4.draw(win)
                if incorrect == 6:
                    line5.draw(win)
                if incorrect == 7:
                    win.close()
            else:
                for i in range(len(word)):
                    if word[i]==guess:
                        empty [i]= guess
            if "".join(empty) == word:
                print("Winner")
                break
            else:
                if incorrect == 7:
                    print("How does it feel to lose to Python?")
                    break
        
        
        


            
                

    en = create_graphics(win)
    enter_guess(win,en)
    

            
main()

