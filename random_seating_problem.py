'''
store 10 students names
swap any 2 students positions
print the new seating arrangement 
'''
students=[]
for i in range(10):
    name = input("enter the names of students:")
    students.append(name)
while True:
    index_1 =  int(input())
    index_2 = int(input())
    if 0 <= index_1 < 10  and 0 <= index_2 < 10:
        students[index_1], students[index_2] =students[index_2], students[index_1]
        break
    else:
        print("print invalid")
print("new seating arrangment:")
for i ,name in 
print(f"{}")