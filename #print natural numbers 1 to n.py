#print natural numbers 1 to n 
num = int(input("enter the value:"))
print(f"natural numbers from 1 to {num}:")
for i in range (1,num+1):
    print(i)

#print natural numbers n to 1 
num= int(input("enter the value:"))
print(f"natural numbers from n to {num}:")
for i in range (num,0,-1):
    print(i)

#print square values from 1 to n 
num= int(input("enter the value:"))
print(f"squares {num}:")
for i in range (1,num+1):
    print(i*i)

#print squares n to 1
num= int(input("enter the value:"))
print(f"squares {num}:")
for i in range (num,0,-1):
    print(i*i)

#print cubes from 1 - n
num= int(input("enter the value:"))
print(f"cubes{num}:")
for i in range (1,num+1):
    print(i*i*i)


#print cubes from n - 1
num = int(input("Enter the value: "))
print(f"Cubes from {num} to 1:")
for i in range(num, 0, -1):
    print(i * i * i)


#write a python program to read an interger valuue from the user and find the number of digits present in that particular number
num = int(input("Enter an integer: "))
temp=num
count = 0
while num != 0:
        num //= 10
        count += 1
print("Number of digits:", count)


