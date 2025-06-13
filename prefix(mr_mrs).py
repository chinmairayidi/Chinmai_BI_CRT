#write the python program to take name as input from the user print the gender classsificarion of the name on basis of prefix 
name = input("Enter the full name with prefix(mr/mrs): ")
lowercase = name.lower()
if lowercase.startswith("mr."):
    gender = "Male"
elif lowercase.startswith("mrs.") or lowercase.startswith("miss"):
    gender = "Female"
else:
    gender = "Gender unknown."
print(f"Name : {name}")
print(f"Gender classification: {gender}")
