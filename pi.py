##pi.py
##This program will calulate pi using the Wallis formula
##Scott Ziegler

def main():
    pi=1
    print("This program will calculate pi using the Wallis formula")
    n=eval(input("Input the number of terms in the series:"))
    numVal=1
    denomVal=1
    for i in range(n):
        num = 2*(i+1)
        numVal=numVal*(num)**2
        denomVal=denomVal*(num-1)*(num+1)
        pi=(numVal/denomVal)
    print("The value is:", pi*2)
main()
