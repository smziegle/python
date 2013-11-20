#6_3.py
#Scott Ziegler

def main():
    n=eval(input("Enter the number of values: "))
    print(sumNCubes(n))
    print(sumN(n))
def sumN(n):
    for i in range(n):
        sum1=(n-1)*(i+1)
    return(sum1)

def sumNCubes(n):
    for i in range(n):
        sum2=((n-1)*(i+1))**3
    return(sum2)


main()
