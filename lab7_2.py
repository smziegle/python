#lab6_1.py
#Scott Ziegler
#This program will count lines words and characters

import sys
def main():
    infile = open(sys.argv[1],"r")
    
    text=infile.read()
    lines=text.split("\n")
    words=text.split(" ")
    chars=len(text)
    outfile = open(sys.argv[2],"w")
    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", chars)
    print(sys.argv[0])
    print(sys.argv[2])
    
main()
