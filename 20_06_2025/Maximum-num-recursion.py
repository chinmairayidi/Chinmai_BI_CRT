size = int(input("Enter the size of list: "))
lst = []
for i in range(size):
    temp = int(input(f"Enter the value {i+1}: "))
    lst.append(temp)
def maxi(lst,max,i,n):
    if(n!=0):
        if(lst[i]>max):
            max = lst[i]
            return maxi(lst,max,i+1,n-1)
        else:
            return maxi(lst,max,i+1,n-1)
    else:
        return max
print(maxi(lst,lst[0],0,size))