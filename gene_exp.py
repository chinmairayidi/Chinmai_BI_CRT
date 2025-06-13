count=int(input("Enter the count of the data :"))
list1=[]
exp=[]
for i in range(count):
    temp=float(input())
    list1.append(temp)
print("user entered list :", list)
for ch in list1:
    if ch<5:
        exp.append('Underexpressed')
    elif ch>=5 and ch<=15:
        exp.append('Normal')
    else:
        exp.append('Overexpressed')
print(f"Expression of the entered list of genes : {exp}")