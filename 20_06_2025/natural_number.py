N=int(input("Enter the value of n: "))
def NaturalNum(N):
    if N==0:
        return 
    NaturalNum(N-1)
    print(N)
NaturalNum(N)
