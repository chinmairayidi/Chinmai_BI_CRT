#positional arguments
def pw (x,y):
    z = x**y
    print(z)
pw (5, 2)

#keyword arguments
def show (name, age):
    print(name,age)
show(name = "kumar" , age="62")

#default arguments
def show (name, age=27):
    print(name,age)
show(name ="ram" , age="62")

#variable length argument
def display(*x):
    x=x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]
    print(x)
display(10,10,10,10,10,10,10)


#key word varible length arguments
def add(**num):
    z = num['a']+num['b']+num['c']
    print(z)
add(a=5,b=3,c=5)

