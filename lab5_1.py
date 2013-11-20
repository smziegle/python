#nameReverse
#Scott Ziegler
#this program will reverse first and last names

def main():
    List=input("Enter your name in the order first name last name:")
    splitList=List.split(" ")
    newList=[]
    for i in range(len(splitList)):
        newList.append(splitList[(i+1)*-1])
    print(", ".join(newList))
main()    
