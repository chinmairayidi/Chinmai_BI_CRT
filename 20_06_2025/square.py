n = int(input("Enter the number: "))
def squa(a):
    if a!=0:
        print(f"Square of {a} is {a*a}")
        return squa(a-1)
    else:
        return
squa(n)