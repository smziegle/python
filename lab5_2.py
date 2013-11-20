#companyName.py
#Scott Ziegler
#this program will give the company name for a web domain

def main():
    List=input("Enter domain:")
    splitList=List.split(".")
    print(splitList[1])
