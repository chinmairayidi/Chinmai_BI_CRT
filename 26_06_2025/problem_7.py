'''
Sort Names Alphabetically

Problem:
Sort a list of names in alphabetical order using a sorting algorithm without built-in sort functions.

Input:
-------------------------
An integer n (1 s n ≤ 500) - number of names 
A list of n names (strings of max length 100)
Output:
---------------------------
List of names sorted alphabetically
Input: ["Zara", "John", "Alex", "Scott"]
Output: ["Alex", "John", "Scott", "Zara"]
'''
def selection_sort(names):
    n = len(names)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if names[j] < names[min_idx]:
                min_idx = j
    names[i], names[min_idx] =names[min_idx], names[i]
    return names
names = ["Zara", "John", "Alex", "Scott"]
output = selection_sort(names)
print("Output:", output)