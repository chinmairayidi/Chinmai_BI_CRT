# write a python program to read the year as input from the user and check wether it is a leap year r not 
year = int(input("year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:   
    print("not a leap year")


