size = int(input("Enter the size of list: "))
lst = []
for i in range(size):
    temp = int(input(f"Enter the value {i+1}: "))
    lst.append(temp)
def mini(lst,min,i,n):
    if(n!=0):
        if(lst[i]<min):
            min = lst[i]
            return mini(lst,min,i+1,n-1)
        else:
            return mini(lst,min,i+1,n-1)
    else:
        return min
print(mini(lst,lst[0],0,size))