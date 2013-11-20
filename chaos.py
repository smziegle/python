Python 3.2.1 (default, Jul 10 2011, 21:51:15) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x = 3.9 * x * (1 - x)
		print(x)

		
>>> main()
This program illustrates a chaotic function
Enter a number between 0 and 1: .4
0.9359999999999999
0.2336256000000002
0.6982742481960964
0.8216805577588637
0.5714343131637907
0.9550988417209882
0.16725167263043805
0.5431863474677594
0.9677262636303364
0.12180535501057962
>>> def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x = 3.9 * x * (1 - x)
		print(x
		

