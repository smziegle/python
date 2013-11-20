#prog3_4
#Scott Ziegler
#This program will calculate your bank total given transaction numbers and balances
def main():
    trans=eval(input("Enter the number of transactions:"))
    balance=eval(input("Enter the inital balance of your account:"))
    for i in range(trans):
        amt=eval(input("Enter the amount of the transaction:"))
        tranBal=balance-(amt+i)
        print("${0:0.2f}".format(tranBal))
main()
