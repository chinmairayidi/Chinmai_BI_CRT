#Write a python program to print natural numbers from N to 1
N=int(input("Enter the value of n: "))
def NaturalNum(N):
    if N!=0:
        print(N) 
        return NaturalNum(N-1)
    return
NaturalNum(N)