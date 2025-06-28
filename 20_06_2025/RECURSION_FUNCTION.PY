'''syntax 
def function_name (parameters)
   if base_condition
       return result
return function_name(modified parameters)
'''
def summ(a,b):
    res = b
    if a!=0:
        res = res + a
        return summ(a-1,res)
    else:
        return res
print(summ(3,0))