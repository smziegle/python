##triangleArea.py
##This program will calculate the area of a triangle
##Scott Ziegler

import math
def main():
    print("This program will calculate the area of a triangle")
    A=eval(input("Give the length of side A:"))
    B=eval(input("Give the length of side B:"))
    C=eval(input("Give the length of side C:"))
    s=(A+B+C)/2
    Area = math.sqrt(s*(s-A)*(s-B)*(s-C))
    print(Area)
main()
