#Scott Ziegler
#algorithms.py
#The binary search was done in .001 seconds while the linear search wsa done in 2.862
def readData(filename):
    
    infile = open(filename,"r")
    read = infile.read()
    lines=read.split("\n")
    values=[]
    for i in range(len(lines)):
        split= lines[i].split(' ')
        for j in range(len(split)):
            values.append(split[j])
    for k in range(len(values)):
        values[k]=eval(values[k])
    
    return values


def isInLinear(srchVal,values):
    for i in range(len(values)):
        if srchVal == values[i]:
            return True
    return False

def isInBinary(srchVal,values):
    min1 = 0
    max1= len(values)-1
    while True:
        mid = (max1+min1)//2
        if values[mid] == srchVal:
            return True
        if srchVal > values[mid]:
            min1 = mid + 1
        if srchVal < values[mid]:
            max1 = mid - 1
        if min1 > max1:
            return False
        
        
def insertionSort(values):
    for i in range(len(values)-1):
        for j in range(len(values)-(1+i)):
            if values[j] > values[j+1]:
                values[j],value[j+1] = values[j+1], values[j]
    return values
def selectionSort(values):
    for i in range(1,len(values)):
        index=1
        j=i-1
        for y in range((i+1), len(values)):
            if value[y]< values[i]:
                index = y
        values[i], values[index]    = values[index],values[i]
    return values
            
            
            







def main():
    values=readData("dataSorted.txt")
    print(isInBinary(5,values))
    print(isInLinear(5,values))
    print(insertionSort(values))
    
main()
    
