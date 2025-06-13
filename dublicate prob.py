#write a python program to remove the duplidcate values from the list
original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7]
list = []
for num in original_list:
    if num not in list:
        list.append(num)
print("given_list:", original_list)
print("List after removing duplicates:", list)

