#code to print positive number or negative number 
num = int(input("enter the integer value :"))
#using if-else
if(num>0):
    print(f"{num} is +ve number")
elif(num<0):
    print(f"{num} is -ve number")
else:
    print(f"{num} is 0")
#using terinary operators
res="+ve num" if(num>0) else"-ve num"
print(f"{num} is {res}")



# write a python program to read the integer value from the user and check wether it is a a digit or the number 
num = int(input("enter the integer valuue :"))
#using if-else
if(num>=-9 and num<=9):
    print(f"{num} is a digit")
else:
    print(f"{num} is number")
#using terinary operators
result="digit" if(num>=-9 and num<=9) else" number"
print(f"{num} is {result}")



# write a python programm to read the integer value as input from the user and check wether it is a two digit number or not a 2 digit number
#using terinary operators
result="two digit" if(num>=-99 and num<=99) else" not a two digit number"
print(f"{num} is {result}")



# write a python programm to read the integer value as input from the user and check wether it is a three digit number or not a 3 digit number
result="two digit" if(num>=-999 and num<=999) else" not a two digit number"
print(f"{num} is {result}")



#write a python program to read amount as input from the user and print the number of notes required in indian currency dimension
#sample test case:
#enter the amount : 3864/-
#2000--------->1
#500---------->3
#100---------->1
#50----------->1
#20----------->0
#10----------->1
#5------------>0
#2------------>2
#1------------>0

#without looping 
amount=int (input("enter the amount/-"))
print("2000=",amount//2000)
amount=amount % 2000
print("500+",amount//500)
amount=amount % 500
print("200=",amount//200)
amount=amount % 200
print("100=",amount//100)
amount=amount % 100
print("50=",amount//50)
amount=amount % 50
print("20=",amount//20)
amount=amount % 20
print("10=",amount//10)
amount=amount % 10
print("5=",amount//5)
amount=amount % 5
print("2=",amount//2)
amount=amount % 2
print("1=",amount//1)
amount=amount % 1
print(amount)


