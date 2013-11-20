#prog6_2.py
#Scott Ziegler

import math
def main():
    radius= eval(input("Enter radius: "))
    sphereVolume(radius)
    sphereArea(radius)

def sphereArea(radius):

    SA=4*math.pi*radius**2
    print("Surface Area=", SA)
    
def sphereVolume(radius):
    V=(4/3)*math.pi**3
    print("Volume=", V)
main()


