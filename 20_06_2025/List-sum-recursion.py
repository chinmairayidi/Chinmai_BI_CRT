lst=[10,20,30]
l = len(lst)
def suml(a,b,c):
    res = b
    if c!=0:
        res = res + a[c-1]
        return suml(a,res,c-1)
    else:
        return res
print(suml(lst,0,l))