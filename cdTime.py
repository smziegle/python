##cdTime.py
##This program will compile the amount of time that tracks take up on a CD.
##Scott Ziegler

def main():
    print("I will compile the amount of track time on a CD.")
    cdNumber = eval(input("Enter the number of CDs you have:"))
    i=0
    totalMinutes = 0
    totalSeconds = 0
    trackMinutes = 0
    trackSeconds = 0
    for j in range(cdNumber):
        trackNumber = eval(input("Enter the number of tracks on CD"+str(j+1)+":"))
        for i in range(trackNumber):
            trackMinutes = eval(input("Enter the number of minutes for track"+str(i+1)+ ":"))
            trackSeconds = eval(input("Enter the number of seconds for track:"+str(i+1)+ ":"))
            totalMinutes = totalMinutes + trackMinutes
            totalSeconds = totalSeconds + trackSeconds
            totalMinutes=(trackSeconds//60)+trackMinutes
            print("The total time on the CD"+str(j+1)+":" "is:", totalMinutes,"minutes", totalSeconds, "seconds")

main()
