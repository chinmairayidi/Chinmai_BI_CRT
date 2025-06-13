#input a ist of number and create 2 new lists:one for even numbers and one for odd numbers
list = input("Enter a list of numbers : ")
num_list = [int(num) for num in list.split()]
odd_list = [num for num in num_list if num % 3 == 0]
even_list = [num for num in num_list if num % 2 == 0]
print("even list:", even_list)
print("odd list:", odd_list)
