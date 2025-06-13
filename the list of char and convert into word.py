#write a python program to the list of characters as input from the user and convert it into a word and print it 
Size=int(input("Enter the Length of List :"))
Char_List=[]
for i in range(Size):
    ch=input("Enter the Character :")
    Char_List.append(ch)
print(Char_List)
Str="-".join(Char_List)
print(Str)
