def main():
	print("This program illustrates a chaotic function")
	x1 = eval(input("Enter a number between 0 and 1: "))
	loop = eval(input("Enter the number of times to print the result:"))
	for i in range(loop):
		x1 = 3.9 * x1 * (1 - x1)
		print(x1)
main()
This program illustrates a chaotic function
Enter a number between 0 and 1: .3
Enter the number of times to print the result:4
0.819
0.5781321000000001
0.951191962303401
0.18106067129594494
>>> 
