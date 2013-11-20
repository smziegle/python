##sphere.py
##This program will calculate the Surface Area and Volume
##Scott Ziegler

import math
def main():
    r=eval(input("Enter the radius of the Sphere:"))
    Volume=(4/3*math.pi*r**3)
    surfaceArea=(4*math.pi*r**2)
    print("This is the Surface Area:", surfaceArea)
    print("This is the Volume:", Volume)
main()
          
