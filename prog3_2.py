#Scott Ziegler
#prog3_2.py
#This program will count the average number of letters in a word in a sentence
def main():
    sentence=input("Enter a sentence to calculate the average word length:")
    words=sentence.split(" ")
    new=""
    for i in words:
        new=len(new+i[0:])
        print(new)
main()

          
