#write a python program to check wether the number is positive or negative using lambda functions
#true if (condition is true  else false )
#terinary operators
res = lambda Num:print("+ve") if(Num>0) else print("-ve")
res(10)


#
def positive(num):
    if (num > 0):
        print("+ve")
    else:
        if(num == 0):
            print("zero")
        else:
            print("-ve")
positive(9)


#write a python program to write a lambda function which prints good students if branch is bioiformatics else bad students
BRANCH = lambda Bioinfo:print("good students") if(Bioinfo=="bioinformatics") else print("bad students")
branch=input()
BRANCH(branch)