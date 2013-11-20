#lab7_4.py
#Scott Ziegler
#This program saves a balance to a file

import sys
def main():
    infile=open("output.txt", "r")
    balance=eval(infile.read())
    withdrawals=eval(input("Enter number of withdraws:"))
    deposits=eval(input("Enter number of deposits:"))
    for i in range(withdrawals):
        withdraw=eval(input("Enter the amount in a negative number:"))
        totalBal=balance+withdraw
        print(totalBal)
    for j in range(deposits):
        deposit=eval(input("Enter the amount in a positive number:"))
        finalBal=totalBal+deposit
        print(finalBal)
main()
