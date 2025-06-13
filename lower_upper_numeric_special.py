'''
write a python program to read  a string as input from the user 
1.print count of number of upper case numbers
2.print count of lower case numbers 
3.print the count of numeric values 
4.print the count of special characters
'''
str=input("enter the string:")
uppercase_alpha=0
lowercase_alpha=0
numeric=0
special_char=0
for ch in str:
    if ch.isupper():
        uppercase_alpha+=1
    elif ch.islower():
        lowercase_alpha+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_char+=1
print(f"count of number of upper case numbers:{uppercase_alpha}")
print(f"count of number of lower case numbers{lowercase_alpha}")
print(f"count of number of numeric values:{numeric}")
print(f"count of number of special characterw:{special_char}")

