'''
sort aand remove duplicates
Problem:
given a list of integers that may contain duplicates, your task is to sort the list in ascending order and remove any duplicates.

input:
a list of integers (1 <= n <= 1000) - the list of integers

output:
sorted list of integers with unique elements

input:[4,2,2,8,4,6]
output:[2, 4, 6, 8]

'''
def sort_and_remove_duplicates(arr):
    arr.sort()
    unique_arr = []
    for num in arr:
        if not unique_arr or unique_arr[-1] != num:
            unique_arr.append(num)
    return unique_arr
arr =[4,2,2,8,6,4]
output = sort_and_remove_duplicates(arr)
print("Output:", output)