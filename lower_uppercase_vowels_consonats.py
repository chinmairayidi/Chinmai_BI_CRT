'''
write a python program to read a string as input from the user and print the count of 
1.uppercase vowels
2.lowercase vowels
3.upper case consonants
4.print the count of lowercase consonants
'''
string = input("Enter the string: ")
u_vowels,l_vowels,u_consonants ,l_consonants=0,0,0,0
for ch in string:
    if ch.isalpha():
        if ch.isupper():
            if ch in "AEIOU":
                u_vowels += 1
            else:
                u_consonants += 1
        elif ch.islower():
            if ch in "aeiou":
                l_vowels += 1
            else:
                l_consonants += 1

print("Lowercase vowels:", l_vowels)
print("Uppercase vowels:", u_vowels)
print("Uppercase consonants:", u_consonants)
print("Lowercase consonants:", l_consonants)
