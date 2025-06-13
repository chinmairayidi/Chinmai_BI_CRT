#write a python program to read the list elements as input from the user and check wether the list of elemeents are multiples of 3 and 5 or not and print the list of elements which are multiples of 3 and 5 
list = input("Enter a list of numbers : ")
num_l = [int(num) for num in list.split()]
new_list = [num for num in num_l if num % 5 == 0]
second_list = [num for num in num_l if num % 3 == 0]
print("Multiples of 5:", new_list)
print("Multiples of 3:", second_list)