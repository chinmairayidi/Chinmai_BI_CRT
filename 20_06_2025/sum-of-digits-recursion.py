number = int(input("Enter the value: "))
def digit_sum(num,res):
    val = res
    if(num!=0):
        val = num%10
        res = res + val
        return digit_sum(num//10,res)
    else:
        return res
print(digit_sum(number,0))