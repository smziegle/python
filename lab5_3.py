#gradeToLetter.py
#Scott Ziegler
#This program will call a letter grade from a number grade

def main():
    grade=eval(input("Enter grade:"))
    letGrade=["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    gradeVal= grade // 10
    print(letGrade[gradeVal])
main()          
