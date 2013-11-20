#prog3_3.py
#Scott Ziegler
#This program will make an acronym out of a series of words given
def main():
    list1 = input("Enter the words to be made an acronym:")
    splitList = list1.split()
    new = ""
    for i in splitList:
        new = new + i[0]
    print(new.upper())
main()
