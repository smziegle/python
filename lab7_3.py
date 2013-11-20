#lab7_3.py
#Scott Ziegler
#This program saves a balance to a file

import sys
def main():
    balance = input("Enter your balance:")
    outfile=open("output.txt", "w")
    print(balance, file=outfile)
main()
