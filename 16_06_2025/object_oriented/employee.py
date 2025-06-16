#example using constructer
class employee:
    def __init__(self):
        print("employee class constructer has been called.....")
E1=employee()
E2=employee()


#write a python program to create a mobile class and perform instantiation for 10 objects
class mobile:
    def __init__(self):
        for i in range(10):
            print("10 objects",id(i),type(i))
    print("hello")
mobile()


