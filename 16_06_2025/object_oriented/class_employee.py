#class Employee:
class Employee:
    def __init__(self, Empname, EmpID, Designation, Salary, DeptName):  # constructor
        print("Object is created.")
        self.Empname = Empname
        self.EmpID = EmpID
        self.Designation = Designation
        self.Salary = Salary
        self.DeptName = DeptName

    def Display_Details(self):
        print(f"\nEmployee Name        : {self.Empname}")
        print(f"Employee ID          : {self.EmpID}")
        print(f"Employee Designation : {self.Designation}")
        print(f"Employee Salary      : {self.Salary}")
        print(f"Department Name      : {self.DeptName}")

# Creating employee objects
E1 = Employee("Jyothi", "EMP01", "Data Analyst", 25000, "DeploymentTeam")
E2 = Employee("Revathi", "EMP02", "Data Engineer", 35000, "EmploymentTeam")
E3 = Employee("Hari", "EMP03", "Data Scientist", 45000, "Teamlead")
E4 = Employee("Pavan", "EMP04", "Developer", 55000, "HOD")
E5 = Employee("Nani", "EMP05", "Tester", 15000, "ProjectTeam")
E6 = Employee("Anu", "EMP06", "Engineer", 65000, "Department")

# Displaying details
E1.Display_Details()
E2.Display_Details()
E3.Display_Details()
E4.Display_Details()
E5.Display_Details()
E6.Display_Details()

