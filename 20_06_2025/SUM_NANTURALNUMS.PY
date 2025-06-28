N=int(input("Enter the value of n: "))
def summ(a,b):
    res = b
    if a!=0:
        res = res + a
        return summ(a-1,res)
    else:
        return res
print(summ(N,0))