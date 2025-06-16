class employee():
    def __init__(self,empname,empid,designation,salary,deptname):
        print("object is created")
        self.empname=empname
        self.empid=empid
        self.designation=designation
        self.salary=salary
        self.deptname=deptname
e1=employee("scott","emp101","data analyst",25000,"deployment team")
print(f"employee name: {e1.empname}")
print(f"employee id: {e1.empid}")
print(f"designation: {e1.designation}")
print(f"salary: {e1.salary}")
print(f"department name:{e1.deptname}")


