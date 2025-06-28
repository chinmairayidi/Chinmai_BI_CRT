#prime n to 1
n = int(input("Enter the number: "))
def prime(a):
    if a!=0:
        c = 0
        for i in range(a):
            if a%(i+1)==0:
                c = c+1
        if(c==2):
            print(f"{a} is prime")
        return prime(a-1)
    else:
        return
prime(n)
#prime 1 to n
print("----------------------------------")
def prime2(a,k):
    if a!=0:
        c = 0
        for i in range(a):
            if k%(i+1)==0:
                c = c+1
        if(c==2):
            print(f"{k} is prime")
        return prime2(a-1,k+1)
    else:
        return
prime2(n,2)