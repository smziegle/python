import sys
def main():
	infile=open("text.txt","r")
	lines=infile.readlines()
	
	for i in range(len(lines)):
		fields=lines[i].split(" ")
		final_grade=0
		for j in range(2,len(fields),2):
			weight=eval(fields[j])
			grade=eval(fields[j+1])
			final_grade=final_grade+((weight*grade)/100)
		print(final_grade)
main()	
