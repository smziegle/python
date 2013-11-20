##coffee.py
##This program will add how much an order of coffee will cost
##Scott Ziegler

def main():
    print("This program will give the cost for an order of coffee")
    order = eval(input("Give the number of orders to be processed:"))
    for  i in range(order):
        pounds = eval(input("Give the amount of pounds you need:"))
        orderCost = (pounds * 10.50) + (pounds * .86) + (1.50 * order)
        print(orderCost)
main()
