#write a python program to read an interger valuse as input from the user and print the multiplication table of it 
num = int(input("Enter a number: "))
[print(f"{num}*{i} = {num * i}") for i in range(1, 11)]




#write a python program to print the multiplication tables from 1 to n 
n = int(input("Enter a number: "))
[print(f"{i} * {j} = {i * j}") for i in range(1,n+1) for j in range(1,11)]


#using loops
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(f"multiplication table of {i}:")
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}")




#write a python program to print the reverse multiplication table of n
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")





#write a apython program to print the reverse multiplication tables of 1 - n 
n = int(input("Enter a number: "))
[print(f"{i} * {j} = {i * j}") for i in range(1,n+1) for j in range(10,0,-1)]




# write a python program to print the resevers emultiplication tables from n to 1 
n = int(input("Enter a number: "))
[print(f"{i} * {j} = {i * j}") for i in range(n,0,-1) for j in range(10,0,-1)]


