def main():
    prev1=1
    prev2=1
    n=eval(input("n:"))
    for i in range(n):
        nxt=prev1+prev2
        prev1=prev1+prev2
        prev2=prev1+prev2
        print(prev1)
main()

        
