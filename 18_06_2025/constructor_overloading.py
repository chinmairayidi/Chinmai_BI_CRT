'''
WRITE A PYTHON PROGRAM TO CREATE AN EMPLOYEE CLASS AND DECLARE THE STATES AND CREATE 5 OBJECTS USING DIFFERENT 
CONSTRUCTORS 

'''
#Write a Python Program to create a employee class and declare the states and create 5 objects using different constructors.
class Employee:
    def init(self, *args):
        if len(args) == 0:
            print("Hey!... i am a none parameterised constructed")
        elif len(args) == 1:
            self.Emp_ID = args[0]
            print("Hey!... i am a one parameterised constructed")
        elif len(args) == 2:
            self.Emp_ID = args[0]
            self.Emp_Name = args[1]
            print("Hey!... i am a two parameterised constructed")
        elif len(args) == 3:
            self.Emp_ID = args[0]
            self.Emp_Name = args[1]
            self.Job = args[2]
            print("Hey!... i am a three parameterised constructed")
        elif len(args) == 4:
            self.Emp_ID = args[0]
            self.Emp_Name = args[1]
            self.Job = args[2]
            self.Salary = args[3]
            print("Hey!... i am a four parameterised constructed")
        elif len(args) == 5:
            self.Emp_ID = args[0]
            self.Emp_Name = args[1]
            self.Job = args[2]
            self.Salary = args[3]
            self.Location = args[4]
            print("Hey!... i am a five parameterised constructed")
        elif len(args) == 6:
            self.Emp_ID = args[0]
            self.Emp_Name = args[1]
            self.Job = args[2]
            self.Salary = args[3]
            self.Location = args[4]
            self.Dept = args[5]
            print("Hey!... i am a six parameterised constructed")
        else:
            print("Too many arguments passed!")

Emp1 = Employee()
Emp2 = Employee("Scott")
Emp3 = Employee("Maharshi", 123)
Emp4 = Employee("Lalasa", 124, "Medical_Coder")
Emp5 = Employee("Kiran", 345, "Debugger", 56000)
Emp6 = Employee("Subbarao", 627, "Python Developer", 65999, "Bangalore")
