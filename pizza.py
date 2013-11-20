import math
def main():
    cost = eval(input("Enter the cost of the pizza:"))
    d = eval(input("Enter the diameter of the pizza:"))
    A = math.pi*(d/2)**2
    costperinch = A/cost
    print("Your pizza cost", costperinch, "per inch")
main()

    
    
