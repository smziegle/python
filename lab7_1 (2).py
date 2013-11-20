#lab6_1.py
#Scott Ziegler
#This program will count lines words and characters

import sys
def main():
    infile = open("myfile.txt","r")
    
    text=infile.read
    lines=infile.split("\n")
    words=infile.split(" ")
    chars=len(infile)
    print(len(lines))
    print(len(words))
    print(len(chars))
    print(sys.argv[0])
main()
