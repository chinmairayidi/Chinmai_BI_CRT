n = int(input("Enter the number: "))
def squa(a,i):
    if a!=0:
        print(f"Square of {i} is {i*i}")
        return squa(a-1,i+1)
    else:
        return
squa(n,1)