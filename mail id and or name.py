#write a python program to read mail id as input from the user and  print user name and organisation name based on mail id (1.name@orgname.com)
email = input("Enter email ID (format: name@orgname.com): ")
list=email.split('@')
print(f"User name: {list[0]}")
org=list[1]
list=org.split('.')
print(f"Organization name: {list[0]}")