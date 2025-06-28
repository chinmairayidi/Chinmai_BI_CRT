def fact(a,res):
    result = res
    if a!=0:
        result = result*a
        return fact(a-1,result)
    else:
        return result
print(fact(5,1))