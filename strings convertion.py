'''
write a python program to read a sentence as input from the user 
1.convert the the string into lowercase
3.conert the string into uppercase
4.convert the characters if the string into lower case if it is in upper case  and conver to upper case if it is in lower case 
4.check if the string is starting with the letter a 
5.print the count of char a from the given string and replace all P's to letter J

'''
str= input("enter the string:")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.startswith('p'))
print(str.count('p'))
str=str.lower
print(str.replace ('p','j'))

