#write a python program to read the list elements as input from the user and print a new list of numbers which are multiples of 5 
list = input("Enter a list of numbers : ")
num_l = [int(num) for num in list.split()]
new_list = [num for num in num_l if num % 5 == 0]
print("Multiples of 5:", new_list)


