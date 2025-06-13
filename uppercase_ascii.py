#write a python program to print upper case alphabets from a -z including their ascii values
for i in range(1,27):
    print(chr(i+64),"->",i+64)
print("-----------------")
for i in range (1,27):
    print(chr(i+96),"->",i+96)




#write a python program to read a character as input from the user and print the ascii valuse of that character 
char = input("Enter a character: ")
if len(char) == 1:
    print("ASCII value of", char, ord(char))
else:
    print("enter one character.")



#write a python program to read a string as input from the user and replace all vowels with 0's
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_string = ""
for ch in string:
    if ch in vowels:
        new_string += '0'
    else:
        new_string += ch
print("String after replacing vowels with 0s:", new_string)



