'''
write a python program to read month number as input from the user and print the respective number of days in that month 
'''
month = int(input("enter month number:"))
if month in [4,6,9,11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
elif month in [1,3,5,7,8,10,12]:
    print("31 days")
else:
    print("invalid month number entered") 