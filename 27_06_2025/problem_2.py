'''
write a python program to read month number as input from the user and check wether it is valid month number or not 
'''
month = int(input("Enter month number:"))
if (month >= 1 and month <= 12):
    print("Valid month number.")
else:
    print("Invalid month number.")