#write a python program to read a sentence as input from the user and print the list of words from the sentence
sentence=input("enter the sentence:")
list=sentence.split(" ")
print(list)
for ch in range(len(sentence)):
        print(sentence(ch),end="")
if(sentence(ch+1)==" "):
    print()
    