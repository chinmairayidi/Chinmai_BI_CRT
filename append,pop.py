n_list=[10,20,30,40,50,60,70,80,90]
print(n_list)
print("Acessing the list elements using forloop with out indexing")
for i in n_list:
    print(i)
print("Acessing the list elements using forloop with indexing")
#range(stop),range(start,stop,stepsize),rane(start,stop)
for i in range(len(n_list)):
    print(n_list[i])
print("Acessing the list elements using while loop with indexing")
i=0
while(i<len(n_list)):
    print(n_list[i])
    i+=1

#list input
size=int(input("enter size of list:"))
prog_lang=[]
#reading list as input
for i in range(size):
    Temp=input("enter a programming language:")
    prog_lang.append(Temp)
print("Elements of the list")
print(prog_lang)

#delete an element from a list
colors=['white','red','blue','black','green']
print(colors)
del colors[2]
print(colors)
del colors



#min,max,summation,append,sorted
size=int(input("enter size of list:"))
num=[]
for i in range(size):
    Temp=int(input(f"enter the element at {i} position:"))
    num.append(Temp)
print(f"given list {num}")
print("maximum element :",max(num))
print("minimum element :",min(num))
print("summation element :",sum(num))
print("sorted list element :",sorted(num))

#append,pop
cartoons=["tom,doremon,shinchan,oggy"]
print(cartoons)
print("After appending")
cartoons.append("shaktishali dragan bayataki raaa")
print(cartoons)
#append adds 
cartoons.pop()
print(cartoons)
cartoons.pop(0)
print(cartoons)



# use of extend
prog_Lang = ['c','c++','java']
print(prog_Lang)
front_end=['html','css','java']
print(front_end)
prog_Lang.extend(front_end)
print()

#to find thenumber of occuenece use count method
print(prog_Lang.count('html'))