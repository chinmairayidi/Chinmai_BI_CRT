#write a python program to  read password as input from the user and check wether it is a valid or invalid password:
password = input("Enter a password: ")
min_length = 8  
if len(password) < min_length:
    print("Invalid password: Must be at least", min_length, "characters long.")
    is_valid = False
else:
    is_valid = True
    print("Valid password.")



'''
#write a python program to  read name ,contact number,mail id and password and make sure that contact number has only 10 digits and mail should have a valid structure following 
name@org.com and password should have  at least three uppercase alphabets and three lowercase alphabets and three special characters and one number and len of passs should not be less than 10
'''

name = input("Enter your name: ")
contact_number = input("Enter your contact number: ")
email = input("Enter your email address: ")
if len(contact_number) != 10:
    print("Invalid contact number. It must contain exactly 10 digits.")
    contact_valid = False
else:
    contact_valid = True
    for digit in contact_number:
        if not ('0' <= digit <= '9'):
            print("Invalid contact number. It must contain only digits.")
            contact_valid = False
            break  
if "@" not in email or "." not in email:
    print("Invalid email address. It must contain @ and .")
    email_valid = False
else:
    email_valid = True
if contact_valid and email_valid:
    print("\nUser Information:")
    print("Name:", name)
    print("Contact Number:", contact_number)
    print("Email:", email)





#write a python program to read a string as input from the user and split the string into three equal halfs using slicing
input_string = input("Enter a string to split: ")
length = len(input_string)
third = length // 3
first_part = input_string[:third]
second_part = input_string[third:2*third]
third_part = input_string[2*third:]
print("\nString Parts:")
print("Part 1:", first_part)
print("Part 2:", second_part)
print("Part 3:", third_part)
