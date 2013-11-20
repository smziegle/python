##newton.py
##This program will find the square root of a number using Sir Isaac Newton's Method
##Scott Ziegler

def main():
    print("This program will find the square root of a number using Sir Isaac Newton's Method.")
    x=eval(input("Input the number to be squared:"))
    
    approx = x/2
    for i  in range(100):
        approx= (approx + x/approx)/2
    print(approx)
main()
