NUM = []
for i in range(1,11):
    NUM.append(i)
print(NUM)
#templating same using list comprehension
#new_list = [expression for item in iteratable object if statement]
new = [i for i in range (1,11)]
print(new)

#write a python program to print even numbers from 1-n using list comprehension
n = int(input("Enter the value of n: "))
even_numbers = [x for x in range(1, n+1) if x % 2 == 0]
print("Even numbers", n, "are:", even_numbers)