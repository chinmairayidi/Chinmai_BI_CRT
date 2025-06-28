st = input("Enter the string: ")
def str(string,num,new_string):
    if num >= len(string):
        return new_string + st[0]
    else:
        new_string = new_string + string[len(string)-num]
        return str(string,num+1,new_string)
print(str(st,1,""))